# LugazGO — Instrucciones operativas para Codex

Este archivo es la constitución de trabajo del proyecto. Se aplica a todo el repositorio.

## 1. Objetivo del repositorio

Mantener una fuente maestra, versionable y verificable de LugazGO. La identidad visual básica de la Fase 0 está cerrada; ninguna fase posterior está autorizada de forma implícita.

## 2. Fase 0 cerrada; fases posteriores bloqueadas

La Fase 0 cerrada comprende exclusivamente:

- logotipo principal;
- símbolo;
- favicon;
- paleta básica.

No desarrollar ni diseñar todavía:

- aplicación o prototipos de aplicación;
- web;
- Notion o cualquier base de lugares;
- modelos de datos funcionales;
- mockups;
- papelería;
- señalética;
- piezas de campaña, redes sociales u otras extensiones de marca.

Las carpetas `app/` y `data/` son reservas estructurales. Hasta que una fase posterior se autorice expresamente, solo pueden contener documentación de espera.

## 3. Fuentes de verdad y prioridad

Ante una discrepancia, usar este orden:

1. una instrucción explícita y reciente de la persona responsable del proyecto;
2. decisiones con estado **Aprobada** o **Bloqueada** en `docs/decisions.md`;
3. archivos SVG maestros auténticos depositados en `brand/logo/`;
4. `docs/brand-context.md`;
5. `README.md` y `docs/roadmap.md`.

Una idea marcada como **Pendiente**, **Propuesta** o **No disponible** no es una decisión aprobada.

## 4. Invariantes de marca confirmados

- El nombre se escribe `LugazGO`, respetando exactamente mayúsculas y minúsculas.
- La marca se centra en descubrir lugares con encanto, tranquilos, poco masificados y menos explotados.
- La personalidad definida es minimalista, eco-friendly, premium, misteriosa y curiosa.
- La dirección cromática es suave, orgánica y pastel. La paleta básica oficial está documentada en `brand/colors/README.md`.
- La `O` distintiva incorpora curvas topográficas que la atraviesan diagonalmente, con lectura tipo `ø`.
- La `O` contiene un punto de ubicación aproximadamente en la zona central/superior derecha.
- La descripción de la `O` fija el concepto, no autoriza a inventar su geometría exacta.

## 5. Reglas de diseño y activos

- No reinterpretar, simplificar, embellecer, recolorear ni redibujar arbitrariamente elementos aprobados.
- No fabricar SVG de sustitución, logotipos provisionales que parezcan maestros ni falsos “originales”.
- Si falta un maestro, registrar la ausencia y pedir el archivo o una autorización expresa para crearlo.
- Tratar los SVG maestros auténticos como activos autoritativos. Modificarlos solo ante una petición explícita y conservar siempre el original sin cambios.
- No rasterizar los maestros SVG. Los PNG u otros derivados, si algún día se autorizan, no sustituyen al vector maestro.
- No cambiar nombres, proporciones, trazados, `viewBox`, punto de ubicación, curvas topográficas o colores aprobados sin una decisión registrada.
- No deducir tipografía, códigos HEX/RGB/CMYK/Pantone, número de curvas, grosores, espaciados o variantes a partir de la descripción verbal.
- No presentar una propuesta como aprobada. Etiquetarla claramente como propuesta y mantenerla fuera de los maestros.

## 6. Protocolo de trabajo

Antes de realizar cambios:

1. leer `docs/decisions.md` y `docs/brand-context.md`;
2. comprobar si existen maestros auténticos en `brand/logo/`;
3. confirmar que la tarea está expresamente autorizada por `docs/decisions.md` y `docs/roadmap.md`;
4. identificar cualquier dato exacto que falte.

Durante el trabajo:

- hacer el cambio mínimo solicitado;
- preservar los archivos existentes y su procedencia;
- separar hechos, decisiones, propuestas y preguntas abiertas;
- evitar ampliar el alcance por iniciativa propia.

Después de un cambio aprobado:

1. actualizar `docs/decisions.md` sin borrar el historial previo;
2. indicar fecha, estado, decisión, motivo y archivos afectados;
3. si una decisión sustituye otra, marcar la anterior como **Sustituida** y enlazar la nueva;
4. actualizar el estado de `README.md` y `docs/roadmap.md` cuando corresponda.

## 7. Criterio de parada

Detenerse y solicitar confirmación cuando:

- la petición pretenda iniciar una fase posterior sin autorización explícita;
- sea necesario inventar una especificación no aprobada;
- falte el SVG maestro que habría que modificar;
- dos fuentes aprobadas entren en conflicto;
- el cambio pueda reinterpretar un elemento aprobado.

## 8. Protección del paquete

- No sobrescribir este `AGENTS.md` mediante una inicialización automática.
- No eliminar placeholders hasta que su ausencia haya quedado resuelta o documentada.
- No guardar secretos, credenciales ni datos personales en el repositorio.
