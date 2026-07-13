#!/usr/bin/env python3
"""
Permanently delete an article from Isabel's "The Future Designer" repo:
removes its entry from data/articles.json, deletes its .md file and its
images/<id>/ folder if any, then regenerates index.html.

Usage:
    python3 delete_article.py --project-dir "<ruta del proyecto>" --id <article-id>
"""
import argparse
import json
import os
import shutil
import subprocess
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project-dir", required=True)
    ap.add_argument("--id", required=True)
    args = ap.parse_args()

    project_dir = args.project_dir
    article_id = args.id

    data_json_path = os.path.join(project_dir, "data", "articles.json")
    with open(data_json_path, encoding="utf-8") as f:
        articles = json.load(f)

    match = next((a for a in articles if a.get("id") == article_id), None)
    if not match:
        print(f"No se encontró ningún artículo con id '{article_id}'", file=sys.stderr)
        sys.exit(1)

    articles = [a for a in articles if a.get("id") != article_id]
    with open(data_json_path, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

    md_path = os.path.join(project_dir, "articles", match["section"], f"{article_id}.md")
    if os.path.exists(md_path):
        os.remove(md_path)

    img_dir = os.path.join(project_dir, "images", article_id)
    if os.path.isdir(img_dir):
        shutil.rmtree(img_dir)

    build_script = os.path.join(project_dir, "build_repo.py")
    if os.path.exists(build_script):
        subprocess.run([sys.executable, build_script], cwd=project_dir, check=True)

    print(json.dumps({"status": "ok", "deleted_id": article_id, "title": match["title"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
