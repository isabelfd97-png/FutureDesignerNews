# Review queue — 2026-08-20 (feedback sobre el rediseño de home)

Rama: `feature/rediseno-home` (ya en marcha con el rediseño base commiteado en a5b6b78 — se reutiliza esta rama en vez de crear una `changes/batch-*` nueva, porque ya es una rama aislada dedicada a este mismo trabajo).

## Grupos
- G1: H1, H5 — mismo problema de fondo (sistema de alturas de la fila superior: hero, carrusel y sidebar deben compartir una altura consistente)
- G2: H2, H3 — mismo componente (cabecera del sidebar), cambios triviales de estilo/icono
- G3: H4 — aislado, cambia interacción y estructura del sidebar (acordeón), no se agrupa con G2 para poder revertirlo solo si hace falta
- G4: H6 — aislado, animación del hero
- G5: H7 — aislado, cambio de UI + animación del segundo carrusel
- G6: H8 — aislado, lógica de reparto de artículos

## [x] H1 — Igualar la altura de las cards grandes de la home
Detalle: "el tamaño de todas las cards, estas grandes que se ofrecen en la home page, debería ser el mismo, el height debería ser el mismo"
Área: hero carousel (.fp-hero) + carrusel "Quizá te interese" (.fp-secondary)
Commit: pendiente (grupo G1, con H5)
Implementado: hero con altura fija 460px (variable --top-row-h) independientemente de si el artículo tiene imagen o no, con line-clamp en título (2 líneas) y resumen (3 líneas) para que el texto nunca desborde. Las 3 cards de "quizá te interese" fijas a 380px cada una, mismo mecanismo de clamp. En mobile (≤900px, todo apilado) se libera a altura automática — no tiene sentido forzar 460px cuando ya no compiten por espacio en la misma fila.

## [ ] H2 — Quitar el fondo negro de "Para repasar"
Detalle: "la sección para repasar, veo como muy... que sea de color negro, no me gusta"
Área: .ency-sidebar-head

## [ ] H3 — El icono de shuffle no se entiende como refresh
Detalle: "el icono este que está a la derecha del título de para repasar, que entendí que es el refresh, no se entiende, así que cambia el icono o algo"
Área: .shuffle-btn / ICONS.shuffle

## [ ] H4 — Clic en un término de "Para repasar" debería expandir inline, no navegar
Detalle: "cuando clicas en uno de los términos... tendría que ser más como las cards... clicas en 'framework' y como que se expande y te dice lo que es... más interactivo, porque ahora mismo clicas y te lleva a la gestión de para repasar"
Área: .ency-mini-row / paintEncySidebar()

## [x] H5 — El sidebar debe tener la misma altura exacta que el hero
Detalle: "la sección de para repasar, que tenga la misma altura exacta que la card que hay a la izquierda, la grande que hemos hablado antes"
Área: .ency-sidebar / .front-top
Commit: pendiente (grupo G1, con H1)
Implementado: mismo mecanismo que H1 — .ency-sidebar usa la misma variable --top-row-h (460px). La lista de términos es flex:1 con overflow-y:auto, así que si algún día caben menos o más términos, la caja no cambia de tamaño. Verificado con getBoundingClientRect: hero y sidebar dan exactamente 460 los dos.

## [ ] H6 — Transición del carrusel del hero más suave
Detalle: "las interacciones de las cards grandes que van pasando... ahora mismo salta, y es horrible... que fueran más soft"
Área: paintHero() / .fp-hero

## [ ] H7 — Carrusel "Quizá te interese": flechas en vez de dot-nav, con animación de scroll
Detalle: "el dot navigation es horrible, es difícil de clicar, me falta como unas arrows, y las arrows las pondría a los lados de la sección... y que cuando cambia haya animación de scroll, ahora mismo salta a las siguientes tres y se ve horrible"
Área: otherCarouselState / paintOtherCarousel()

## [ ] H8 — Reestructurar el reparto de artículos: hero a 3, secciones fijas abajo
Detalle: "en las cards grandes que están a la izquierda [el hero] que solo hayan tres artículos y el resto los puedes ir poniendo abajo... debajo de quizá te interese pondrás Teoría, la sección de Práctica y luego una sección de Novedades... en el futuro serán como máximo cinco últimos artículos"
Área: renderPortada() — reparto de list.slice(...) y secciones inferiores
