# Flujo editorial, permisos y papel de Notion

**Estado:** estados, autoridad final y papel de Notion aprobados; algunos detalles operativos están pendientes en `07-decisiones-pendientes.md`.

## Flujo principal

`candidato → investigando → verificado → aprobado → publicado → revisión → archivado`

Las devoluciones para corregir un expediente no eliminan el historial. Archivar no equivale a borrar.

## Definición de estados

| Estado | Significado | Condiciones mínimas de entrada |
|---|---|---|
| `candidato` | Propuesta todavía no evaluada. | Nombre o referencia, territorio aproximado, categoría propuesta, origen y fecha de alta. |
| `investigando` | Expediente activo. | Responsable asignado, comprobación inicial de encaje y plan de fuentes. |
| `verificado` | La información ha superado revisión documental. | Requisitos obligatorios, dos fuentes independientes, comprobación de ubicación, vigencia, puntuación y riesgos documentados. |
| `aprobado` | Selección editorial autorizada humanamente. | Expediente verificado, contenido preparado, licencias y precisión revisadas; aprobación de Jerónimo. |
| `publicado` | Existe una proyección pública autorizada. | Aprobación de publicación de Jerónimo, versión exportable y fecha registrada. |
| `revisión` | El destino requiere revalidación programada o extraordinaria. | Motivo, alcance, responsable y prioridad registrados. |
| `archivado` | No continúa activo o se retira conservando trazabilidad. | Motivo y decisión de Jerónimo. |

`Verificado documentalmente` y `Visitado por LugazGO` son atributos de verificación, no estados alternativos.

## Transiciones y autoridad

| Transición | Quién puede prepararla | Quién la autoriza |
|---|---|---|
| candidato → investigando | asistentes, herramientas o Jerónimo | responsable editorial operativo |
| investigando → verificado | investigador | revisor de fuentes autorizado |
| verificado → investigando | revisor | revisor de fuentes autorizado, con motivos |
| verificado → aprobado | nadie de forma automática | solo Jerónimo |
| aprobado → publicado | preparación técnica futura | solo Jerónimo |
| publicado → revisión | asistentes o revisores pueden alertar | responsable editorial; la visibilidad se trata por separado |
| revisión → investigando | revisor | responsable editorial |
| revisión → publicado | preparación de correcciones | solo Jerónimo |
| cualquier estado → archivado | cualquiera puede proponer | solo Jerónimo |
| publicado → retirado de la vista pública | cualquiera puede alertar | solo Jerónimo, salvo una medida técnica de emergencia futura que deberá regularse |

Durante el piloto, si no se ha designado otro revisor de fuentes, Jerónimo asumirá también esa revisión. Ninguna IA puede aprobar, publicar, retirar o archivar.

## Controles de cada transición

Toda transición registra:

- estado anterior y nuevo;
- persona o herramienta que propuso el cambio;
- persona que lo autorizó cuando proceda;
- fecha y motivo;
- lista de comprobación aplicable;
- lagunas, excepciones o contradicciones;
- versión del expediente y de la rúbrica utilizada.

Las automatizaciones futuras podrán señalar campos incompletos, fechas vencidas o incoherencias, pero no sustituirán las decisiones reservadas a una persona.

## Notion durante el piloto

- La base maestra editorial se llama `Destinos`.
- Notion conserva candidatos, investigación, evaluaciones, fuentes, decisiones y estado.
- Antes de adaptar la base se deberá comparar su estructura real con el modelo conceptual; esta documentación no presupone que ya contenga todos los campos.
- Solo los destinos aprobados y cuya publicación haya autorizado Jerónimo pueden formar parte de una exportación pública.
- La web no consulta Notion directamente desde el navegador.
- Las credenciales no se incluyen en contenido, repositorio ni proyección pública.
- Los cambios públicos no escriben de vuelta en Notion durante el MVP.

## Relación futura con la aplicación

La dirección de datos autorizada para el piloto es unidireccional:

`Notion editorial → validación y lista positiva de campos → formato público controlado → aplicación`

Quedan para una fase técnica la elección entre exportación manual o sincronización automatizada, su frecuencia, el formato, el almacenamiento y la recuperación ante fallos.

El contrato futuro deberá garantizar:

1. selección exclusiva de registros autorizados;
2. exclusión de campos internos y coordenadas sensibles;
3. validación de datos obligatorios y licencias;
4. versión y trazabilidad de cada exportación;
5. retirada controlada y propagación de restricciones urgentes;
6. ausencia de secretos en el cliente público.

## Revisión programada y extraordinaria

Una revisión puede activarse por fecha prevista, cierre, cambio de acceso, incidente, petición de autoridad, cambio ambiental, licencia caducada, contradicción entre fuentes o señal de masificación.

El comportamiento público exacto de un destino mientras está en `revisión` requiere aprobación: puede permanecer visible, mostrar un aviso o retirarse temporalmente según el riesgo. Un riesgo grave, cierre oficial o petición fundada debe escalarse de inmediato a Jerónimo.
