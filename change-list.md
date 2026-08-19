# Review queue — 2026-08-19

## Grupos
- Sin agrupar: los 7 ítems tocan preocupaciones distintas (infra de despliegue, restyle subjetivo, forma de icono, eliminación de widget, claridad de iconos, bug de CSS, y redisño de layout). Aunque R1/R2 comparten componente visual (el post-it) y R6/R7 comparten componente (botón de repaso), sus causas raíz y su tipo de cambio son diferentes — mezclarlos dificultaría revisar o revertir uno sin el otro. Cada ítem = su propio commit.

## [x] R1 — Imagen del post-it de la editora jefe no se ve en producción
Detalle: "ahora mismo en la web subida la imagen del postit de la editora jefe no se ve, arreglalo pls"
Área: masthead / subtitle post-it
Commit: pendiente
Causa: GitHub Pages construye con Jekyll por defecto, que ignora cualquier carpeta que empiece por "_" (como images/_shared/) salvo que exista un archivo .nojekyll en la raíz. Confirmado con curl: la imagen daba 404 en producción mientras el resto de portadas (sin "_" en la ruta) cargaban bien. Fix: añadido .nojekyll vacío en la raíz del repo.

## [ ] R2 — Texto y tipografía del post-it de la editora jefe demasiado "redondita", estilo más gamberro
Detalle: "El texto de nota de la editora jefe, la fuente y la tipografía no me mola, la veo demasiado redondita. Arreglalo y el estilo general de ese postit que sea un pelin más gamberro y que de inicio no tape el título de The Future Designer"
Área: masthead / subtitle post-it (mismo componente que R1)

## [ ] R3 — La estrellita animada de "Nuevo" debería ser un fueguito
Detalle: "En nuevo la estrellkita esa que se mueve no quiero que la forma sea una estrellita, quiero que sea un fueguito"
Área: badge/icono "Nuevo"

## [ ] R4 — Quitar la sección Strike
Detalle: "la sección de strike no la necesitamos creo, quitala"
Área: navegación / secciones

## [ ] R5 — Buscador e histórico no se entienden solo con iconos
Detalle: "el buscador y el historico, creo que simplemente con esos iconos no se entiende, podrías ponerlo de otra forma o completarlo con texto?"
Área: nav / iconos buscador-histórico

## [ ] R6 — Botón "Lo sabía" en cards de Enciclopedia no se lee hasta hacer hover
Detalle: "Me encanta en enciclopedia que pongas las cards para revisar pero el botón de lo sabía no se lee hasta que hago hover"
Área: Enciclopedia / cards de revisión

## [ ] R7 — Dar más protagonismo a la acción de "revisar" (altura de titular / CTA inicial)
Detalle: "Dale más importancia a la acción de revisar poniéndola por ejemplo a la altura del titular, o que sea más como un CTA al principio que invite al usuario a revisar"
Área: Enciclopedia / layout de sección (relacionado con R6)
