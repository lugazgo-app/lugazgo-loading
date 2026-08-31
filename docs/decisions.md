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
- **Resolución posterior:** D015 autoriza la definición documental de la Fase 1 sin reabrir ni modificar la Fase 0.

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
- **Resolución posterior:** D015 activa expresamente la Fase 1 documental; este cierre y todos sus límites visuales permanecen vigentes.

## D015 — Activación y alcance de la Fase 1

- **Estado:** Aprobada
- **Fecha:** 2026-08-31
- **Decisión:** Se activa la Fase 1 para definir documentalmente la propuesta de valor, el MVP, los criterios editoriales, el modelo conceptual de datos, el flujo de validación, el gobierno de fuentes y el piloto.
- **Incluye:** sistema editorial interno y definición de una experiencia pública mínima.
- **Excluye:** frontend, backend, base de datos ejecutable, integración con Notion, investigación territorial, incorporación de destinos, elección de framework o hosting y cambios de identidad visual.
- **Relación con fases anteriores:** No reabre la Fase 0. El modelo conceptual se incorpora a la Fase 1 por instrucción expresa, sustituyendo la separación anterior del roadmap sin autorizar su implementación técnica.
- **Archivos afectados:** `AGENTS.md`, `README.md`, `docs/roadmap.md`, `docs/phase-1/`, `app/README.md` y `data/README.md`.

## D016 — MVP, acción principal, métricas e idiomas

- **Estado:** Aprobada
- **Fecha:** 2026-08-31
- **Decisión:** El MVP tendrá una capa editorial interna y una experiencia pública con catálogo o tarjetas, mapa, búsqueda, filtros básicos, ficha, guardado local, compartir y apertura segura de indicaciones.
- **Acción principal:** Encontrar un lugar desconocido relevante, consultar su ficha y guardarlo, compartirlo o mostrar intención de visitarlo.
- **Métricas iniciales:** 35 % de paso a ficha; 10 % de acciones significativas; 8 de cada 10 participantes encuentran un destino sin ayuda; 7 de cada 10 descubren uno nuevo que considerarían visitar.
- **Idioma:** La primera versión será española y el modelo permitirá traducciones independientes sin duplicar destinos. Portugués será el siguiente idioma prioritario.
- **Exclusiones:** cuentas, comentarios, valoraciones, reservas, marketplace, rutas complejas, gamificación, pagos y aportaciones públicas sin moderación.
- **Archivos afectados:** `docs/phase-1/01-propuesta-valor-y-mvp.md` y `docs/phase-1/03-modelo-conceptual-de-datos.md`.

## D017 — Política de admisión y puntuación editorial

- **Estado:** Aprobada
- **Fecha:** 2026-08-31
- **Decisión:** La admisión combina requisitos obligatorios con una puntuación ponderada sobre 100 y umbral inicial de 70.
- **Pesos:** singularidad e interés diferencial 25; baja masificación 25; valor natural, cultural o patrimonial 20; visita responsable 15; calidad paisajística, narrativa o experiencial 10; calidad y trazabilidad 5.
- **Vetos:** Un requisito obligatorio incumplido no se compensa. La masificación alta veta la admisión y un riesgo ambiental, cultural, vecinal o de seguridad inaceptable impide publicar.
- **Categorías y exclusiones:** Se aplican las listas aprobadas en `docs/phase-1/02-politica-editorial-y-evaluacion.md`; los enclaves de municipios grandes quedan fuera del MVP salvo decisión futura.
- **Archivos afectados:** `docs/phase-1/02-politica-editorial-y-evaluacion.md`.

## D018 — Protección de ubicaciones y espacios sensibles

- **Estado:** Aprobada
- **Fecha:** 2026-08-31
- **Decisión:** Cada destino utiliza precisión `EXACTA`, `APROXIMADA` u `OCULTA`; ante una duda razonable sobre el impacto no se publican coordenadas exactas por defecto.
- **Bloqueos:** Prohibición o cierre, riesgo grave, acceso ilegal, expolio, sensibilidad ambiental o cultural, petición fundada de una autoridad e información insuficiente para una visita segura.
- **Implicación:** Las coordenadas internas sensibles no forman parte de la proyección pública y las indicaciones solo se habilitan cuando estén autorizadas.
- **Archivos afectados:** `docs/phase-1/02-politica-editorial-y-evaluacion.md` y `docs/phase-1/03-modelo-conceptual-de-datos.md`.

## D019 — Verificación, vigencia y licencias

- **Estado:** Aprobada
- **Fecha:** 2026-08-31
- **Decisión:** Un destino verificado requiere dos fuentes independientes y fiables, fuente oficial o primaria para restricciones cuando aplique, ubicación cruzada, fecha de revisión y trazabilidad de afirmaciones principales.
- **Vigencia:** 12 meses para acceso, cierres, horarios, permisos y restricciones; 24 meses para información general o confirmación de estabilidad.
- **Visita:** No es obligatoria para el piloto; se distingue `Verificado documentalmente` de `Visitado por LugazGO`.
- **Derechos:** Textos originales y medios propios, autorizados o con licencia compatible; material dudoso no se publica.
- **Archivos afectados:** `docs/phase-1/03-modelo-conceptual-de-datos.md` y `docs/phase-1/05-fuentes-licencias-y-actualizacion.md`.

## D020 — Gobierno editorial y papel de Notion

- **Estado:** Aprobada
- **Fecha:** 2026-08-31
- **Decisión:** Durante el piloto, la base de Notion `Destinos` será la fuente maestra editorial. Solo registros aprobados y autorizados para publicación podrán transferirse a la experiencia pública mediante un proceso controlado futuro.
- **Seguridad:** La web no consultará Notion directamente desde el navegador ni expondrá credenciales.
- **Autoridad:** Asistentes y herramientas pueden proponer e investigar. El paso a verificado exige revisión de fuentes. Solo Jerónimo Gamero Olivera puede aprobar, publicar, retirar o archivar. Ninguna IA publica automáticamente.
- **Estados:** `candidato → investigando → verificado → aprobado → publicado → revisión → archivado`.
- **Archivos afectados:** `docs/phase-1/04-flujo-editorial-y-notion.md`.

## D021 — Muestra piloto

- **Estado:** Aprobada
- **Fecha:** 2026-08-31
- **Decisión:** El piloto tendrá 40 destinos, aproximadamente 28 de España y 12 de Portugal, al menos 8 territorios administrativos, máximo 6 por territorio y máximo 40 % de una misma categoría principal.
- **Diversidad:** Incluirá núcleos habitados, naturaleza, patrimonio cultural e industrial o arqueológico, equilibrando interior, costa, montaña, ruralidad y accesibilidad.
- **Límite:** No se seleccionan ni investigan destinos todavía. El objetivo futuro de hasta 10 por provincia española y división portuguesa equivalente no se ejecuta antes de validar el piloto.
- **Archivos afectados:** `docs/phase-1/06-plan-piloto.md`.

## D022 — Infraestructura y servicios externos fuera de alcance

- **Estado:** Bloqueada
- **Fecha:** 2026-08-31
- **Decisión:** El dominio oficial y el correo corporativo existen en IONOS, con renovación automática y 2FA configurados. No se modifican IONOS, DNS, dominio, correo ni Netlify durante la Fase 1 documental.
- **También pendiente:** framework, proveedor de mapas, base de datos, hosting, analítica e integración técnica.
- **Archivos afectados:** `docs/phase-1/README.md`, `docs/phase-1/07-decisiones-pendientes.md` y `docs/roadmap.md`.

## D023 — Consolidación de repositorios sin sustituir el SVG público

- **Estado:** Aprobada
- **Fecha:** 2026-08-31
- **Decisión:** `lugazgo-app/lugazgo-loading` pasa a ser el repositorio remoto principal de LugazGO mediante la incorporación del historial y del alcance documental del Starter. La landing publicada se conserva inicialmente sin cambios.
- **Diferencia documentada:** El activo público `lugazgo-primary.svg` de la raíz tiene SHA-256 `3BDA4C8096ADF9FA43083658015E3A9ECFA20AA69465303AC7F63CB1D22AB9C9`; el maestro aprobado `brand/logo/lugazgo-primary.svg` tiene SHA-256 `D23C1D5D247AAEC262C6BB56B9DF7FF6522FBF9E4B25A69B2F9256F51A4C6BFC`. No son idénticos byte a byte.
- **Motivo:** Evitar interrupciones en la landing y separar la consolidación técnica de una futura revisión visual del activo publicado.
- **Regla:** No sustituir, normalizar ni redirigir el SVG público por inferencia. Cualquier cambio requiere una revisión y aprobación separadas.
- **Archivos afectados:** `docs/decisions.md`. Se conservan sin cambios `CNAME`, `index.html`, `background-topografia.png` y el `lugazgo-primary.svg` de la raíz.
- **Fuera de alcance:** Notion, IONOS, DNS, GitHub Pages y normalización o incorporación de Destinos.

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
