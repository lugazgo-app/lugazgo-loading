---
name: clean-code
description: Refactorización de LugazGO con extracción de handlers, regresión y controles SAST/SCA sin alterar el comportamiento aprobado.
---

# Clean Code — LugazGO

## Contexto obligatorio
Leer `AGENTS.md`, `docs/decisions.md` y las especificaciones vigentes. Confirmar el repositorio y la rama antes de intervenir. El repositorio de la landing no es el código de la PWA.

## Refactorización
1. Registrar comportamientos existentes con pruebas de caracterización.
2. Extraer manejadores reales (eventos, rutas, acciones) de componentes UI cuando existan. Un handler adapta entradas, valida, delega la operación y traduce respuestas; la lógica de negocio queda en módulos independientes del DOM y la infraestructura.
3. Favorecer responsabilidad única, nombres explícitos, composición, funciones pequeñas, guard clauses, tipado y errores controlados. Evitar abstracciones vacías, dependencias adicionales, estado global y duplicación de reglas.
4. Preservar accesibilidad, enlaces, guardados/rutas, sincronización URL y permisos de precisión geográfica; no filtrar coordenadas protegidas al cliente.
5. No inventar handlers en HTML/CSS estático: no hay extracción que ejecutar.

## Seguridad
- **SAST**: ejecutar CodeQL o Semgrep según el stack y revisar manualmente XSS, DOM sinks, inyección, deserialización, datos personales, secretos, validación y autorización.
- **SCA**: inventariar manifests y lockfiles; ejecutar `npm audit`, `pip-audit`, `osv-scanner` u otro según el ecosistema; registrar CVE/GHSA, criticidad, versión afectada, remediación y lockfile verificado. Si no hay dependencias de software declaradas, marcar SCA como no aplicable, nunca como «cero vulnerabilidades».
- Para la landing ejecutar `python3 scripts/audit_static_site.py` como chequeo acotado, **no** como sustituto de SAST integral.

## Validación y entrega
Ejecutar tests, lint, build y auditorías aplicables; distinguir pruebas ejecutadas de las pendientes. Exponer cambios mínimos y verificables en una PR sin despliegue ni merge automáticos; documentar riesgos residuales y diffs.
