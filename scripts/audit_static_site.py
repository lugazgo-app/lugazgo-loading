#!/usr/bin/env python3
"""Narrow static security checks for the LugazGO landing (not full SAST/SCA)."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []
INSTAGRAM = "https://instagram.com/lugazgo.app"
EXPECTED_CSP = {
    "default-src": ("'none'",),
    "script-src": ("'none'",),
    "object-src": ("'none'",),
    "style-src": ("'unsafe-inline'",),
    "img-src": ("'self'",),
    "font-src": ("'self'",),
    "connect-src": ("'none'",),
    "base-uri": ("'none'",),
    "form-action": ("'none'",),
}

def valid_csp(policy):
    if not policy.isascii() or re.search(r"[\x00-\x08\x0b\x0e-\x1f\x7f]", policy):
        return False
    directives = {}
    for directive in policy.split(";"):
        parts = directive.split()
        if not parts:
            continue
        name, *sources = parts
        name = name.lower()
        if name in directives:
            return False
        directives[name] = tuple(sources)
    return directives == EXPECTED_CSP

def fail(message):
    ERRORS.append(message)

def local_asset(value, location):
    parsed = urlsplit(value.strip())
    if parsed.scheme or parsed.netloc or ".." in Path(parsed.path).parts:
        fail(f"{location}: unsafe or remote resource {value}")
    elif not (ROOT / parsed.path.lstrip("/")).is_file():
        fail(f"{location}: missing resource {value}")

class CheckHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.csp_count = 0
        self.in_head = False
        self.resource_seen = False
        self.links = 0

    def handle_endtag(self, tag):
        if tag == "head":
            self.in_head = False

    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if tag == "head":
            self.in_head = True
        if tag in {"link", "style", "img", "body"}:
            self.resource_seen = True
        if tag in {"script", "iframe", "object", "embed", "form", "base"}:
            fail(f"unexpected active element {tag}")
        for name, value in pairs:
            if name.lower().startswith("on"):
                fail(f"inline event attribute {name}")
            if value and re.match(r"\s*(javascript|vbscript|data):", value, re.I):
                fail(f"unsafe attribute URI {name}")
        if tag == "meta" and (attrs.get("http-equiv") or "").lower() == "content-security-policy":
            self.csp_count += 1
            if not self.in_head or self.resource_seen:
                fail("CSP must appear in head before styles and resources")
            if len(attrs) != len(pairs) or not valid_csp(attrs.get("content") or ""):
                fail("CSP directives must match the approved source lists without duplicates")
        if tag in {"img", "link"}:
            resource = attrs.get("src" if tag == "img" else "href")
            if resource:
                local_asset(resource, tag)
        if tag == "a":
            href = (attrs.get("href") or "").rstrip("/")
            if href != INSTAGRAM:
                fail(f"unexpected outbound destination {href}")
            else:
                self.links += 1
            if attrs.get("target") == "_blank":
                rel = set((attrs.get("rel") or "").split())
                if not {"noopener", "noreferrer"} <= rel:
                    fail("target=_blank without noopener noreferrer")

def check_svg(path):
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as error:
        fail(f"{path}: invalid SVG XML: {error}")
        return
    for element in root.iter():
        tag = element.tag.rsplit("}", 1)[-1].lower()
        if tag in {"script", "foreignobject", "iframe", "animate", "set"}:
            fail(f"{path}: active SVG tag {tag}")
        for attr, value in element.attrib.items():
            attr = attr.rsplit("}", 1)[-1].lower()
            if attr.startswith("on") or re.search(r"\b(javascript|vbscript):", value, re.I):
                fail(f"{path}: active SVG attribute {attr}")
            if attr == "href" and not value.startswith("#"):
                fail(f"{path}: external SVG link {value}")

def main():
    content = (ROOT / "index.html").read_text(encoding="utf-8")
    parser = CheckHTML()
    parser.feed(content)
    if parser.csp_count != 1:
        fail("expected exactly one CSP meta element")
    if parser.links != 1:
        fail("expected exactly one approved Instagram destination")
    for resource in re.findall(r"url\(\s*['\"]?([^)'\"\s]+)", content, re.I):
        local_asset(resource, "CSS")
    for path in ROOT.rglob("*.svg"):
        check_svg(path)
    manifests = ("package.json", "pnpm-lock.yaml", "package-lock.json", "yarn.lock",
                 "requirements.txt", "poetry.lock", "Pipfile.lock", "Cargo.lock", "go.mod")
    found = [name for name in manifests if (ROOT / name).exists()]
    if found:
        fail(f"New dependency manifests require an ecosystem SCA audit: {found}")
    else:
        print("SCA: not applicable — no software dependency manifests")
    for error in ERRORS:
        print("FAIL:", error, file=sys.stderr)
    if ERRORS:
        return 1
    print("PASS: HTML, approved links, local resources, CSP, and SVG checks")
    return 0

if __name__ == "__main__":
    sys.exit(main())
