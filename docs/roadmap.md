# LugazGO — Roadmap por fases

El roadmap distingue el trabajo autorizado ahora de las direcciones futuras. Una fase futura no constituye autorización para iniciarla.

## Fase 0 — Identidad visual básica

**Estado:** Activa y bloqueada a su alcance.  
**Objetivo:** Consolidar los cuatro componentes básicos sin ampliar el sistema de marca.

### Entregables

- logotipo principal en SVG;
- símbolo en SVG;
- favicon en SVG;
- paleta básica con valores exactos aprobados.

### Situación de partida

- El concepto y la dirección de marca están documentados.
- Los tres SVG maestros no estaban disponibles durante la migración.
- Posteriormente se recuperaron 16 SVG y 3 PDF, ya inventariados en `brand/references/recovered-assets/`, pero aún no se ha aprobado qué archivos deben actuar como maestros canónicos.
- La dirección cromática está definida, pero sus valores exactos están pendientes.

### Próximas acciones permitidas

1. Validar la procedencia y precedencia de los SVG recuperados.
2. Confirmar cuáles corresponden a logo, símbolo y favicon sin modificarlos.
3. Registrar el mapeo entre nombres originales y nombres canónicos antes de incorporarlos a `brand/logo/`.
4. Documentar la paleta exacta cuando exista una aprobación explícita.
5. Resolver únicamente los detalles necesarios de estos cuatro entregables.

### Criterio de cierre

La fase puede considerarse terminada cuando:

- existen maestros SVG auténticos o expresamente aprobados para los tres activos;
- la paleta básica tiene valores exactos aprobados;
- `docs/decisions.md` refleja las aprobaciones y archivos finales;
- no hay activos provisionales presentados como definitivos.

### Exclusiones durante esta fase

No iniciar app, web, Notion, base de datos, mockups, papelería, señalética ni extensiones de campaña.

---

## Fase 1 — Sistema de lugares y conocimiento

**Estado:** Futura; no autorizada.  
**Dirección conocida:** Reunir y organizar información sobre lugares.  
**Sin decidir:** herramienta concreta —incluido Notion—, criterios editoriales, flujo de revisión, taxonomía y alcance.

Esta fase solo podrá comenzar tras cerrar o desbloquear expresamente la Fase 0 y registrar una nueva decisión.

---

## Fase 2 — Modelo de datos

**Estado:** Futura; no autorizada.  
**Dependencia:** Requisitos y contenido de la Fase 1.  
**Sin decidir:** entidades, campos, fuentes, arquitectura, almacenamiento, privacidad y tecnología.

No crear esquemas ni archivos de datos funcionales durante la fase actual.

---

## Fase 3 — Producto o aplicación LugazGO

**Estado:** Futura; no autorizada.  
**Dependencia:** Identidad básica cerrada y modelo de datos aprobado.  
**Sin decidir:** funcionalidades, plataformas, experiencia de usuario, arquitectura, tecnología, monetización y calendario.

No crear código, prototipos ni mockups de la aplicación durante la fase actual.

---

## Extensiones sin fase aprobada

Web, papelería, señalética, campañas, redes sociales, merchandising y otras aplicaciones de marca no tienen una fase aprobada. Permanecen fuera de alcance hasta que una decisión futura las priorice.

## Puerta de paso entre fases

Para activar una fase futura se necesita:

1. una instrucción explícita de la persona responsable;
2. una entrada nueva en `docs/decisions.md` con estado **Aprobada** o **Bloqueada**;
3. alcance, entregables y exclusiones definidos;
4. actualización de este roadmap y del estado del `README.md`.
