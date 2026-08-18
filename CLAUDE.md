# The Future Designer

Sitio estático personal (no framework, no backend): `build_repo.py` lee `data/articles.json`
y genera `index.html` (todo el CSS/JS va inline). Lenguaje visual brutalista: blanco/negro/naranja,
trazo grueso, sombras duras. La lógica completa de la portada y las decisiones de diseño están
documentadas para no-devs en `docs/homepage-logic.md` — léelo antes de tocar la portada.

## Añadir un artículo

Los artículos se guardan con `scripts/save_article.py` (slugifica el título, escribe
`articles/<section>/<id>.md`, hace upsert en `data/articles.json` y reconstruye `index.html`).
Ya no genera ninguna portada automática — ver más abajo.

1. **No resumas de más.** Cuando Isabel te pase el material fuente (un doc, una nota, un
   artículo), el `content_md` tiene que recoger todo lo sustancial que trajo — pasos, reglas,
   listas, ejemplos, plantillas. No es un resumen del resumen. Si algo no cabe o dudas si
   merece su propia sección, pregúntale antes de decidir tú qué se queda fuera.
2. **Nunca elimines contenido de un artículo ya guardado sin comentárselo primero.** Si al
   revisar o reescribir un artículo ves algo que sobra, redundante o desactualizado, dile qué
   es y por qué crees que debería salir — espera su confirmación antes de borrarlo. Esto
   aplica a `content_md`, `key_points`, `glossary`, todo.
3. Guarda el artículo como siempre con `scripts/save_article.py`.
4. Para la imagen de portada, sigue la skill **`portada-articulo`**: Isabel la trae, nunca se
   genera con código. Pídesela, guárdala en `images/<id>/`, actualiza `data/articles.json` y
   reconstruye.
5. **Enséñale el resultado completo y espera su aprobación antes de hacer commit o push de
   nada.** "Completo" incluye poder ver todo el `content_md`, no solo un resumen de que "ya
   está listo".
6. Solo después de su aprobación: commit + push si lo pide.

## Anotaciones sobre un artículo

Cuando Isabel quiera debatir un artículo mientras lo lee (dudas, comentarios, ampliaciones),
usa la skill **`anotar-articulo`** — anota citas exactas del texto, nunca al final sin más.

## Nota sobre `scripts/generate_cover_art.py`

Se intentó generar las portadas por código (boceteado a doble pasada, luego estilo doodle
limpio) y no llegó al nivel que Isabel buscaba. El script se queda en el repo como referencia
de las 10 portadas antiguas que aún lo usan, pero **no se usa para nada nuevo**: ni artículos
nuevos ni el resto de portadas, que Isabel irá reemplazando ella misma una a una con la skill
`portada-articulo`.
