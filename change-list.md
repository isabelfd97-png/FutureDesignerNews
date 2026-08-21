# Review queue — 2026-08-20 (feedback sobre el rediseño de home)

Rama: `feature/rediseno-home` (ya en marcha con el rediseño base commiteado en a5b6b78 — se reutiliza esta rama en vez de crear una `changes/batch-*` nueva, porque ya es una rama aislada dedicada a este mismo trabajo).

## Resumen
8/8 hechos, 0 en pausa. Sin dudas de interpretación reseñables — todo implementado tal como se pidió. Rama `feature/rediseno-home`, commits a5b6b78..626da8b. Lista para revisar en Chrome.

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
Implementado: hero con altura fija (variable --top-row-h) independientemente de si el artículo tiene imagen o no, con line-clamp en título (2 líneas) y resumen (3 líneas) para que el texto nunca desborde. Las 3 cards de "quizá te interese" con altura fija, mismo mecanismo de clamp. En mobile (≤900px, todo apilado) se libera a altura automática.
Fix post-revisión: con 460px de altura y la imagen a 260px, el texto (título+resumen) no cabía en el espacio restante ni siquiera ya recortado a 2+3 líneas — el contenedor lo cortaba a lo bruto antes de que el propio recorte pudiera mostrar los puntos suspensivos con normalidad. Subí --top-row-h a 520px, bajé la imagen del hero a 230px y la altura de las cards del carrusel a 420px. Verificado con scrollHeight vs clientHeight en las 3 posiciones del hero y las 3 cards del carrusel: cero desbordamiento en todos los casos.

## [x] H2 — Quitar el fondo negro de "Para repasar"
Detalle: "la sección para repasar, veo como muy... que sea de color negro, no me gusta"
Área: .ency-sidebar-head
Commit: pendiente (grupo G2, con H3)
Implementado: fondo de la cabecera de negro a naranja de acento — mismo color que el banner "Se olvida lo que no se repasa" de Enciclopedia (R7 del lote anterior), así queda coherente con el resto de CTAs de repaso del sitio.

## [x] H3 — El icono de shuffle no se entiende como refresh
Detalle: "el icono este que está a la derecha del título de para repasar, que entendí que es el refresh, no se entiende, así que cambia el icono o algo"
Área: .shuffle-btn / ICONS.shuffle
Commit: pendiente (grupo G2, con H2)
Implementado: sustituido el icono de shuffle (flechas cruzadas) por una flecha circular de refresco — el símbolo estándar y universalmente reconocible, coincide con cómo tú misma lo describiste ("entendí que es el refresh"). También amplié la animación de giro al hacer clic de 180° a 360° para reforzar la sensación de "recargar".

## [x] H4 — Clic en un término de "Para repasar" debería expandir inline, no navegar
Detalle: "cuando clicas en uno de los términos... tendría que ser más como las cards... clicas en 'framework' y como que se expande y te dice lo que es... más interactivo, porque ahora mismo clicas y te lleva a la gestión de para repasar"
Área: .ency-mini-row / paintEncySidebar()
Commit: pendiente (G3)
Implementado: cada término es ahora una mini-card plegable (acordeón, solo uno abierto a la vez) — clic muestra la definición completa y un link "De: {artículo}" que sí navega, pero directo al artículo (no a una búsqueda en Enciclopedia). Quité el mecanismo anterior (pendingEncySearch) que ya no se usa. Flecha que rota 90° al abrir/cerrar como pista visual.

## [x] H5 — El sidebar debe tener la misma altura exacta que el hero
Detalle: "la sección de para repasar, que tenga la misma altura exacta que la card que hay a la izquierda, la grande que hemos hablado antes"
Área: .ency-sidebar / .front-top
Commit: pendiente (grupo G1, con H1)
Implementado: mismo mecanismo que H1 — .ency-sidebar usa la misma variable --top-row-h (520px tras el fix de H1). La lista de términos es flex:1 con overflow-y:auto, así que si algún día caben menos o más términos, la caja no cambia de tamaño. Verificado con getBoundingClientRect: hero y sidebar siempre dan el mismo valor.

## [x] H6 — Transición del carrusel del hero más suave
Detalle: "las interacciones de las cards grandes que van pasando... ahora mismo salta, y es horrible... que fueran más soft"
Área: paintHero() / .fp-hero
Commit: pendiente (G4)
Implementado: cross-fade — al cambiar de titular (dot, flecha o autoplay), el contenedor baja a opacidad 0 en 220ms, se sustituye el contenido, y sube de nuevo. Los puntos se actualizan al instante (no forman parte del fundido).

## [x] H7 — Carrusel "Quizá te interese": flechas en vez de dot-nav, con animación de scroll
Detalle: "el dot navigation es horrible, es difícil de clicar, me falta como unas arrows, y las arrows las pondría a los lados de la sección... y que cuando cambia haya animación de scroll, ahora mismo salta a las siguientes tres y se ve horrible"
Área: otherCarouselState / paintOtherCarousel()
Commit: pendiente (G5)
Implementado: quité los puntos, añadí flechas a los lados (izquierda de la primera card, derecha de la última — mismo estilo que las del hero). Página anterior/siguiente con deslizamiento (translateX + fade, 220ms) en vez de salto instantáneo. Navegación circular (llegar al final vuelve al principio). Las flechas se ocultan (visibility, no display, para no mover el layout) si solo hay una página.

## [x] H8 — Reestructurar el reparto de artículos: hero a 3, secciones fijas abajo
Detalle: "en las cards grandes que están a la izquierda [el hero] que solo hayan tres artículos y el resto los puedes ir poniendo abajo... debajo de quizá te interese pondrás Teoría, la sección de Práctica y luego una sección de Novedades... en el futuro serán como máximo cinco últimos artículos"
Área: renderPortada() — reparto de list.slice(...) y secciones inferiores
Commit: pendiente (G6)
Implementado: hero baja de 5 a 3 artículos, "Quizá te interese" toma los 6 siguientes (2 páginas de 3), y el resto se agrupa por sección (Teoría/Práctica/Novedades, mismo orden que ya tenían en SECTIONS) con tope de 5 por sección. Las 3 secciones se muestran siempre, en ese orden fijo, aunque no les toque ningún artículo — con un mensaje de estado vacío en vez de desaparecer, tal como dijiste que se vería "un poco vacío" por ahora. Con los 12 artículos actuales: Teoría 1, Práctica 2, Novedades 0 (vacía).
