"""
Genera una ilustración de portada (SVG) por artículo: una escena a medida para cada uno,
al estilo "dibujado a mano" — trazo boceteado (doble pasada, ligero temblor de línea, como
rotulador), blanco y negro puro, fondo neutro liso, sin texto dentro de la imagen.

Cada artículo tiene su propia función de composición (`SCENES`), dibujada con las primitivas
"sketchy_*" (líneas, rects, círculos y polígonos con jitter determinista) que representan la
idea del artículo, no su contenido literal. Un artículo nuevo sin escena propia cae a una marca
abstracta genérica (ver `fallback_scene`) hasta que se le dibuje la suya.

Uso:
    python3 scripts/generate_cover_art.py            # regenera todas las portadas
"""
import argparse, json, os, math, random, runpy, subprocess

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE, "data", "articles.json")
IMAGES_DIR = os.path.join(BASE, "images")

g = runpy.run_path(os.path.join(BASE, "build_repo.py"))
articles = g["articles"]

INK, PAPER = "#111111", "#ffffff"
W, H, SW = 1200, 630, 6  # canvas + grosor de trazo estándar

# ---------------------------------------------------------------- geometría base
def deg(cx, cy, r, a):
    rad = math.radians(a)
    return cx + r * math.cos(rad), cy + r * math.sin(rad)

def jitter_pt(x, y, r, rng):
    a = rng.uniform(0, 2 * math.pi)
    d = rng.uniform(0, r)
    return x + d * math.cos(a), y + d * math.sin(a)

def _dense(points, closed, n_sub):
    """Subdivide cada segmento para tener puntos intermedios que temblar."""
    out = []
    n = len(points)
    span = n if closed else n - 1
    for i in range(span):
        p0 = points[i]
        p1 = points[(i + 1) % n]
        for t in range(n_sub):
            out.append((p0[0] + (p1[0] - p0[0]) * t / n_sub, p0[1] + (p1[1] - p0[1]) * t / n_sub))
    if not closed:
        out.append(points[-1])
    return out

# ---------------------------------------------------------------- primitivas "boceteadas"
def sketchy_path(points, seed, passes=2, rough=4, sw=SW, closed=False, n_sub=4, stroke=INK, opacity=0.9):
    dense = _dense(points, closed, n_sub)
    out = []
    for p in range(passes):
        rng = random.Random((seed, p))
        jittered = [jitter_pt(x, y, rough, rng) for (x, y) in dense]
        if closed:
            jittered.append(jittered[0])
        d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in jittered)
        out.append(f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{sw}" '
                   f'stroke-linecap="round" stroke-linejoin="round" opacity="{opacity}"/>')
    return "".join(out)

def sketchy_line(x1, y1, x2, y2, seed, passes=2, rough=3.5, sw=SW, segments=5, stroke=INK):
    pts = [(x1 + (x2 - x1) * t / segments, y1 + (y2 - y1) * t / segments) for t in range(segments + 1)]
    return sketchy_path(pts, seed, passes, rough, sw, closed=False, n_sub=1, stroke=stroke)

def sketchy_rect(x, y, w, h, seed, passes=2, rough=3.5, sw=SW, stroke=INK, n_sub=4):
    pts = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    return sketchy_path(pts, seed, passes, rough, sw, closed=True, n_sub=n_sub, stroke=stroke)

def sketchy_circle(cx, cy, r, seed, passes=2, rough=3.5, sw=SW, n=26, stroke=INK):
    pts = [deg(cx, cy, r, 360 * i / n) for i in range(n)]
    return sketchy_path(pts, seed, passes, rough, sw, closed=True, n_sub=1, stroke=stroke)

def sketchy_polygon(points, seed, passes=2, rough=3.5, sw=SW, stroke=INK, n_sub=3):
    return sketchy_path(points, seed, passes, rough, sw, closed=True, n_sub=n_sub, stroke=stroke)

def sketchy_arc(cx, cy, r, a0, a1, seed, passes=2, rough=3.5, sw=SW, n=22, stroke=INK):
    steps = max(int(n * abs(a1 - a0) / 180), 6)
    pts = [deg(cx, cy, r, a0 + (a1 - a0) * i / steps) for i in range(steps + 1)]
    return sketchy_path(pts, seed, passes, rough, sw, closed=False, n_sub=1, stroke=stroke)

def solid_blob(points, seed, rough=5, fill=INK, n_sub=3, closed=True):
    """Silueta rellena de negro sólido con el borde ligeramente irregular (a mano)."""
    dense = _dense(points, closed, n_sub)
    rng = random.Random(seed)
    jittered = [jitter_pt(x, y, rough, rng) for (x, y) in dense]
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in jittered) + " Z"
    return f'<path d="{d}" fill="{fill}"/>'

def arrowhead(tip, angle_deg, size=24, seed=0):
    tx, ty = tip
    left = math.radians(angle_deg + 180 - 26)
    right = math.radians(angle_deg + 180 + 26)
    p1 = (tx + size * math.cos(left), ty + size * math.sin(left))
    p2 = (tx + size * math.cos(right), ty + size * math.sin(right))
    return solid_blob([tip, p1, p2], seed, rough=1.5)

def sparkle(cx, cy, size, seed):
    """Pequeña marca de brillo/doodle a mano — firma discreta del set."""
    pts = [(cx, cy - size), (cx + size * 0.16, cy - size * 0.16), (cx + size, cy),
           (cx + size * 0.16, cy + size * 0.16), (cx, cy + size), (cx - size * 0.16, cy + size * 0.16),
           (cx - size, cy), (cx - size * 0.16, cy - size * 0.16)]
    return solid_blob(pts, seed, rough=1.2, n_sub=1)

def frame_wrap(body, seed):
    frame = sketchy_rect(12, 12, W - 24, H - 24, (seed, "frame"), passes=2, rough=3, sw=6)
    spark = sparkle(W - 78, 78, 20, (seed, "spark"))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <rect width="{W}" height="{H}" fill="{PAPER}"/>
  {body}
  {frame}
  {spark}
</svg>'''


# ---------------------------------------------------------------- escenas (una por artículo)
def scene_rl_basics():
    """Aprendizaje por refuerzo: agente en una rejilla, recompensa, y el bucle que los une."""
    gx, gy, cell, n = 380, 155, 106, 3
    s = []
    s.append(sketchy_rect(gx, gy, cell * n, cell * n, "rl-grid", sw=6))
    for i in range(1, n):
        s.append(sketchy_line(gx + i * cell, gy, gx + i * cell, gy + cell * n, ("rl-v", i), sw=3.5))
        s.append(sketchy_line(gx, gy + i * cell, gx + cell * n, gy + i * cell, ("rl-h", i), sw=3.5))
    ax, ay = gx + cell * 0.5, gy + cell * 2.5
    s.append(solid_blob([(ax - 24, ay - 24), (ax + 24, ay - 24), (ax + 24, ay + 24), (ax - 24, ay + 24)], "rl-agent"))
    sx, sy = gx + cell * 2.5, gy + cell * 0.5
    star_pts = [deg(sx, sy, 30 if i % 2 == 0 else 13, -90 + i * 36) for i in range(10)]
    s.append(solid_blob(star_pts, "rl-star", rough=2, n_sub=1))
    s.append(sketchy_arc(600, 315, 300, -60, 220, "rl-loop", sw=6))
    tip = deg(600, 315, 300, 220)
    s.append(arrowhead(tip, 220 + 90, size=28, seed="rl-arrow"))
    return "".join(s)

def scene_astryx_design_system():
    """Design system: componentes apilados, uno resaltado, con un cursor apuntando."""
    s = []
    boxes = [(430, 210, 260, 170), (470, 250, 260, 170), (510, 290, 260, 170)]
    for i, (x, y, w, h) in enumerate(boxes):
        if i == 2:
            s.append(solid_blob([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], f"astryx-{i}", rough=4))
        else:
            s.append(sketchy_rect(x, y, w, h, f"astryx-{i}", sw=5.5))
    cx, cy = 792, 432
    s.append(solid_blob([(cx, cy), (cx, cy + 62), (cx + 16, cy + 46), (cx + 26, cy + 70),
                          (cx + 40, cy + 62), (cx + 28, cy + 40), (cx + 50, cy + 40)], "astryx-cursor", rough=2))
    return "".join(s)

def scene_claude_agents():
    """Qué es un agente: una cabeza-robot con herramientas orbitando, unidas por líneas."""
    cx, cy = 600, 300
    s = [sketchy_rect(cx - 130, cy - 110, 260, 220, "agent-head", sw=6.5)]
    s.append(solid_blob([(cx - 80, cy - 40), (cx - 20, cy - 40), (cx - 20, cy + 20), (cx - 80, cy + 20)], "agent-eye1", rough=2.5))
    s.append(solid_blob([(cx + 20, cy - 40), (cx + 80, cy - 40), (cx + 80, cy + 20), (cx + 20, cy + 20)], "agent-eye2", rough=2.5))
    s.append(sketchy_line(cx, cy - 110, cx, cy - 160, "agent-antenna", sw=5))
    s.append(sketchy_circle(cx, cy - 178, 16, "agent-antenna-tip", sw=5))
    gx, gy, r = cx + 260, cy - 60, 60
    teeth = []
    for i in range(8):
        a0, a1 = i * 45 - 12, i * 45 + 12
        teeth.append(deg(gx, gy, r, a0))
        teeth.append(deg(gx, gy, r + 26, (a0 + a1) / 2))
        teeth.append(deg(gx, gy, r, a1))
    s.append(sketchy_polygon(teeth, "agent-gear", sw=4.5))
    s.append(sketchy_circle(gx, gy, 22, "agent-gear-hub", sw=4.5))
    s.append(sketchy_line(cx + 120, cy - 20, gx - 60, gy, "agent-line1", sw=4))
    bx, by = cx - 260, cy + 90
    s.append(solid_blob([(bx - 55, by - 40), (bx + 55, by - 40), (bx + 55, by + 40), (bx - 55, by + 40)], "agent-tool", rough=3))
    s.append(sketchy_line(cx - 120, cy + 40, bx + 55, by, "agent-line2", sw=4))
    return "".join(s)

def scene_context_window():
    """A dónde va tu contexto: archivos cayendo por un embudo hacia una caja (context window)."""
    s = []
    files = [(390, 120, 70, 90, -8), (520, 90, 70, 90, 5), (650, 130, 70, 90, -4), (770, 95, 70, 90, 9)]
    for i, (x, y, w, h, rot) in enumerate(files):
        s.append(f'<g transform="rotate({rot} {x + w/2} {y + h/2})">'
                 f'{sketchy_rect(x, y, w, h, f"ctx-file-{i}", sw=4.5)}</g>')
    fx, fy = 600, 300
    s.append(sketchy_polygon([(fx - 220, 250), (fx + 220, 250), (fx + 60, 420), (fx - 60, 420)], "ctx-funnel", sw=6))
    s.append(solid_blob([(fx - 90, 440), (fx + 90, 440), (fx + 90, 570), (fx - 90, 570)], "ctx-box", rough=4))
    return "".join(s)

def scene_usage_limits():
    """Límites de uso: un medidor de combustible con la aguja casi en la zona roja (sólida)."""
    cx, cy, r = 600, 400, 260
    s = [sketchy_arc(cx, cy, r, 180, 360, "gauge-arc", sw=8)]
    wedge = [(cx, cy)] + [deg(cx, cy, r, a) for a in range(180, 226, 5)]
    s.append(solid_blob(wedge, "gauge-wedge", rough=3))
    needle_tip = deg(cx, cy, r - 40, 205)
    s.append(sketchy_line(cx, cy, needle_tip[0], needle_tip[1], "gauge-needle", sw=8))
    s.append(arrowhead(needle_tip, 205, size=22, seed="gauge-arrow"))
    s.append(solid_blob([deg(cx, cy, 24, a) for a in range(0, 360, 45)], "gauge-hub", rough=2))
    for a in range(180, 361, 30):
        x0, y0 = deg(cx, cy, r + 14, a)
        x1, y1 = deg(cx, cy, r + 38, a)
        s.append(sketchy_line(x0, y0, x1, y1, ("gauge-tick", a), sw=4))
    return "".join(s)

def scene_dictionary():
    """Diccionario de IA: libro abierto con marcapáginas y reglas cortas (no texto)."""
    cx, cy = 600, 330
    s = [
        sketchy_polygon([(cx, cy - 130), (cx - 260, cy - 90), (cx - 260, cy + 150), (cx, cy + 120)], "book-l", sw=6),
        sketchy_polygon([(cx, cy - 130), (cx + 260, cy - 90), (cx + 260, cy + 150), (cx, cy + 120)], "book-r", sw=6),
        sketchy_line(cx, cy - 130, cx, cy + 120, "book-spine", sw=6),
    ]
    for i in range(3):
        yy = cy - 40 + i * 40
        s.append(sketchy_line(cx - 200, yy - 8 * i, cx - 40, yy - 4 * i, ("book-rl", i), sw=4))
        s.append(sketchy_line(cx + 40, yy - 4 * i, cx + 200, yy - 8 * i, ("book-rr", i), sw=4))
    s.append(solid_blob([(cx + 130, cy - 128), (cx + 178, cy - 128), (cx + 178, cy - 10),
                          (cx + 154, cy - 34), (cx + 130, cy - 10)], "book-mark", rough=2.5))
    return "".join(s)

def scene_generic_web_design():
    """5 trucos anti-genérico: dos ventanas de navegador, una vacía y otra con una marca propia."""
    s = []
    for i, x in enumerate((260, 660)):
        y, w, h = 165, 280, 300
        s.append(sketchy_rect(x, y, w, h, f"web-{i}", sw=6))
        s.append(sketchy_line(x, y + 46, x + w, y + 46, f"web-bar-{i}", sw=4.5))
        for j in range(3):
            cx2, cy2 = x + 30 + j * 26, y + 23
            if i == 1:
                s.append(solid_blob([deg(cx2, cy2, 8, a) for a in range(0, 360, 45)], f"web-dot-{i}-{j}", rough=1.5))
            else:
                s.append(sketchy_circle(cx2, cy2, 8, f"web-dot-{i}-{j}", sw=3))
        if i == 0:
            s.append(sketchy_line(x + 40, y + 100, x + w - 40, y + 100, "web-l1", sw=4))
            s.append(sketchy_line(x + 40, y + 140, x + w - 90, y + 140, "web-l2", sw=4))
            s.append(sketchy_line(x + 40, y + 180, x + w - 60, y + 180, "web-l3", sw=4))
        else:
            s.append(solid_blob([(x + w / 2, y + 90), (x + w - 60, y + 230), (x + 60, y + 230)], "web-mark", rough=3))
    return "".join(s)

def scene_pragnanz():
    """Ley de Prägnanz: una forma irregular se convierte en un círculo limpio."""
    s = []
    cx, cy = 420, 315
    rnd = random.Random(7)
    pts = [deg(cx, cy, 150 + rnd.uniform(-55, 55), i * (360 / 11)) for i in range(11)]
    s.append(sketchy_polygon(pts, "prag-blob", sw=6))
    s.append(sketchy_line(650, 315, 745, 315, "prag-arrow-line", sw=7))
    s.append(arrowhead((770, 315), 0, size=32, seed="prag-arrow-head"))
    s.append(solid_blob([deg(960, 315, 140, a) for a in range(0, 360, 20)], "prag-circle", rough=4))
    return "".join(s)

def scene_designmd():
    """design.md: un archivo con reglas cortas entra en una cabeza-robot."""
    s = []
    fx, fy, fw, fh = 300, 155, 260, 330
    s.append(sketchy_polygon([(fx, fy), (fx + fw - 60, fy), (fx + fw, fy + 60), (fx + fw, fy + fh), (fx, fy + fh)],
                              "md-file", sw=6, n_sub=4))
    s.append(sketchy_line(fx + fw - 60, fy, fx + fw - 60, fy + 60, "md-fold1", sw=4.5))
    s.append(sketchy_line(fx + fw - 60, fy + 60, fx + fw, fy + 60, "md-fold2", sw=4.5))
    for i in range(5):
        yy = fy + 110 + i * 40
        s.append(sketchy_line(fx + 40, yy, fx + fw - 40 - (20 if i % 2 else 0), yy, ("md-rule", i), sw=4.5))
    s.append(sketchy_line(fx + fw + 40, fy + fh / 2, 780, fy + fh / 2, "md-arrow-line", sw=6))
    s.append(arrowhead((780, fy + fh / 2), 0, size=26, seed="md-arrow-head"))
    cx, cy = 920, fy + fh / 2
    s.append(sketchy_rect(cx - 100, cy - 90, 200, 170, "md-robot", sw=7))
    s.append(sketchy_rect(cx - 55, cy - 25, 40, 40, "md-eye1", sw=4.5))
    s.append(solid_blob([(cx + 15, cy - 25), (cx + 55, cy - 25), (cx + 55, cy + 15), (cx + 15, cy + 15)], "md-eye2", rough=2))
    return "".join(s)

def scene_taste_skill():
    """Anti-slop: formas irregulares caen por un tamiz y solo las limpias pasan."""
    s = []
    rnd = random.Random(3)
    for i in range(4):
        cx, cy = 380 + i * 130, 140
        pts = [deg(cx, cy, 34 + rnd.uniform(-10, 14), a + rnd.uniform(-10, 10)) for a in range(0, 360, 60)]
        s.append(sketchy_polygon(pts, f"taste-blob-{i}", sw=4, n_sub=2))
    mesh_y = 300
    s.append(sketchy_line(280, mesh_y, 920, mesh_y, "taste-mesh", sw=7))
    for x in range(320, 921, 60):
        s.append(sketchy_line(x, mesh_y - 16, x, mesh_y + 16, ("taste-tick", x), sw=4))
    for i, cx in enumerate((460, 600, 740)):
        if i == 1:
            s.append(solid_blob([deg(cx, 470, 40, a) for a in range(0, 360, 30)], f"taste-c-{i}", rough=3))
        else:
            s.append(sketchy_circle(cx, 470, 40, f"taste-c-{i}", sw=5))
    return "".join(s)

def scene_two_level_loop():
    """Loop de 2 niveles: dos bucles concéntricos alrededor de una marca de verificación."""
    cx, cy = 600, 315
    s = [sketchy_arc(cx, cy, 250, -40, 260, "loop-outer", sw=6.5)]
    s.append(arrowhead(deg(cx, cy, 250, 260), 260 + 90, size=26, seed="loop-outer-arrow"))
    s.append(sketchy_arc(cx, cy, 150, 200, 500, "loop-inner", sw=6.5))
    s.append(arrowhead(deg(cx, cy, 150, 140), 140 + 90, size=22, seed="loop-inner-arrow"))
    s.append(sketchy_line(cx - 45, cy, cx - 12, cy + 40, "loop-check1", sw=12))
    s.append(sketchy_line(cx - 12, cy + 40, cx + 55, cy - 45, "loop-check2", sw=12))
    return "".join(s)

SCENES = {
    "aprendizaje-por-refuerzo-basico": scene_rl_basics,
    "meta-abre-astryx-su-design-system-interno-y-ya-funciona-en-figma-make": scene_astryx_design_system,
    "claude-agents-que-son-y-como-crear-uno": scene_claude_agents,
    "donde-va-realmente-tu-contexto-de-diseno-en-claude": scene_context_window,
    "los-disenadores-gastan-los-limites-de-uso-de-claude-mas-rapido-que-nad": scene_usage_limits,
    "diccionario-de-ia-para-disenadores": scene_dictionary,
    "5-trucos-para-que-claude-code-no-te-de-un-diseno-web-generico": scene_generic_web_design,
    "la-ley-de-pragnanz-el-buen-diseno-es-quitar-no-anadir": scene_pragnanz,
    "designmd-buenas-practicas-para-el-archivo-que-le-da-a-la-ia-tu-sistema": scene_designmd,
    "taste-skill-el-framework-anti-slop-para-que-tu-agente-de-ia-tenga-buen": scene_taste_skill,
    "el-loop-de-2-niveles-para-que-claude-deje-de-autopuntuarse-su-propio-d": scene_two_level_loop,
}

def fallback_scene(article_id):
    """Marca abstracta genérica para un artículo sin escena propia todavía: un rombo
    boceteado descentrado con un círculo sólido, variado de forma determinista por id."""
    h = sum(ord(c) for c in article_id)
    cx, cy = 600 + (h % 80 - 40), 315
    r = 190
    pts = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
    s = [sketchy_polygon(pts, article_id + "-diamond", sw=6.5)]
    s.append(solid_blob([deg(cx, cy, 46, a) for a in range(0, 360, 30)], article_id + "-dot", rough=3))
    return "".join(s)


CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
]

def render_preview(svg_paths):
    """Renderiza cada SVG a PNG a tamaño real (1200x630) con Chrome headless, para poder
    revisarlos con Read antes de dar nada por bueno. Se guardan fuera del repo, en /tmp."""
    chrome = next((c for c in CHROME_CANDIDATES if os.path.exists(c)), None)
    if not chrome:
        print("(No se encontró Chrome para generar la vista previa — ábrelo manualmente.)")
        return []
    out_dir = "/tmp/cover_previews"
    os.makedirs(out_dir, exist_ok=True)
    pngs = []
    for svg_path in svg_paths:
        article_id = os.path.basename(os.path.dirname(svg_path))
        out_png = os.path.join(out_dir, f"{article_id}.png")
        subprocess.run(
            [chrome, "--headless", "--disable-gpu", f"--screenshot={out_png}",
             "--window-size=1200,630", f"file://{os.path.abspath(svg_path)}"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        pngs.append(out_png)
    return pngs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="Genera solo el artículo con este id (por defecto: todos)")
    ap.add_argument("--preview", action="store_true",
                     help="Además, renderiza cada portada a PNG (vía Chrome headless) para revisarla")
    args = ap.parse_args()

    targets = [a for a in articles if a["id"] == args.only] if args.only else articles
    if args.only and not targets:
        print(f"No existe ningún artículo con id '{args.only}'.")
        return

    changed = []
    svg_paths = []
    for a in targets:
        scene_fn = SCENES.get(a["id"])
        body = scene_fn() if scene_fn else fallback_scene(a["id"])
        out_dir = os.path.join(IMAGES_DIR, a["id"])
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "cover.svg")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(frame_wrap(body, a["id"]))
        svg_paths.append(out_path)
        rel_path = f"images/{a['id']}/cover.svg"
        if a.get("images") != [rel_path]:
            a["images"] = [rel_path]
        changed.append(a["id"])
        if not scene_fn:
            print(f"  ! '{a['id']}' no tiene escena propia todavía — usando la genérica de repuesto.")

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)
    print(f"Generadas {len(changed)} portadas.")

    if args.preview:
        pngs = render_preview(svg_paths)
        for p in pngs:
            print(f"Vista previa: {p}")


if __name__ == "__main__":
    main()
