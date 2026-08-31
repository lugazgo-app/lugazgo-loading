# Decisiones pendientes de la Fase 1

Este registro separa cuestiones no aprobadas de las decisiones ya cerradas en `../decisions.md`. Ningún punto se completa por inferencia.

## Pendientes antes de adaptar Notion o ejecutar el piloto

| ID | Decisión necesaria | Motivo |
|---|---|---|
| F1-P01 | Inspeccionar la estructura actual de la base `Destinos` y aprobar su mapeo al modelo conceptual. | La base existe, pero su esquema no está disponible en el espejo local. |
| F1-P02 | Designar, si procede, revisores de fuentes distintos de Jerónimo y definir sustituciones. | El paso a `verificado` exige revisión, pero solo está fijada la autoridad final. |
| F1-P03 | Aprobar el comportamiento público mientras un destino está en `revisión`. | Estado editorial y visibilidad pública no deben confundirse. |
| F1-P04 | Calibrar con expedientes reales las anclas de masificación y la matriz de fragilidad. | Los pesos y vetos están aprobados; los límites operativos deben probarse. |
| F1-P05 | Aprobar los campos y filtros públicos exactos del catálogo y del mapa. | Las funciones están definidas, no su taxonomía de interfaz. |
| F1-P06 | Decidir si la puntuación y sus componentes serán públicos o solo internos. | La transparencia puede ayudar, pero también simplificar en exceso el juicio editorial. |
| F1-P07 | Fijar el mínimo de medios por ficha y la política cuando no haya fotografía publicable. | Los derechos están regulados, no el requisito editorial de cobertura visual. |
| F1-P08 | Aprobar un protocolo de emergencia para cierres, riesgos o peticiones de retirada cuando Jerónimo no esté disponible. | La autoridad está clara, pero falta continuidad operativa. |

## Pendientes antes del desarrollo técnico

| ID | Decisión necesaria | Motivo |
|---|---|---|
| F1-P09 | Elegir exportación manual o sincronización automatizada, formato, frecuencia y recuperación ante fallos. | Notion es maestro editorial, pero la integración no está autorizada todavía. |
| F1-P10 | Definir valores y reglas definitivas de `publication_visibility`. | El modelo separa estado y visibilidad, pero no impone una solución técnica. |
| F1-P11 | Elegir proveedor de mapas y reglas para abrir indicaciones sin filtrar ubicaciones. | Se aplaza junto con arquitectura y privacidad. |
| F1-P12 | Definir analítica, consentimiento, retención y método de cálculo de sesiones y acciones. | Las métricas están aprobadas, no su instrumentación. |
| F1-P13 | Concretar almacenamiento local, caducidad y eliminación de destinos guardados. | Guardar localmente está dentro del MVP, no su implementación. |
| F1-P14 | Definir accesibilidad funcional y criterios de aceptación de la experiencia pública. | Debe resolverse antes de construir y probar la interfaz. |

## Pendientes antes del escalado territorial

| ID | Decisión necesaria | Motivo |
|---|---|---|
| F1-P15 | Definir la división territorial portuguesa equivalente para el objetivo de hasta 10 destinos. | El modelo es flexible, pero la cuota necesita una unidad inequívoca. |
| F1-P16 | Aprobar umbrales editoriales de capacidad y tiempos operativos tras medir el piloto. | No existen aún datos reales sobre coste de investigación y mantenimiento. |
| F1-P17 | Decidir cuándo incorporar portugués, lenguas territoriales e inglés y quién revisará las traducciones. | El modelo las admite; solo español está aprobado para la primera versión. |
| F1-P18 | Aprobar explícitamente el escalado tras evaluar el piloto. | El piloto no activa automáticamente la cobertura completa. |

## Decisiones deliberadamente aplazadas

No forman parte de la Fase 1 documental: framework, lenguaje, base de datos, arquitectura, hosting, proveedor de despliegue, CI/CD, monetización y calendario de desarrollo. Tampoco se modifica IONOS, DNS, dominio, correo o Netlify.
