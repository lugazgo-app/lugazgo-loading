# LugazGO — Codex Starter

Paquete maestro de migración para abrir LugazGO como proyecto de Codex.

**Estado del paquete:** cierre técnico mínimo de la Fase 0 completado; maestros SVG, derivados de favicon y paleta básica aprobados y trazados.

**Fecha de la migración:** 30 de agosto de 2026.

**Fase 0:** cerrada el 30 de agosto de 2026; ninguna fase posterior está autorizada.

## Visión

LugazGO ayuda a descubrir lugares con encanto, tranquilos, poco masificados y menos explotados. La marca busca despertar curiosidad por destinos con carácter sin convertir el descubrimiento en una experiencia ruidosa o genérica.

## Propósito de este repositorio

Convertir el estado válido de LugazGO en una fuente maestra de archivos y decisiones. Este paquete no traslada conversaciones completas ni hipótesis descartadas: conserva únicamente lo confirmado, registra lo pendiente y evita rellenar huecos con invenciones.

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
- alcance de la Fase 0 limitado a logo, símbolo, favicon y paleta básica.

Queda fuera del cierre de la Fase 0 y no lo bloquea:

- tipografía;
- eslogan;
- tono editorial;
- tamaños mínimos;
- aplicaciones de marca y reglas avanzadas.

La geometría y estructura autoritativas son las de los SVG aprobados. No se han creado especificaciones nuevas ni se autoriza reconstruirlos por inferencia.

## Maestros canónicos y trazabilidad

`brand/logo/` contiene los tres maestros confirmados:

- `lugazgo-primary.svg` — logotipo principal;
- `lugazgo-symbol.svg` — símbolo independiente;
- `favicon.svg` — favicon maestro basado en la versión optimizada de 32 px.

También contiene `lugazgo-favicon-16.svg`, `lugazgo-favicon-24.svg` y `lugazgo-favicon-32.svg` como derivados válidos por tamaño. `brand/logo/README.md` registra el archivo de origen y el SHA-256 de cada maestro y derivado.

Los SVG de `brand/references/recovered-assets/` se conservan intactos. Las copias canónicas coinciden byte a byte con sus originales y se validaron como XML.

## Estructura

```text
LugazGO-Codex-Starter/
├── AGENTS.md
├── README.md
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
├── archive/
│   └── source-packages/
├── docs/
│   ├── brand-context.md
│   ├── decisions.md
│   └── roadmap.md
├── data/
│   └── README.md
└── app/
    └── README.md
```

## Cómo empezar

1. Abre la carpeta `LugazGO-Codex-Starter` como proyecto en Codex.
2. Lee `AGENTS.md`, `docs/decisions.md` y `docs/brand-context.md` antes de pedir cambios.
3. Usa `brand/logo/` como fuente de los maestros visuales y `brand/colors/README.md` como especificación de la paleta básica.
4. Consulta `brand/logo/README.md` y `docs/decisions.md` para verificar procedencia, SHA-256 y alcance.
5. Conserva `brand/references/recovered-assets/` como referencia intacta; no muevas ni modifiques esos archivos.
6. No inicies una aplicación, elijas framework ni actives otra fase sin una decisión explícita posterior.

No ejecutes una inicialización que sobrescriba `AGENTS.md`; ya contiene las reglas específicas de LugazGO.

## Disciplina de cambios

Toda modificación futura que altere una decisión o un activo aprobado debe quedar registrada en `docs/decisions.md`. Una propuesta no modifica el estado oficial hasta recibir aprobación explícita.
