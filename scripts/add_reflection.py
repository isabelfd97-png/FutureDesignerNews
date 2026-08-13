#!/usr/bin/env python3
"""
Append a reflection (synthesized from a debate with Claude) to an existing article
in Isabel's "The Future Designer" learning repo.

Usage:
    python3 add_reflection.py --data-file reflection.json
    cat reflection.json | python3 add_reflection.py

Input JSON schema:
{
  "project_dir": "/Users/isabelferrer-dalmau/Desktop/10 Articles and news",
  "article_id": "the-existing-article-id",
  "text": "La reflexión ya redactada, en markdown ligero (párrafos, ** negrita **, etc.)",
  "date": "2026-07-16"   # optional, defaults to today
}

What it does (deliberately different from save_article.py):
  1. Loads the EXISTING entry for article_id from data/articles.json — does not touch
     any other field (title, content_md, glossary, materials, images...). This script
     only ever appends to the "reflections" list, never overwrites the rest of the article.
  2. Appends {"date": ..., "text": ...} to that entry's "reflections" list (creates the
     list if it doesn't exist yet).
  3. Appends the same reflection, in readable form, to the bottom of the article's .md file.
  4. Runs build_repo.py to regenerate index.html.

Fails loudly (non-zero exit, no partial writes) if article_id doesn't exist — this script
is only for adding to an article that's already there, never for creating a new one.
"""
import argparse
import json
import os
import sys
import subprocess
from datetime import date


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
    ap.add_argument("--data-file", help="Path to a JSON file with the reflection data")
    args = ap.parse_args()

    if args.data_file:
        with open(args.data_file, encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)

    project_dir = data["project_dir"]
    article_id = data["article_id"].strip()
    text = data["text"].strip()
    reflection_date = data.get("date") or date.today().isoformat()

    if not text:
        print("El texto de la reflexión está vacío, no se guarda nada.", file=sys.stderr)
        sys.exit(1)

    data_json_path = os.path.join(project_dir, "data", "articles.json")
    articles = load_json(data_json_path, [])
    idx = next((i for i, a in enumerate(articles) if a.get("id") == article_id), None)
    if idx is None:
        print(
            f"No existe ningún artículo con id '{article_id}' en {data_json_path}. "
            f"Este script solo añade reflexiones a artículos ya guardados — revisa el id "
            f"(puedes buscarlo por título dentro de data/articles.json).",
            file=sys.stderr,
        )
        sys.exit(1)

    entry = articles[idx]
    reflections = entry.get("reflections") or []
    reflections.append({"date": reflection_date, "text": text})
    entry["reflections"] = reflections
    articles[idx] = entry
    save_json(data_json_path, articles)

    # --- also append to the .md file, so the file itself stays the readable source of truth ---
    section = entry.get("section", "")
    md_path = os.path.join(project_dir, "articles", section, f"{article_id}.md")
    if os.path.exists(md_path):
        with open(md_path, "a", encoding="utf-8") as f:
            f.write(f"\n\n## Reflexión ({reflection_date})\n{text}\n")
    else:
        print(f"  (aviso: no se encontró {md_path} para anexar la reflexión en texto, "
              f"pero sí se guardó en articles.json)", file=sys.stderr)

    # --- regenerate the site ---
    build_script = os.path.join(project_dir, "build_repo.py")
    if os.path.exists(build_script):
        subprocess.run([sys.executable, build_script], cwd=project_dir, check=True)

    print(json.dumps({
        "status": "ok",
        "article_id": article_id,
        "reflection_count": len(reflections),
        "md_path": md_path,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
