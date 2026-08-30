# Propuesta de valor y alcance del MVP

**Estado:** decisiones de producto aprobadas.

**Ámbito futuro:** España y Portugal.

**Idioma inicial:** español, con el modelo preparado para traducciones.

## Problema

La información sobre pueblos, pedanías, espacios naturales y patrimonio menos conocido está dispersa, presenta calidad desigual y con frecuencia no permite distinguir entre un descubrimiento compatible con una visita responsable y un lugar masificado, frágil, inseguro o mal documentado.

Quienes buscan tranquilidad, naturaleza, cultura o patrimonio deben invertir demasiado esfuerzo en verificar si un lugar encaja con sus intereses, cómo puede visitarse legalmente y qué impacto puede tener su difusión.

## Propuesta de valor

LugazGO ofrece una selección editorial pequeña, trazable y responsable de lugares con interés diferencial fuera del circuito turístico habitual. Cada destino se investiga, evalúa y aprueba humanamente antes de publicarse, con información suficiente para descubrirlo sin ocultar restricciones, riesgos o límites de acceso.

El valor no reside en acumular el mayor número de lugares, sino en reducir el ruido, justificar la selección y proteger aquello cuya difusión exige cautela.

## Públicos iniciales

- personas que buscan tranquilidad y desconexión;
- viajeros interesados en naturaleza, cultura y patrimonio;
- público sensible a la sostenibilidad y al impacto del turismo.

## Acción principal

> Encontrar un lugar desconocido que encaje con los intereses del usuario, consultar su ficha y guardarlo, compartirlo o mostrar intención de visitarlo.

## Dos capas del MVP

### A. Sistema editorial interno

Debe permitir definir posteriormente una solución para:

- gestionar candidatos;
- investigar y verificar afirmaciones;
- registrar fuentes, fechas y licencias;
- calcular y justificar la evaluación editorial;
- aplicar revisión y aprobación humana;
- controlar qué información puede publicarse;
- publicar, revisar, retirar y archivar con trazabilidad.

Durante el piloto, Notion será la fuente maestra de esta capa.

### B. Experiencia pública mínima

La futura primera versión debe incluir:

- exploración mediante listado o tarjetas;
- mapa;
- búsqueda por nombre, alias o territorio;
- filtros básicos por categorías y atributos editoriales que se determinen;
- ficha individual del destino;
- guardado local sin cuenta;
- función de compartir;
- apertura de indicaciones únicamente cuando sea seguro mostrar la ubicación.

El mapa y cualquier acción de navegación deben respetar `EXACTA`, `APROXIMADA` u `OCULTA`. La ficha no puede reconstruir ni filtrar una localización protegida mediante URLs, metadatos o datos internos.

## Funciones excluidas de la primera versión

- registro o perfiles de usuarios;
- sincronización de guardados entre dispositivos;
- comentarios y valoraciones públicas;
- reservas;
- marketplace;
- rutas complejas o planificador de itinerarios;
- gamificación;
- planes de pago;
- aportaciones públicas sin moderación;
- anuncios, promociones o publicaciones pagadas;
- publicación automática por IA;
- consulta directa de Notion desde el navegador.

## Idiomas y nombres

- La interfaz y el contenido inicial estarán en español.
- Cada destino tendrá una identidad única, independiente de sus traducciones.
- Se conservará el topónimo oficial y podrán registrarse variantes locales, portuguesas, cooficiales e históricas.
- Portugués será el siguiente idioma prioritario; inglés se valorará después.
- Los contenidos traducibles se mantendrán separados del registro central para no duplicar destinos.
- Las lenguas territoriales podrán incorporarse progresivamente sin bloquear el MVP.

## Objetivos iniciales de validación

| Indicador | Objetivo inicial |
|---|---:|
| Sesiones que pasan del catálogo o mapa a una ficha | al menos 35 % |
| Sesiones con guardar, compartir o consultar cómo llegar | al menos 10 % |
| Participantes que encuentran sin ayuda un destino relevante | al menos 8 de cada 10 |
| Participantes que descubren algo nuevo y considerarían visitarlo | al menos 7 de cada 10 |

Estas cifras sirven para validar la hipótesis del MVP. No son compromisos comerciales ni autorizan por sí solas el escalado.

## Principios de producto

1. **Selección antes que volumen.** La cuota futura es un máximo, no una obligación de rellenar territorios con candidatos débiles.
2. **Evidencia antes que afirmación.** Las afirmaciones relevantes deben poder rastrearse hasta sus fuentes.
3. **Protección antes que alcance.** La difusión se limita cuando pueda causar daño.
4. **Aprobación humana antes que publicación.** Ninguna automatización publica destinos.
5. **Datos mínimos públicos.** Solo se exporta lo necesario y autorizado para la experiencia pública.
