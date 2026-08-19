# Review queue — 2026-08-19

## Resumen
7/7 hechos, 0 en pausa. 2 con duda anotada para revisar juntas: R2 (drag desactivado en mobile, ver detalle) y R4 (interpretación de "sección Strike" como el widget de racha del masthead). Rama `changes/batch-2026-08-19`, commits 1edae2b..48b51d6.

## Grupos
- Sin agrupar: los 7 ítems tocan preocupaciones distintas (infra de despliegue, restyle subjetivo, forma de icono, eliminación de widget, claridad de iconos, bug de CSS, y redisño de layout). Aunque R1/R2 comparten componente visual (el post-it) y R6/R7 comparten componente (botón de repaso), sus causas raíz y su tipo de cambio son diferentes — mezclarlos dificultaría revisar o revertir uno sin el otro. Cada ítem = su propio commit.

## [x] R1 — Imagen del post-it de la editora jefe no se ve en producción
Detalle: "ahora mismo en la web subida la imagen del postit de la editora jefe no se ve, arreglalo pls"
Área: masthead / subtitle post-it
Commit: 1edae2b
Causa: GitHub Pages construye con Jekyll por defecto, que ignora cualquier carpeta que empiece por "_" (como images/_shared/) salvo que exista un archivo .nojekyll en la raíz. Confirmado con curl: la imagen daba 404 en producción mientras el resto de portadas (sin "_" en la ruta) cargaban bien. Fix: añadido .nojekyll vacío en la raíz del repo.

## [x] R2 — Texto y tipografía del post-it de la editora jefe demasiado "redondita", estilo más gamberro
Detalle: "El texto de nota de la editora jefe, la fuente y la tipografía no me mola, la veo demasiado redondita. Arreglalo y el estilo general de ese postit que sea un pelin más gamberro y que de inicio no tape el título de The Future Designer"
Área: masthead / subtitle post-it
Commit: e3b1291
Implementado: nombre en Archivo Black mayúsculas (la misma fuente de los titulares), frase y firma en Space Mono (en vez de Space Grotesk, la fuente redondita del cuerpo del sitio), borde negro grueso + sombra dura sólida (el lenguaje visual "brutalista" que ya usan las cards), rotación algo más marcada.
Duda: para que "de inicio no tape el título" en mobile (donde el post-it absolute-positioned se comía la mitad de "THE FUTURE DESIGNER"), lo pasé a flujo normal (position: relative, debajo del título) solo en viewports ≤760px, y ahí desactivé el arrastre — el drag por pointer asume posicionamiento absoluto y con relative el cálculo de offsets se rompe. En desktop (>760px) el post-it sigue siendo absoluto y arrastrable exactamente como antes, y ahí ya no tapaba el título. Alternativa descartada: mantenerlo absolute en mobile y solo bajar el "top" — requería adivinar la altura exacta del título en cada breakpoint y es frágil ante cualquier cambio futuro de tamaño de fuente.

## [x] R3 — La estrellita animada de "Nuevo" debería ser un fueguito
Detalle: "En nuevo la estrellkita esa que se mueve no quiero que la forma sea una estrellita, quiero que sea un fueguito"
Área: badge/icono "Nuevo"
Commit: 6be7b26 (+ fix de legibilidad en revisión conjunta, ver abajo)
Implementado: sustituido el polígono de estrella de 8 puntas por el path de llama que ya existía en ICONS.flame (reutilizado del icono de racha), mismo color de acento. Verificado el shape aislado antes de aplicarlo.
Fix post-revisión (intento 1, descartado): Isabel detectó en Chrome que el texto "¡Nuevo!" no se leía sobre el fueguito. Causa: el bbox natural de ese path (14×21.8 dentro de un viewBox 24×24) es más estrecho que el badge cuadrado de 76×76px, así que el fueguito no llegaba a los bordes laterales y el texto caía parcialmente sobre fondo blanco/transparente. Probé viewBox recortado + preserveAspectRatio="none" para estirar el fueguito de borde a borde — Isabel lo vio en Chrome y el estiramiento deformaba la llama (se veía "amp[l]iada horizontalmente rara", ya no parecía fuego).
Fix post-revisión (intento 2, aplicado): revertido el preserveAspectRatio="none" — el fueguito mantiene su proporción natural sin deformarse (viewBox recortado a su bbox real, sin estirar). Para la legibilidad del texto, en vez de depender de que el fondo naranja llegue hasta los bordes, le añadí un halo/contorno oscuro (text-shadow en las 4 direcciones + sombra difusa) a `.ticker-badge span` — así "¡Nuevo!" se lee igual de bien caiga sobre naranja, blanco o cualquier otro fondo. Verificado en el sitio real.

## [x] R4 — Quitar la sección Strike
Detalle: "la sección de strike no la necesitamos creo, quitala"
Área: masthead (widget de racha)
Commit: 427f5bd
Duda: no existe ninguna "sección Strike" en el código ni en la navegación. Lo más parecido es el widget de "racha" (streak) del masthead — el icono de llama junto al buscador y el historial, que muestra "Xd" con un tooltip de días seguidos. Interpreté que se refería a eso (probablemente "strike" por confusión con el término, no "racha") y lo he quitado del masthead junto con su CSS y funciones muertas (streakPhrase). Dejé intacto el stat "Racha" del panel de progreso/historial (línea con stat-block), porque es un elemento distinto, ya etiquetado con texto claro, y no pareció lo que pedías quitar — si también quieres que desaparezca, dilo y lo saco.

## [x] R5 — Buscador e histórico no se entienden solo con iconos
Detalle: "el buscador y el historico, creo que simplemente con esos iconos no se entiende, podrías ponerlo de otra forma o completarlo con texto?"
Área: masthead-utils (buscador + historial)
Commit: 59055a0
Implementado: los dos botones ahora llevan icono + texto ("Buscar" / "Historial") en todos los tamaños de pantalla — antes eran icon-only con solo un title. Comprobado por medida (198px de ancho combinado en un viewport de 390px) que no desborda en mobile. Quité la clase icon-only y su CSS asociada, ya sin uso.

## [x] R6 — Botón "Lo sabía" en cards de Enciclopedia no se lee hasta hacer hover
Detalle: "Me encanta en enciclopedia que pongas las cards para revisar pero el botón de lo sabía no se lee hasta que hago hover"
Área: Enciclopedia / modal de repaso (flashcards)
Commit: 24d9e7e
Causa: bug real de especificidad CSS, no percepción — .flash-actions button (0,1,1 de especificidad) ponía background: var(--bg) [blanco], y esa regla le ganaba a .flash-yes { background: var(--ink) } (0,1,0) aunque .flash-yes viniera después en el archivo, porque en CSS gana la especificidad, no el orden. Resultado: texto blanco sobre fondo blanco, invisible hasta el hover (que sí tenía especificidad suficiente para ganar). Fix: subí la regla a .flash-actions .flash-yes (0,2,0). Verificado con getComputedStyle en el navegador: antes bg blanco/texto blanco, después bg negro/texto blanco.

## [x] R7 — Dar más protagonismo a la acción de "revisar" (altura de titular / CTA inicial)
Detalle: "Dale más importancia a la acción de revisar poniéndola por ejemplo a la altura del titular, o que sea más como un CTA al principio que invite al usuario a revisar"
Área: Enciclopedia / section-hero
Commit: 48b51d6
Implementado: moví el botón "Repasar (N)" de la barra de búsqueda (donde competía visualmente con el input) a la fila del titular "Enciclopedia" — misma altura que el h2, a la derecha. Lo convertí en un CTA propio (.review-cta): fondo naranja de acento, sombra dura, más grande que el botón original. En mobile se apila justo debajo del titular, antes del buscador. Solo aparece si hay términos guardados (si la enciclopedia está vacía no tiene sentido invitar a repasar).
