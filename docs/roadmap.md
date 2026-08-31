# LugazGO — Roadmap por fases

El roadmap distingue el trabajo autorizado ahora de las direcciones futuras. Una fase futura no constituye autorización para iniciarla.

## Fase 0 — Identidad visual básica

**Estado:** Cerrada el 2026-08-30.

**Objetivo cumplido:** Consolidar los cuatro componentes básicos sin ampliar el sistema de marca.

### Entregables cerrados

- logotipo principal: `brand/logo/lugazgo-primary.svg`;
- símbolo principal: `brand/logo/lugazgo-symbol.svg`;
- favicon principal: `brand/logo/favicon.svg`;
- derivados de favicon optimizados para 16, 24 y 32 px en `brand/logo/`;
- paleta básica oficial en `brand/colors/README.md`.

### Resultado de cierre

- El logotipo y el símbolo proceden de los SVG expresamente aprobados de `brand/references/recovered-assets/integration-wordmark/`.
- El favicon principal procede de la versión optimizada de 32 px; las variantes de 16, 24 y 32 px se conservan como derivados válidos para sus tamaños.
- Los originales recuperados permanecen intactos y las copias canónicas coinciden byte a byte con ellos.
- Todos los SVG copiados son XML válido.
- Los nombres, valores HEX y límites de la paleta básica están documentados.
- `docs/decisions.md` y `brand/logo/README.md` registran procedencia y SHA-256.

### Alcance del cierre

La Fase 0 queda limitada exclusivamente a logotipo, símbolo, favicon y paleta básica. La tipografía, el eslogan, el tono editorial, los tamaños mínimos, las aplicaciones de marca y las reglas avanzadas no forman parte de este cierre ni lo bloquean.

### Exclusiones

El cierre de la Fase 0 no autoriza app, web, Notion, base de datos, modelo funcional, mockups, papelería, señalética, extensiones de campaña ni elección de framework. Todo ello requiere una decisión posterior explícita.

D015 autoriza posteriormente la definición documental de la Fase 1. No modifica ni reabre los activos o límites visuales cerrados aquí.

---

## Fase 1 — Sistema de lugares y conocimiento

**Estado:** Activa para definición documental desde el 2026-08-31.

**Objetivo:** Definir el producto y el sistema editorial antes de cualquier desarrollo.

**Fuente principal:** `docs/phase-1/`.

### Entregables

- propuesta de valor y alcance del MVP;
- funciones imprescindibles y exclusiones;
- categorías, requisitos, vetos y rúbrica editorial;
- modelo conceptual de datos preparado para traducciones;
- estados, transiciones, permisos y papel de Notion;
- política de fuentes, licencias, sensibilidad y actualización;
- plan piloto de 40 destinos;
- registro de decisiones pendientes.

### Alcance operativo

Notion será la fuente maestra editorial durante el piloto. La base se llama `Destinos`, pero no se modifica ni integra todavía. El sistema editorial y la experiencia pública se especifican documentalmente, sin construirlos.

### Exclusiones

- frontend, backend y base de datos ejecutable;
- integración, exportación o sincronización real con Notion;
- investigación o incorporación de destinos concretos;
- prototipos, pantallas o mockups;
- framework, proveedor de mapas, hosting o analítica;
- cambios de identidad visual;
- IONOS, DNS, dominio, correo y Netlify.

La Fase 1 no termina ni escala automáticamente: necesita resolver los pendientes críticos, ejecutar el piloto en una autorización posterior y recibir aprobación humana.

---

## Fase 2 — Preparación técnica e integración de datos

**Estado:** Futura; no autorizada.

**Dependencia:** Modelo conceptual, flujo editorial y decisiones críticas de la Fase 1.

**Sin decidir:** almacenamiento, formato público, validación ejecutable, sincronización con Notion, seguridad, privacidad, recuperación y tecnología.

La Fase 1 define entidades y campos de forma conceptual. No crear esquemas ejecutables, integraciones ni datos de destinos mientras esta fase técnica siga sin autorización.

---

## Fase 3 — Producto o aplicación LugazGO

**Estado:** Futura; no autorizada.

**Dependencia:** Identidad básica cerrada, Fase 1 validada y preparación técnica autorizada.

**Sin decidir:** diseño detallado, arquitectura, tecnología, monetización y calendario. El alcance funcional inicial está definido en `docs/phase-1/01-propuesta-valor-y-mvp.md`.

No crear código, prototipos ni mockups de la aplicación mientras esta fase siga sin autorización.

---

## Extensiones sin fase aprobada

Web, papelería, señalética, campañas, redes sociales, merchandising y otras aplicaciones de marca no tienen una fase aprobada. Permanecen fuera de alcance hasta que una decisión futura las priorice.

## Puerta de paso entre fases

Para activar una fase futura se necesita:

1. una instrucción explícita de la persona responsable;
2. una entrada nueva en `docs/decisions.md` con estado **Aprobada** o **Bloqueada**;
3. alcance, entregables y exclusiones definidos;
4. actualización de este roadmap y del estado del `README.md`.
