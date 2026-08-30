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

---

## Fase 1 — Sistema de lugares y conocimiento

**Estado:** Futura; no autorizada.  
**Dirección conocida:** Reunir y organizar información sobre lugares.  
**Sin decidir:** herramienta concreta —incluido Notion—, criterios editoriales, flujo de revisión, taxonomía y alcance.

Esta fase solo podrá comenzar mediante una nueva decisión explícita; el cierre de la Fase 0 no la activa automáticamente.

---

## Fase 2 — Modelo de datos

**Estado:** Futura; no autorizada.  
**Dependencia:** Requisitos y contenido de la Fase 1.  
**Sin decidir:** entidades, campos, fuentes, arquitectura, almacenamiento, privacidad y tecnología.

No crear esquemas ni archivos de datos funcionales mientras esta fase siga sin autorización.

---

## Fase 3 — Producto o aplicación LugazGO

**Estado:** Futura; no autorizada.  
**Dependencia:** Identidad básica cerrada y modelo de datos aprobado.  
**Sin decidir:** funcionalidades, plataformas, experiencia de usuario, arquitectura, tecnología, monetización y calendario.

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
