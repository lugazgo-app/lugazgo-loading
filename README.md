# LugazGO

Repositorio principal consolidado de LugazGO. Mantiene la landing publicada en la raíz e incorpora la documentación, los maestros de marca y el historial del anterior `LugazGO-Codex-Starter`.

**Estado del paquete:** Fase 0 cerrada y Fase 1 activa para definición documental del producto y del sistema editorial.

**Fecha de consolidación:** 31 de agosto de 2026.

**Fase 0:** cerrada el 30 de agosto de 2026.

**Fase 1:** activa desde el 31 de agosto de 2026, sin desarrollo ni investigación territorial.

## Visión

LugazGO ayuda a descubrir lugares con encanto, tranquilos, poco masificados y menos explotados. La marca busca despertar curiosidad por destinos con carácter sin convertir el descubrimiento en una experiencia ruidosa o genérica.

## Propósito de este repositorio

Mantener en un único historial verificable la landing pública, los maestros de marca y las decisiones confirmadas de LugazGO. El repositorio registra lo pendiente y evita rellenar huecos con invenciones.

## Estado actual

Está confirmado:

- nombre: `LugazGO`;
- propósito centrado en lugares con encanto, tranquilos, poco masificados y menos explotados;
- personalidad minimalista, eco-friendly, premium, misteriosa y curiosa;
- dirección cromática suave, orgánica y pastel;
- concepto de la `O` distintiva con curvas topográficas diagonales tipo `ø` y un punto de ubicación aproximadamente central/superior derecho;
- logotipo principal canónico en `brand/logo/lugazgo-primary.svg`;
- símbolo principal canónico en `brand/logo/lugazgo-symbol.svg`;
- favicon principal en `brand/logo/favicon.svg` y derivados optimizados para 16, 24 y 32 px;
- paleta básica oficial documentada en `brand/colors/README.md`;
- alcance de la Fase 0 limitado a logo, símbolo, favicon y paleta básica;
- MVP con sistema editorial interno y experiencia pública mínima;
- Notion como fuente maestra editorial del piloto;
- modelo conceptual, política editorial, flujo y piloto documentados en `docs/phase-1/`;
- piloto previsto de 40 destinos, todavía sin selección ni investigación.

Queda fuera del cierre de la Fase 0 y no lo bloquea:

- tipografía;
- eslogan;
- tono editorial;
- tamaños mínimos;
- aplicaciones de marca y reglas avanzadas.

La geometría y estructura autoritativas son las de los SVG aprobados. La Fase 1 no modifica la identidad ni autoriza reconstruirla por inferencia.

## Landing publicada

La landing está formada por `CNAME`, `index.html`, `background-topografia.png` y el `lugazgo-primary.svg` de la raíz. Estos cuatro archivos se conservaron sin cambios durante la consolidación.

El SVG público de la raíz no coincide byte a byte con el maestro aprobado de `brand/logo/lugazgo-primary.svg`. La diferencia y sus hashes están registrados en D023 de `docs/decisions.md`; no se autoriza sustituir el activo público hasta completar una revisión separada.

## Fase 1

`docs/phase-1/` define la propuesta de valor, el MVP, los criterios editoriales, la puntuación, el modelo conceptual de datos, las transiciones, el papel de Notion, la trazabilidad, las licencias y el piloto.

Todavía no existen frontend, backend, base de datos, integración, destinos investigados ni configuración de despliegue. IONOS, DNS, dominio, correo y Netlify quedan fuera de alcance.

## Maestros canónicos y trazabilidad

`brand/logo/` contiene los tres maestros confirmados:

- `lugazgo-primary.svg` — logotipo principal;
- `lugazgo-symbol.svg` — símbolo independiente;
- `favicon.svg` — favicon maestro basado en la versión optimizada de 32 px.

También contiene `lugazgo-favicon-16.svg`, `lugazgo-favicon-24.svg` y `lugazgo-favicon-32.svg` como derivados válidos por tamaño. `brand/logo/README.md` registra el archivo de origen y el SHA-256 de cada maestro y derivado.

Los SVG de `brand/references/recovered-assets/` se conservan intactos. Las copias canónicas coinciden byte a byte con sus originales y se validaron como XML.

## Estructura

```text
lugazgo-loading/
├── AGENTS.md
├── README.md
├── CNAME
├── index.html
├── background-topografia.png
├── lugazgo-primary.svg
├── brand/
│   ├── logo/
│   │   ├── README.md
│   │   ├── lugazgo-primary.svg
│   │   ├── lugazgo-symbol.svg
│   │   ├── favicon.svg
│   │   ├── lugazgo-favicon-16.svg
│   │   ├── lugazgo-favicon-24.svg
│   │   └── lugazgo-favicon-32.svg
│   ├── colors/
│   │   └── README.md
│   └── references/
│       ├── README.md
│       └── recovered-assets/
│           ├── README.md
│           ├── SHA256SUMS.txt
│           ├── integration-wordmark/
│           └── vector-kit/
├── docs/
│   ├── brand-context.md
│   ├── decisions.md
│   ├── roadmap.md
│   └── phase-1/
│       ├── README.md
│       ├── 01-propuesta-valor-y-mvp.md
│       ├── 02-politica-editorial-y-evaluacion.md
│       ├── 03-modelo-conceptual-de-datos.md
│       ├── 04-flujo-editorial-y-notion.md
│       ├── 05-fuentes-licencias-y-actualizacion.md
│       ├── 06-plan-piloto.md
│       └── 07-decisiones-pendientes.md
├── data/
│   └── README.md
└── app/
    └── README.md
```

## Cómo empezar

1. Abre el repositorio `lugazgo-loading` como proyecto en Codex.
2. Lee `AGENTS.md`, `docs/decisions.md`, `docs/brand-context.md` y `docs/phase-1/README.md` antes de pedir cambios.
3. Usa `brand/logo/` como fuente de los maestros visuales y `brand/colors/README.md` como especificación de la paleta básica.
4. Consulta `brand/logo/README.md` y `docs/decisions.md` para verificar procedencia, SHA-256 y alcance.
5. Conserva `brand/references/recovered-assets/` como referencia intacta; no muevas ni modifiques esos archivos.
6. Usa `docs/phase-1/` para el trabajo documental autorizado; no inicies aplicación, integración, investigación territorial ni elección tecnológica sin una decisión posterior.

No ejecutes una inicialización que sobrescriba `AGENTS.md`; ya contiene las reglas específicas de LugazGO.

## Disciplina de cambios

Toda modificación futura que altere una decisión o un activo aprobado debe quedar registrada en `docs/decisions.md`. Una propuesta no modifica el estado oficial hasta recibir aprobación explícita.
