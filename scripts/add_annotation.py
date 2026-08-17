#!/usr/bin/env python3
"""
Append an inline annotation (a highlighted quote + note) to an existing article in
Isabel's "The Future Designer" learning repo. Used by the "anotar-articulo" skill while
she's reading an article and debating it with Claude.

Usage:
    python3 add_annotation.py --data-file annotation.json
    cat annotation.json | python3 add_annotation.py

Input JSON schema:
{
  "project_dir": "/Users/isabelferrer-dalmau/Desktop/10 Articles and news",
  "article_id": "the-existing-article-id",
  "quote": "the EXACT phrase from that article's content_md this annotation refers to",
  "type": "ampliacion" | "ejemplo",
  "text": "the annotation itself, in Isabel's/Claude's synthesized voice",
  "date": "2026-08-17"   # optional, defaults to today
}

What it does (deliberately different from save_article.py):
  1. Loads the EXISTING entry for article_id from data/articles.json — does not touch
     any other field. Only ever appends to that entry's "annotations" list.
  2. Requires `quote` to be an exact, verbatim substring of that article's content_md —
     this is what the front-end uses to find and underline the phrase in place. Fails
     loudly (no partial writes) if the quote isn't found, so a bad match is caught here
     rather than silently failing to render.
  3. Requires `type` to be one of ampliacion / ejemplo.
  4. Runs build_repo.py to regenerate index.html.

Two annotations CAN share the exact same `quote` on purpose — e.g. an "ampliacion" explaining
something plus an "ejemplo" making it concrete, both anchored to the same sentence. The
front-end groups annotations by quote and renders both highlights (and both post-its) at
once when that happens; it's a supported case, not a bug.

Never commits or pushes — that stays a separate, explicit step after Isabel has reviewed
the rendered annotation (see CLAUDE.md, "Añadir un artículo" / the anotar-articulo skill).
"""
import argparse
import json
import os
import sys
import subprocess
from datetime import date

VALID_TYPES = {"ampliacion", "ejemplo"}


def load_json(path, default):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return default


def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-file", help="Path to a JSON file with the annotation data")
    args = ap.parse_args()

    if args.data_file:
        with open(args.data_file, encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)

    project_dir = data["project_dir"]
    article_id = data["article_id"].strip()
    quote = data["quote"].strip()
    annot_type = data.get("type", "ampliacion").strip()
    text = data["text"].strip()
    annot_date = data.get("date") or date.today().isoformat()

    if annot_type not in VALID_TYPES:
        print(f"Tipo de anotación desconocido '{annot_type}'. Debe ser una de: {sorted(VALID_TYPES)}",
              file=sys.stderr)
        sys.exit(1)
    if not quote:
        print("La cita (quote) está vacía — hace falta la frase exacta del artículo a resaltar.",
              file=sys.stderr)
        sys.exit(1)
    if not text:
        print("El texto de la anotación está vacío, no se guarda nada.", file=sys.stderr)
        sys.exit(1)

    data_json_path = os.path.join(project_dir, "data", "articles.json")
    articles = load_json(data_json_path, [])
    idx = next((i for i, a in enumerate(articles) if a.get("id") == article_id), None)
    if idx is None:
        print(
            f"No existe ningún artículo con id '{article_id}' en {data_json_path}. "
            f"Este script solo añade anotaciones a artículos ya guardados.",
            file=sys.stderr,
        )
        sys.exit(1)

    entry = articles[idx]
    content = entry.get("content_md", "")
    if quote not in content:
        print(
            f"La cita no aparece tal cual en el content_md de '{article_id}'. "
            f"Tiene que ser una frase EXACTA (misma puntuación, mayúsculas, etc.) — "
            f"revisa el texto en data/articles.json y vuelve a intentarlo.",
            file=sys.stderr,
        )
        sys.exit(1)

    annotations = entry.get("annotations") or []
    annotations.append({"quote": quote, "type": annot_type, "text": text, "date": annot_date})
    entry["annotations"] = annotations
    articles[idx] = entry
    save_json(data_json_path, articles)

    # --- regenerate the site ---
    build_script = os.path.join(project_dir, "build_repo.py")
    if os.path.exists(build_script):
        subprocess.run([sys.executable, build_script], cwd=project_dir, check=True)

    print(json.dumps({
        "status": "ok",
        "article_id": article_id,
        "type": annot_type,
        "annotation_count": len(annotations),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
