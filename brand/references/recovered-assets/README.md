# Activos vectoriales recuperados

**Estado:** material recuperado y ordenado; pendiente de validación como fuente oficial.

Esta carpeta conserva, sin modificar sus nombres ni su contenido, todos los activos gráficos localizados en la raíz de trabajo el 30 de agosto de 2026. Su presencia aquí no sustituye el estado pendiente de los maestros definido en `docs/decisions.md`.

## Contenido

### `integration-wordmark/`

Dos SVG que aparecieron sueltos y también dentro de `archive/source-packages/lugazgo-go-integracion-wordmark-svg.zip`:

- `lugazgo-logo-corregido.svg` — composición de logotipo con `viewBox` `0 0 3538 980`;
- `lugazgo-o-maestra.svg` — símbolo O con `viewBox` `0 0 1000 1000`.

### `vector-kit/`

Paquete encontrado originalmente como `lugazgo_vector/`:

- 14 SVG;
- 3 PDF de una página;
- `LEEME.txt`, conservado como nota de procedencia del paquete.

Incluye logotipo principal, símbolo, icono, tres favicons, cinco nombres de variante monocromática, paleta y láminas de previsualización.

## Comprobaciones técnicas

- Los 16 SVG recuperados son XML válido y contienen `viewBox`.
- Ningún SVG contiene `<image>`, datos Base64, scripts, filtros ni enlaces externos.
- `lugazgo-paleta.svg`, `lugazgo-previsualizacion-vectorial.svg` y `lugazgo-versiones-monocromaticas.svg` conservan texto vivo en Arial; son láminas de presentación, no maestros completamente trazados.
- Las dos láminas de presentación reutilizan identificadores XML; funcionan como documento visual, pero no conviene extraer nodos de ellas sin normalizar los identificadores.
- Los tres PDF son válidos, no cifrados, de una página y fueron exportados por Inkscape/Cairo. No contienen imágenes raster ni fuentes; se conservan como exportaciones vectoriales y no sustituyen a los SVG.
- `SHA256SUMS.txt` permite comprobar que los archivos recuperados no cambian.

## Ambigüedades detectadas

- `lugazgo-logo-corregido.svg` y `vector-kit/lugazgo-logo-principal.svg` no son equivalentes: cambian el encuadre y la colocación/escala de la G y la O. El nombre “corregido” y su aparición posterior sugieren una revisión, pero no constituyen una aprobación. El PDF del logo corresponde en proporción a la versión anterior.
- `lugazgo-o-maestra.svg` y `vector-kit/lugazgo-simbolo-o.svg` comparten geometría y colores, aunque difieren en estructura e identificadores XML.
- `vector-kit/lugazgo-logo-monocromo.svg` y `vector-kit/lugazgo-logo-monocromo-tierra-oscura.svg` son copias exactas, con el mismo SHA-256.
- No hay base suficiente para elegir cuál de los tres favicons o el icono debe convertirse en el futuro `favicon.svg` canónico.
- El kit declara geometría y colores exactos, mientras la documentación de migración los mantiene pendientes. La discrepancia debe resolverse mediante una aprobación explícita.

## Regla de uso

Tratar estos archivos como originales recuperados de procedencia conocida, pero no como maestros oficiales. Cuando se valide una opción, copiarla a `brand/logo/` sin sobrescribir este material, registrar el mapeo y la procedencia en `docs/decisions.md`, y mantener el nombre original documentado.
