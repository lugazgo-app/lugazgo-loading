# Modelo conceptual de datos de destinos

**Estado:** modelo documental de Fase 1. No constituye un esquema de base de datos ni elige tecnología.

## Principios

- Un destino existe una sola vez, con independencia de idiomas, aliases o categorías.
- Los datos editoriales internos se separan de la proyección pública.
- Las afirmaciones importantes se relacionan con fuentes concretas.
- Las coordenadas internas sensibles nunca se exportan por defecto.
- El historial editorial es inmutable y registra quién hizo cada cambio.
- El modelo admite España y Portugal sin fijar todavía la equivalencia territorial portuguesa para la cuota futura.
- No se almacenan credenciales ni datos personales innecesarios.

## Entidades

| Entidad | Finalidad |
|---|---|
| `Destino` | Identidad estable y gobierno editorial del lugar. |
| `ContenidoIdioma` | Texto traducible por destino e idioma. |
| `NombreAlternativo` | Topónimos oficiales, locales, históricos y aliases. |
| `Territorio` | Jerarquía administrativa y geográfica flexible. |
| `Localizacion` | Coordenadas internas, precisión pública y sensibilidad. |
| `Categoria` / `DestinoCategoria` | Taxonomía principal y secundaria. |
| `EvaluacionEditorial` | Requisitos, notas, total, riesgos y recomendación. |
| `CondicionAcceso` | Acceso, permisos, cierres, horarios, cupos y estacionalidad. |
| `Fuente` | Procedencia bibliográfica o institucional. |
| `Afirmacion` / `AfirmacionFuente` | Trazabilidad entre hechos publicados y evidencias. |
| `Medio` | Fotografías u otros recursos con licencia y atribución. |
| `Revision` | Revisiones programadas o provocadas por cambios. |
| `HistorialEstado` | Auditoría de transiciones y decisiones humanas. |
| `Publicacion` | Versión y fecha de la proyección pública autorizada. |

## Destino

| Campo conceptual | Obligatorio | Público | Descripción |
|---|---:|---:|---|
| `destination_id` | sí | sí | Identificador estable, independiente de Notion y del nombre. |
| `notion_record_id` | durante piloto | no | Referencia al registro maestro en “Destinos”. |
| `editorial_state` | sí | no | Estado del flujo editorial. |
| `publication_visibility` | sí | no | Control independiente de si la proyección pública está visible. Sus valores exactos siguen pendientes. |
| `official_name` | sí | sí | Topónimo oficial conservado sin traducir. |
| `official_name_language` | sí | sí | Idioma o contexto lingüístico del topónimo. |
| `primary_category_id` | sí | sí | Categoría principal para filtros y cuotas. |
| `country_code` | sí | sí | España o Portugal mediante código normalizado. |
| `municipality_or_equivalent` | sí | sí | Municipio o unidad local equivalente. |
| `short_editorial_key` | sí | no | Clave estable legible para control editorial; no sustituye al identificador. |
| `sensitivity_level` | sí | no | Nivel de fragilidad o sensibilidad vigente. |
| `location_precision` | sí | sí | `EXACTA`, `APROXIMADA` u `OCULTA`. |
| `verification_type` | sí desde verificado | sí | `Verificado documentalmente` o `Visitado por LugazGO`. |
| `created_at` | sí | no | Fecha de alta. |
| `updated_at` | sí | no | Última modificación del expediente. |
| `published_at` | si se publica | sí | Primera publicación. |
| `last_verified_at` | desde verificado | sí | Fecha de última verificación editorial. |
| `next_review_at` | desde aprobado | no | Próxima revisión prevista. |
| `editorial_owner` | sí en investigación | no | Responsable operativo del expediente. |

`Visitado por LugazGO` es un atributo verificable adicional; nunca se infiere de la verificación documental.

## Contenido por idioma

Cada fila pertenece a un destino y un idioma. No se duplica el destino.

| Campo | Obligatorio para publicar en ese idioma | Descripción |
|---|---:|---|
| `language_code` | sí | Idioma del contenido. |
| `display_name` | sí | Nombre mostrado; no altera el topónimo oficial. |
| `slug` | sí | Identificador legible único dentro del idioma. |
| `short_summary` | sí | Resumen para tarjeta y resultados. |
| `description` | sí | Texto público original y factual. |
| `why_it_matters` | sí | Singularidad y motivos editoriales de selección. |
| `highlights` | sí | Lista estructurada de elementos principales. |
| `responsible_visit_guidance` | sí | Pautas de bajo impacto. |
| `access_summary` | sí | Condiciones de acceso vigentes. |
| `safety_summary` | cuando aplique | Advertencias sin sustituir información oficial. |
| `accessibility_summary` | cuando haya evidencia | Información disponible sobre accesibilidad. |
| `best_time_guidance` | cuando aplique | Estacionalidad sin promover periodos sensibles. |
| `translation_status` | sí | Borrador, revisada o aprobada. |
| `translator_or_source` | si traducido | Autoría o procedencia de la traducción. |

La publicación inicial exige contenido español aprobado. Otros idiomas son opcionales hasta que se autoricen.

## Nombres alternativos

| Campo | Descripción |
|---|---|
| `name` | Forma alternativa. |
| `language_code` | Idioma cuando se conozca. |
| `name_type` | Oficial alternativo, local, cooficial, portugués, histórico o alias de búsqueda. |
| `validity_or_period` | Vigencia o periodo histórico si aplica. |
| `source_id` | Fuente que respalda la forma. |
| `is_public` | Permite excluir notas internas o formas dudosas. |

## Territorio

La jerarquía no se limita a columnas fijas. Cada territorio tiene `territory_id`, `name`, `country_code`, `territory_type`, `parent_territory_id`, identificador oficial cuando exista y fuente.

Debe poder representar país, comunidad o región, provincia, distrito, región autónoma, municipio y otras unidades necesarias. La unidad portuguesa equivalente a provincia para el objetivo futuro sigue pendiente de aprobación; el modelo no la presupone.

## Localización

| Campo | Público | Descripción |
|---|---:|---|
| `internal_latitude` / `internal_longitude` | no | Coordenada de trabajo, con acceso restringido. |
| `internal_accuracy` | no | Precisión y método de obtención. |
| `public_latitude` / `public_longitude` | solo si procede | Coordenada exacta o punto desplazado autorizado. |
| `location_precision` | sí | Nivel aprobado. |
| `location_description` | sí | Área comunicable cuando no se muestran coordenadas. |
| `directions_allowed` | sí | Indica si se puede abrir navegación externa. |
| `location_source_id` | no | Fuente usada para comprobar la ubicación. |
| `location_verified_at` | no | Fecha de comprobación cruzada. |
| `sensitivity_reason` | no | Justificación protegida. |
| `embargo_or_authority_request` | no | Restricción y evidencia asociada. |

La exportación elimina siempre las coordenadas internas. `OCULTA` no debe incluir enlaces, metadatos de medios ni textos que permitan reconstruir la posición.

## Categorías

La taxonomía parte de las categorías aprobadas y admite jerarquía futura. `DestinoCategoria` indica si la categoría es principal o secundaria y conserva la justificación editorial.

No se crean categorías para negocios, alojamientos, eventos o grandes ciudades en el MVP.

## Evaluación editorial

Cada evaluación conserva una versión y no sobrescribe evaluaciones anteriores.

Campos mínimos:

- identificador de destino, versión, evaluador y fecha;
- resultado y evidencia de cada requisito obligatorio;
- seis notas de 0 a 5 y seis contribuciones ponderadas;
- total sobre 100 y umbral aplicado;
- indicadores de masificación y conclusión de veto;
- evaluación de autenticidad;
- probabilidad, gravedad y riesgo residual de fragilidad;
- nivel de precisión recomendado;
- recomendación: continuar, verificar, aprobar, revisar o archivar;
- observaciones y fuentes relacionadas.

## Condiciones de acceso

Puede haber varias condiciones con distinta vigencia:

- tipo y legalidad del acceso;
- titular o gestor responsable cuando sea público;
- horarios, cierre o apertura;
- permiso, reserva, cupo o tarifa oficial;
- estacionalidad y periodo de aplicación;
- modo de acceso y limitaciones de movilidad;
- riesgo o advertencia conocida;
- URL y contacto oficial cuando sean publicables;
- fecha de inicio, fecha de fin, última comprobación y próxima revisión;
- fuente que confirma la condición.

Un cierre vigente o una restricción crítica debe poder retirar la información de navegación sin borrar el historial.

## Fuentes y afirmaciones

`Fuente` contiene: título, organización o autor, tipo, URL o referencia, fecha de publicación, fecha de consulta, territorio, idioma, licencia si aplica, nivel de calidad y notas internas.

`Afirmacion` contiene: texto factual normalizado, categoría del hecho, criticidad, estado de verificación, fecha de vigencia y si puede publicarse.

`AfirmacionFuente` relaciona muchas fuentes con muchas afirmaciones e indica si cada fuente confirma, contradice o contextualiza. Así se conservan discrepancias sin ocultarlas.

## Medios y licencias

Cada medio registra:

- identificador, destino y tipo de recurso;
- archivo o referencia de origen;
- autor y titular de derechos;
- procedencia y URL original;
- licencia, versión y prueba del permiso;
- atribución obligatoria;
- restricciones de uso y fecha de caducidad si existe;
- descripción y texto alternativo por idioma;
- fecha, ubicación sensible y decisión de eliminar metadatos;
- estado editorial: propuesto, derechos verificados, aprobado o rechazado.

Solo los medios con derechos verificados y aprobación pueden publicarse.

## Revisiones, estados y publicación

`Revision` registra motivo, alcance, responsable, fechas, hallazgos, cambios requeridos y resolución. `HistorialEstado` registra estado anterior, nuevo estado, actor, fecha, motivo y evidencia de autorización.

`Publicacion` conserva versión, idioma, fecha, aprobador, huella o identificador del paquete exportado y lista de campos incluidos. Una nueva publicación no borra la trazabilidad de la anterior.

## Proyección pública permitida

Solo puede generarse cuando el destino está aprobado para publicación y la acción ha sido autorizada por Jerónimo Gamero Olivera. La proyección usa una lista positiva de campos y excluye:

- notas editoriales y evaluaciones internas no destinadas al público;
- coordenadas internas y motivos sensibles;
- credenciales, identificadores privados y datos personales;
- medios sin derechos verificados;
- fuentes o documentos con restricciones de redistribución;
- información caducada o pendiente de revisión crítica.

La decisión de mostrar o no la puntuación editorial al público sigue pendiente.
