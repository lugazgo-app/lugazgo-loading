# LugazGO — Registro de decisiones

Este documento separa decisiones confirmadas, alcance bloqueado y asuntos pendientes. No borres entradas históricas: cuando una decisión cambie, añade otra y marca la anterior como **Sustituida**.

## Estados

- **Aprobada:** forma parte de la definición vigente del proyecto.
- **Bloqueada:** aprobada y protegida contra ampliaciones o cambios implícitos.
- **Pendiente:** necesita una decisión explícita; no se puede completar por inferencia.
- **No disponible:** se sabe qué elemento hace falta, pero el archivo o dato no estaba accesible durante la migración.
- **Sustituida:** dejó de estar vigente por una decisión posterior identificada.

> Las fechas siguientes indican cuándo se consolidó el registro. Las fechas originales de aprobación no estaban documentadas en el material accesible.

## D001 — Nombre de marca

- **Estado:** Aprobada
- **Registrada:** 2026-08-30
- **Decisión:** La marca se llama `LugazGO` y debe conservar esa capitalización.
- **Implicación:** No usar variantes como `Lugazgo`, `LUGAZGO` o `lugazgo` como nombre principal sin una nueva aprobación.

## D002 — Enfoque de la marca

- **Estado:** Aprobada
- **Registrada:** 2026-08-30
- **Decisión:** LugazGO se centra en descubrir lugares con encanto, tranquilos, poco masificados y menos explotados.
- **Implicación:** La identidad debe apoyar el descubrimiento selectivo y con personalidad.

## D003 — Personalidad

- **Estado:** Aprobada
- **Registrada:** 2026-08-30
- **Decisión:** La personalidad es minimalista, eco-friendly, premium, misteriosa y curiosa.
- **Implicación:** Estos atributos orientan la evaluación; no fijan por sí solos tipografías, formas o colores exactos.

## D004 — Dirección cromática

- **Estado:** Sustituida por D013
- **Registrada:** 2026-08-30
- **Decisión:** Los colores deben sentirse suaves, orgánicos y pastel.
- **Situación original:** Los nombres y valores exactos, combinaciones, jerarquías y equivalencias estaban pendientes.
- **Regla:** No inventar códigos HEX/RGB/CMYK/Pantone a partir de esta descripción.
- **Sustituida:** 2026-08-30 por D013, que conserva la dirección y aprueba la paleta básica exacta.

## D005 — Concepto distintivo de la O

- **Estado:** Aprobada en concepto
- **Registrada:** 2026-08-30
- **Decisión:** La `O` incorpora curvas topográficas que la atraviesan diagonalmente, con lectura tipo `ø`, y un punto de ubicación aproximadamente en la zona central/superior derecha.
- **Resolución posterior:** D010 y D011 fijan la geometría autoritativa mediante los SVG aprobados, sin reconstruirla ni traducirla a nuevas especificaciones.
- **Regla:** La descripción no autoriza una reconstrucción aproximada que se presente como maestro.

## D006 — Alcance de la fase actual

- **Estado:** Bloqueada
- **Registrada:** 2026-08-30
- **Decisión:** Trabajar exclusivamente en logotipo principal, símbolo, favicon y paleta básica.
- **Fuera de alcance:** app, web, Notion, base de lugares, modelo de datos funcional, mockups, papelería, señalética y extensiones de marca.
- **No bloquean el cierre:** tipografía, eslogan, tono editorial, tamaños mínimos, aplicaciones de marca y reglas avanzadas.
- **Desbloqueo:** Requiere una decisión explícita registrada aquí.
- **Cierre:** D014 registra el cierre técnico mínimo de esta fase sin autorizar una fase posterior.

## D007 — Formato de maestros visuales

- **Estado:** Bloqueada
- **Registrada:** 2026-08-30
- **Decisión:** Los maestros de logo, símbolo y favicon deben conservarse como SVG vectoriales.
- **Regla:** No rasterizarlos ni sustituirlos por PNG, JPG u otro derivado.

## D008 — Protección contra reinterpretaciones

- **Estado:** Bloqueada
- **Registrada:** 2026-08-30
- **Decisión:** No reinterpretar arbitrariamente elementos aprobados.
- **Implicación:** Cualquier rediseño, simplificación, recoloreado o cambio geométrico requiere solicitud y aprobación explícitas.

## D009 — Registro de cambios futuros

- **Estado:** Aprobada
- **Registrada:** 2026-08-30
- **Decisión:** Toda aprobación que cambie el estado de la marca debe añadirse a este registro.
- **Contenido mínimo:** identificador, fecha, estado, decisión, motivo y archivos afectados.

## D010 — Logotipo principal canónico

- **Estado:** Aprobada
- **Registrada:** 2026-08-30
- **Decisión:** `brand/logo/lugazgo-primary.svg` es el logotipo principal canónico.
- **Origen preservado:** `brand/references/recovered-assets/integration-wordmark/lugazgo-logo-corregido.svg`.
- **SHA-256 de origen y destino:** `D23C1D5D247AAEC262C6BB56B9DF7FF6522FBF9E4B25A69B2F9256F51A4C6BFC`.
- **Motivo:** Se aprobó expresamente la precedencia de la composición corregida.
- **Archivos afectados:** `brand/logo/lugazgo-primary.svg` y `brand/logo/README.md`.
- **Integridad:** El destino debe conservar una coincidencia byte a byte con el origen; no se autorizan cambios de geometría, color, `viewBox`, trazados ni estructura interna.

## D011 — Símbolo principal canónico

- **Estado:** Aprobada
- **Registrada:** 2026-08-30
- **Decisión:** `brand/logo/lugazgo-symbol.svg` es el símbolo principal canónico.
- **Origen preservado:** `brand/references/recovered-assets/integration-wordmark/lugazgo-o-maestra.svg`.
- **SHA-256 de origen y destino:** `37CD431BA3AB93417171096092E8D32FC2F38B6DB6A59DAA495AC7A8931D823F`.
- **Motivo:** Se aprobó expresamente la precedencia de la `O` maestra.
- **Archivos afectados:** `brand/logo/lugazgo-symbol.svg` y `brand/logo/README.md`.
- **Integridad:** El destino debe conservar una coincidencia byte a byte con el origen; no se autorizan cambios de geometría, color, `viewBox`, trazados ni estructura interna.

## D012 — Favicon canónico y derivados por tamaño

- **Estado:** Aprobada
- **Registrada:** 2026-08-30
- **Decisión:** `brand/logo/favicon.svg` es el favicon canónico y procede de la versión optimizada de 32 px. Las versiones de 16, 24 y 32 px se conservan como derivados válidos, no como candidatos enfrentados.
- **Origen del maestro:** `brand/references/recovered-assets/vector-kit/lugazgo-favicon-32.svg`.
- **SHA-256 del maestro, su origen y el derivado de 32 px:** `DD59C6B939CA2187DA3D7AE706327CC420C723C36873B7EE8FB1174F1D5451E7`.
- **Derivado de 16 px:** `brand/logo/lugazgo-favicon-16.svg`, desde `brand/references/recovered-assets/vector-kit/lugazgo-favicon-16.svg`, SHA-256 `3506CDB17A18098472B3C05FF0DBC7D4DFE4DEC63494ED82B18ED9650A6079C8`.
- **Derivado de 24 px:** `brand/logo/lugazgo-favicon-24.svg`, desde `brand/references/recovered-assets/vector-kit/lugazgo-favicon-24.svg`, SHA-256 `7E40232451E3672B6F6A94B9EA9B053706EE85D1768CFA6B24769EFB9B0B86EA`.
- **Derivado de 32 px:** `brand/logo/lugazgo-favicon-32.svg`, desde `brand/references/recovered-assets/vector-kit/lugazgo-favicon-32.svg`, SHA-256 `DD59C6B939CA2187DA3D7AE706327CC420C723C36873B7EE8FB1174F1D5451E7`.
- **Motivo:** Cada variante contiene una optimización específica para su tamaño objetivo.
- **Archivos afectados:** `brand/logo/favicon.svg`, `brand/logo/lugazgo-favicon-16.svg`, `brand/logo/lugazgo-favicon-24.svg`, `brand/logo/lugazgo-favicon-32.svg` y `brand/logo/README.md`.
- **Integridad:** Cada destino debe coincidir byte a byte con su origen.

## D013 — Paleta básica oficial

- **Estado:** Aprobada
- **Registrada:** 2026-08-30
- **Decisión:** La paleta oficial conserva la dirección suave, orgánica y pastel y queda fijada por estos valores: Tierra Suave `#8B7058`, Verde Salvia `#8F9D76`, Azul Brumoso `#91B5C8`, Verde Liquen `#C1CCAD`, Marfil Cálido `#F1E5D2`, Tierra Oscura `#55483D` y Terracota Mineral `#C98E72`.
- **Motivo:** Se aprobaron expresamente los nombres y valores HEX necesarios para cerrar la paleta básica.
- **Archivos afectados:** `brand/colors/README.md`, `docs/decisions.md`, `docs/roadmap.md`, `docs/brand-context.md` y `README.md`.
- **Sustituye a:** D004 en cuanto a la especificación exacta que estaba pendiente.
- **Límite:** No aprueba jerarquías, combinaciones, equivalencias ni reglas avanzadas de uso.

## D014 — Cierre técnico mínimo de la Fase 0

- **Estado:** Aprobada
- **Registrada:** 2026-08-30
- **Decisión:** Se cierra técnicamente la Fase 0 con alcance exclusivo de logotipo, símbolo, favicon y paleta básica.
- **Motivo:** Los tres maestros SVG y los derivados de favicon tienen procedencia e integridad registradas, y la paleta básica dispone de valores exactos aprobados.
- **No bloquean el cierre:** tipografía, eslogan, tono editorial, tamaños mínimos, aplicaciones de marca y reglas avanzadas.
- **Fases futuras:** El cierre no autoriza una aplicación, la elección de un framework ni el inicio implícito de ninguna fase posterior.
- **Archivos afectados:** `AGENTS.md`, `README.md`, `brand/logo/README.md`, `brand/colors/README.md`, `docs/brand-context.md`, `docs/decisions.md` y `docs/roadmap.md`.

## A001 — Disponibilidad de activos durante la migración

- **Estado:** No disponible
- **Auditada:** 2026-08-30
- **Resultado:** No había archivos en `sources/` ni adjuntos accesibles en la conversación de migración.
- **Faltan:** `lugazgo-primary.svg`, `lugazgo-symbol.svg` y `favicon.svg` auténticos.
- **Acción permitida:** incorporar los originales cuando se recuperen, sin reinterpretarlos.

## A002 — Activos vectoriales recuperados y ordenados

- **Estado al auditar:** Pendiente de validación
- **Auditada:** 2026-08-30
- **Resultado:** Se localizaron 16 SVG nativos, 3 PDF vectoriales y 2 paquetes ZIP. Los SVG son XML válido, tienen `viewBox` y no contienen imágenes embebidas, Base64, scripts, filtros ni enlaces externos. Los PDF son exportaciones vectoriales de una página, sin imágenes raster ni fuentes.
- **Organización:** Los activos extraídos se conservaron sin renombrar ni modificar en `brand/references/recovered-assets/`; los ZIP originales se archivaron en `archive/source-packages/`.
- **Discrepancias:** Existen dos composiciones distintas del logotipo, dos representaciones estructurales de la misma geometría del símbolo, varias opciones de favicon y valores cromáticos que no constaban como aprobados en la migración.
- **Regla:** Esta recuperación no aprueba un maestro ni una paleta. El mapeo a `lugazgo-primary.svg`, `lugazgo-symbol.svg` y `favicon.svg`, así como los colores exactos, requiere una decisión explícita posterior.
- **Trazabilidad:** `brand/references/recovered-assets/README.md` documenta el inventario y `SHA256SUMS.txt` fija la integridad de los archivos.
- **Resolución posterior:** D010, D011, D012 y D013 registran la validación expresa y los mapeos aprobados sin modificar el material recuperado.

## P001 — Especificaciones todavía abiertas

- **Estado al registrar:** Pendiente
- **Registrada:** 2026-08-30
- **Incluye:** paleta exacta, tipografía, geometría exacta, espaciados, versiones cromáticas, tamaños mínimos y reglas de uso.
- **Nota:** No se consideran necesarias para inventar en la migración; se resolverán mediante decisiones futuras dentro del alcance autorizado.
- **Resolución posterior:** D010, D011 y D012 fijan los maestros gráficos; D013 resuelve la paleta exacta; D014 deja el resto fuera del alcance y de los bloqueos de cierre de la Fase 0.

## Plantilla para una decisión nueva

```markdown
## D0XX — Título

- **Estado:** Propuesta | Aprobada | Bloqueada | Sustituida
- **Fecha:** AAAA-MM-DD
- **Decisión:** Qué se decidió exactamente.
- **Motivo:** Por qué se decidió.
- **Archivos afectados:** Rutas concretas o “ninguno”.
- **Sustituye a:** Identificador anterior, si aplica.
```
