---
name: portada-articulo
description: "Poner la imagen de portada de un artículo de The Future Designer — Isabel la trae, Claude nunca la genera."
argument-hint: "<id o título del artículo>"
allowed-tools:
  - Read
  - Bash
---

<objective>
Cada artículo necesita una imagen de portada (la que sale en el titular, las tarjetas medianas
y la cuadrícula). **Isabel la trae — no se genera con código.** Se probó un generador
procedural (`scripts/generate_cover_art.py`, boceteado y luego estilo doodle) y no dio el
nivel que buscaba; ese script se queda en el repo como referencia histórica de las 10 portadas
antiguas, pero no se usa para nada nuevo a partir de ahora.
</objective>

<process>
1. **Identifica el artículo.** Búscalo en `data/articles.json` por id o por título.

2. **Pídele la imagen a Isabel.** No la generes tú de ninguna forma (ni SVG procedural, ni
   descripción para un generador externo). Espera a que ella:
   - te dé la ruta de un archivo en su disco, o
   - adjunte la imagen directamente en la conversación, o
   - te pase una URL.

3. **Guárdala** en `images/<article-id>/cover.<ext>` (misma convención que ya usa
   `scripts/save_article.py`), respetando el formato que ella traiga (PNG, JPG, SVG...) —
   no la conviertas ni la reproceses.
   - Ruta local → cópiala con `cp`.
   - Adjunta en el chat → normalmente queda accesible como archivo local; cópiala igual.
   - URL → descárgala (mismo patrón que `download_image()` en `scripts/save_article.py`).
   - Si el artículo ya tenía una portada con otro nombre de archivo (p. ej. un `cover.svg`
     generado antes), bórrala para no dejar huérfanos sueltos en `images/<id>/`.

4. **Actualiza `data/articles.json`**: pon `"images": ["images/<id>/cover.<ext>"]` en la
   entrada de ese artículo (sustituye lo que hubiera).

5. **Reconstruye** con `python3 build_repo.py`.

6. **Enséñaselo** — abre el artículo y/o la portada para que lo confirme antes de tocar git.
   Nunca hagas commit ni push por tu cuenta; eso lo decide ella, como con cualquier otro
   cambio del sitio.
</process>

<notes>
- Esto sustituye el paso "diseña una escena en scripts/generate_cover_art.py" que tenía antes
  el flujo de "Añadir un artículo" en CLAUDE.md.
- Si Isabel dice que irá pasando las portadas de los artículos existentes de una en una,
  trátalo igual: identifica el artículo, pide la imagen, guarda, actualiza, reconstruye,
  enseña — un artículo a la vez, no adelantes trabajo con los demás.
</notes>
