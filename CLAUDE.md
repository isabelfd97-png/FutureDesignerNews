# The Future Designer

Sitio estático personal (no framework, no backend): `build_repo.py` lee `data/articles.json`
y genera `index.html` (todo el CSS/JS va inline). Lenguaje visual brutalista: blanco/negro/naranja,
trazo grueso, sombras duras. La lógica completa de la portada y las decisiones de diseño están
documentadas para no-devs en `docs/homepage-logic.md` — léelo antes de tocar la portada.

## Añadir un artículo

Los artículos se guardan con `scripts/save_article.py` (slugifica el título, escribe
`articles/<section>/<id>.md`, hace upsert en `data/articles.json` y reconstruye `index.html`).

**Todo artículo nuevo tiene que llevar su propia ilustración de portada — esto no es opcional:**

1. Guarda el artículo como siempre con `scripts/save_article.py`. Este paso ya genera
   automáticamente una portada de repuesto (genérica) para que nunca quede una imagen vacía.
2. Diseña una ilustración a medida para ese artículo en `scripts/generate_cover_art.py`:
   añade una función `scene_<nombre>()` nueva usando las primitivas `sketchy_*` ya existentes
   (trazo boceteado a doble pasada, blanco y negro puro, sin texto dentro de la imagen, fondo
   neutro liso) y regístrala en el diccionario `SCENES` con el id del artículo. La composición
   tiene que representar el tema real de ese artículo — no reutilices la escena de otro artículo
   ni te quedes con la genérica de `fallback_scene`.
3. Renderiza una vista previa: `python3 scripts/generate_cover_art.py --only <id> --preview`
   y abre/lee el PNG que genera.
4. **Enséñale la portada a Isabel y espera su aprobación antes de hacer commit o push de nada.**
   Si pide cambios, ajusta la escena y vuelve a renderizar.
5. Solo después de su aprobación: `python3 build_repo.py`, y luego commit + push si lo pide.

Las 11 funciones `scene_*` ya escritas en `scripts/generate_cover_art.py` son la referencia del
lenguaje visual establecido (grosor de trazo, la chispa-firma en la esquina, relleno sólido vs.
contorno para marcar el elemento importante de cada escena).
