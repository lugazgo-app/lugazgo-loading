import unittest

from audit_static_site import CheckHTML, ERRORS, valid_csp


POLICY = ("default-src 'none'; script-src 'none'; object-src 'none'; "
          "style-src 'unsafe-inline'; img-src 'self'; font-src 'self'; "
          "connect-src 'none'; base-uri 'none'; form-action 'none'")


class CspTests(unittest.TestCase):
    def test_complete_policy_is_valid(self):
        self.assertTrue(valid_csp(POLICY))

    def test_rejects_duplicate_and_weakened_directives(self):
        for policy in (
            "script-src 'self'; " + POLICY,
            POLICY.replace("script-src 'none'", "script-src 'none' https:"),
            POLICY.replace("script-src 'none'", "x-script-src 'none'"),
            POLICY.replace("object-src 'none'", "object-src 'none'\u00a0*"),
            POLICY + "; script-src-elem https:",
            POLICY.replace("base-uri 'none'; ", ""),
        ):
            with self.subTest(policy=policy):
                self.assertFalse(valid_csp(policy))

    def test_rejects_policy_after_styles_or_outside_head(self):
        meta = f'<meta http-equiv="Content-Security-Policy" content="{POLICY}">'
        for html in (f"<head><style></style>{meta}</head>", f"<head></head><body>{meta}"):
            with self.subTest(html=html):
                ERRORS.clear()
                CheckHTML().feed(html)
                self.assertTrue(ERRORS)


if __name__ == "__main__":
    unittest.main()
