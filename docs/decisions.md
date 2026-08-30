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

- **Estado:** Aprobada en concepto; especificación exacta Pendiente
- **Registrada:** 2026-08-30
- **Decisión:** Los colores deben sentirse suaves, orgánicos y pastel.
- **Pendiente:** Nombres y valores exactos de los colores, combinaciones, jerarquías y equivalencias.
- **Regla:** No inventar códigos HEX/RGB/CMYK/Pantone a partir de esta descripción.

## D005 — Concepto distintivo de la O

- **Estado:** Aprobada en concepto
- **Registrada:** 2026-08-30
- **Decisión:** La `O` incorpora curvas topográficas que la atraviesan diagonalmente, con lectura tipo `ø`, y un punto de ubicación aproximadamente en la zona central/superior derecha.
- **Pendiente:** Geometría exacta, cantidad y grosor de curvas, ángulo, proporciones, tamaño y posición precisa del punto.
- **Regla:** La descripción no autoriza una reconstrucción aproximada que se presente como maestro.

## D006 — Alcance de la fase actual

- **Estado:** Bloqueada
- **Registrada:** 2026-08-30
- **Decisión:** Trabajar exclusivamente en logotipo principal, símbolo, favicon y paleta básica.
- **Fuera de alcance:** app, web, Notion, base de lugares, modelo de datos funcional, mockups, papelería, señalética y extensiones de marca.
- **Desbloqueo:** Requiere una decisión explícita registrada aquí.

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

## A001 — Disponibilidad de activos durante la migración

- **Estado:** No disponible
- **Auditada:** 2026-08-30
- **Resultado:** No había archivos en `sources/` ni adjuntos accesibles en la conversación de migración.
- **Faltan:** `lugazgo-primary.svg`, `lugazgo-symbol.svg` y `favicon.svg` auténticos.
- **Acción permitida:** incorporar los originales cuando se recuperen, sin reinterpretarlos.

## A002 — Activos vectoriales recuperados y ordenados

- **Estado:** Pendiente de validación
- **Auditada:** 2026-08-30
- **Resultado:** Se localizaron 16 SVG nativos, 3 PDF vectoriales y 2 paquetes ZIP. Los SVG son XML válido, tienen `viewBox` y no contienen imágenes embebidas, Base64, scripts, filtros ni enlaces externos. Los PDF son exportaciones vectoriales de una página, sin imágenes raster ni fuentes.
- **Organización:** Los activos extraídos se conservaron sin renombrar ni modificar en `brand/references/recovered-assets/`; los ZIP originales se archivaron en `archive/source-packages/`.
- **Discrepancias:** Existen dos composiciones distintas del logotipo, dos representaciones estructurales de la misma geometría del símbolo, varias opciones de favicon y valores cromáticos que no constaban como aprobados en la migración.
- **Regla:** Esta recuperación no aprueba un maestro ni una paleta. El mapeo a `lugazgo-primary.svg`, `lugazgo-symbol.svg` y `favicon.svg`, así como los colores exactos, requiere una decisión explícita posterior.
- **Trazabilidad:** `brand/references/recovered-assets/README.md` documenta el inventario y `SHA256SUMS.txt` fija la integridad de los archivos.

## P001 — Especificaciones todavía abiertas

- **Estado:** Pendiente
- **Registrada:** 2026-08-30
- **Incluye:** paleta exacta, tipografía, geometría exacta, espaciados, versiones cromáticas, tamaños mínimos y reglas de uso.
- **Nota:** No se consideran necesarias para inventar en la migración; se resolverán mediante decisiones futuras dentro del alcance autorizado.

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
