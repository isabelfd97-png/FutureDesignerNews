#!/usr/bin/env python3
"""
Save an article into Isabel's "The Future Designer" learning repo.

Usage:
    python3 save_article.py --data-file article.json
    cat article.json | python3 save_article.py

Input JSON schema:
{
  "project_dir": "/Users/isabelferrer-dalmau/Desktop/10 Articles and news",
  "title": "...",
  "url": "https://...",
  "section": "ia-producto",        # one of the 4 fixed section slugs
  "subsection": "...",             # free text, optional
  "summary": "...",
  "key_points": ["...", "..."],
  "content_md": "## De qué va\n...",   # body only, no images/original-link footer
  "image_urls": ["https://...jpg"],    # optional, absolute URLs
  "glossary": [{"term": "...", "definition": "..."}],  # optional, jargon explained in plain language
  "date_added": "2026-07-12"       # optional, defaults to today
}

What it does:
  1. Slugifies the title into a stable id.
  2. Downloads any image_urls into images/<id>/ (skips ones that fail, never fatal).
  3. Writes articles/<section>/<id>.md with frontmatter + images + body + glossary + original link.
  4. Upserts the entry into data/articles.json (matched by id).
  5. Runs build_repo.py inside project_dir to regenerate index.html.
"""
import argparse
import json
import os
import re
import shutil
import sys
import subprocess
import unicodedata
import urllib.request
from datetime import date

VALID_SECTIONS = {"design-2-0", "claude", "figma", "engineering", "ai"}
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"


def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-zA-Z0-9\s-]", "", text).strip().lower()
    text = re.sub(r"[\s-]+", "-", text)
    return text[:70].strip("-") or "articulo"


def load_json(path, default):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return default


def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def download_image(url, dest_path):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=15) as resp, open(dest_path, "wb") as out:
            out.write(resp.read())
        return True
    except Exception as e:
        print(f"  ! No se pudo descargar imagen ({url}): {e}", file=sys.stderr)
        return False


def guess_ext(url):
    m = re.search(r"\.(jpg|jpeg|png|gif|webp)(\?|$)", url.lower())
    return m.group(1) if m else "jpg"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-file", help="Path to a JSON file with the article data")
    args = ap.parse_args()

    if args.data_file:
        with open(args.data_file, encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)

    project_dir = data["project_dir"]
    title = data["title"].strip()
    url = data["url"].strip()
    section = data["section"].strip()
    subsection = (data.get("subsection") or "").strip()
    summary = data.get("summary", "").strip()
    key_points = data.get("key_points", [])
    content_md = data.get("content_md", "").strip()
    image_urls = data.get("image_urls", []) or []
    image_paths = data.get("image_paths", []) or []
    glossary = data.get("glossary", []) or []
    date_added = data.get("date_added") or date.today().isoformat()
    dictionary = bool(data.get("dictionary", False))

    if section not in VALID_SECTIONS:
        print(f"Sección desconocida '{section}'. Debe ser una de: {sorted(VALID_SECTIONS)}", file=sys.stderr)
        sys.exit(1)

    article_id = slugify(title)

    # --- images ---
    image_rel_paths = []
    if image_urls or image_paths:
        img_dir_abs = os.path.join(project_dir, "images", article_id)
        os.makedirs(img_dir_abs, exist_ok=True)
        counter = 1
        for img_url in image_urls[:3]:
            ext = guess_ext(img_url)
            fname = f"img{counter}.{ext}"
            dest = os.path.join(img_dir_abs, fname)
            if download_image(img_url, dest):
                image_rel_paths.append(f"images/{article_id}/{fname}")
                counter += 1
        for src_path in image_paths[:3]:
            if not os.path.exists(src_path):
                print(f"  ! No existe el archivo de imagen local: {src_path}", file=sys.stderr)
                continue
            ext = os.path.splitext(src_path)[1].lstrip(".").lower() or "jpg"
            fname = f"img{counter}.{ext}"
            dest = os.path.join(img_dir_abs, fname)
            shutil.copyfile(src_path, dest)
            image_rel_paths.append(f"images/{article_id}/{fname}")
            counter += 1

    # --- build content with images prepended ---
    image_md = "\n".join(f"![]({p})" for p in image_rel_paths)
    full_content_md = (image_md + "\n\n" + content_md).strip() if image_md else content_md

    # --- write the .md file (source of truth, human-readable) ---
    md_dir = os.path.join(project_dir, "articles", section)
    os.makedirs(md_dir, exist_ok=True)
    md_path = os.path.join(md_dir, f"{article_id}.md")
    frontmatter = (
        "---\n"
        f"title: {title}\n"
        f"url: {url}\n"
        f"section: {section}\n"
        f"subsection: {subsection}\n"
        f"date_added: {date_added}\n"
        "---\n\n"
    )
    md_body = full_content_md
    if glossary:
        md_body += "\n\n## Para aprender\n" + "\n".join(
            f"- **{g.get('term','')}**: {g.get('definition','')}" for g in glossary
        )
    md_body += f"\n\n---\nArtículo original: {url}\n"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(frontmatter + md_body)

    # --- upsert into data/articles.json ---
    data_json_path = os.path.join(project_dir, "data", "articles.json")
    articles = load_json(data_json_path, [])
    entry = {
        "id": article_id,
        "title": title,
        "url": url,
        "section": section,
        "subsection": subsection,
        "summary": summary,
        "key_points": key_points,
        "content_md": full_content_md,
        "images": image_rel_paths,
        "glossary": glossary,
        "date_added": date_added,
        "dictionary": dictionary,
    }
    existing_idx = next((i for i, a in enumerate(articles) if a.get("id") == article_id), None)
    if existing_idx is not None:
        articles[existing_idx] = entry
        action = "actualizado"
    else:
        articles.append(entry)
        action = "añadido"
    save_json(data_json_path, articles)

    # --- regenerate the site ---
    build_script = os.path.join(project_dir, "build_repo.py")
    if os.path.exists(build_script):
        subprocess.run([sys.executable, build_script], cwd=project_dir, check=True)

    print(json.dumps({
        "status": "ok",
        "action": action,
        "id": article_id,
        "section": section,
        "md_path": md_path,
        "images_saved": image_rel_paths,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
