# Auditoría inicial — LugazGO

**Fecha de corte:** 30 de agosto de 2026  
**Raíz física auditada:** `C:\Jero\PROYECTOS\PMD002_LugazGO`  
**Raíz lógica del proyecto:** `C:\Jero\PROYECTOS\PMD002_LugazGO\LugazGO-Codex-Starter`  
**Alcance:** inspección de todos los archivos y carpetas, estructura, documentación, formatos gráficos, dependencias, comandos, estado de Git y estado funcional.  
**Modificaciones realizadas durante esta tarea:** únicamente la creación de este informe. No se ha modificado código, configuración ni ningún recurso gráfico.

Este documento separa deliberadamente los hechos comprobados de las recomendaciones. Los activos recuperados se describen tal como existen, pero no se declaran maestros oficiales ni se aprueban decisiones de marca.

## 1. Hechos comprobados

### 1.1 Resumen ejecutivo

| Área | Estado comprobado |
|---|---|
| Naturaleza del proyecto | Repositorio estático de documentación e identidad visual; no es una aplicación ejecutable. |
| Fase activa | Fase 0: logotipo, símbolo, favicon y paleta básica. El alcance está bloqueado a estos elementos. |
| Inventario previo a este informe | 36 archivos, 14 directorios y 217.507 bytes. Este informe pasa a ser el archivo número 37. |
| Código fuente | No existe código de aplicación ni archivos fuente ejecutables. |
| Vectores | 16 SVG nativos y 3 PDF vectoriales. |
| Git | La raíz y el Starter no son repositorios Git. |
| Dependencias de software | No hay manifiestos, lockfiles ni dependencias instaladas en el proyecto. |
| Comandos | No existen comandos de instalación, ejecución, build, test, lint o despliegue. |
| Recursos oficiales | Los activos encontrados están recuperados y trazados, pero siguen pendientes de validación canónica. |
| `sources\` | Carpeta vacía y protegida como referencia de solo lectura por el `AGENTS.md` raíz. |

Antes de crear este informe se comprobaron 13 Markdown, 16 SVG, 3 PDF, 2 TXT y 2 ZIP. No había archivos vacíos, enlaces simbólicos, puntos de reanálisis, artefactos de compilación ni carpetas de dependencias. La única carpeta vacía era `sources\`.

### 1.2 Estructura completa

La estructura siguiente contiene todos los archivos existentes después de añadir este informe:

```text
C:\Jero\PROYECTOS\PMD002_LugazGO\
├── AGENTS.md
├── sources\
│   └── [vacía; referencia de solo lectura]
└── LugazGO-Codex-Starter\
    ├── AGENTS.md
    ├── README.md
    ├── app\
    │   └── README.md
    ├── archive\
    │   └── source-packages\
    │       ├── LugazGO-Codex-Starter.zip
    │       ├── lugazgo-go-integracion-wordmark-svg.zip
    │       └── README.md
    ├── brand\
    │   ├── colors\
    │   │   └── README.md
    │   ├── logo\
    │   │   └── README.md
    │   └── references\
    │       ├── README.md
    │       └── recovered-assets\
    │           ├── README.md
    │           ├── SHA256SUMS.txt
    │           ├── integration-wordmark\
    │           │   ├── lugazgo-logo-corregido.svg
    │           │   └── lugazgo-o-maestra.svg
    │           └── vector-kit\
    │               ├── LEEME.txt
    │               ├── lugazgo-favicon-16.svg
    │               ├── lugazgo-favicon-24.svg
    │               ├── lugazgo-favicon-32.svg
    │               ├── lugazgo-icono.svg
    │               ├── lugazgo-logo-monocromo-blanco.svg
    │               ├── lugazgo-logo-monocromo-negro.svg
    │               ├── lugazgo-logo-monocromo-tierra-oscura.svg
    │               ├── lugazgo-logo-monocromo-verde-salvia.svg
    │               ├── lugazgo-logo-monocromo.svg
    │               ├── lugazgo-logo-principal.pdf
    │               ├── lugazgo-logo-principal.svg
    │               ├── lugazgo-paleta.svg
    │               ├── lugazgo-previsualizacion-vectorial.pdf
    │               ├── lugazgo-previsualizacion-vectorial.svg
    │               ├── lugazgo-simbolo-o.pdf
    │               ├── lugazgo-simbolo-o.svg
    │               └── lugazgo-versiones-monocromaticas.svg
    ├── data\
    │   └── README.md
    └── docs\
        ├── AUDITORIA_INICIAL.md
        ├── brand-context.md
        ├── decisions.md
        └── roadmap.md
```

### 1.3 Tecnologías y formatos utilizados

| Tecnología o formato | Uso comprobado | Observaciones |
|---|---|---|
| Markdown | Reglas operativas, contexto de marca, registro de decisiones, roadmap, inventarios y placeholders. | Es el formato dominante de documentación. |
| SVG/XML | 16 archivos vectoriales. | Los 16 son XML válido, incluyen `viewBox` y no contienen imágenes embebidas, Base64, scripts, `foreignObject`, filtros ni enlaces HTTP externos. |
| PDF 1.5 | 3 exportaciones vectoriales. | Una página por archivo, sin cifrado, imágenes raster ni fuentes incrustadas. |
| ZIP | 2 paquetes fuente archivados. | Se conservan para trazabilidad; no son la versión de trabajo. |
| SHA-256 | Manifiesto de integridad y hashes de paquetes. | Las 20 entradas de `SHA256SUMS.txt` existen y coinciden con sus archivos. |
| Inkscape 1.4 | Metadato `Creator` de los tres PDF. | Describe la herramienta de exportación; no es una dependencia instalada o configurada por el proyecto. |
| Cairo 1.18.4 | Metadato `Producer` de los tres PDF. | Describe el productor PDF; no es una dependencia declarada por el proyecto. |
| Arial / `sans-serif` | Texto vivo de tres láminas SVG. | Arial no está incluida en el proyecto. El resto de logos y símbolos auditados usa geometría trazada. |

No se encontró ningún lenguaje de programación, framework, runtime, base de datos, servicio externo, API, sistema de build, contenedor ni configuración de hosting.

### 1.4 Dependencias

#### Dependencias declaradas

No existe ninguna. No se encontraron:

- `package.json`, `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock` o `bun.lockb`;
- `pyproject.toml`, `requirements*.txt`, `Pipfile` o `poetry.lock`;
- `Cargo.toml`, `go.mod`, `pom.xml`, archivos Gradle, `composer.json` o `Gemfile`;
- `Dockerfile`, Compose, `Makefile`, CMake, soluciones o proyectos .NET;
- `node_modules`, `.venv`, `vendor` ni otra carpeta de dependencias.

#### Dependencias ambientales de visualización

| Dependencia | Alcance | Estado |
|---|---|---|
| Visor/editor compatible con Markdown, SVG y PDF | Inspeccionar la documentación y los activos. | No está fijado un producto ni una versión. |
| Arial o su fallback `sans-serif` | Renderizar el texto vivo de `lugazgo-paleta.svg`, `lugazgo-previsualizacion-vectorial.svg` y `lugazgo-versiones-monocromaticas.svg`. | La fuente no está empaquetada; el aspecto puede variar si Arial no está instalada. |
| Codex | Flujo de trabajo sugerido en el README. | Herramienta de trabajo, no dependencia de código. |

### 1.5 Comandos de instalación, ejecución y verificación

No hay una aplicación que arrancar y no existe un punto de entrada.

| Operación | Comando disponible |
|---|---|
| Instalación | Ninguno. |
| Ejecución o servidor local | Ninguno. |
| Build o compilación | Ninguno. |
| Tests | Ninguno. |
| Lint o formateo | Ninguno. |
| Generación de activos | Ninguno documentado. |
| Despliegue | Ninguno. |

La búsqueda en todos los Markdown y TXT no encontró instrucciones para `npm`, `pnpm`, `yarn`, `node`, `python`, `pip`, `cargo`, `go`, `dotnet`, `gradle`, `maven`, `make` o `docker`. Los únicos bloques de código preexistentes eran un árbol de carpetas y una plantilla Markdown de decisión; ninguno es ejecutable.

El flujo documentado es manual:

1. abrir `LugazGO-Codex-Starter` en Codex;
2. leer `AGENTS.md`, `docs\decisions.md` y `docs\brand-context.md`;
3. validar qué activos recuperados son oficiales;
4. copiar los aprobados a `brand\logo\` sin alterar los originales;
5. registrar el mapeo y la decisión.

### 1.6 Estado de Git

Se ejecutaron estas comprobaciones:

```powershell
git -C "C:\Jero\PROYECTOS\PMD002_LugazGO" status --short --branch
git -C "C:\Jero\PROYECTOS\PMD002_LugazGO\LugazGO-Codex-Starter" status --short --branch
```

Ambas devolvieron:

```text
fatal: not a git repository (or any of the parent directories): .git
```

No existe `.git` en la raíz ni en el Starter. En consecuencia, no hay rama, commits, historial, tags, remotos ni estado de cambios versionado. Tampoco existe `.gitignore`.

### 1.7 Archivos SVG y rutas exactas

Todas las rutas de esta tabla son relativas a `C:\Jero\PROYECTOS\PMD002_LugazGO\LugazGO-Codex-Starter\`.

| Ruta exacta | Dimensiones declaradas | Contenido y estado comprobado |
|---|---|---|
| `brand\references\recovered-assets\integration-wordmark\lugazgo-logo-corregido.svg` | `viewBox 0 0 3538 980` | Wordmark trazado; revisión distinta de `lugazgo-logo-principal.svg`. No está aprobado como maestro. |
| `brand\references\recovered-assets\integration-wordmark\lugazgo-o-maestra.svg` | `viewBox 0 0 1000 1000` | Símbolo O trazado; misma geometría y colores que `lugazgo-simbolo-o.svg`, con estructura e identificadores diferentes. |
| `brand\references\recovered-assets\vector-kit\lugazgo-favicon-16.svg` | `viewBox 0 0 1000 1000`; `width/height 16` | O y punto; las curvas se omiten intencionadamente para 16 px. |
| `brand\references\recovered-assets\vector-kit\lugazgo-favicon-24.svg` | `viewBox 0 0 1000 1000`; `width/height 24` | O, punto y una curva topográfica. |
| `brand\references\recovered-assets\vector-kit\lugazgo-favicon-32.svg` | `viewBox 0 0 1000 1000`; `width/height 32` | O, punto y dos curvas topográficas. |
| `brand\references\recovered-assets\vector-kit\lugazgo-icono.svg` | `viewBox 0 0 1000 1000` | Símbolo sobre un fondo marfil `#F1E5D2` incorporado; no es transparente. |
| `brand\references\recovered-assets\vector-kit\lugazgo-logo-monocromo-blanco.svg` | `viewBox 0 0 3637 1120` | Versión blanca negativa con fondo `#55483D` incorporado. |
| `brand\references\recovered-assets\vector-kit\lugazgo-logo-monocromo-negro.svg` | `viewBox 0 0 3637 1120` | Wordmark monocromo negro, completamente trazado. |
| `brand\references\recovered-assets\vector-kit\lugazgo-logo-monocromo-tierra-oscura.svg` | `viewBox 0 0 3637 1120` | Copia exacta de `lugazgo-logo-monocromo.svg`. |
| `brand\references\recovered-assets\vector-kit\lugazgo-logo-monocromo-verde-salvia.svg` | `viewBox 0 0 3637 1120` | Variante monocroma verde salvia, completamente trazada. |
| `brand\references\recovered-assets\vector-kit\lugazgo-logo-monocromo.svg` | `viewBox 0 0 3637 1120` | Alias exacto de la variante tierra oscura; el nombre no identifica el color. |
| `brand\references\recovered-assets\vector-kit\lugazgo-logo-principal.svg` | `viewBox 0 0 3637 1120` | Integración anterior del wordmark, completamente trazada. Difiere en encuadre y transformaciones de la G y la O respecto a la versión “corregido”. |
| `brand\references\recovered-assets\vector-kit\lugazgo-paleta.svg` | `viewBox 0 0 1900 450` | Lámina de paleta con 14 nodos de texto vivo en Arial. |
| `brand\references\recovered-assets\vector-kit\lugazgo-previsualizacion-vectorial.svg` | `viewBox 0 0 2800 1800` | Lámina con 27 nodos de texto vivo y varios identificadores SVG repetidos. |
| `brand\references\recovered-assets\vector-kit\lugazgo-simbolo-o.svg` | `viewBox 0 0 1000 1000` | Símbolo O vectorial; geométricamente equivalente a `lugazgo-o-maestra.svg`. |
| `brand\references\recovered-assets\vector-kit\lugazgo-versiones-monocromaticas.svg` | `viewBox 0 0 3600 1800` | Lámina con 4 nodos de texto vivo y varios identificadores SVG repetidos. |

Comprobación común a los 16 SVG:

- XML válido;
- `viewBox` presente;
- cero elementos `<image>`;
- cero imágenes raster o datos Base64;
- cero scripts, `foreignObject` y filtros;
- cero enlaces HTTP externos.

### 1.8 Otros recursos gráficos y de trazabilidad

#### PDF

| Ruta exacta | Tamaño | Hechos comprobados |
|---|---:|---|
| `brand\references\recovered-assets\vector-kit\lugazgo-logo-principal.pdf` | 4.344 B | PDF 1.5, una página, vectorial, no cifrado. Sus proporciones corresponden al SVG principal anterior, no al wordmark “corregido”. |
| `brand\references\recovered-assets\vector-kit\lugazgo-previsualizacion-vectorial.pdf` | 107.744 B | PDF 1.5, una página, vectorial, no cifrado. |
| `brand\references\recovered-assets\vector-kit\lugazgo-simbolo-o.pdf` | 2.439 B | PDF 1.5, una página, vectorial, no cifrado. |

Los tres PDF indican `Creator: Inkscape 1.4` y `Producer: cairo 1.18.4`. No contienen recursos de imagen ni de fuente.

#### Paquetes ZIP

| Ruta exacta | Contenido | Estado |
|---|---|---|
| `archive\source-packages\LugazGO-Codex-Starter.zip` | Snapshot original de 10 archivos del Starter. | Archivo histórico. Cuatro entradas siguen siendo idénticas a sus archivos actuales y seis documentos tienen versiones posteriores fuera del ZIP. |
| `archive\source-packages\lugazgo-go-integracion-wordmark-svg.zip` | `lugazgo-logo-corregido.svg` y `lugazgo-o-maestra.svg`. | Los dos archivos coinciden byte a byte con las copias recuperadas en `integration-wordmark\`. |

#### Integridad y procedencia

- `brand\references\recovered-assets\SHA256SUMS.txt` contiene 20 hashes; los 20 coinciden.
- `brand\references\recovered-assets\vector-kit\LEEME.txt` documenta el paquete vectorial recuperado.
- `brand\references\recovered-assets\README.md` registra clasificación, comprobaciones y ambigüedades.
- `archive\source-packages\README.md` registra los hashes de los ZIP; ambos coinciden.

#### Paleta presente en el kit recuperado

Los siguientes valores aparecen literalmente en `lugazgo-paleta.svg`. Son hechos del archivo, no colores aprobados por el registro de decisiones.

| Nombre presente en el SVG | HEX presente |
|---|---|
| Tierra Suave | `#8B7058` |
| Verde Salvia | `#8F9D76` |
| Azul Brumoso | `#91B5C8` |
| Verde Liquen | `#C1CCAD` |
| Marfil Cálido | `#F1E5D2` |
| Tierra Oscura | `#55483D` |
| Terracota Mineral | `#C98E72` |

No se encontraron PNG, JPG, WebP, GIF, AI, EPS, CDR, DXF, DWG, EMF o WMF.

### 1.9 Funcionalidades actuales

El proyecto no ofrece funcionalidad de usuario final. Actualmente funciona como repositorio documental y archivo trazable de la Fase 0.

| Funcionalidad actual | Implementación |
|---|---|
| Contexto de marca | `docs\brand-context.md` |
| Registro de decisiones y estados | `docs\decisions.md` |
| Roadmap y límites de fase | `docs\roadmap.md` |
| Reglas operativas | `AGENTS.md` |
| Inventario de activos recuperados | `brand\references\recovered-assets\README.md` |
| Comprobación manual de integridad | `brand\references\recovered-assets\SHA256SUMS.txt` |
| Conservación de entregas originales | `archive\source-packages\` |
| Placeholders para fases futuras | `app\README.md` y `data\README.md` |

No existen aplicación, web, frontend, backend, API, servidor, base de datos, modelo de datos, integración con Notion, scripts, pruebas, CI/CD, despliegue ni hosting. `app\` y `data\` contienen solo documentación de espera.

### 1.10 Errores, inconsistencias y riesgos detectados

Los siguientes puntos son hallazgos, no instrucciones para modificarlos.

| ID | Tipo | Hallazgo comprobado | Efecto actual |
|---|---|---|---|
| H-01 | Duplicado exacto | `lugazgo-logo-monocromo.svg` y `lugazgo-logo-monocromo-tierra-oscura.svg` tienen 2.986 B y el mismo SHA-256: `060D4BB2124E3B0359FAAB1220A30DF76D2065BEAC9CB36A8D53B7B684B6213C`. | Redundancia y ambigüedad del nombre genérico. |
| H-02 | Identificadores SVG repetidos | `lugazgo-previsualizacion-vectorial.svg` repite `aro-o` 14 veces, `curva-topografica-1` 12, `curva-topografica-2` 10 y `punto-localizacion` 14. | El archivo se renderiza, pero la selección por ID mediante DOM/CSS resulta ambigua. |
| H-03 | Identificadores SVG repetidos | `lugazgo-versiones-monocromaticas.svg` repite cuatro veces cada uno de los IDs `aro-o`, `curva-topografica-1`, `curva-topografica-2` y `punto-localizacion`. | El archivo se renderiza, pero la selección por ID mediante DOM/CSS resulta ambigua. |
| H-04 | Precedencia no resuelta | `lugazgo-logo-corregido.svg` y `lugazgo-logo-principal.svg` son composiciones distintas. | No puede determinarse por los archivos cuál debe ser el maestro canónico. |
| H-05 | Exportación desalineada | `lugazgo-logo-principal.pdf` corresponde a la composición anterior y no a `lugazgo-logo-corregido.svg`. | No existe PDF equivalente comprobado para la revisión “corregido”. |
| H-06 | Duplicidad conceptual | `lugazgo-o-maestra.svg` y `lugazgo-simbolo-o.svg` comparten geometría y colores, pero difieren en estructura e IDs. | Hay dos candidatos equivalentes sin precedencia aprobada. |
| H-07 | Favicon no resuelto | Existen tres SVG específicos de 16, 24 y 32 px y un icono con fondo, pero no existe `brand\logo\favicon.svg`. | No hay maestro de favicon canónico aprobado. |
| H-08 | Dependencia tipográfica no empaquetada | Tres láminas usan `font-family="Arial, sans-serif"` con texto vivo. | La apariencia puede variar entre sistemas; estas láminas no son maestros totalmente trazados. |
| H-09 | Snapshot histórico desactualizado | El ZIP `LugazGO-Codex-Starter.zip` conserva versiones anteriores de 6 de sus 10 documentos. | Descomprimirlo no reproduce el estado documental actual. |
| H-10 | Ausencia de control de versiones | No existe repositorio Git. | No hay historial, comparación de cambios, ramas ni restauración mediante Git. |
| H-11 | Especificaciones sin aprobar | El kit contiene geometría y siete valores HEX, mientras `docs\decisions.md` mantiene la geometría, paleta exacta y tipografía como pendientes. | Los datos recuperados no pueden tratarse como oficiales sin una decisión posterior. |
| H-12 | Maestros canónicos ausentes | `brand\logo\` solo contiene `README.md`; faltan `lugazgo-primary.svg`, `lugazgo-symbol.svg` y `favicon.svg`. | La Fase 0 no cumple todavía su criterio de cierre. |

### 1.11 Elementos pendientes ya documentados

#### Dentro de la Fase 0

- validar procedencia y precedencia de los activos recuperados;
- aprobar y copiar el logotipo canónico a `brand\logo\lugazgo-primary.svg`;
- aprobar y copiar el símbolo canónico a `brand\logo\lugazgo-symbol.svg`;
- aprobar y copiar el favicon canónico a `brand\logo\favicon.svg`;
- aprobar nombres y valores exactos de la paleta;
- definir tipografía;
- confirmar geometría, espaciados, versiones cromáticas y fondos permitidos;
- definir tamaños mínimos, márgenes y reglas de accesibilidad;
- registrar todas las aprobaciones y mapeos en `docs\decisions.md`.

#### Información de marca todavía no definida

- público objetivo detallado;
- propuesta verbal o eslogan;
- tono de voz editorial;
- reglas de aplicación fuera de los cuatro activos básicos.

#### Fases futuras no autorizadas

- Fase 1: sistema de lugares y conocimiento, incluida la decisión sobre Notion u otra herramienta;
- Fase 2: modelo de datos, entidades, campos, fuentes, almacenamiento y privacidad;
- Fase 3: aplicación, funcionalidades, plataforma, experiencia, arquitectura, tecnología y monetización;
- web, papelería, señalética, campañas, redes sociales, merchandising y otras extensiones.

## 2. Recomendaciones

Las siguientes son recomendaciones derivadas de los hechos anteriores. No se han ejecutado.

### 2.1 Prioridad alta: cerrar la fuente de verdad visual

1. Obtener una aprobación explícita que elija entre `lugazgo-logo-corregido.svg` y `lugazgo-logo-principal.svg`.
2. Confirmar cuál de `lugazgo-o-maestra.svg` y `lugazgo-simbolo-o.svg` debe ser el símbolo canónico.
3. Definir si el favicon maestro parte de la versión de 16, 24 o 32 px, del icono con fondo o de otro original.
4. Registrar el mapeo en `docs\decisions.md` antes de crear los nombres canónicos en `brand\logo\`.
5. Conservar siempre intactos los archivos de `brand\references\recovered-assets\` y copiar, no mover, los aprobados.

### 2.2 Prioridad alta: resolver la especificación de marca

1. Validar o rechazar expresamente los siete colores del SVG de paleta.
2. Aprobar tipografía, geometría, espaciados, fondos, tamaños mínimos y accesibilidad.
3. Distinguir en la documentación qué decisiones provienen del kit recuperado y cuáles han sido aprobadas por la persona responsable.

### 2.3 Prioridad media: corregir derivados sin alterar los originales

1. Si se aprueba el wordmark “corregido”, regenerar un PDF que corresponda exactamente a esa composición.
2. Crear copias derivadas normalizadas de las dos láminas con IDs repetidos si van a manipularse mediante DOM o CSS.
3. Decidir si `lugazgo-logo-monocromo.svg` es un alias intencionado; si lo es, documentarlo. Si no lo es, conservar solo una copia de trabajo, manteniendo el original recuperado.
4. Convertir el texto de las láminas a trazados únicamente si se necesita portabilidad visual y existe autorización; conservar también las versiones con texto vivo.

### 2.4 Prioridad media: trazabilidad técnica

1. Inicializar Git cuando se autorice y crear un primer commit que preserve este estado auditado.
2. Añadir una comprobación automatizada, no destructiva, para XML válido, IDs únicos, ausencia de raster embebido y coincidencia de SHA-256.
3. Mantener `LugazGO-Codex-Starter.zip` como snapshot histórico y generar un paquete de distribución nuevo solo cuando los maestros canónicos estén aprobados.

### 2.5 Prioridad futura: aplicación

No elegir framework, lenguaje, base de datos ni comandos de ejecución durante la Fase 0. Cuando la Fase 3 se autorice, documentar entonces:

- stack y versiones;
- instalación y variables de entorno;
- comandos de desarrollo, build, test, lint y despliegue;
- arquitectura, dependencias y modelo de datos;
- estrategia de pruebas, CI/CD y hosting.

## 3. Conclusión

El proyecto está ordenado y es técnicamente consistente como archivo documental de identidad visual. Los recursos vectoriales son válidos y trazables, pero no existe todavía una fuente maestra aprobada en `brand\logo\`. La carencia principal no es de implementación: es de decisiones canónicas sobre logo, símbolo, favicon y paleta. No debe iniciarse trabajo de aplicación hasta cerrar o desbloquear explícitamente la Fase 0.
