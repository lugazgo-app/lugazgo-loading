# LugazGO — Fase 1: sistema de lugares y conocimiento

**Estado:** activa para definición documental desde el 31 de agosto de 2026.

**Autorización:** decisiones D015 a D022 de `../decisions.md`.

**Responsable de aprobación final:** Jerónimo Gamero Olivera.

## Objetivo

Definir, antes de desarrollar la aplicación, el MVP de LugazGO, sus criterios editoriales, el modelo conceptual de datos, el flujo de validación y el piloto de 40 destinos.

La Fase 1 produce especificaciones y decisiones. No produce frontend, backend, base de datos ejecutable, integración con Notion, selección territorial ni configuración de infraestructura.

## Documentos

| Documento | Contenido |
|---|---|
| `01-propuesta-valor-y-mvp.md` | Problema, propuesta de valor, públicos, funciones del MVP, exclusiones y métricas. |
| `02-politica-editorial-y-evaluacion.md` | Tipos admitidos, requisitos, exclusiones, puntuación y tratamiento de masificación, autenticidad y fragilidad. |
| `03-modelo-conceptual-de-datos.md` | Entidades, campos, relaciones, multilingüismo y proyección pública. |
| `04-flujo-editorial-y-notion.md` | Estados, transiciones, permisos, controles y papel de Notion. |
| `05-fuentes-licencias-y-actualizacion.md` | Evidencias, trazabilidad, calidad, vigencia, derechos y revisiones. |
| `06-plan-piloto.md` | Diseño y evaluación de la muestra de 40 destinos, sin identificar lugares concretos. |
| `07-decisiones-pendientes.md` | Cuestiones que todavía requieren aprobación humana o que se aplazan a una fase técnica. |

## Fuentes de verdad

Si existe una discrepancia, se aplica este orden:

1. instrucción explícita y reciente de la persona responsable;
2. decisiones aprobadas o bloqueadas en `../decisions.md`;
3. estos documentos de Fase 1;
4. `../roadmap.md` y el `README.md` del proyecto;
5. la auditoría inicial, únicamente como fotografía histórica de su fecha de corte.

## Límites

- La identidad visual cerrada en la Fase 0 permanece intacta.
- Notion es la fuente maestra editorial durante el piloto, pero no se modifica ni integra en esta fase documental.
- No se investigan ni incorporan todavía los 40 destinos.
- No se eligen framework, proveedor de mapas, base de datos, analítica, hosting ni mecanismo de sincronización.
- IONOS, dominio, DNS, correo, Netlify y credenciales quedan fuera de alcance.
