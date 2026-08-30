# LugazGO — Codex Starter

Paquete maestro de migración para abrir LugazGO como proyecto de Codex.

**Estado del paquete:** estructura y contexto consolidados; activos vectoriales recuperados y ordenados, pendientes de validación como maestros.  
**Fecha de la migración:** 30 de agosto de 2026.  
**Fase activa:** identidad visual básica, con alcance bloqueado.

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
- alcance actual limitado a logo, símbolo, favicon y paleta básica.

No está confirmado o no está aprobado todavía:

- qué SVG recuperado debe actuar como maestro canónico de logo, símbolo y favicon;
- valores cromáticos exactos;
- tipografía;
- geometría exacta de las curvas, el punto y el resto del logotipo;
- variantes o reglas de aplicación más amplias.

Por tanto, los archivos recuperados se mantienen como referencias trazables y **no se presentan automáticamente como maestros aprobados**.

## Activos recuperados pendientes de validación

La estructura sigue esperando estos tres SVG confirmados en `brand/logo/`:

- `lugazgo-primary.svg` — logotipo principal;
- `lugazgo-symbol.svg` — símbolo independiente;
- `favicon.svg` — favicon maestro.

Se localizaron 16 SVG y 3 PDF en dos conjuntos posteriores a la migración. Están inventariados, sin modificar, en `brand/references/recovered-assets/`. Consulta su `README.md` y `brand/logo/README.md` antes de elegir o copiar un maestro.

El kit recuperado también contiene una paleta con nombres y valores HEX. Esos datos permanecen pendientes de validación y no sustituyen una aprobación explícita.

## Estructura

```text
LugazGO-Codex-Starter/
├── AGENTS.md
├── README.md
├── brand/
│   ├── logo/
│   │   └── README.md
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
3. Revisa los activos recuperados y valida expresamente qué variantes son las oficiales.
4. Copia los SVG aprobados a `brand/logo/` sin rasterizarlos ni reinterpretarlos; conserva los originales y registra el mapeo en `docs/decisions.md`.
5. Documenta los valores exactos de la paleta únicamente cuando hayan sido aprobados.
6. Trabaja solo en logo, símbolo, favicon y paleta hasta que una nueva decisión desbloquee otra fase.

No ejecutes una inicialización que sobrescriba `AGENTS.md`; ya contiene las reglas específicas de LugazGO.

## Disciplina de cambios

Toda modificación futura que altere una decisión o un activo aprobado debe quedar registrada en `docs/decisions.md`. Una propuesta no modifica el estado oficial hasta recibir aprobación explícita.
