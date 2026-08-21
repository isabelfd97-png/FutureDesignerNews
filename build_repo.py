import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE, "data", "articles.json")
COMMANDS_FILE = os.path.join(BASE, "data", "commands.json")
OUT_FILE = os.path.join(BASE, "index.html")

with open(DATA_FILE, encoding="utf-8") as f:
    articles = json.load(f)

with open(COMMANDS_FILE, encoding="utf-8") as f:
    commands = json.load(f)

SECTIONS = [
    {
        "slug": "teoria",
        "name": "Teoría",
        "desc": "Conceptos y principios de fondo, sin fecha de caducidad: fundamentos de IA, terminología de referencia, teoría del diseño.",
        "icon": "book",
    },
    {
        "slug": "practica",
        "name": "Práctica",
        "desc": "Guías accionables para trabajar mejor con Claude: contexto, límites de uso, agentes, CLAUDE.md y cómo evitar el diseño genérico.",
        "icon": "claude",
    },
    {
        "slug": "novedades",
        "name": "Novedades",
        "desc": "Lanzamientos, herramientas y kits descargables: lo que está pasando ahora en design systems y agentes de IA.",
        "icon": "materials",
    },
]

def pixel_svg(rows):
    """Genera un icono pixel-art a partir de un patrón de '#'/'.'."""
    size = len(rows)
    cells = "".join(
        f'<rect x="{x}" y="{y}" width="1" height="1"/>'
        for y, row in enumerate(rows)
        for x, ch in enumerate(row)
        if ch == "#"
    )
    return f'<svg viewBox="0 0 {size} {size}" fill="currentColor" shape-rendering="crispEdges">{cells}</svg>'

# Iconos funcionales pequeños (12x12) — usados en botones y controles.
# search, arrow, heart, history y flame se quedan con iconografía de línea normal (ver más abajo).
PIXEL12 = {'close': ['##........##', '###......###', '.###....###.', '..###..###..', '...######...', '....####....', '....####....', '...######...', '..###..###..', '.###....###.', '###......###', '##........##'], 'check': ['............', '............', '...........#', '..........##', '.........##.', '#.......##..', '##.....##...', '.##...##....', '..##.##.....', '...###......', '....#.......', '............'], 'trash': ['...######...', '..#......#..', '.##########.', '..#.####.#..', '..#.####.#..', '..#.####.#..', '..#.####.#..', '..#.####.#..', '..#.####.#..', '..#.####.#..', '..#......#..', '...######...'], 'restore': ['............', '............', '....####.##.', '...#....#.#.', '..#......#..', '..#.........', '..#.........', '..#.........', '...#........', '....####....', '............', '............'], 'star': ['.....#......', '....###.....', '....#.#.....', '............', '.##.....##..', '##.......##.', '.##.....##..', '............', '....#.#.....', '....###.....', '.....#......', '............'], 'star-filled': ['.....#......', '....###.....', '....###.....', '....###.....', '.#########..', '###########.', '.#########..', '....###.....', '....###.....', '....###.....', '.....#......', '............'], 'edit': ['.........##.', '........####', '.......###..', '......###...', '.....###....', '....###.....', '...###......', '..###.......', '.###........', '.##.........', '.#..........', '.##.........'], 'link': ['............', '....#.......', '..#####.....', '..#...#.....', '.##...#.....', '..#...#.#...', '..#########.', '......#...#.', '.....##...#.', '......#...#.', '......####..', '............'], 'cards': ['............', '....#######.', '....#.....#.', '....#.....#.', '.#######..#.', '.#..#..#..#.', '.#..#..#..#.', '.#..#######.', '.#.....#....', '.#.....#....', '.#######....', '............'], 'eye': ['............', '....####....', '..##....##..', '.#........#.', '#....##....#', '#...####...#', '#...####...#', '#....##....#', '.#........#.', '..##....##..', '....####....', '............'], 'chart': ['............', '............', '.........###', '.........###', '.........###', '.....###.###', '.....###.###', '.....###.###', '.###.###.###', '.###.###.###', '.###.###.###', '############'], 'wrench': ['............', '..###.......', '.##.##......', '...###......', '...###......', '...####.....', '.....###....', '......###...', '.......###..', '........###.', '.........###', '..........#.'], 'question': ['....####....', '..##....##..', '.##......##.', '........##..', '.......##...', '......##....', '.....##.....', '.....##.....', '............', '.....##.....', '.....##.....', '............'], 'plus': ['............', '.....##.....', '.....##.....', '.....##.....', '.....##.....', '##########..', '##########..', '.....##.....', '.....##.....', '.....##.....', '.....##.....', '............']}

# Iconos pixel-art (12x12) — secciones, artículo principal. Estilo icono, no ilustración: formas simples y limpias.
PIXEL16 = {'px-robot': ['......#.....', '......#.....', '..████████..', '..█......█..', '███......███', '███.█..█.███', '███.█..█.███', '..█......█..', '..█.████.█..', '..████████..', '............', '............'], 'px-chip': ['...█..█..█..', '...█..█..█..', '..████████..', '███......███', '..█.████.█..', '..█.█..█.█..', '███.█..█.███', '..█.████.█..', '..█......█..', '████████████', '...█..█..█..', '...█..█..█..'], 'px-book': ['............', '..████████..', '..█..██..█..', '..█..██..█..', '..████████..', '..█..██..█..', '..████████..', '..█..██..█..', '..████████..', '..█..██..█..', '..████████..', '............'], 'px-chat': ['............', '.██████████.', '.█........█.', '.█........█.', '.█.█.█.█.█.█.', '.█.█.█.█.█.█.', '.█........█.', '.██████████.', '...█........', '..█.........', '.█..........', '............'], 'px-palette': ['............', '............', '....████....', '...██..██...', '..█.█..█.█..', '..█.....██..', '.█......███.', '..█......█..', '..█.........', '...█........', '....████....', '............'], 'px-brain': ['............', '............', '....████....', '...█..█.█...', '..█...█..█..', '..█████..█..', '.█....█...█.', '..█...████..', '..█...█..█..', '...█..█.█...', '....████....', '............'], 'px-terminal': ['............', '............', '.██████████.', '.█........█.', '.█.█......█.', '.█..█.....█.', '.█...█....█.', '.█..█.....█.', '.█.█..███.█.', '.██████████.', '............', '............'], 'layers': ['............', '.....███....', '...██...██..', '.███.....███', '....█████...', '...██...██..', '.██.......██', '...██...██..', '....█████...', '.███.....███', '...██...██..', '.....███....'], 'px-star': ['............', '.....██.....', '.....██.....', '.....██.....', '.....██.....', '.██████████.', '.██████████.', '.....██.....', '.....██.....', '.....██.....', '.....██.....', '............']}
# Iconos de sección (16x16), más densos/con más peso visual que los del artículo principal
PIXEL16['layers'] = ['................', '................', '.......###......', '....##.....##...', '..##.........##.', '....##.....##...', '.......###......', '....##.....##...', '..##.........##.', '....##.....##...', '.......###......', '....##.....##...', '..##.........##.', '....##.....##...', '.......###......', '................']
PIXEL16['chip'] = ['....#...#...#...', '....#...#...#...', '....#...#...#...', '...##########...', '################', '...##......##...', '...##.####.##...', '...##.####.##...', '#####.####.#####', '...##.####.##...', '...##......##...', '...##########...', '################', '....#...#...#...', '....#...#...#...', '....#...#...#...']
PIXEL16['book'] = ['......##........', '..############..', '..##..##.....#..', '..######.#####..', '..##..##.....#..', '..######.#####..', '..##..##.....#..', '..##..##.....#..', '..##..##.....#..', '..######.#####..', '..##..##.....#..', '..######.#####..', '..##..##.....#..', '..##..##.....#..', '..############..', '................']
PIXEL16['chat-code'] = ['................', '.##############.', '.##############.', '.#............#.', '.#...#.##.#...#.', '.#..#..##..#..#.', '.#.#...##...#.#.', '.#..#..##..#..#.', '.#...#.##.#...#.', '.#............#.', '.##############.', '................', '....#...........', '...#............', '..#.............', '................']
PIXEL16['design-2-0'] = ['................', '................', '......#####.....', '....#######..##.', '...###.......#..', '...##........##.', '..##.............', '..##...##.......', '..##...##.......', '..##.............', '..##.............', '...##.......#...', '...###.....###..', '....#########...', '......#####.....', '................']
PIXEL16['claude'] = ['........#.......', '........#.......', '........#.......', '..############..', '..############..', '..##........##..', '################', '################', '################', '################', '####........####', '..##.######.##..', '..############..', '..############..', '................', '................']
PIXEL16['materials'] = ['................', '................', '........#.......', '......##.##.....', '....##.....##...', '..##.........##.', '..###.......###.', '..#..##...##..#.', '..#....###....#.', '..#...#####...#.', '..#...#####...#.', '..#...#####...#.', '..#...#####...#.', '...##...#...##..', '.....##.#.##....', '.......###......']
PIXEL16['px-box'] = ['............', '......#.....', '....##.##...', '..##.....##.', '.##.......##', '.#.##...##.#', '.#...###...#', '.#....#....#', '.#....#....#', '.##...#...##', '...##.#.##..', '.....###....']

ICONS = {}
for _key, _rows in {**PIXEL12, **PIXEL16}.items():
    ICONS[_key] = pixel_svg(_rows)

# Iconografía de línea normal (no pixel art) para: buscar, flechas, corazón, historial, racha
ICONS['search'] = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>'
ICONS['arrow'] = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ICONS['history'] = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7.5v5l3.2 1.9"/></svg>'
ICONS['heart'] = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 20.5s-7.5-4.6-10-9.3C.4 7.9 2 4.5 5.4 4c2-.3 3.8.6 4.9 2.3.8 1.2 1.7 1.2 2.5 0C13.8 4.6 15.6 3.7 17.6 4c3.4.5 5 3.9 3.4 7.2-2.5 4.7-9 9.3-9 9.3Z"/></svg>'
ICONS['heart-filled'] = '<svg viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M12 20.5s-7.5-4.6-10-9.3C.4 7.9 2 4.5 5.4 4c2-.3 3.8.6 4.9 2.3.8 1.2 1.7 1.2 2.5 0C13.8 4.6 15.6 3.7 17.6 4c3.4.5 5 3.9 3.4 7.2-2.5 4.7-9 9.3-9 9.3Z"/></svg>'
ICONS['flame'] = '<svg viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M12 2c1 3-2 4-2 7a3 3 0 0 0 6 0c0-1-0.5-2-1-2 2 0 4 2 4 5.5A7 7 0 1 1 8 12.5C8 9 9 6 12 2Z"/></svg>'
ICONS['refresh'] = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20 11A8 8 0 1 0 18 16"/><path d="M20 4v6h-6"/></svg>'

# Ilustración pixel-art única por artículo (16x16, más detallada), pensada para el tema concreto de cada uno.
# Los artículos futuros sin entrada aquí caen al icono por keyword/sección (pixelIconFor en JS).
ARTICLE_ICONS_ROWS = {'aprendizaje-por-refuerzo-basico': ['................', '................', '.....######.....', '...##......###..', '...#........#...', '......####...#..', '.....##..##.....', '.....#.##.#.....', '.....#.##.#.....', '.....##..##.....', '..#...####......', '...#........#...', '..###......##...', '.....######.....', '................', '................'], 'meta-abre-astryx-su-design-system-interno-y-ya-funciona-en-figma-make': ['.........####...', '.........####...', '.....########...', '..###########...', '..#.#####.......', '..#######.......', '......#####.....', '....##.....#....', '...#........##..', '..#############.', '..#...........#.', '..#.#########.#.', '..#...........#.', '..#############.', '................', '................'], 'claude-agents-que-son-y-como-crear-uno': ['....#...........', '....#...........', '#########.......', '#.......#.......', '#.##.##.#.......', '#.##.##.#.......', '#.##.##.#.......', '#.......#.......', '#.#####.#...#...', '#########.#####.', '.........#######', '.........##...##', '........###...##', '.........##...##', '.........#######', '..........#####.'], 'donde-va-realmente-tu-contexto-de-diseno-en-claude': ['................', '................', '..############..', '..#.##.....#.#..', '..#..........#..', '..############..', '................', '..############..', '..#.##.....#.#..', '..#..........#..', '..############..', '................', '..############..', '..#.##.....#.#..', '..#..........#..', '..############..'], 'los-disenadores-gastan-los-limites-de-uso-de-claude-mas-rapido-que-nad': ['................', '................', '................', '................', '.############...', '.####...#...#...', '.####..#....###.', '.####..#....###.', '.####.####..###.', '.####...#...###.', '.####...#...#...', '.############...', '................', '................', '................', '................'], 'diccionario-de-ia-para-disenadores': ['...........#....', '...........#....', '.......####.#...', '....###.#.###...', '..##....#....##.', '..#.....#.....#.', '..#.#########.#.', '..#.....#.....#.', '..#.#########.#.', '..#.....#.....#.', '..#.#########.#.', '..#.....#.....#.', '..###...#...###.', '.....#######....', '................', '................'], '5-trucos-para-que-claude-code-no-te-de-un-diseno-web-generico': ['................', '################', '#.#.#.#..#####.#', '#..............#', '################', '#..............#', '#......##......#', '#......##......#', '#....######....#', '#...########...#', '#....######....#', '#......##......#', '#......##......#', '################', '................', '................']}
ARTICLE_ICONS = {aid: pixel_svg(rows) for aid, rows in ARTICLE_ICONS_ROWS.items()}

# Icono de "varita mágica" para el empty state de Últimas entradas (todo revisado / limpio)
ICONS['wand'] = pixel_svg(['............', '............', '.......##...', '......####..', '......####..', '.......##...', '......#.....', '.....#......', '...##.......', '...#........', '..#.........', '.#..........'])

data_json = json.dumps(articles, ensure_ascii=False)
commands_json = json.dumps(commands, ensure_ascii=False)
sections_json = json.dumps(SECTIONS, ensure_ascii=False)
icons_json = json.dumps(ICONS, ensure_ascii=False)
article_icons_json = json.dumps(ARTICLE_ICONS, ensure_ascii=False)

TEMPLATE = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Future Designer</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap');
  :root {
    --bg: #ffffff;
    --ink: #0a0a0a;
    --muted: #7a7a7a;
    --accent: #ff5a1f;
    --line: #0a0a0a;
    --top-row-h: 520px;
  }
  * { box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body {
    margin: 0;
    font-family: 'Space Grotesk', Helvetica, Arial, sans-serif;
    background-color: var(--bg);
    background-image: radial-gradient(rgba(10,10,10,0.16) 1px, transparent 1.4px);
    background-size: 22px 22px;
    color: var(--ink);
  }
  a { color: inherit; }
  .wrap { max-width: 1160px; margin: 0 auto; padding: 0 24px; }
  main.wrap { padding-top: 34px; }
  .mono { font-family: 'Space Mono', monospace; }

  /* ---- Masthead ---- */
  header.masthead { padding: 30px 24px 0; border-bottom: 4px solid var(--ink); position: relative; }
  .top-bar { display: flex; align-items: center; justify-content: flex-end; gap: 12px; flex-wrap: wrap; }

  .live {
    display: flex; align-items: center; justify-content: center; gap: 8px; margin: 4px 0 2px;
    font-family: 'Space Mono', monospace; font-size: 11px; letter-spacing: 1.5px;
    text-transform: uppercase; color: var(--muted);
  }
  .live .dot-wrap { position: relative; width: 9px; height: 9px; }
  .live .dot-wrap::before, .live .dot-wrap::after {
    content: ""; position: absolute; inset: 0; border-radius: 50%; background: var(--accent);
  }
  .live .dot-wrap::after {
    animation: radar 1.6s ease-out infinite;
  }
  @keyframes radar { 0% { transform: scale(1); opacity: .8; } 100% { transform: scale(3.2); opacity: 0; } }

  h1.title {
    font-family: 'Archivo Black', 'Space Grotesk', sans-serif;
    font-weight: 400; font-size: 62px; letter-spacing: -2px;
    margin: 14px 0 30px; text-align: center; text-transform: uppercase; line-height: .92;
  }
  h1.title span { display: inline-block; opacity: 0; transform: translateY(18px) rotate(-1deg); animation: riseIn .55s cubic-bezier(.2,.8,.2,1) forwards; }
  h1.title span:nth-child(odd) { color: var(--accent); }
  @keyframes riseIn { to { opacity: 1; transform: translateY(0) rotate(0); } }

  /* ---- Masthead utils: buscar, historial ---- */
  .masthead-utils {
    display: flex; align-items: center; gap: 8px; flex: none;
  }
  .masthead-search-btn {
    height: 38px; flex: none; display: flex; align-items: center; gap: 6px;
    padding: 0 14px; border: 2px solid var(--ink); background: transparent; color: var(--ink); cursor: pointer;
    font-family: 'Space Mono', monospace; font-size: 11px; letter-spacing: 1px; text-transform: uppercase; font-weight: 700;
  }
  .masthead-search-btn svg { width: 15px; height: 15px; flex: none; }
  .masthead-search-btn:hover { background: var(--accent); border-color: var(--accent); color: #fff; }

  .masthead-utils .hist-link {
    display: flex; align-items: center; gap: 6px; height: 38px; flex: none;
    padding: 0 14px; border: 2px solid var(--ink); font-family: 'Space Mono', monospace;
    font-size: 11px; letter-spacing: 1px; text-transform: uppercase; text-decoration: none;
    color: var(--ink); font-weight: 700;
  }
  .masthead-utils .hist-link svg { width: 15px; height: 15px; }
  .masthead-utils .hist-link:hover, .masthead-utils .hist-link.active { background: var(--accent); border-color: var(--accent); color: #fff; }

  /* ---- Nota "Ofrecido por Isabel": el mismo post-it que las anotaciones, pero arrastrable ---- */
  .subtitle {
    position: absolute; top: 20px; left: 24px; width: 280px; z-index: 6;
    display: flex; flex-direction: column; gap: 7px;
    background: #ffddc2; border: 2px solid var(--ink); box-shadow: 5px 6px 0 var(--ink);
    padding: 13px 16px 15px; transform: rotate(-4deg);
    cursor: grab; touch-action: none; user-select: none;
  }
  .subtitle.dragging { cursor: grabbing; box-shadow: 8px 10px 0 var(--ink); z-index: 50; transition: none; }
  .subtitle-row { display: flex; align-items: center; gap: 9px; }
  .subtitle-avatar {
    width: 46px; height: 46px; border-radius: 50%; border: 2px solid var(--ink); flex: none;
    object-fit: cover; object-position: center 15%; background: #fff; pointer-events: none;
  }
  .subtitle-text { display: flex; flex-direction: column; gap: 2px; }
  .subtitle-name {
    font-family: 'Archivo Black', sans-serif; font-weight: 400; font-size: 14px; letter-spacing: -.2px;
    text-transform: uppercase; color: var(--ink);
  }
  .subtitle-byline {
    font-family: 'Space Mono', monospace; font-size: 10.5px; font-weight: 700; letter-spacing: .3px;
    text-transform: uppercase; color: var(--accent); text-decoration: underline; cursor: pointer;
  }
  .subtitle-phrase { font-family: 'Space Mono', monospace; font-size: 12px; line-height: 1.45; color: var(--ink); font-weight: 400; }

  /* ---- Ticker ---- */
  .ticker {
    margin: 0 -24px;
    border-top: 2px solid var(--accent); border-bottom: 2px solid var(--accent);
    background: rgba(255, 90, 31, 0.06);
    white-space: nowrap; position: relative; cursor: pointer;
  }
  .ticker:hover { background: rgba(255, 90, 31, 0.12); }
  .ticker-scroll { overflow: hidden; }
  .ticker-track { display: inline-block; padding: 8px 0; animation: scrollTicker 64s linear infinite; }
  .ticker:hover .ticker-track { animation-play-state: paused; }
  .ticker .item { font-family: 'Space Mono', monospace; font-size: 12px; letter-spacing: .5px; padding: 0 22px; color: var(--muted); text-decoration: none; }
  .ticker a.item:hover { color: var(--accent); }
  .ticker a.item:hover b { color: var(--accent); }
  .ticker .item b { color: var(--ink); font-weight: 700; }
  .ticker.empty-state .ticker-track { animation: none; padding: 8px 22px; }
  @keyframes scrollTicker { from { transform: translateX(0); } to { transform: translateX(-50%); } }

  .ticker-badge {
    position: absolute; top: -16px; left: 18px; z-index: 3; pointer-events: none;
    display: flex; align-items: center; gap: 6px;
    background: var(--accent); border: 2px solid var(--ink); box-shadow: 3px 4px 0 var(--ink);
    padding: 6px 11px 6px 8px;
    animation: burstWiggle 2.6s ease-in-out infinite;
  }
  .ticker-badge svg.burst { width: 14px; height: 14px; flex: none; color: #fff; }
  .ticker-badge span {
    font-family: 'Space Mono', monospace; font-size: 10.5px; font-weight: 700;
    letter-spacing: .5px; text-transform: uppercase; color: #fff; white-space: nowrap; line-height: 1;
  }
  @keyframes burstWiggle {
    0%, 100% { transform: rotate(-6deg); }
    50% { transform: rotate(-2deg); }
  }
  .ticker.empty-state .ticker-badge { display: none; }

  /* ---- Modal de artículos sin valorar (teleprompter) ---- */
  .ticker-modal {
    position: fixed; inset: 0; background: rgba(10,10,10,0.55); z-index: 55;
    display: none; align-items: flex-start; justify-content: center; padding-top: 10vh;
  }
  .ticker-modal.open { display: flex; }
  .ticker-modal-panel {
    width: 100%; max-width: 640px; margin: 0 24px; background: var(--bg);
    border: 2px solid var(--ink); box-shadow: 10px 10px 0 rgba(0,0,0,0.25);
    max-height: 72vh; display: flex; flex-direction: column; overflow: hidden;
  }
  .ticker-modal-header { display: flex; align-items: center; justify-content: space-between; padding: 16px 20px; border-bottom: 2px solid var(--ink); }
  .ticker-modal-header h3 { margin: 0; font-family: 'Archivo Black', sans-serif; font-weight: 400; font-size: 17px; text-transform: uppercase; letter-spacing: -.5px; }
  .close-btn-sm { border: 2px solid var(--ink); background: var(--bg); width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; cursor: pointer; flex: none; }
  .close-btn-sm:hover { background: var(--accent); border-color: var(--accent); color: #fff; }
  .close-btn-sm svg { width: 14px; height: 14px; }
  .ticker-modal-list { overflow-y: auto; padding: 4px 0; }
  .tm-row { display: flex; align-items: center; justify-content: space-between; gap: 14px; padding: 14px 20px; border-bottom: 1px solid #eee; transition: opacity .25s ease, transform .25s ease; }
  .tm-row.tm-row-out { opacity: 0; transform: translateX(14px); }
  .tm-title { flex: 1; min-width: 0; text-decoration: none; color: var(--ink); display: flex; flex-direction: column; gap: 4px; cursor: pointer; }
  .tm-title:hover h4 { color: var(--accent); }
  .tm-title h4 { margin: 0; font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 14.5px; line-height: 1.3; }
  .tm-stars { display: flex; gap: 2px; flex: none; }
  .tm-stars .star-btn { border: none; background: transparent; padding: 2px; cursor: pointer; color: var(--ink); }
  .tm-stars .star-btn svg { width: 16px; height: 16px; display: block; }
  .tm-stars .star-btn:hover, .tm-stars .star-btn.on { color: var(--accent); }

  /* ---- Nav ---- */
  nav.sections {
    margin: 0 -24px;
    padding: 0 24px;
    display: flex; justify-content: center; align-items: stretch;
  }
  .links-wrap { min-width: 0; display: flex; align-items: stretch; position: relative; }
  nav.sections .links {
    display: flex; flex-wrap: nowrap; overflow-x: auto; scroll-behavior: smooth;
    scrollbar-width: none; -ms-overflow-style: none;
  }
  nav.sections .links::-webkit-scrollbar { display: none; }
  .links-arrow {
    flex: none; width: 32px; display: flex; align-items: center; justify-content: center;
    background: var(--bg); border: none; cursor: pointer; color: var(--ink);
  }
  .links-arrow.left svg { transform: scaleX(-1); }
  .links-arrow svg { width: 13px; height: 13px; }
  .links-arrow:hover { color: var(--accent); }
  .links-arrow.hidden { display: none; }
  nav.sections a {
    position: relative; text-decoration: none; color: var(--ink); flex: none;
    padding: 13px 18px; font-size: 12px; letter-spacing: 1.4px; text-transform: uppercase;
    font-weight: 700; white-space: nowrap; font-family: 'Space Mono', monospace;
  }
  nav.sections a::after {
    content: ""; position: absolute; left: 0; right: 0; bottom: 0; height: 3px;
    background: var(--accent); transform: scaleX(0); transform-origin: left; transition: transform .18s ease;
  }
  nav.sections a:hover::after, nav.sections a.active::after { transform: scaleX(1); }
  nav.sections a:hover, nav.sections a.active { color: var(--accent); }

  /* ---- Glossary (article view) ---- */
  .art-glossary { margin-top: 40px; padding-top: 18px; border-top: 3px solid var(--ink); }
  .art-glossary h4 { font-family: 'Space Mono', monospace; font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase; color: var(--accent); margin: 0 0 14px; }
  .glossary-item { display: flex; gap: 12px; align-items: flex-start; padding: 12px 0; border-bottom: 1px solid #e5e5e5; }
  .glossary-item:last-child { border-bottom: none; }
  .glossary-item .gterm { flex: 1; }
  .glossary-item .gterm b { font-family: 'Space Grotesk', sans-serif; font-size: 14.5px; display: block; margin-bottom: 3px; }
  .glossary-item .gterm span { font-size: 13.5px; color: var(--muted); line-height: 1.5; }
  .like-btn { border: 2px solid var(--ink); background: var(--bg); width: 34px; height: 34px; flex: none; display: flex; align-items: center; justify-content: center; cursor: pointer; }
  .like-btn svg { width: 16px; height: 16px; }
  .like-btn:hover { border-color: var(--accent); color: var(--accent); }
  .like-btn.liked { background: var(--accent); border-color: var(--accent); color: #fff; }
  /* ---- Reflexiones (de la skill Article Debate) ---- */
  .art-reflections { margin-top: 32px; border: 2px solid var(--ink); }
  .art-reflections h4 { display: flex; align-items: center; gap: 8px; margin: 0; padding: 12px 18px; background: var(--ink); color: #fff; font-family: 'Space Mono', monospace; font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase; }
  .art-reflections h4 svg { width: 16px; height: 16px; }
  .reflection-entry { padding: 16px 18px; }
  .reflection-entry + .reflection-entry { border-top: 1px dashed #ccc; }
  .reflection-date { font-family: 'Space Mono', monospace; font-size: 10px; letter-spacing: .5px; text-transform: uppercase; color: var(--accent); font-weight: 700; }
  .reflection-text { margin: 6px 0 0; font-size: 15px; line-height: 1.65; }
  .reflection-text p { margin: 0 0 10px; }
  .reflection-text p:last-child { margin-bottom: 0; }

  /* ---- Artículos relacionados ---- */
  .art-related { margin-top: 40px; padding-top: 18px; border-top: 3px solid var(--ink); }
  .art-related h4 { display: flex; align-items: center; gap: 8px; margin: 0 0 10px; font-family: 'Space Mono', monospace; font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase; color: var(--accent); }
  .art-related h4 svg { width: 14px; height: 14px; }
  .art-related .rail { padding-bottom: 4px; }

  .dict-badge {
    flex: none; display: flex; align-items: center; gap: 5px; font-family: 'Space Mono', monospace;
    font-size: 9.5px; letter-spacing: .5px; text-transform: uppercase; color: var(--accent);
  }
  .dict-badge svg { width: 14px; height: 14px; }

  /* ---- Enciclopedia ---- */
  .ency-toolbar { display: flex; align-items: center; gap: 16px; margin-top: 18px; }
  .ency-toolbar .ency-search-row { flex: 1; margin: 0; }
  .review-btn {
    display: flex; align-items: center; gap: 8px; flex: none; background: var(--ink); color: #fff; border: 2px solid var(--ink);
    font-family: 'Space Mono', monospace; font-size: 11px; font-weight: 700; letter-spacing: .8px; text-transform: uppercase;
    padding: 10px 16px; cursor: pointer;
  }
  .review-btn svg { width: 15px; height: 15px; }
  .review-btn:hover { background: var(--accent); border-color: var(--accent); }

  /* ---- Banner de repasar, estilo anuncio, encima de la lista de Enciclopedia ---- */
  .ency-review-banner {
    display: flex; align-items: center; justify-content: space-between; gap: 20px; flex-wrap: wrap;
    background: var(--accent); border: 2px solid var(--ink); box-shadow: 5px 6px 0 var(--ink);
    padding: 22px 26px; margin: 22px 0 8px; color: #fff;
  }
  .ency-review-banner-text { display: flex; flex-direction: column; gap: 4px; }
  .ency-review-banner-text strong {
    font-family: 'Archivo Black', sans-serif; font-weight: 400; font-size: 21px; letter-spacing: -.5px;
    text-transform: uppercase; line-height: 1.15;
  }
  .ency-review-banner-text span {
    font-family: 'Space Mono', monospace; font-size: 11px; letter-spacing: .5px; text-transform: uppercase; opacity: .92;
  }
  .review-cta {
    display: flex; align-items: center; gap: 9px; flex: none; background: var(--ink); color: #fff; border: 2px solid var(--ink);
    font-family: 'Space Mono', monospace; font-size: 12.5px; font-weight: 700; letter-spacing: .8px; text-transform: uppercase;
    padding: 14px 20px; cursor: pointer; box-shadow: 4px 5px 0 rgba(0,0,0,.35);
  }
  .review-cta svg { width: 17px; height: 17px; }
  .review-cta:hover { background: #fff; color: var(--ink); transform: translate(-2px,-2px); box-shadow: 6px 7px 0 rgba(0,0,0,.35); }

  .ency-search-row { display: flex; align-items: center; gap: 10px; border-bottom: 2px solid var(--ink); padding: 10px 0; margin: 18px 0 6px; }
  .ency-search-row svg { width: 16px; height: 16px; color: var(--muted); flex: none; }
  .ency-search-row input { flex: 1; border: none; outline: none; background: transparent; font-family: 'Space Grotesk', sans-serif; font-size: 15px; color: var(--ink); }

  .ency-layout { display: flex; gap: 28px; align-items: flex-start; margin-top: 10px; }
  .ency-list { flex: 1; min-width: 0; }
  .ency-letter-group { margin-bottom: 8px; }
  .ency-letter-heading {
    font-family: 'Archivo Black', sans-serif; font-weight: 400; font-size: 26px; color: var(--accent);
    padding: 18px 0 6px; border-bottom: 3px solid var(--ink); scroll-margin-top: 90px;
  }
  .ency-vlist { display: flex; flex-direction: column; }
  .ency-row { padding: 16px 0; border-bottom: 1px solid #e5e5e5; display: flex; flex-direction: column; gap: 6px; }
  .ency-row b { font-family: 'Space Grotesk', sans-serif; font-size: 16px; }
  .ency-row p { margin: 0; font-size: 13.5px; color: var(--muted); line-height: 1.55; }
  .ency-row .src { font-family: 'Space Mono', monospace; font-size: 10.5px; text-transform: uppercase; letter-spacing: .5px; color: var(--accent); cursor: pointer; text-decoration: none; width: fit-content; }
  .ency-row .src:hover { text-decoration: underline; }

  .ency-index {
    position: sticky; top: 110px; flex: none; display: flex; flex-direction: column; gap: 1px;
    font-family: 'Space Mono', monospace; font-size: 10.5px; font-weight: 700; max-height: 70vh; overflow-y: auto;
  }
  .ency-index::-webkit-scrollbar { display: none; }
  .ency-index a { color: var(--muted); text-decoration: none; padding: 2px 4px; text-align: center; }
  .ency-index a:hover { color: var(--ink); }
  .ency-index a.active { color: var(--accent); }

  /* ---- Claude Commands (pestaña dentro de Enciclopedia) ---- */
  .ency-tabs { margin: 16px 0 0; }
  .cmd-group-heading {
    font-family: 'Archivo Black', sans-serif; font-weight: 400; font-size: 18px; color: var(--accent);
    text-transform: uppercase; letter-spacing: -.3px; padding: 18px 0 6px; border-bottom: 3px solid var(--ink); scroll-margin-top: 90px;
  }
  .cmd-row { padding: 16px 0; border-bottom: 1px solid #e5e5e5; display: flex; flex-direction: column; gap: 8px; }
  .cmd-row-head { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }
  .cmd-name { font-family: 'Space Mono', monospace; font-size: 16px; font-weight: 700; color: var(--ink); }
  .cmd-tag {
    font-family: 'Space Mono', monospace; font-size: 9.5px; letter-spacing: .5px; text-transform: uppercase;
    color: #fff; background: var(--accent); padding: 2px 8px;
  }
  .cmd-desc { margin: 0; font-size: 13.5px; color: var(--muted); line-height: 1.55; }
  .cmd-example {
    margin: 0; background: #f4f4f4; border: 1px solid #ddd; padding: 9px 11px;
    font-family: 'Space Mono', monospace; font-size: 12px; line-height: 1.5; overflow-x: auto; white-space: pre-wrap;
  }
  .cmd-notes { margin: 0; font-size: 12.5px; font-style: italic; color: var(--ink); }

  /* ---- Flashcards de repaso ---- */
  .flash-panel { max-width: 460px; }
  .flash-modal-body { padding: 26px 22px 22px; display: flex; flex-direction: column; align-items: center; gap: 18px; }
  .flash-progress { font-family: 'Space Mono', monospace; font-size: 11px; letter-spacing: 1px; color: var(--muted); align-self: flex-start; }
  .flash-card {
    width: 100%; min-height: 200px; border: 2px solid var(--ink); background: var(--bg);
    display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center;
    padding: 30px 22px; cursor: pointer; gap: 14px;
  }
  .flash-card.revealed { cursor: default; border-color: var(--accent); }
  .flash-term { font-family: 'Archivo Black', sans-serif; font-weight: 400; font-size: 24px; text-transform: uppercase; letter-spacing: -.5px; line-height: 1.15; }
  .flash-tap { font-family: 'Space Mono', monospace; font-size: 11px; letter-spacing: .5px; color: var(--muted); text-transform: uppercase; }
  .flash-def { margin: 0; font-size: 14.5px; line-height: 1.6; color: var(--ink); }
  .flash-card .src { font-family: 'Space Mono', monospace; font-size: 10.5px; text-transform: uppercase; letter-spacing: .5px; color: var(--accent); text-decoration: none; }
  .flash-card .src:hover { text-decoration: underline; }
  .flash-actions { display: flex; gap: 12px; width: 100%; }
  .flash-actions button {
    flex: 1; border: 2px solid var(--ink); background: var(--bg); padding: 12px; cursor: pointer;
    font-family: 'Space Mono', monospace; font-size: 11.5px; font-weight: 700; letter-spacing: .5px; text-transform: uppercase;
    display: flex; align-items: center; justify-content: center; gap: 6px;
  }
  .flash-actions button svg { width: 14px; height: 14px; }
  .flash-no:hover { background: #eee; }
  .flash-actions .flash-yes { background: var(--ink); color: #fff; }
  .flash-yes:hover { background: var(--accent); border-color: var(--accent); }
  .flash-done { display: flex; flex-direction: column; align-items: center; gap: 14px; text-align: center; padding: 10px 0 6px; }
  .flash-done svg { width: 34px; height: 34px; color: var(--accent); }
  .flash-done p { margin: 0; font-size: 15px; }

  @media (max-width: 760px) {
    .ency-index { position: fixed; right: 6px; top: 50%; transform: translateY(-50%); background: rgba(255,255,255,.92); padding: 4px 2px; z-index: 10; }
  }

  /* ---- Controls ---- */
  .controls { display: flex; gap: 0; border-bottom: 1px solid #ccc; margin-top: 14px; }
  input[type=text] {
    flex: 1; min-width: 160px; padding: 10px 4px; border: none; font-size: 14px;
    font-family: 'Space Grotesk', sans-serif; background: transparent; color: var(--ink);
  }
  input[type=text]:focus { outline: none; }
  .chips { display: flex; gap: 8px; flex-wrap: wrap; padding: 12px 0; }
  .chip {
    font-family: 'Space Mono', monospace; font-size: 10.5px; letter-spacing: 1px; text-transform: uppercase; font-weight: 700;
    border: 2px solid var(--ink); padding: 5px 11px; cursor: pointer; background: var(--bg); color: var(--ink);
  }
  .chip.active, .chip:hover { background: var(--ink); color: #fff; }

  main { padding-bottom: 70px; }
  .count { font-family: 'Space Mono', monospace; font-size: 11px; letter-spacing: 1px; text-transform: uppercase; color: var(--muted); margin: 14px 0; }

  /* ---- Section hero ---- */
  .section-hero { display: flex; align-items: center; gap: 16px; padding: 6px 0 10px; }
  .section-hero .icon { width: 44px; height: 44px; flex: none; }
  .section-hero .icon svg { width: 100%; height: 100%; }
  .section-hero h2 { font-family: 'Archivo Black', sans-serif; font-weight: 400; font-size: 32px; margin: 0; text-transform: uppercase; letter-spacing: -1px; }
  .section-hero p { margin: 4px 0 0; color: var(--muted); font-size: 13.5px; }

  /* ---- Panel de progreso (Historial) ---- */
  .progress-panel { margin: 24px 0 8px; border: 2px solid var(--ink); }
  .stat-row { display: flex; }
  .stat-block { flex: 1; padding: 18px 16px; text-align: center; border-right: 2px solid var(--ink); }
  .stat-block:last-child { border-right: none; }
  .stat-num { font-family: 'Archivo Black', sans-serif; font-weight: 400; font-size: 30px; color: var(--accent); line-height: 1; }
  .stat-label { font-family: 'Space Mono', monospace; font-size: 10px; letter-spacing: 1px; text-transform: uppercase; color: var(--muted); margin-top: 6px; }
  .stat-bars { border-top: 2px solid var(--ink); padding: 16px 18px; display: flex; flex-direction: column; gap: 10px; }
  .stat-bar-row { display: flex; align-items: center; gap: 10px; }
  .stat-bar-label { flex: 0 0 150px; font-family: 'Space Mono', monospace; font-size: 10.5px; letter-spacing: .5px; text-transform: uppercase; color: var(--ink); }
  .stat-bar-track { flex: 1; height: 8px; background: #eee; }
  .stat-bar-fill { height: 100%; background: var(--accent); }
  .stat-bar-count { flex: none; font-family: 'Space Mono', monospace; font-size: 11px; color: var(--muted); width: 20px; text-align: right; }

  .subsection-title {
    font-family: 'Space Mono', monospace; font-size: 11px; letter-spacing: 2px; text-transform: uppercase; color: #fff;
    background: var(--accent); display: inline-block; padding: 4px 10px; font-weight: 700; margin: 28px 0 0;
    scroll-margin-top: 90px;
  }

  /* ---- Secondary nav (subsections) ---- */
  .subnav { display: flex; gap: 8px; flex-wrap: wrap; padding: 16px 0 0; }
  .subnav-pill {
    font-family: 'Space Mono', monospace; font-size: 10.5px; letter-spacing: 1px; text-transform: uppercase;
    font-weight: 700; border: 2px solid var(--ink); padding: 5px 11px; text-decoration: none; color: var(--ink);
    background: var(--bg); cursor: pointer; -webkit-appearance: none; appearance: none;
  }
  .subnav-pill:hover { color: var(--accent); border-color: var(--accent); }
  .subnav-pill.active { background: var(--ink); color: var(--bg); border-color: var(--ink); }

  /* ---- Rail (horizontal scroll) ---- */
  .rail { display: flex; gap: 16px; overflow-x: auto; padding: 6px 4px 18px; margin-top: 4px; scroll-behavior: smooth; }
  .rail .card { flex: 0 0 300px; }
  .rail::-webkit-scrollbar { height: 6px; }
  .rail::-webkit-scrollbar-track { background: transparent; }
  .rail::-webkit-scrollbar-thumb { background: var(--ink); }

  /* ---- Front page: tabloide, cronología pura ---- */
  .front-label {
    font-family: 'Space Mono', monospace; font-size: 10.5px; letter-spacing: 2px; text-transform: uppercase; color: #fff;
    background: var(--ink); display: inline-block; padding: 4px 10px; font-weight: 700; margin: 26px 0 12px; width: fit-content;
  }
  .front-divider { display: flex; align-items: center; gap: 12px; margin: 34px 0 4px; }
  .front-divider::before, .front-divider::after { content: ''; flex: 1; height: 3px; background: var(--ink); }
  .front-divider::before { max-width: 28px; }
  .front-divider .front-label { margin: 0; flex: none; }

  /* ---- Fila superior: carrusel de titular + columna de Enciclopedia ---- */
  /* Hero y sidebar comparten la misma altura fija (--top-row-h) para que no bailen
     de tamaño según lo largo que sea el título/resumen de cada artículo. */
  .front-top { display: grid; grid-template-columns: 2.3fr 1fr; gap: 26px; align-items: start; margin-top: 4px; }
  #hero-slot { transition: opacity .22s ease; }
  #hero-slot.fading { opacity: 0; }
  .front-lead .fp-hero { height: var(--top-row-h); display: flex; flex-direction: column; }
  .front-lead .fp-hero .fp-img, .front-lead .fp-hero .fp-noimg { height: 230px; flex: none; }
  .front-lead .fp-hero .fp-body { gap: 8px; flex: 1; min-height: 0; overflow: hidden; }
  .front-lead .fp-hero h2 {
    font-size: 32px; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;
  }
  .front-lead .fp-hero p {
    font-size: 14.5px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
  }
  /* La fecha se ancla siempre al borde inferior de la card, así un artículo con
     título/resumen corto no deja un hueco vacío flotando antes del final. */
  .front-lead .fp-hero .date { margin-top: auto; }
  /* Neutraliza el tamaño extra grande de .no-media fuera de la home para que un
     titular sin imagen mantenga la misma altura/proporciones que uno con imagen. */
  .front-lead .fp-hero.no-media h2 { font-size: 32px; }
  .front-lead .fp-hero.no-media p { font-size: 14.5px; }

  /* ---- Controles del carrusel de titular (flechas + puntos) ---- */
  .lead-controls { display: flex; align-items: center; justify-content: center; gap: 16px; margin-top: 14px; }
  .lead-arrow {
    border: 2px solid var(--ink); background: var(--bg); width: 30px; height: 30px; flex: none;
    display: flex; align-items: center; justify-content: center; cursor: pointer; color: var(--ink);
  }
  .lead-arrow svg { width: 13px; height: 13px; }
  .lead-arrow.left svg { transform: scaleX(-1); }
  .lead-arrow:hover { background: var(--accent); border-color: var(--accent); color: #fff; }
  .lead-dots { display: flex; gap: 8px; }
  .lead-dot {
    width: 12px; height: 12px; border-radius: 50%; background: #ddd; border: 2px solid var(--ink);
    padding: 0; cursor: pointer;
  }
  .lead-dot.on { background: var(--accent); border-color: var(--accent); }

  /* ---- Titular sin imagen: icono de sección, sin bloque gris ---- */
  .lead-icon { width: 52px; height: 52px; color: var(--ink); margin-bottom: 4px; image-rendering: pixelated; }
  .lead-icon svg { width: 100%; height: 100%; shape-rendering: crispEdges; }

  /* ---- Columna junto al titular: término del día + chuleta de comandos ---- */
  .ency-sidebar-stack { height: var(--top-row-h); display: flex; flex-direction: column; gap: 14px; }

  /* Término del día: post-it que gira en 3D al hacer clic, como el de la editora */
  .term-of-day { position: relative; flex: none; height: 160px; cursor: pointer; perspective: 480px; }
  /* la definición vive en su propio post-it debajo — otro color, ligera rotación
     propia — no un fondo plano, como si hubiera un segundo papel pegado ahí. */
  .term-of-day-back {
    position: absolute; inset: 0; z-index: 0; display: flex; flex-direction: column; justify-content: center; gap: 10px;
    padding: 16px 18px; background: #fff3b0; transform: rotate(2deg);
    box-shadow: 0 10px 16px -8px rgba(10,10,10,.4), 0 2px 4px rgba(10,10,10,.15);
  }
  .term-of-day-back p { margin: 0; font-size: 13px; line-height: 1.5; color: var(--ink); overflow-y: auto; }
  .term-of-day-back .src {
    font-family: 'Space Mono', monospace; font-size: 10px; text-transform: uppercase; letter-spacing: .5px;
    color: var(--accent); cursor: pointer; text-decoration: none; flex: none;
  }
  .term-of-day-back .src:hover { text-decoration: underline; }

  /* la nota de arriba: se despega desde el borde superior (donde está la cinta) —
     se levanta, se inclina y se echa a un lado, en vez de voltearse como una tarjeta.
     Vuelve a bajar y "pegarse" al tocar otra vez. */
  .term-of-day-lift {
    position: absolute; inset: 0; z-index: 1; transform-origin: top center;
    transform: rotate(-2deg) rotateX(0deg); transform-style: preserve-3d;
    transition: transform .55s cubic-bezier(.45,0,.4,1);
  }
  /* se queda doblada hacia atrás por la bisagra de arriba (donde está la cinta),
     no sale disparada — como cuando levantas un post-it agarrándolo por abajo. */
  .term-of-day.flipped .term-of-day-lift { transform: rotate(-2deg) rotateX(-160deg); }
  .term-of-day-face {
    position: absolute; inset: 0; backface-visibility: hidden; display: flex; flex-direction: column;
    justify-content: center; gap: 6px; padding: 18px 20px 26px;
    background: #ffddc2;
    box-shadow: 0 14px 20px -10px rgba(10,10,10,.45), 0 3px 6px rgba(10,10,10,.18);
    clip-path: polygon(0 0, 100% 0, 100% calc(100% - 24px), calc(100% - 24px) 100%, 0 100%);
    transition: box-shadow .15s ease;
  }
  .term-of-day:hover .term-of-day-face {
    box-shadow: 0 18px 24px -8px rgba(10,10,10,.5), 0 4px 8px rgba(10,10,10,.2);
  }
  /* esquina curvada: el pico de papel que se despega, con degradado de sombra */
  .term-of-day-face .curl {
    position: absolute; right: 0; bottom: 0; width: 24px; height: 24px;
    background: linear-gradient(135deg, #f6d5b3 0%, #f6d5b3 45%, rgba(10,10,10,.35) 62%, rgba(10,10,10,.15) 100%);
    clip-path: polygon(100% 0, 100% 100%, 0 100%);
  }
  /* dos trocitos de cinta sujetando la nota: fijos en .term-of-day, no se mueven con
     el despegue (como la cinta real, que se queda pegada a la mesa) */
  .term-of-day > .tape {
    position: absolute; top: -11px; z-index: 2; width: 48px; height: 24px; pointer-events: none;
    background:
      linear-gradient(115deg, transparent 0%, transparent 38%, rgba(255,255,255,.65) 46%, rgba(255,255,255,.65) 54%, transparent 62%, transparent 100%),
      linear-gradient(rgba(244, 172, 180, .68), rgba(244, 172, 180, .68));
    box-shadow: 0 2px 4px rgba(10,10,10,.25);
    border-radius: 1px;
  }
  .term-of-day > .tape-left { left: 6px; transform: rotate(-16deg); }
  .term-of-day > .tape-right { right: 6px; transform: rotate(14deg); }
  .term-of-day-label {
    font-family: 'Space Mono', monospace; font-size: 10px; letter-spacing: 1.2px; text-transform: uppercase;
    color: var(--accent); font-weight: 700;
  }
  .term-of-day-face b {
    font-family: 'Archivo Black', sans-serif; font-weight: 400; font-size: 22px; text-transform: uppercase;
    letter-spacing: -.3px; line-height: 1.1;
  }
  .term-of-day-hint {
    font-family: 'Space Mono', monospace; font-size: 10.5px; color: var(--muted); text-transform: uppercase; letter-spacing: .5px;
  }

  /* Chuleta de comandos: lista alfabética con scroll interno */
  .cmd-cheatsheet { flex: 1; min-height: 0; border: 2px solid var(--ink); display: flex; flex-direction: column; }
  .cmd-cheatsheet-head { padding: 10px 14px; border-bottom: 2px solid var(--ink); background: var(--ink); }
  .cmd-cheatsheet-head h3 {
    margin: 0; font-family: 'Space Mono', monospace; font-size: 11px; letter-spacing: 1.5px;
    text-transform: uppercase; font-weight: 700; color: #fff;
  }
  .cmd-cheat-list { flex: 1; min-height: 0; overflow-y: auto; }
  .cmd-cheat-row { padding: 10px 14px; border-bottom: 1px solid #e5e5e5; display: flex; flex-direction: column; gap: 3px; }
  .cmd-cheat-row:last-child { border-bottom: none; }
  .cmd-cheat-row b { font-family: 'Space Mono', monospace; font-size: 12.5px; font-weight: 700; color: var(--ink); }
  .cmd-cheat-row span { font-size: 11.5px; line-height: 1.4; color: var(--muted); }
  .ency-sidebar-empty { padding: 20px 14px; font-size: 12.5px; color: var(--muted); text-align: center; }

  /* ---- Carrusel paginado de "quizá te interese" (dot-nav, sin autoplay) ---- */
  .other-carousel { display: flex; align-items: center; gap: 14px; }
  .other-carousel-viewport { flex: 1; min-width: 0; overflow: hidden; }
  .other-carousel-arrow {
    flex: none; border: 2px solid var(--ink); background: var(--bg); width: 34px; height: 34px;
    display: flex; align-items: center; justify-content: center; cursor: pointer; color: var(--ink);
  }
  .other-carousel-arrow svg { width: 13px; height: 13px; }
  .other-carousel-arrow.left svg { transform: scaleX(-1); }
  .other-carousel-arrow:hover { background: var(--accent); border-color: var(--accent); color: #fff; }
  .other-carousel-arrow.hidden { visibility: hidden; }
  .other-carousel-page {
    display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px;
    transition: transform .22s ease, opacity .22s ease;
  }
  .other-carousel-page.slide-out-left { transform: translateX(-22px); opacity: 0; }
  .other-carousel-page.slide-out-right { transform: translateX(22px); opacity: 0; }
  .other-carousel-page.slide-in-right, .other-carousel-page.slide-in-left { opacity: 0; }
  .other-carousel-page.slide-in-right { transform: translateX(22px); }
  .other-carousel-page.slide-in-left { transform: translateX(-22px); }
  @media (max-width: 720px) { .other-carousel-page { grid-template-columns: 1fr; } }

  @media (max-width: 900px) {
    .front-top { grid-template-columns: 1fr; }
    /* Apiladas, hero y sidebar no necesitan compartir altura exacta */
    .front-lead .fp-hero, .front-lead .fp-hero.no-media, .ency-sidebar-stack { height: auto; }
    .cmd-cheatsheet { max-height: 320px; }
  }

  @media (max-width: 760px) {
    .front-lead .fp-hero .fp-img, .front-lead .fp-hero .fp-noimg { height: 180px; }
    .front-lead .fp-hero h2 { font-size: 23px; }
  }

  .fp-card {
    position: relative; display: block; text-decoration: none; color: var(--ink); border: 2px solid var(--ink);
    transition: transform .15s ease, box-shadow .15s ease, border-color .15s ease, color .15s ease;
  }
  .fp-card:hover { color: var(--accent); border-color: var(--accent); transform: translate(-4px,-4px); box-shadow: 6px 6px 0 var(--ink); }
  .fp-card .fp-img { width: 100%; display: block; object-fit: cover; filter: grayscale(100%) contrast(1.08); border-bottom: 2px solid var(--ink); }
  .fp-card:hover .fp-img { border-color: var(--accent); }
  .fp-card .fp-body { padding: 18px; display: flex; flex-direction: column; gap: 8px; }
  .fp-noimg { display: flex; align-items: center; justify-content: center; background: #f2f2f2; border-bottom: 2px solid var(--ink); }
  .fp-card:hover .fp-noimg { border-color: var(--accent); }
  .fp-noimg svg { width: 30%; max-width: 64px; height: auto; color: var(--ink); opacity: .5; }
  .fp-hero .fp-noimg { height: 320px; }

  .fp-hero .fp-img { height: 320px; }
  .fp-hero h2 { margin: 0; font-family: 'Archivo Black', sans-serif; font-weight: 400; font-size: 36px; line-height: 1.02; letter-spacing: -1px; text-transform: uppercase; }
  .fp-hero p { margin: 0; font-size: 15px; line-height: 1.55; color: var(--ink); }
  .fp-hero.no-media .fp-body { padding: 40px 32px; gap: 14px; }
  .fp-hero.no-media h2 { font-size: 44px; }
  .fp-hero.no-media p { font-size: 16.5px; }

  /* ---- Portada: tarjeta de segundo nivel (reutilizada en el carrusel de "quizá te interese") ---- */
  /* Altura fija para que las 3 cards de una misma página del carrusel midan siempre lo mismo. */
  .fp-secondary { height: 420px; display: flex; flex-direction: column; }
  .fp-secondary .fp-img, .fp-secondary .fp-noimg { height: 190px; flex: none; }
  .fp-secondary .fp-body { flex: 1; min-height: 0; overflow: hidden; }
  .fp-secondary h3 {
    margin: 0; font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 21px; line-height: 1.18;
    display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
  }
  .fp-secondary p {
    margin: 0; font-size: 13.5px; line-height: 1.5; color: var(--ink);
    display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;
  }
  .fp-secondary .date { font-family: 'Space Mono', monospace; font-size: 10.5px; color: var(--muted); margin-top: 2px; }

  /* ---- Leído / no leído ---- */

  /* ---- Grid / cards ---- */
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; margin-top: 14px; }
  .card {
    position: relative; background: var(--bg); border: 2px solid var(--ink);
    padding: 20px; display: flex; flex-direction: column; gap: 10px; cursor: pointer;
    transition: transform .15s ease, box-shadow .15s ease, border-color .15s ease, color .15s ease;
    text-decoration: none;
  }
  .card:hover { color: var(--accent); border-color: var(--accent); transform: translate(-5px,-5px); box-shadow: 6px 6px 0 var(--ink); }
  .card-body { display: flex; flex-direction: column; gap: 8px; min-width: 0; }
  .tag { display: inline-block; font-family: 'Space Mono', monospace; font-size: 10px; letter-spacing: 1.2px; color: var(--accent); border: 1px solid var(--accent); padding: 3px 9px; width: fit-content; font-weight: 700; text-transform: uppercase; }
  .card p {
    display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;
  }

  /* ---- Insignia de "con anotaciones": avatar de Isabel + bocadillo ---- */
  /* solo el subrayado: nada de caja, ni avatar — el mismo rotulador que las anotaciones
     dentro del artículo, directamente sobre la miniatura */
  .annot-flag { position: absolute; top: 10px; right: 10px; z-index: 4; }
  .annot-flag-text {
    font-family: 'Space Mono', monospace; font-size: 15px; font-weight: 700;
    letter-spacing: .2px; color: #fff; white-space: nowrap; padding: 8px 12px;
    background-image: linear-gradient(103deg, transparent 0%, transparent 2%, var(--accent) 4%, var(--accent) 95%, transparent 97%, transparent 100%);
  }
  @media (max-width: 480px) { .annot-flag-text { font-size: 12px; } }
  .card .annot-flag { top: 6px; right: 6px; }
  .card .annot-flag-text { font-size: 11px; padding: 5px 8px; }
  .card h3 { margin: 0; font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 20px; line-height: 1.2; transition: transform .2s ease; }
  .card:hover h3 { transform: skewX(-1deg); }
  .card p { margin: 0; font-size: 13.5px; line-height: 1.5; color: var(--ink); }
  .card .date { font-family: 'Space Mono', monospace; font-size: 10.5px; color: var(--muted); margin-top: auto; }
  .empty { text-align: center; color: var(--muted); padding: 60px 0; font-style: italic; }

  /* ---- Historial ---- */
  table.hist { width: 100%; border-collapse: collapse; margin-top: 16px; }
  table.hist th { text-align: left; font-family: 'Space Mono', monospace; font-size: 10.5px; letter-spacing: 1.2px; text-transform: uppercase; border-bottom: 3px solid var(--ink); padding: 8px 6px; }
  table.hist td { padding: 10px 6px; border-bottom: 1px solid #ddd; font-size: 13.5px; vertical-align: top; }
  table.hist tr.hidden-row td { text-decoration: line-through; color: #bbb; }
  .row-actions { display: flex; gap: 6px; }
  .del-btn { border: 2px solid var(--ink); background: var(--bg); width: 28px; height: 28px; display: inline-flex; align-items: center; justify-content: center; cursor: pointer; }
  .del-btn svg { width: 14px; height: 14px; }
  .del-btn:hover { background: var(--accent); border-color: var(--accent); color: #fff; }
  .del-btn.restore-btn:hover { background: var(--ink); border-color: var(--ink); }
  .del-btn.perm-btn:hover { background: var(--accent); border-color: var(--accent); }
  .hist-title { cursor: pointer; font-weight: 700; }
  .hist-title:hover { color: var(--accent); }
  .hist-status { font-family: 'Space Mono', monospace; font-size: 10px; text-transform: uppercase; letter-spacing: .5px; color: var(--accent); }
  .toast { position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); background: var(--ink); color: #fff; padding: 12px 18px; font-size: 12px; font-family: 'Space Mono', monospace; max-width: 480px; z-index: 50; display: none; }
  .toast button { margin-left: 10px; background: var(--accent); border: none; color: #fff; padding: 4px 8px; font-size: 10.5px; cursor: pointer; text-transform: uppercase; letter-spacing: .5px; }

  /* ---- Article overlay ---- */
  .overlay { position: fixed; inset: 0; background: var(--bg); z-index: 40; overflow-y: auto; display: none; }
  .overlay.open { display: block; }
  .overlay-inner { max-width: 720px; margin: 0 auto; padding: 60px 24px 100px; position: relative; }
  .overlay .close-btn { position: fixed; top: 20px; right: 24px; width: 36px; height: 36px; border: 2px solid var(--ink); background: var(--bg); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 41; }
  .overlay .close-btn:hover { background: var(--accent); border-color: var(--accent); color: #fff; }
  .overlay .close-btn svg { width: 16px; height: 16px; }
  .art-cover-wrap { position: relative; width: 100%; height: min(38vh, 320px); overflow: hidden; }
  .art-cover-wrap img { width: 100%; height: 100%; object-fit: cover; display: block; filter: grayscale(100%) contrast(1.05); }
  .art-cover-wrap::after {
    content: ''; position: absolute; inset: 0; pointer-events: none;
    background: linear-gradient(to bottom, rgba(255,255,255,0) 55%, var(--bg) 96%);
  }
  @media (max-width: 640px) { .art-cover-wrap { height: min(30vh, 220px); } }
  .overlay-inner.has-cover { padding-top: 22px; }
  .art-icon { width: 46px; height: 46px; color: var(--ink); margin-bottom: 10px; }
  .art-icon svg { width: 100%; height: 100%; shape-rendering: crispEdges; }
  .art-tag { font-family: 'Space Mono', monospace; font-size: 10.5px; letter-spacing: 1.4px; text-transform: uppercase; color: var(--accent); font-weight: 700; }
  .art-title { font-family: 'Archivo Black', sans-serif; font-weight: 400; font-size: 42px; line-height: 1.05; margin: 10px 0 6px; letter-spacing: -1px; opacity: 0; transform: translateY(10px); animation: riseIn .5s ease forwards .1s; }
  .art-meta {
    font-family: 'Space Mono', monospace; font-size: 11.5px; color: var(--muted);
    border-bottom: 1px solid #ddd; padding-bottom: 18px; margin-bottom: 20px;
    display: flex; align-items: center; justify-content: space-between; gap: 12px; flex-wrap: wrap;
  }
  .art-body h2 { font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 21px; margin: 26px 0 8px; }
  .art-body p { font-size: 16px; line-height: 1.7; margin: 0 0 14px; }
  .art-body ul { font-size: 15.5px; line-height: 1.7; padding-left: 22px; }
  .art-body strong { background: linear-gradient(transparent 60%, rgba(255,90,31,.3) 60%); }

  /* ---- Anotaciones: ampliaciones (amarillo) y ejemplos (azul) sobre una cita del texto ----
     El resaltado imita un rotulador fosforito pasado a mano; si una misma frase tiene los
     dos tipos a la vez, se ven los dos rayados uno encima del otro, en vez de mezclarse. ---- */
  mark.annot {
    background: none; color: inherit; cursor: pointer; padding: 0.03em 0.15em;
    box-decoration-break: clone; -webkit-box-decoration-break: clone;
  }
  mark.annot .annot-icon { display: inline-flex; gap: 2px; margin-left: 2px; vertical-align: -1px; }
  mark.annot .annot-icon svg { width: 12px; height: 12px; opacity: .7; }
  mark.annot:hover .annot-icon svg, mark.annot.open .annot-icon svg { opacity: 1; }
  mark.annot-ampliacion { background-image: linear-gradient(103deg, transparent 0%, transparent 2%, rgba(255,209,10,.6) 4%, rgba(255,209,10,.6) 95%, transparent 97%, transparent 100%); }
  mark.annot-ejemplo { background-image: linear-gradient(103deg, transparent 0%, transparent 2%, rgba(96,170,255,.5) 4%, rgba(96,170,255,.5) 95%, transparent 97%, transparent 100%); }
  mark.annot-ampliacion.annot-ejemplo {
    background-image:
      linear-gradient(103deg, transparent 0%, transparent 2%, rgba(255,209,10,.6) 4%, rgba(255,209,10,.6) 95%, transparent 97%, transparent 100%),
      linear-gradient(103deg, transparent 0%, transparent 2%, rgba(96,170,255,.5) 4%, rgba(96,170,255,.5) 95%, transparent 97%, transparent 100%);
    background-position: 0 100%, 0 0%;
    background-size: 100% 48%, 100% 52%;
    background-repeat: no-repeat, no-repeat;
  }

  /* nota tipo post-it, fija justo debajo de la frase subrayada (se mueve con el texto
     al hacer scroll porque vive dentro de .overlay-inner, no pegada al viewport) */
  .annot-note {
    position: absolute; width: 340px; z-index: 5; cursor: pointer;
    border: 2px solid var(--ink); box-shadow: 3px 4px 0 rgba(10,10,10,.3);
    padding: 13px 16px 14px; font-size: 13px; line-height: 1.48;
    transform: rotate(-1.1deg);
  }
  .annot-note.stack-2 { transform: rotate(1.6deg); }
  .annot-note-ampliacion { background: #fff1a6; }
  .annot-note-ejemplo { background: #bfe0ff; }
  .annot-note-close {
    position: absolute; top: 5px; right: 5px; width: 22px; height: 22px; border: none;
    background: transparent; cursor: pointer; display: flex; align-items: center; justify-content: center;
    opacity: .6;
  }
  .annot-note-close:hover { opacity: 1; }
  .annot-note-close svg { width: 11px; height: 11px; }
  .annot-note-label { display: flex; align-items: center; gap: 6px; font-family: 'Space Mono', monospace; font-size: 10px; letter-spacing: 1px; text-transform: uppercase; font-weight: 700; margin-bottom: 7px; padding-right: 22px; color: var(--ink); }
  .annot-note-label svg { width: 13px; height: 13px; flex: none; }
  .annot-note-text { color: var(--ink); display: block; }
  .annot-note-text a { color: var(--ink); text-decoration: underline; }
  @media (max-width: 640px) { .annot-note { width: min(84vw, 340px); } }
  .art-figure { margin: 22px 0; }
  .art-figure img { width: 100%; height: auto; display: block; border: 2px solid var(--ink); filter: grayscale(100%) contrast(1.05); }
  .art-figure figcaption { font-family: 'Space Mono', monospace; font-size: 11px; color: var(--muted); margin-top: 6px; }
  .card .thumb { display: block; width: 100%; height: 160px; object-fit: contain; background: var(--bg); border: 2px solid var(--ink); filter: grayscale(100%) contrast(1.05); margin-bottom: 4px; }
  .card:hover .thumb { border-color: var(--accent); }
  .art-original-inline {
    display: inline-flex; align-items: center; gap: 6px; text-decoration: none;
    font-family: 'Space Mono', monospace; font-size: 11.5px; font-weight: 700;
    letter-spacing: .4px; text-transform: uppercase; color: var(--accent);
    border-bottom: 2px solid var(--accent); padding-bottom: 1px; flex: none;
  }
  .art-original-inline:hover { color: var(--ink); border-color: var(--ink); }
  .art-original-inline svg { width: 13px; height: 13px; }

  /* ---- Materiales incluidos (artículos de la sección Materials) ---- */
  .art-materials { margin: 28px 0; }
  .art-materials h4 { display: flex; align-items: center; gap: 8px; margin: 0 0 14px; font-family: 'Space Mono', monospace; font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase; color: var(--accent); }
  .art-materials h4 svg { width: 18px; height: 18px; color: var(--accent); }
  .materials-list { display: flex; flex-direction: column; gap: 2px; }
  .material-item { border: 2px solid var(--ink); background: var(--bg); padding: 14px 16px; }
  .material-item + .material-item { border-top: none; }
  .material-head { display: flex; align-items: baseline; justify-content: space-between; gap: 10px; flex-wrap: wrap; }
  .material-name { font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 15.5px; }
  .material-tag { flex: none; font-family: 'Space Mono', monospace; font-size: 9px; font-weight: 700; letter-spacing: .8px; text-transform: uppercase; background: var(--ink); color: #fff; padding: 3px 8px; }
  .material-desc { margin: 6px 0 0; font-size: 13.5px; line-height: 1.5; color: var(--muted); }
  .material-cmd { display: block; margin-top: 10px; font-family: 'Space Mono', monospace; font-size: 12px; background: #f2f2f2; border: 1px solid #ddd; padding: 8px 10px; overflow-x: auto; white-space: pre; cursor: pointer; }
  .material-cmd:hover { border-color: var(--accent); color: var(--accent); }
  .material-cmd.copied { border-color: var(--accent); background: #fff0ea; color: var(--accent); }

  /* ---- Bloque de código largo (plantillas, etc.), con botón de copiar ---- */
  .code-block {
    position: relative; display: block; margin: 16px 0; font-family: 'Space Mono', monospace;
    font-size: 12.5px; line-height: 1.65; background: #f7f7f7; border: 2px solid var(--ink);
    padding: 30px 18px 18px; overflow-x: auto; white-space: pre; cursor: pointer;
  }
  .code-block:hover { border-color: var(--accent); }
  .code-block.copied { border-color: var(--accent); background: #fff0ea; }
  .code-block::before {
    content: 'Copiar'; position: absolute; top: 8px; right: 10px;
    font-family: 'Space Mono', monospace; font-size: 9.5px; letter-spacing: .5px; text-transform: uppercase;
    color: var(--muted); background: #fff; padding: 3px 7px; border: 1px solid #ddd;
  }
  .code-block:hover::before { color: var(--accent); border-color: var(--accent); }
  .code-block.copied::before { content: 'Copiado ✓'; color: var(--accent); border-color: var(--accent); background: #fff0ea; }
  .material-link { display: inline-flex; align-items: center; gap: 5px; margin-top: 10px; font-family: 'Space Mono', monospace; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .5px; text-decoration: none; }
  .material-link:hover { color: var(--accent); }
  .material-link svg { width: 12px; height: 12px; }

  /* ---- Spotlight search ---- */
  .spotlight {
    position: fixed; inset: 0; background: rgba(10,10,10,0.55); z-index: 60;
    display: none; align-items: flex-start; justify-content: center; padding-top: 12vh;
  }
  .spotlight.open { display: flex; }
  .spotlight-panel {
    width: 100%; max-width: 620px; margin: 0 24px; background: var(--bg);
    border: 2px solid var(--ink); box-shadow: 10px 10px 0 rgba(0,0,0,0.25);
    max-height: 70vh; display: flex; flex-direction: column; overflow: hidden;
  }
  .spotlight-input-row { display: flex; align-items: center; gap: 12px; padding: 16px 18px; border-bottom: 2px solid var(--ink); }
  .spotlight-input-row svg { width: 18px; height: 18px; color: var(--muted); flex: none; }
  .spotlight-input-row input {
    flex: 1; border: none; outline: none; background: transparent;
    font-family: 'Space Grotesk', sans-serif; font-size: 18px; color: var(--ink);
  }
  .spotlight-results { overflow-y: auto; }
  .spotlight-item {
    display: flex; align-items: center; gap: 12px; padding: 12px 18px; cursor: pointer;
    text-decoration: none; color: var(--ink); border-bottom: 1px solid #eee;
  }
  .spotlight-item:last-child { border-bottom: none; }
  .spotlight-item:hover, .spotlight-item.sel { background: var(--accent); color: #fff; }
  .spotlight-item .icon { width: 18px; height: 18px; flex: none; }
  .spotlight-item .meta { flex: 1; min-width: 0; }
  .spotlight-item .meta b { display: block; font-family: 'Space Grotesk', sans-serif; font-size: 14px; font-weight: 700; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .spotlight-item .meta span { display: block; font-family: 'Space Mono', monospace; font-size: 10.5px; letter-spacing: .5px; text-transform: uppercase; color: var(--muted); margin-top: 2px; }
  .spotlight-item:hover .meta span, .spotlight-item.sel .meta span { color: rgba(255,255,255,.85); }
  .spotlight-empty { padding: 24px 18px; color: var(--muted); font-size: 13.5px; text-align: center; }
  .spotlight-hint { font-family: 'Space Mono', monospace; font-size: 10.5px; color: var(--muted); padding: 10px 18px; border-top: 1px solid #eee; }

  /* ---- Rating (stars) ---- */
  .art-rating { display: flex; align-items: center; gap: 10px; margin: 4px 0 22px; }
  .art-rating .rlabel { font-family: 'Space Mono', monospace; font-size: 10.5px; letter-spacing: 1.2px; text-transform: uppercase; color: var(--muted); }
  .art-rating .stars { display: flex; gap: 3px; }
  .art-rating .star-btn { border: none; background: transparent; padding: 2px; cursor: pointer; color: var(--ink); }
  .art-rating .star-btn svg { width: 21px; height: 21px; display: block; }
  .art-rating .star-btn:hover, .art-rating .star-btn.on { color: var(--accent); }

  /* ---- Footer ---- */
  footer.site-footer { border-top: 4px solid var(--ink); margin-top: 60px; background: var(--ink); color: #fff; }
  footer.site-footer .footer-inner { padding: 44px 24px 40px; text-align: center; }
  footer.site-footer .footer-brand { font-family: 'Archivo Black', sans-serif; font-weight: 400; font-size: 22px; letter-spacing: -.5px; text-transform: uppercase; }
  footer.site-footer .footer-brand span { color: var(--accent); }
  footer.site-footer .footer-tag { font-family: 'Space Mono', monospace; font-size: 11.5px; letter-spacing: .5px; color: rgba(255,255,255,.55); margin-top: 10px; }
  footer.site-footer .footer-meta { font-family: 'Space Mono', monospace; font-size: 10px; letter-spacing: 1px; text-transform: uppercase; color: rgba(255,255,255,.35); margin-top: 22px; padding-top: 18px; border-top: 1px solid rgba(255,255,255,.15); }

  ::selection { background: var(--accent); color: #fff; }

  /* ---- Historial: tabla con scroll horizontal en móvil ---- */
  .hist-scroll { overflow-x: auto; -webkit-overflow-scrolling: touch; }

  /* ================= RESPONSIVE ================= */
  @media (max-width: 900px) {
    .wrap { padding: 0 18px; }
    header.masthead { padding: 40px 18px 0; }
    .ticker { margin: 0 -18px; }
    nav.sections { margin: 0 -18px; padding: 0 22px; }
  }

  @media (max-width: 760px) {
    h1.title { font-size: 46px; letter-spacing: -1.5px; margin: 18px 0 12px; }
    .subtitle {
      position: relative; top: auto; left: auto; width: 100%; max-width: 300px;
      margin: 0 0 22px; padding: 11px 14px 13px;
    }
    .subtitle-avatar { width: 34px; height: 34px; }
    .subtitle-name { font-size: 12.5px; }
    .subtitle-phrase { font-size: 12px; }

    nav.sections a { padding: 12px 14px; font-size: 11px; }
    .masthead-utils .hist-link { padding: 0 14px; }

    .fp-hero h2 { font-size: 26px; }
    .fp-hero p { font-size: 13.5px; }
    .fp-hero.no-media .fp-body { padding: 26px 22px; gap: 10px; }
    .fp-hero.no-media h2 { font-size: 30px; }
    .fp-hero.no-media p { font-size: 14px; }

    .rail .card { flex: 0 0 78vw; }
    .grid { grid-template-columns: 1fr; }

    .section-hero { flex-direction: column; align-items: flex-start; gap: 10px; }
    .section-hero h2 { font-size: 26px; }

    .ency-review-banner { padding: 18px 20px; }
    .ency-review-banner-text strong { font-size: 17px; }

    .art-title { font-size: 30px; }
    .art-body p, .art-body ul { font-size: 15px; }
    .overlay-inner { padding: 60px 18px 80px; }

    .ency-toolbar { flex-direction: column; align-items: stretch; gap: 10px; }
    .ency-layout { flex-direction: column; gap: 8px; }
    .ency-index {
      position: static; flex-direction: row; flex-wrap: wrap; max-height: none;
      justify-content: flex-start; gap: 2px 8px; padding: 10px 0; border-bottom: 1px solid #e5e5e5; margin-bottom: 10px;
      transform: none; top: auto; right: auto; background: transparent;
    }

    table.hist { min-width: 520px; }
    .stat-row { flex-wrap: wrap; }
    .stat-block { flex: 1 1 33%; padding: 14px 8px; }
    .stat-num { font-size: 24px; }
    .stat-bar-label { flex-basis: 100px; font-size: 9.5px; }

    .spotlight, .ticker-modal { padding-top: 8vh; }
  }

  @media (max-width: 480px) {
    .wrap { padding: 0 14px; }
    main.wrap { padding-top: 24px; }
    header.masthead { padding: 32px 14px 0; }
    .ticker { margin: 0 -14px; }
    nav.sections { margin: 0 -14px; padding: 0 18px; }

    h1.title { font-size: 34px; margin-bottom: 10px; }
    .subtitle { max-width: 100%; padding: 9px 11px 11px; margin-bottom: 18px; }
    .subtitle-avatar { width: 28px; height: 28px; }
    .subtitle-name { font-size: 11.5px; }
    .subtitle-phrase { font-size: 11px; }

    .masthead-utils { gap: 6px; }
    .masthead-search-btn { height: 34px; padding: 0 10px; font-size: 9.5px; }
    .masthead-utils .hist-link { height: 34px; padding: 0 10px; font-size: 9.5px; }

    .fp-hero h2 { font-size: 22px; }
    .fp-hero.no-media h2 { font-size: 24px; }
    .art-title { font-size: 25px; }
    .section-hero h2 { font-size: 22px; }

    .rail .card { flex: 0 0 86vw; }
    .ticker-badge { left: 10px; }
  }
</style>
</head>
<body>

<header class="masthead">
  <div class="wrap">
    <div class="top-bar">
      <div class="masthead-utils" id="masthead-utils"></div>
    </div>
    <div class="live" id="live-kicker"></div>
    <h1 class="title" id="masthead-title"></h1>
    <div class="subtitle" id="subtitle"></div>
  </div>
  <div class="ticker" id="ticker"><div class="ticker-badge" id="ticker-badge"></div><div class="ticker-scroll"><div class="ticker-track" id="ticker-track"></div></div></div>
  <nav class="sections" id="section-nav"></nav>
</header>

<main class="wrap" id="main"></main>

<footer class="site-footer">
  <div class="wrap footer-inner">
    <div class="footer-brand">The <span>Future</span> Designer</div>
    <div class="footer-tag">Un archivo personal de aprendizaje — artículo a artículo, IA a IA.</div>
    <div class="footer-meta" id="footer-meta"></div>
  </div>
</footer>

<div class="overlay" id="overlay">
  <div class="close-btn" id="close-overlay"></div>
  <div class="art-cover-wrap" id="art-cover-wrap"></div>
  <div class="overlay-inner" id="overlay-inner"></div>
</div>

<div class="toast" id="toast"></div>

<div class="ticker-modal" id="flash-modal">
  <div class="ticker-modal-panel flash-panel">
    <div class="ticker-modal-header">
      <h3>Repasar términos</h3>
      <button class="close-btn-sm" id="flash-modal-close"></button>
    </div>
    <div class="flash-modal-body" id="flash-modal-body"></div>
  </div>
</div>

<div class="spotlight" id="spotlight">
  <div class="spotlight-panel">
    <div class="spotlight-input-row">
      <span id="spotlight-icon"></span>
      <input type="text" id="spotlight-input" placeholder="Buscar artículos, secciones, términos..." autocomplete="off">
    </div>
    <div class="spotlight-results" id="spotlight-results"></div>
  </div>
</div>

<script>
const ARTICLES = __ARTICLES_JSON__;
const COMMANDS = __COMMANDS_JSON__;
const SECTIONS = __SECTIONS_JSON__;
const ICONS = __ICONS_JSON__;
const ARTICLE_ICONS = __ARTICLE_ICONS_JSON__;

function bySlug(slug) { return SECTIONS.find(s => s.slug === slug); }

/* ---------- truncado limpio con puntos suspensivos ---------- */
function truncate(str, maxLen) {
  if (!str) return '';
  if (str.length <= maxLen) return str;
  const cut = str.slice(0, maxLen);
  const lastSpace = cut.lastIndexOf(' ');
  const base = lastSpace > maxLen * 0.6 ? cut.slice(0, lastSpace) : cut;
  return base.trim() + '…';
}

/* ---------- masthead animated title ---------- */
(function(){
  const el = document.getElementById('masthead-title');
  const text = "The Future Designer";
  text.split(' ').forEach((word, wi) => {
    const span = document.createElement('span');
    span.textContent = word + ' ';
    span.style.animationDelay = (wi * 0.09) + 's';
    el.appendChild(span);
  });
})();

/* ---------- live kicker: date, time, radar ---------- */
function renderLiveKicker() {
  const el = document.getElementById('live-kicker');
  function paint() {
    const now = new Date();
    const date = now.toLocaleDateString('es-ES', { day: '2-digit', month: 'short', year: 'numeric' }).toUpperCase();
    const time = now.toLocaleTimeString('es-ES', { hour: '2-digit', minute: '2-digit' });
    el.innerHTML = `<span class="dot-wrap"></span> En directo · ${date} · ${time}`;
  }
  paint();
  setInterval(paint, 30000);
}

/* ---------- subtitle: nota post-it arrastrable, firma de la creadora ---------- */
const SUBTITLE_PHRASES = [
  'Aquí no decide ningún algoritmo. Decido yo, con más pestañas abiertas que criterio.',
  'La IA redacta, pero el mal gusto de elegir qué leer sigue siendo mío.',
  'Ningún LLM ha votado si esto merece la pena. Esa parte la hago yo, a mano.',
  'Curado por una humana con síndrome del impostor y demasiada curiosidad.',
  'Yo leo, yo decido — la IA solo aguanta el ritmo que le pongo.',
];
const LINKEDIN_URL = 'https://www.linkedin.com/in/isabel-ferrer-dalmau-productdesigner/';

function renderSubtitle() {
  const el = document.getElementById('subtitle');
  const phrase = SUBTITLE_PHRASES[Math.floor(Math.random() * SUBTITLE_PHRASES.length)];
  el.innerHTML = `
    <div class="subtitle-row">
      <img class="subtitle-avatar" src="images/_shared/annotations-avatar.png" alt="Isabel Ferrer - Dalmau">
      <div class="subtitle-text">
        <span class="subtitle-name">Nota de la editora jefe</span>
        <a class="subtitle-byline" href="${LINKEDIN_URL}" target="_blank" rel="noopener">Isabel Ferrer - Dalmau</a>
      </div>
    </div>
    <span class="subtitle-phrase">${phrase}</span>`;
  makeDraggable(el, 'postitPos');
}

/* ---------- post-it arrastrable (masthead) ---------- */
function makeDraggable(el, storageKey) {
  const parent = el.offsetParent || el.parentElement;
  const mobileFlow = () => window.innerWidth <= 760; // en mobile el post-it vive en el flujo normal, bajo el titulo — nada de arrastre
  let saved = null;
  try { saved = JSON.parse(localStorage.getItem(storageKey)); } catch(e) {}
  if (saved && !mobileFlow()) { el.style.left = saved.x + 'px'; el.style.top = saved.y + 'px'; }

  let dragging = false, offX = 0, offY = 0;

  el.addEventListener('pointerdown', e => {
    if (mobileFlow()) return;
    if (e.target.closest('a, button')) return;
    dragging = true;
    el.setPointerCapture(e.pointerId);
    const rect = el.getBoundingClientRect();
    offX = e.clientX - rect.left;
    offY = e.clientY - rect.top;
    el.classList.add('dragging');
  });

  el.addEventListener('pointermove', e => {
    if (!dragging) return;
    const pRect = parent.getBoundingClientRect();
    const elRect = el.getBoundingClientRect();
    let x = e.clientX - pRect.left - offX;
    let y = e.clientY - pRect.top - offY;
    x = Math.max(-elRect.width * 0.3, Math.min(x, pRect.width - elRect.width * 0.7));
    y = Math.max(0, Math.min(y, pRect.height - elRect.height * 0.5));
    el.style.left = x + 'px';
    el.style.top = y + 'px';
  });

  const stop = e => {
    if (!dragging) return;
    dragging = false;
    el.classList.remove('dragging');
    localStorage.setItem(storageKey, JSON.stringify({ x: parseFloat(el.style.left), y: parseFloat(el.style.top) }));
  };
  el.addEventListener('pointerup', stop);
  el.addEventListener('pointercancel', stop);
}

/* ---------- ticker: titulares más recientes ---------- */
function renderTicker() {
  const wrap = document.getElementById('ticker');
  const track = document.getElementById('ticker-track');
  const badge = document.getElementById('ticker-badge');
  if (badge && !badge.dataset.filled) {
    badge.innerHTML = `<svg class="burst" viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M12 2c1 3-2 4-2 7a3 3 0 0 0 6 0c0-1-0.5-2-1-2 2 0 4 2 4 5.5A7 7 0 1 1 8 12.5C8 9 9 6 12 2Z"/></svg><span>¡Nuevo!</span>`;
    badge.dataset.filled = '1';
  }
  const items = visibleArticles()
    .slice()
    .sort((x, y) => (y.date_added || '').localeCompare(x.date_added || ''));
  if (!items.length) { wrap.style.display = 'none'; return; }
  wrap.style.display = '';
  const build = () => items.map(a => {
    const sec = bySlug(a.section);
    return `<a class="item" href="#/articulo/${a.id}"><b>${sec ? sec.name : ''}</b> — ${a.title}</a>`;
  }).join('');
  track.innerHTML = build() + build();
}

/* ---------- soft-delete (papelera) + borrado definitivo (historial) ---------- */
function getHidden() { try { return JSON.parse(localStorage.getItem('hiddenArticles') || '[]'); } catch(e) { return []; } }
function setHidden(arr) { localStorage.setItem('hiddenArticles', JSON.stringify(arr)); }
function getDeleted() { try { return JSON.parse(localStorage.getItem('deletedArticles') || '[]'); } catch(e) { return []; } }
function setDeleted(arr) { localStorage.setItem('deletedArticles', JSON.stringify(arr)); }

function visibleArticles() {
  const hidden = getHidden();
  const deleted = getDeleted();
  return ARTICLES.filter(a => !hidden.includes(a.id) && !deleted.includes(a.id));
}

/* ---------- footer ---------- */
function renderFooter() {
  const el = document.getElementById('footer-meta');
  const n = ARTICLES.length;
  el.textContent = `${n} artículo${n === 1 ? '' : 's'} guardado${n === 1 ? '' : 's'} · actualizado ${new Date().toLocaleDateString('es-ES', { day: '2-digit', month: 'short', year: 'numeric' })}`;
}

/* ---------- reflexiones (sintetizadas por la skill Article Debate) ---------- */
function reflectionsHtml(a) {
  if (!a.reflections || !a.reflections.length) return '';
  const entries = [...a.reflections].reverse().map(r => `
    <div class="reflection-entry">
      <div class="reflection-date">${r.date || ''}</div>
      <div class="reflection-text">${mdToHtml(r.text || '')}</div>
    </div>
  `).join('');
  return `<div class="art-reflections"><h4>${ICONS['chat-code']} Tu reflexión</h4>${entries}</div>`;
}

/* ---------- artículos relacionados ---------- */
function relatedArticles(a) {
  const pool = visibleArticles().filter(x => x.id !== a.id);
  const myTerms = new Set((a.glossary || []).map(g => g.term.toLowerCase()));
  const scored = pool.map(x => {
    let score = 0;
    if (a.subsection && x.subsection === a.subsection) score += 2;
    else if (x.section === a.section) score += 1;
    const shared = (x.glossary || []).some(g => myTerms.has(g.term.toLowerCase()));
    if (shared) score += 2;
    return { x, score };
  }).filter(s => s.score > 0);
  scored.sort((p, q) => q.score - p.score || (q.x.date_added || '').localeCompare(p.x.date_added || ''));
  return scored.slice(0, 3).map(s => s.x);
}

function relatedHtml(a) {
  const rel = relatedArticles(a);
  if (!rel.length) return '';
  return `<div class="art-related">
    <h4>${ICONS.link} Relacionados</h4>
    <div class="rail">${rel.map(cardHtml).join('')}</div>
  </div>`;
}

/* ---------- modal del teleprompter: artículos nuevos sin valorar ---------- */
/* ---------- liked glossary terms (enciclopedia) ---------- */
function getLikedTerms() { try { return JSON.parse(localStorage.getItem('likedTerms') || '[]'); } catch(e) { return []; } }
function setLikedTerms(arr) { localStorage.setItem('likedTerms', JSON.stringify(arr)); }
function termKey(articleId, idx) { return `${articleId}::${idx}`; }
function toggleLikedTerm(key) {
  const liked = getLikedTerms();
  const i = liked.indexOf(key);
  if (i === -1) liked.push(key); else liked.splice(i, 1);
  setLikedTerms(liked);
  return liked.includes(key);
}

/* ---------- streak (solo para el stat-block "Racha" del panel de progreso) ---------- */
function computeStreak() {
  const dates = new Set(ARTICLES.map(a => a.date_added));
  let streak = 0;
  let cursor = new Date();
  while (true) {
    const iso = cursor.toISOString().slice(0,10);
    if (dates.has(iso)) { streak++; cursor.setDate(cursor.getDate() - 1); }
    else break;
  }
  return streak;
}

/* ---------- nav ---------- */
function renderNav(active) {
  const nav = document.getElementById('section-nav');
  const items = [{slug:'', name:'Inicio'}]
    .concat(SECTIONS.map(s=>({slug:s.slug,name:s.name})))
    .concat([{slug:'enciclopedia', name:'Enciclopedia'}]);
  const links = items.map(it => {
    const href = it.slug ? `#/${it.slug}` : '#/';
    const cls = (active === it.slug) ? 'active' : '';
    return `<a href="${href}" class="${cls}">${it.name}</a>`;
  }).join('');
  nav.innerHTML = `
    <div class="links-wrap">
      <button class="links-arrow left hidden" id="links-prev" title="Ver anteriores">${ICONS.arrow}</button>
      <div class="links" id="nav-links">${links}</div>
      <button class="links-arrow right hidden" id="links-next" title="Ver más">${ICONS.arrow}</button>
    </div>`;
  setupLinksScroll();
  renderMastheadUtils(active);
}

function renderMastheadUtils(active) {
  const utils = document.getElementById('masthead-utils');
  const histCls = active === 'historial' ? 'active' : '';
  utils.innerHTML = `
    <button class="masthead-search-btn" id="masthead-search-btn" title="Buscar">${ICONS.search}<span>Buscar</span></button>
    <a href="#/historial" class="hist-link ${histCls}" title="Historial">${ICONS.history}<span>Historial</span></a>`;
  document.getElementById('masthead-search-btn').addEventListener('click', openSpotlight);
}

function setupLinksScroll() {
  const track = document.getElementById('nav-links');
  const prev = document.getElementById('links-prev');
  const next = document.getElementById('links-next');
  function update() {
    const overflow = track.scrollWidth > track.clientWidth + 2;
    prev.classList.toggle('hidden', !overflow || track.scrollLeft <= 2);
    next.classList.toggle('hidden', !overflow || track.scrollLeft >= track.scrollWidth - track.clientWidth - 2);
  }
  prev.addEventListener('click', () => { track.scrollBy({ left: -160, behavior: 'smooth' }); });
  next.addEventListener('click', () => { track.scrollBy({ left: 160, behavior: 'smooth' }); });
  track.addEventListener('scroll', update);
  window.addEventListener('resize', update);
  update();
}

/* ---------- markdown -> html (small subset) ---------- */
/* ---------- anotaciones: ampliaciones y ejemplos sobre una cita exacta ---------- */
const ANNOT_META = {
  ampliacion: { icon: 'plus', label: 'Ampliación' },
  ejemplo: { icon: 'eye', label: 'Ejemplo' },
};

/* varias anotaciones pueden compartir la misma cita a propósito (p. ej. una ampliación y
   su ejemplo sobre la misma frase) — se agrupan para pintar un único resaltado con los
   dos rayados a la vez, en vez de intentar envolver el mismo texto dos veces */
function groupAnnotationsByQuote(annotations) {
  const groups = new Map();
  (annotations || []).forEach((an, idx) => {
    if (!an.quote) return;
    if (!groups.has(an.quote)) groups.set(an.quote, []);
    groups.get(an.quote).push(idx);
  });
  return groups;
}

/* envuelve, dentro de una línea de texto ya en plano, cada cita sin usar que aparezca en
   ella — las citas más largas van primero para que una corta no rompa a una que la
   contiene; cada cita se resalta como mucho una vez en todo el artículo */
function applyAnnotations(text, annotations, usedQuotes) {
  let result = text;
  const groups = groupAnnotationsByQuote(annotations);
  const quotes = [...groups.keys()].sort((a, b) => b.length - a.length);
  quotes.forEach(quote => {
    if (usedQuotes.has(quote) || !result.includes(quote)) return;
    const idxs = groups.get(quote);
    const types = [...new Set(idxs.map(i => annotations[i].type === 'ejemplo' ? 'ejemplo' : 'ampliacion'))];
    const classes = types.map(t => `annot-${t}`).join(' ');
    const icons = types.map(t => ICONS[(ANNOT_META[t] || ANNOT_META.ampliacion).icon]).join('');
    result = result.replace(quote,
      `<mark class="annot ${classes}" data-annot-idxs="${idxs.join(',')}" tabindex="0">${quote}<span class="annot-icon">${icons}</span></mark>`);
    usedQuotes.add(quote);
  });
  return result;
}

function escapeHtml(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function mdToHtml(md, annotations) {
  if (!md) return '';
  const lines = md.replace(/\r/g,'').split('\n');
  const used = new Set();
  let html = '';
  let inList = false;
  const inlineFmt = (s) => applyAnnotations(s, annotations, used)
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    .replace(/\[(.+?)\]\((.+?)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
  let i = 0;
  while (i < lines.length) {
    const l = lines[i].trim();
    // bloque ```...``` -> se copia tal cual, no se interpreta como markdown (así una
    // plantilla que lleva sus propios ## o - por dentro no se rompe al renderizarla)
    if (l.startsWith('```')) {
      const codeLines = [];
      i++;
      while (i < lines.length && !lines[i].trim().startsWith('```')) { codeLines.push(lines[i]); i++; }
      i++;
      if (inList) { html += '</ul>'; inList = false; }
      const raw = codeLines.join('\n');
      html += `<pre class="code-block" data-copy="${raw.replace(/"/g, '&quot;')}" title="Copiar">${escapeHtml(raw)}</pre>`;
      continue;
    }
    const imgMatch = l.match(/^!\[(.*?)\]\((.+?)\)$/);
    if (imgMatch) {
      if (inList) { html += '</ul>'; inList = false; }
      html += `<figure class="art-figure"><img src="${imgMatch[2]}" alt="${imgMatch[1]}" loading="lazy">${imgMatch[1] ? `<figcaption>${imgMatch[1]}</figcaption>` : ''}</figure>`;
    } else if (l.startsWith('## ')) {
      if (inList) { html += '</ul>'; inList = false; }
      html += `<h2>${inlineFmt(l.slice(3))}</h2>`;
    } else if (l.startsWith('# ')) {
      if (inList) { html += '</ul>'; inList = false; }
      html += `<h2>${inlineFmt(l.slice(2))}</h2>`;
    } else if (l.startsWith('- ') || l.startsWith('* ')) {
      if (!inList) { html += '<ul>'; inList = true; }
      html += `<li>${inlineFmt(l.slice(2))}</li>`;
    } else if (l === '---') {
      if (inList) { html += '</ul>'; inList = false; }
    } else if (l === '') {
      if (inList) { html += '</ul>'; inList = false; }
    } else {
      if (inList) { html += '</ul>'; inList = false; }
      html += `<p>${inlineFmt(l)}</p>`;
    }
    i++;
  }
  if (inList) html += '</ul>';
  return html;
}

/* ---------- card rendering ---------- */
function annotBadgeHtml(a) {
  if (!a.annotations || !a.annotations.length) return '';
  return `<div class="annot-flag"><span class="annot-flag-text">¡Con anotaciones!</span></div>`;
}

function cardHtml(a) {
  const sec = bySlug(a.section);
  const thumb = (a.images && a.images.length) ? `<img class="thumb" src="${a.images[0]}" alt="" loading="lazy">` : '';
  return `<a class="card" href="#/articulo/${a.id}" data-id="${a.id}">
    ${annotBadgeHtml(a)}
    ${thumb}
    <div class="card-body">
      <span class="tag">${sec ? sec.name : a.section}${a.subsection ? ' · ' + a.subsection : ''}</span>
      <h3>${a.title}</h3>
      <p>${a.summary}</p>
      <div class="date">Añadido: ${a.date_added || '—'}</div>
    </div>
  </a>`;
}

/* ---------- front page (tabloide, cronología pura) ---------- */
/* ---------- icono pixel-art del titular, elegido según el contenido ---------- */
const LEAD_ICON_RULES = [
  ['px-box', /\bskill\b|plantilla|repo(sitorio)?|descargar|recurso/i],
  ['px-terminal', /\bcli\b|terminal|comando|consola|\bscript\b/i],
  ['px-chip', /\bapi\b|\bmcp\b|servidor|protocolo|integraci[oó]n/i],
  ['px-book', /diccionario|t[eé]rmino|glosario|definici[oó]n|concepto/i],
  ['px-chat', /ingenier[oa]s?|developer|desarrollador|colaborar|comunicaci[oó]n/i],
  ['px-palette', /figma|dise[ñn]o|design|plugin|plantilla|\bui\b|\bux\b/i],
  ['px-robot', /claude|\bia\b|\bai\b|agente|modelo|\bllm\b|inteligencia artificial/i],
  ['px-brain', /aprend|estudio|repaso/i],
];
const LEAD_ICON_BY_SECTION = {
  'teoria': 'px-brain',
  'practica': 'px-robot',
  'novedades': 'px-box',
};
function pixelIconFor(a) {
  const text = `${a.title} ${a.summary} ${a.subsection || ''}`;
  const hit = LEAD_ICON_RULES.find(([, re]) => re.test(text));
  if (hit) return hit[0];
  return LEAD_ICON_BY_SECTION[a.section] || 'px-star';
}

/* Cada artículo tiene su propia ilustración pixel-art (ARTICLE_ICONS). Si un artículo
   nuevo todavía no tiene la suya dibujada a mano, cae al icono por palabra clave/sección. */
function articleIconSvg(a) {
  return ARTICLE_ICONS[a.id] || ICONS[pixelIconFor(a)];
}

function leadHtml(a) {
  const sec = bySlug(a.section);
  const hasImg = a.images && a.images.length;
  const img = hasImg ? `<img class="fp-img" src="${a.images[0]}" alt="" loading="lazy">` : '';
  return `<a class="fp-card fp-hero ${hasImg ? '' : 'no-media'}" href="#/articulo/${a.id}">
    ${annotBadgeHtml(a)}
    ${img}
    <div class="fp-body">
      ${!hasImg ? `<div class="lead-icon">${articleIconSvg(a)}</div>` : ''}
      <span class="tag">${sec ? sec.name : a.section}${a.subsection ? ' · ' + a.subsection : ''}</span>
      <h2>${truncate(a.title, 100)}</h2>
      <p>${truncate(a.summary, 160)}</p>
      <div class="date mono">${a.date_added || '—'}</div>
    </div>
  </a>`;
}

/* ---------- tarjeta de segundo nivel (tamaño medio) ---------- */
function secondaryHtml(a) {
  const sec = bySlug(a.section);
  const media = (a.images && a.images.length)
    ? `<img class="fp-img" src="${a.images[0]}" alt="" loading="lazy">`
    : `<div class="fp-noimg">${articleIconSvg(a)}</div>`;
  return `<a class="fp-card fp-secondary ${(a.images && a.images.length) ? '' : 'no-media'}" href="#/articulo/${a.id}">
    ${annotBadgeHtml(a)}
    ${media}
    <div class="fp-body">
      <span class="tag">${sec ? sec.name : a.section}${a.subsection ? ' · ' + a.subsection : ''}</span>
      <h3>${truncate(a.title, 90)}</h3>
      <p>${truncate(a.summary, 120)}</p>
      <div class="date mono">${a.date_added || '—'}</div>
    </div>
  </a>`;
}

/* ---------- portada: feed cronológico en 3 tamaños ----------
   El más reciente manda (titular grande), los 2 siguientes van en tamaño
   medio y el resto en la cuadrícula de tarjetas. Puro orden por fecha. */
/* ---------- carrusel de titular (autoplay 5s + flechas + puntos) ---------- */
let heroTimer = null;
const heroState = { items: [], index: 0 };

function paintHero() {
  const { items, index } = heroState;
  const slot = document.getElementById('hero-slot');
  if (!slot || !items.length) return;

  const swap = () => { slot.innerHTML = leadHtml(items[index]); slot.classList.remove('fading'); };
  if (slot.children.length) {
    slot.classList.add('fading');
    setTimeout(swap, 220);
  } else {
    swap();
  }

  const dotsWrap = document.getElementById('hero-dots');
  dotsWrap.innerHTML = items.length > 1
    ? items.map((_, i) => `<button class="lead-dot ${i === index ? 'on' : ''}" data-i="${i}" aria-label="Titular ${i + 1}"></button>`).join('')
    : '';
  dotsWrap.querySelectorAll('.lead-dot').forEach(d => d.addEventListener('click', () => {
    heroState.index = +d.dataset.i;
    paintHero();
    restartHeroTimer();
  }));
}
function heroStep(delta) {
  const n = heroState.items.length;
  if (!n) return;
  heroState.index = (heroState.index + delta + n) % n;
  paintHero();
}
function restartHeroTimer() {
  clearHeroTimer();
  if (heroState.items.length > 1) heroTimer = setInterval(() => heroStep(1), 5000);
}
function clearHeroTimer() {
  if (heroTimer) { clearInterval(heroTimer); heroTimer = null; }
}

/* ---------- carrusel paginado de "quizá te interese" (dot-nav, sin autoplay) ---------- */
const otherCarouselState = { pages: [], index: 0 };

function paintOtherCarousel(direction) {
  const wrap = document.getElementById('other-carousel-slot');
  if (!wrap) return;
  const page = otherCarouselState.pages[otherCarouselState.index] || [];
  const html = `<div class="other-carousel-page">${page.map(secondaryHtml).join('')}</div>`;

  const outgoing = wrap.firstElementChild;
  if (direction && outgoing) {
    outgoing.classList.add(direction > 0 ? 'slide-out-left' : 'slide-out-right');
    setTimeout(() => {
      wrap.innerHTML = html;
      const incoming = wrap.firstElementChild;
      incoming.classList.add(direction > 0 ? 'slide-in-right' : 'slide-in-left');
      requestAnimationFrame(() => requestAnimationFrame(() => incoming.classList.remove('slide-in-right', 'slide-in-left')));
    }, 220);
  } else {
    wrap.innerHTML = html;
  }
}
function otherCarouselStep(delta) {
  const n = otherCarouselState.pages.length;
  if (!n) return;
  otherCarouselState.index = (otherCarouselState.index + delta + n) % n;
  paintOtherCarousel(delta);
}

/* ---------- término del día (post-it que gira, junto al titular) ---------- */
function pickTermOfDay(terms) {
  if (!terms.length) return null;
  const iso = todayISO();
  let hash = 0;
  for (let i = 0; i < iso.length; i++) hash = (hash * 31 + iso.charCodeAt(i)) >>> 0;
  return terms[hash % terms.length];
}
let termOfDayFlipped = false;

function paintTermOfDay(term) {
  const wrap = document.getElementById('term-of-day');
  if (!wrap) return;
  if (!term) {
    wrap.innerHTML = `<div class="ency-sidebar-empty">Aún no hay términos guardados. Dale a ${ICONS.heart} en los que veas dentro de un artículo.</div>`;
    return;
  }
  wrap.innerHTML = `
    <span class="tape tape-left"></span><span class="tape tape-right"></span>
    <div class="term-of-day-back">
      <p>${term.definition}</p>
      <a class="src" data-open="${term.articleId}">De: ${term.articleTitle}</a>
    </div>
    <div class="term-of-day-lift">
      <div class="term-of-day-face">
        <span class="curl"></span>
        <span class="term-of-day-label">Término del día</span>
        <b>${term.term}</b>
        <span class="term-of-day-hint">Toca para despegarlo</span>
      </div>
    </div>
  `;
  wrap.classList.toggle('flipped', termOfDayFlipped);
  wrap.addEventListener('click', () => {
    termOfDayFlipped = !termOfDayFlipped;
    wrap.classList.toggle('flipped', termOfDayFlipped);
  });
  wrap.querySelector('[data-open]').addEventListener('click', e => {
    e.stopPropagation();
    location.hash = '#/articulo/' + e.currentTarget.dataset.open;
  });
}

/* ---------- chuleta de comandos de Claude (junto al titular) ---------- */
function cmdCheatRowHtml(c) {
  return `<div class="cmd-cheat-row">
    <b>${escapeHtml(c.name)}</b>
    <span>${escapeHtml(c.description)}</span>
  </div>`;
}
function paintCmdCheatsheet() {
  const wrap = document.getElementById('cmd-cheat-list');
  if (!wrap) return;
  if (!COMMANDS.length) {
    wrap.innerHTML = `<div class="ency-sidebar-empty">Aún no hay comandos guardados aquí.</div>`;
    return;
  }
  const sorted = COMMANDS.slice().sort((a, b) => a.name.replace(/^\//, '').localeCompare(b.name.replace(/^\//, ''), 'es', { sensitivity: 'base' }));
  wrap.innerHTML = sorted.map(cmdCheatRowHtml).join('');
}

function renderPortada() {
  renderNav('');
  const main = document.getElementById('main');
  const list = visibleArticles()
    .slice()
    .sort((x, y) => (y.date_added || '').localeCompare(x.date_added || ''));

  if (!list.length) {
    main.innerHTML = `<div class="empty">Todavía no hay artículos.</div>`;
    return;
  }

  heroState.items = list.slice(0, 3);
  heroState.index = 0;

  const otherItems = list.slice(3, 9);
  otherCarouselState.pages = [];
  for (let i = 0; i < otherItems.length; i += 3) otherCarouselState.pages.push(otherItems.slice(i, i + 3));
  otherCarouselState.index = 0;

  const rest = list.slice(9);
  const bySection = {};
  rest.forEach(a => { (bySection[a.section] = bySection[a.section] || []).push(a); });

  const encyTerms = buildEncyTerms();
  const termOfDay = pickTermOfDay(encyTerms);

  main.innerHTML = `
    <div class="front-top">
      <div class="front-lead">
        <div id="hero-slot"></div>
        <div class="lead-controls">
          <button class="lead-arrow left" id="hero-prev" title="Titular anterior">${ICONS.arrow}</button>
          <div class="lead-dots" id="hero-dots"></div>
          <button class="lead-arrow" id="hero-next" title="Siguiente titular">${ICONS.arrow}</button>
        </div>
      </div>
      <div class="ency-sidebar-stack">
        <div class="term-of-day" id="term-of-day"></div>
        <aside class="cmd-cheatsheet">
          <div class="cmd-cheatsheet-head"><h3>Chuleta de comandos</h3></div>
          <div class="cmd-cheat-list" id="cmd-cheat-list"></div>
        </aside>
      </div>
    </div>
    ${otherCarouselState.pages.length ? `
      <div class="front-divider"><span class="front-label">Quizá te interese</span></div>
      <div class="other-carousel">
        <button class="other-carousel-arrow left" id="other-prev" title="Anteriores">${ICONS.arrow}</button>
        <div class="other-carousel-viewport" id="other-carousel-slot"></div>
        <button class="other-carousel-arrow right" id="other-next" title="Siguientes">${ICONS.arrow}</button>
      </div>
    ` : ''}
    ${SECTIONS.map(s => {
      const items = (bySection[s.slug] || []).slice(0, 5);
      return `
        <div class="front-divider"><span class="front-label">${s.name}</span></div>
        ${items.length
          ? `<div class="grid">${items.map(cardHtml).join('')}</div>`
          : `<div class="empty">Todavía no hay más artículos de ${s.name.toLowerCase()} por aquí — vuelve pronto.</div>`}
      `;
    }).join('')}
  `;

  paintHero();
  restartHeroTimer();
  document.getElementById('hero-prev').addEventListener('click', () => { heroStep(-1); restartHeroTimer(); });
  document.getElementById('hero-next').addEventListener('click', () => { heroStep(1); restartHeroTimer(); });

  paintTermOfDay(termOfDay);
  paintCmdCheatsheet();

  if (otherCarouselState.pages.length) {
    paintOtherCarousel();
    const multi = otherCarouselState.pages.length > 1;
    document.getElementById('other-prev').classList.toggle('hidden', !multi);
    document.getElementById('other-next').classList.toggle('hidden', !multi);
    document.getElementById('other-prev').addEventListener('click', () => otherCarouselStep(-1));
    document.getElementById('other-next').addEventListener('click', () => otherCarouselStep(1));
  }
}

function railHtml(items) {
  return `<div class="rail">${items.map(cardHtml).join('')}</div>`;
}

const sectionState = { slug: null, list: [], subsections: [], hasOtros: false, activeSub: null };

function renderSection(slug) {
  const sec = bySlug(slug);
  renderNav(slug);
  const main = document.getElementById('main');
  if (!sec) { main.innerHTML = '<p>Sección no encontrada.</p>'; return; }
  const list = visibleArticles().filter(a => a.section === slug);
  const subsections = [...new Set(list.map(a => a.subsection).filter(Boolean))].sort();
  const hasOtros = list.some(a => !a.subsection);

  sectionState.slug = slug;
  sectionState.list = list;
  sectionState.subsections = subsections;
  sectionState.hasOtros = hasOtros;
  sectionState.activeSub = null; // null = "Todas"

  if (list.length === 0) {
    main.innerHTML = `
      <div class="section-hero"><div class="icon">${ICONS[sec.icon]}</div><div><h2>${sec.name}</h2><p>${sec.desc}</p></div></div>
      <div class="empty">Aún no hay artículos en esta sección.</div>
    `;
    return;
  }

  main.innerHTML = `
    <div class="section-hero">
      <div class="icon">${ICONS[sec.icon]}</div>
      <div><h2>${sec.name}</h2><p>${sec.desc}</p></div>
    </div>
    <div id="subnav-out"></div>
    <div id="sections-out"></div>
  `;
  paintSectionSubnav();
  paintSectionBody();
}

function paintSectionSubnav() {
  const wrap = document.getElementById('subnav-out');
  if (!wrap) return;
  const { subsections, hasOtros, activeSub } = sectionState;
  if (!subsections.length) { wrap.innerHTML = ''; return; }
  const pillHtml = (label, subVal, isActive) =>
    `<button class="subnav-pill ${isActive ? 'active' : ''}" data-sub="${subVal}">${label}</button>`;
  wrap.innerHTML = `<div class="subnav">
    ${pillHtml('Todas', '', activeSub === null)}
    ${subsections.map(s => pillHtml(s, s, activeSub === s)).join('')}
    ${hasOtros ? pillHtml('Otros', '__otros__', activeSub === '__otros__') : ''}
  </div>`;
  wrap.querySelectorAll('[data-sub]').forEach(btn => {
    btn.addEventListener('click', () => {
      sectionState.activeSub = btn.dataset.sub === '' ? null : btn.dataset.sub;
      paintSectionSubnav();
      paintSectionBody();
    });
  });
}

function paintSectionBody() {
  const wrap = document.getElementById('sections-out');
  if (!wrap) return;
  const { list, activeSub } = sectionState;
  const byDate = (x, y) => (y.date_added || '').localeCompare(x.date_added || '');
  let items;
  if (activeSub === null) items = list.slice().sort(byDate);
  else if (activeSub === '__otros__') items = list.filter(a => !a.subsection).sort(byDate);
  else items = list.filter(a => a.subsection === activeSub).sort(byDate);

  wrap.innerHTML = items.length
    ? `<div class="grid">${items.map(cardHtml).join('')}</div>`
    : `<div class="empty">No hay artículos aquí.</div>`;
}

function progressPanelHtml(list) {
  const bySection = SECTIONS.map(sec => ({ sec, count: list.filter(a => a.section === sec.slug).length }));
  const maxCount = Math.max(1, ...bySection.map(b => b.count));
  const termCount = buildEncyTerms().length;
  const streak = computeStreak();
  return `<div class="progress-panel">
    <div class="stat-row">
      <div class="stat-block"><div class="stat-num">${list.length}</div><div class="stat-label">Artículos</div></div>
      <div class="stat-block"><div class="stat-num">${termCount}</div><div class="stat-label">Términos</div></div>
      <div class="stat-block"><div class="stat-num">${streak}</div><div class="stat-label">Racha</div></div>
    </div>
    <div class="stat-bars">
      ${bySection.map(b => `
        <div class="stat-bar-row">
          <span class="stat-bar-label">${b.sec.name}</span>
          <div class="stat-bar-track"><div class="stat-bar-fill" style="width:${Math.round(b.count / maxCount * 100)}%"></div></div>
          <span class="stat-bar-count">${b.count}</span>
        </div>
      `).join('')}
    </div>
  </div>`;
}

function renderHistorial() {
  renderNav('historial');
  const hidden = getHidden();
  const deleted = getDeleted();
  const list = ARTICLES.filter(a => !deleted.includes(a.id))
    .sort((x,y)=>(y.date_added||'').localeCompare(x.date_added||''));
  const main = document.getElementById('main');
  main.innerHTML = `
    <div class="section-hero"><div><h2>Historial</h2><p>Todo lo que has ido añadiendo, con fecha. Manda a la papelera lo que ya no te interese, y desde ahí restáuralo o bórralo del todo.</p></div></div>
    ${progressPanelHtml(list)}
    <div class="hist-scroll">
      <table class="hist">
        <thead><tr><th>Título</th><th>Sección</th><th>Fecha</th><th></th></tr></thead>
        <tbody id="hist-body"></tbody>
      </table>
    </div>
  `;
  const body = document.getElementById('hist-body');
  body.innerHTML = list.map(a => {
    const sec = bySlug(a.section);
    const isHidden = hidden.includes(a.id);
    const actions = isHidden
      ? `<div class="row-actions">
          <button class="del-btn restore-btn" data-restore="${a.id}" title="Restaurar">${ICONS.restore}</button>
          <button class="del-btn perm-btn" data-perm="${a.id}" title="Eliminar definitivamente">${ICONS.close}</button>
        </div>`
      : `<button class="del-btn" data-del="${a.id}" title="Mover a la papelera">${ICONS.trash}</button>`;
    return `<tr class="${isHidden ? 'hidden-row' : ''}" data-id="${a.id}">
      <td><span class="hist-title" data-open="${a.id}">${a.title}</span>${isHidden ? '<div class="hist-status">En la papelera</div>' : ''}</td>
      <td>${sec ? sec.name : a.section}</td>
      <td>${a.date_added || '—'}</td>
      <td>${actions}</td>
    </tr>`;
  }).join('');

  body.querySelectorAll('[data-open]').forEach(el => el.addEventListener('click', () => { location.hash = '#/articulo/' + el.dataset.open; }));

  body.querySelectorAll('[data-del]').forEach(btn => btn.addEventListener('click', () => {
    const id = btn.dataset.del;
    const h = getHidden();
    if (!h.includes(id)) { h.push(id); setHidden(h); renderHistorial(); }
  }));

  body.querySelectorAll('[data-restore]').forEach(btn => btn.addEventListener('click', () => {
    const id = btn.dataset.restore;
    setHidden(getHidden().filter(x => x !== id));
    renderHistorial();
  }));

  body.querySelectorAll('[data-perm]').forEach(btn => btn.addEventListener('click', () => {
    const id = btn.dataset.perm;
    const a = ARTICLES.find(x => x.id === id);
    if (!confirm(`¿Eliminar definitivamente "${a.title}"? Esto lo borra también del disco.`)) return;
    const d = getDeleted();
    if (!d.includes(id)) { d.push(id); setDeleted(d); }
    setHidden(getHidden().filter(x => x !== id));
    renderHistorial();
    showToast(a);
  }));
}

function showToast(article) {
  const toast = document.getElementById('toast');
  const phrase = `Elimina definitivamente el artículo: "${article.title}" (id: ${article.id})`;
  toast.innerHTML = `Ya no aparece en el sitio. Para borrarlo también del disco (el .md, sus imágenes y la entrada del índice), pídeselo a Claude en el chat.
    <button id="copy-phrase">Copiar frase</button>`;
  toast.style.display = 'block';
  document.getElementById('copy-phrase').addEventListener('click', () => {
    navigator.clipboard && navigator.clipboard.writeText(phrase);
  });
  clearTimeout(window.__toastTimer);
  window.__toastTimer = setTimeout(() => { toast.style.display = 'none'; }, 6000);
}

/* ---------- materiales incluidos (artículos de la sección Materials) ---------- */
function materialsHtml(a) {
  if (!a.materials || !a.materials.length) return '';
  const items = a.materials.map(m => `
    <div class="material-item">
      <div class="material-head">
        <span class="material-name">${m.name || ''}</span>
        ${m.tag ? `<span class="material-tag">${m.tag}</span>` : ''}
      </div>
      ${m.description ? `<p class="material-desc">${m.description}</p>` : ''}
      ${m.install ? `<code class="material-cmd" data-copy="${m.install.replace(/"/g, '&quot;')}" title="Copiar comando">${m.install}</code>` : ''}
      ${m.url ? `<a class="material-link" href="${m.url}" target="_blank" rel="noopener">Ver material ${ICONS.arrow}</a>` : ''}
    </div>
  `).join('');
  return `<div class="art-materials"><h4>${ICONS.materials} Materiales incluidos</h4><div class="materials-list">${items}</div></div>`;
}

function glossaryHtml(a) {
  if (!a.glossary || !a.glossary.length) return '';
  const liked = getLikedTerms();
  const items = a.glossary.map((g, idx) => {
    if (a.dictionary) {
      return `<div class="glossary-item">
        <div class="gterm"><b>${g.term}</b><span>${g.definition}</span></div>
        <div class="dict-badge">${ICONS.book} En Enciclopedia</div>
      </div>`;
    }
    const key = termKey(a.id, idx);
    const isLiked = liked.includes(key);
    return `<div class="glossary-item">
      <div class="gterm"><b>${g.term}</b><span>${g.definition}</span></div>
      <button class="like-btn ${isLiked ? 'liked' : ''}" data-term-key="${key}" title="Guardar en Enciclopedia">${isLiked ? ICONS['heart-filled'] : ICONS.heart}</button>
    </div>`;
  }).join('');
  return `<div class="art-glossary"><h4>Para aprender</h4>${items}</div>`;
}

function renderArticleOverlay(id) {
  const a = ARTICLES.find(x => x.id === id);
  const overlay = document.getElementById('overlay');
  const inner = document.getElementById('overlay-inner');
  if (!a) { overlay.classList.remove('open'); return; }
  const sec = bySlug(a.section);
  const hasCover = a.images && a.images.length;
  const coverWrap = document.getElementById('art-cover-wrap');
  coverWrap.innerHTML = hasCover ? `<img src="${a.images[0]}" alt="" loading="lazy">` : '';
  coverWrap.style.display = hasCover ? '' : 'none';
  inner.classList.toggle('has-cover', !!hasCover);
  inner.innerHTML = `
    <div class="art-icon">${articleIconSvg(a)}</div>
    <div class="art-tag">${sec ? sec.name : a.section}${a.subsection ? ' · ' + a.subsection : ''}</div>
    <h1 class="art-title">${a.title}</h1>
    <div class="art-meta mono">
      <span>Añadido el ${a.date_added || '—'}</span>
      ${a.url ? `<a class="art-original-inline" href="${a.url}" target="_blank" rel="noopener">${ICONS.link} Leer el artículo original</a>` : ''}
    </div>
    <div class="art-body">${mdToHtml(a.content_md || a.summary, a.annotations)}</div>
    ${materialsHtml(a)}
    ${reflectionsHtml(a)}
    ${glossaryHtml(a)}
    ${relatedHtml(a)}
  `;
  inner.querySelectorAll('[data-term-key]').forEach(btn => btn.addEventListener('click', () => {
    const nowLiked = toggleLikedTerm(btn.dataset.termKey);
    btn.classList.toggle('liked', nowLiked);
    btn.innerHTML = nowLiked ? ICONS['heart-filled'] : ICONS.heart;
  }));
  inner.querySelectorAll('[data-copy]').forEach(el => el.addEventListener('click', () => {
    const text = el.getAttribute('data-copy');
    if (navigator.clipboard) navigator.clipboard.writeText(text);
    el.classList.add('copied');
    if (el.classList.contains('code-block')) {
      // bloques largos ya muestran "Copiado ✓" en su propia etiqueta de la esquina
      setTimeout(() => el.classList.remove('copied'), 1400);
    } else {
      const original = el.textContent;
      el.textContent = 'Copiado ✓';
      setTimeout(() => { el.classList.remove('copied'); el.textContent = original; }, 1400);
    }
  }));
  wireAnnotations(a);
  overlay.classList.add('open');
  window.scrollTo(0,0);
}

/* click en una cita subrayada -> abre uno (o dos, si coinciden ampliación + ejemplo)
   post-it pegados justo debajo, dentro del propio artículo — nada de fondo oscuro; se
   cierran solo con su X, y se mueven con el texto al hacer scroll */
function closeAnnotNotesFor(mark) {
  const inner = mark.closest('#overlay-inner');
  if (!inner) return;
  inner.querySelectorAll(`.annot-note[data-for-mark="${mark.dataset.annotIdxs}"]`).forEach(n => n.remove());
  mark.classList.remove('open');
}

function wireAnnotations(a) {
  const inner = document.getElementById('overlay-inner');
  if (!inner) return;
  inner.querySelectorAll('.annot').forEach(mark => {
    mark.addEventListener('click', () => {
      if (mark.classList.contains('open')) { closeAnnotNotesFor(mark); return; }

      const idxs = mark.dataset.annotIdxs.split(',').map(Number);
      const NOTE_W = 340, STACK_DX = 64, STACK_DY = 46;
      const containerRect = inner.getBoundingClientRect();
      const markRect = mark.getBoundingClientRect();
      const top = markRect.bottom - containerRect.top + 10;
      const left = Math.max(0, Math.min(markRect.left - containerRect.left, inner.clientWidth - NOTE_W - STACK_DX));

      idxs.forEach((idx, i) => {
        const an = (a.annotations || [])[idx];
        if (!an) return;
        const meta = ANNOT_META[an.type] || ANNOT_META.ampliacion;
        const note = document.createElement('div');
        note.className = `annot-note annot-note-${an.type} ${i === 1 ? 'stack-2' : ''}`;
        note.dataset.forMark = mark.dataset.annotIdxs;
        note.style.top = (top + i * STACK_DY) + 'px';
        note.style.left = (left + i * STACK_DX) + 'px';
        note.innerHTML = `
          <button class="annot-note-close">${ICONS.close}</button>
          <span class="annot-note-label">${ICONS[meta.icon]} ${meta.label}</span>
          <span class="annot-note-text">${an.text}</span>
        `;
        inner.appendChild(note);
        note.querySelector('.annot-note-close').addEventListener('click', () => closeAnnotNotesFor(mark));
        // tocar un post-it (fuera de su X) lo trae al frente de la pila, como uno real
        note.addEventListener('click', e => {
          if (e.target.closest('.annot-note-close')) return;
          inner.appendChild(note);
        });
      });
      mark.classList.add('open');
    });
  });
}
document.addEventListener('keydown', e => {
  if (e.key !== 'Escape') return;
  document.querySelectorAll('.annot-note').forEach(n => n.remove());
  document.querySelectorAll('.annot.open').forEach(m => m.classList.remove('open'));
});

/* ---------- repaso espaciado (sistema Leitner, 5 cajas) ---------- */
const SRS_BOX_DAYS = { 1: 1, 2: 3, 3: 7, 4: 14, 5: 30 };
function getSRS() { try { return JSON.parse(localStorage.getItem('termSRS') || '{}'); } catch(e) { return {}; } }
function setSRS(obj) { localStorage.setItem('termSRS', JSON.stringify(obj)); }
function todayISO() { return new Date().toISOString().slice(0,10); }

function termsDue(terms) {
  const srs = getSRS();
  return terms.filter(t => {
    const s = srs[t.key];
    return !s || s.due <= todayISO();
  });
}

function reviewTerm(key, knewIt) {
  const srs = getSRS();
  const cur = srs[key] || { box: 0, due: todayISO() };
  const box = knewIt ? Math.min(5, cur.box + 1) : 1;
  const due = new Date();
  due.setDate(due.getDate() + SRS_BOX_DAYS[box]);
  srs[key] = { box, due: due.toISOString().slice(0,10) };
  setSRS(srs);
}

/* ---------- modal de flashcards ---------- */
const flashState = { queue: [], index: 0, revealed: false };

function openFlashModal(allTerms) {
  flashState.queue = termsDue(allTerms);
  flashState.index = 0;
  flashState.revealed = false;
  document.getElementById('flash-modal').classList.add('open');
  paintFlashCard();
}
function closeFlashModal() {
  document.getElementById('flash-modal').classList.remove('open');
  renderEnciclopedia(); // refresca el contador de "Repasar (N)"
}

function paintFlashCard() {
  const wrap = document.getElementById('flash-modal-body');
  const { queue, index, revealed } = flashState;
  if (index >= queue.length) {
    wrap.innerHTML = `<div class="flash-done">
      ${ICONS['star-filled']}
      <p>${queue.length ? '¡Repaso completo!' : 'Estás al día — no hay términos pendientes de repaso.'}</p>
      <button class="review-btn" id="flash-close-btn">Cerrar</button>
    </div>`;
    document.getElementById('flash-close-btn').addEventListener('click', closeFlashModal);
    return;
  }
  const t = queue[index];
  wrap.innerHTML = `
    <div class="flash-progress">${index + 1} / ${queue.length}</div>
    <div class="flash-card ${revealed ? 'revealed' : ''}" id="flash-card">
      <div class="flash-term">${t.term}</div>
      ${revealed ? `
        <p class="flash-def">${t.definition}</p>
        <a class="src" data-open="${t.articleId}">De: ${t.articleTitle}</a>
      ` : `<div class="flash-tap">Toca para ver la definición</div>`}
    </div>
    ${revealed ? `
      <div class="flash-actions">
        <button class="flash-no" id="flash-no">No me acordaba</button>
        <button class="flash-yes" id="flash-yes">${ICONS.check} Lo sabía</button>
      </div>
    ` : ''}
  `;
  if (!revealed) {
    document.getElementById('flash-card').addEventListener('click', () => { flashState.revealed = true; paintFlashCard(); });
  } else {
    document.getElementById('flash-no').addEventListener('click', () => { reviewTerm(t.key, false); flashState.index++; flashState.revealed = false; paintFlashCard(); });
    document.getElementById('flash-yes').addEventListener('click', () => { reviewTerm(t.key, true); flashState.index++; flashState.revealed = false; paintFlashCard(); });
    wrap.querySelector('[data-open]').addEventListener('click', e => { e.stopPropagation(); location.hash = '#/articulo/' + t.articleId; });
  }
}

function encyLetterOf(term) {
  let l = (term || '?').trim().charAt(0).toUpperCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  return /[A-Z]/.test(l) ? l : '#';
}

function buildEncyTerms() {
  const liked = getLikedTerms();
  const terms = [];
  ARTICLES.forEach(a => {
    (a.glossary || []).forEach((g, idx) => {
      const key = termKey(a.id, idx);
      if (a.dictionary || liked.includes(key)) terms.push({ ...g, key, articleId: a.id, articleTitle: a.title });
    });
  });
  terms.sort((x, y) => x.term.localeCompare(y.term, 'es', { sensitivity: 'base' }));
  return terms;
}

function encyTabsHtml(view) {
  return `<div class="subnav ency-tabs">
    <a href="#/enciclopedia" class="subnav-pill ${view === 'terminos' ? 'active' : ''}">Términos</a>
    <a href="#/enciclopedia/comandos" class="subnav-pill ${view === 'comandos' ? 'active' : ''}">Claude Commands</a>
  </div>`;
}

function renderEnciclopedia(view) {
  view = view === 'comandos' ? 'comandos' : 'terminos';
  renderNav('enciclopedia');
  const main = document.getElementById('main');

  if (view === 'comandos') {
    main.innerHTML = `
      <div class="section-hero"><div><h2>Enciclopedia</h2><p>Comandos de Claude que merece la pena tener a mano, con ejemplo y notas.</p></div></div>
      ${encyTabsHtml(view)}
      <div id="cmd-out"></div>
    `;
    renderComandos();
    return;
  }

  const terms = buildEncyTerms();
  const due = termsDue(terms);
  const banner = terms.length ? `
    <div class="ency-review-banner">
      <div class="ency-review-banner-text">
        <strong>${due.length ? 'Se olvida lo que no se repasa' : 'Al día. Por ahora.'}</strong>
        <span>${due.length ? `${due.length} término${due.length === 1 ? '' : 's'} esperando` : 'Vuelve cuando el olvido llame a la puerta'}</span>
      </div>
      <button class="review-cta" id="ency-review-btn">${ICONS.cards} Repasar${due.length ? ` (${due.length})` : ''}</button>
    </div>` : '';

  main.innerHTML = `
    <div class="section-hero"><div><h2>Enciclopedia</h2><p>Los términos que te ha interesado guardar, con su definición y de dónde salieron.</p></div></div>
    ${encyTabsHtml(view)}
    ${banner}
    <div id="ency-out"></div>
  `;
  if (terms.length) document.getElementById('ency-review-btn').addEventListener('click', () => openFlashModal(terms));

  const out = document.getElementById('ency-out');
  if (!terms.length) {
    out.innerHTML = `<div class="empty">Aún no has guardado ningún término. Dale a ${ICONS.heart} en los términos nuevos que veas dentro de un artículo.</div>`;
    return;
  }

  out.innerHTML = `
    <div class="ency-toolbar">
      <div class="ency-search-row">${ICONS.search}<input type="text" id="ency-search" placeholder="Buscar en la Enciclopedia..." autocomplete="off"></div>
    </div>
    <div class="ency-layout">
      <div class="ency-list" id="ency-list"></div>
      <div class="ency-index" id="ency-index"></div>
    </div>
  `;
  document.getElementById('ency-search').addEventListener('input', e => paintEncyList(terms, e.target.value));
  paintEncyList(terms, '');

  if (window.__pendingReviewOpen) {
    window.__pendingReviewOpen = false;
    openFlashModal(terms);
  }
}

/* ---------- Claude Commands (pestaña de consulta dentro de Enciclopedia) ---------- */
const cmdState = { groupBy: 'categoria', query: '' };

function renderComandos() {
  const out = document.getElementById('cmd-out');
  if (!COMMANDS.length) {
    out.innerHTML = `<div class="empty">Aún no hay comandos guardados aquí.</div>`;
    return;
  }
  out.innerHTML = `
    <div class="ency-toolbar">
      <div class="ency-search-row">${ICONS.search}<input type="text" id="cmd-search" placeholder="Buscar comandos..." autocomplete="off"></div>
      <div class="subnav" style="margin:0;">
        <button class="subnav-pill ${cmdState.groupBy === 'categoria' ? 'active' : ''}" data-group="categoria">Por categoría</button>
        <button class="subnav-pill ${cmdState.groupBy === 'az' ? 'active' : ''}" data-group="az">A-Z</button>
      </div>
    </div>
    <div class="ency-layout">
      <div class="ency-list" id="cmd-list"></div>
      <div class="ency-index" id="cmd-index"></div>
    </div>
  `;
  const searchInput = document.getElementById('cmd-search');
  searchInput.value = cmdState.query;
  searchInput.addEventListener('input', e => { cmdState.query = e.target.value; paintCommandsList(); });
  out.querySelectorAll('[data-group]').forEach(btn => {
    btn.addEventListener('click', () => { cmdState.groupBy = btn.dataset.group; renderComandos(); });
  });
  paintCommandsList();
}

function cmdRowHtml(c) {
  return `<div class="cmd-row">
    <div class="cmd-row-head"><b class="cmd-name">${escapeHtml(c.name)}</b><span class="cmd-tag">${escapeHtml(c.category)}</span></div>
    <p class="cmd-desc">${escapeHtml(c.description)}</p>
    ${c.example ? `<pre class="cmd-example">${escapeHtml(c.example)}</pre>` : ''}
    ${c.notes ? `<p class="cmd-notes">${escapeHtml(c.notes)}</p>` : ''}
  </div>`;
}

function paintCommandsList() {
  const q = (cmdState.query || '').trim().toLowerCase();
  const filtered = q
    ? COMMANDS.filter(c => (c.name + ' ' + c.description + ' ' + (c.notes || '') + ' ' + c.category).toLowerCase().includes(q))
    : COMMANDS;

  const list = document.getElementById('cmd-list');
  const index = document.getElementById('cmd-index');
  if (!list || !index) return;

  if (window.__cmdObserver) { window.__cmdObserver.disconnect(); window.__cmdObserver = null; }

  if (!filtered.length) {
    list.innerHTML = `<div class="empty">Sin resultados para "${escapeHtml(cmdState.query)}".</div>`;
    index.innerHTML = '';
    return;
  }

  const keyOf = c => cmdState.groupBy === 'az' ? encyLetterOf(c.name.replace(/^\//, '')) : (c.category || 'Otros');
  const groups = {};
  filtered.forEach(c => { const k = keyOf(c); (groups[k] = groups[k] || []).push(c); });
  const keys = Object.keys(groups).sort((a, b) => a.localeCompare(b, 'es', { sensitivity: 'base' }));

  list.innerHTML = keys.map((k, i) => `
    <div class="ency-letter-group">
      <div class="cmd-group-heading" id="cmd-group-${i}" data-idx="${i}">${escapeHtml(k)}</div>
      <div class="ency-vlist">${groups[k].map(cmdRowHtml).join('')}</div>
    </div>
  `).join('');

  index.innerHTML = keys.map((k, i) => `<a href="#cmd-group-${i}" data-idx="${i}" class="${i === 0 ? 'active' : ''}">${escapeHtml(k)}</a>`).join('');

  index.querySelectorAll('a').forEach(a => a.addEventListener('click', e => {
    e.preventDefault();
    const target = document.getElementById(`cmd-group-${a.dataset.idx}`);
    if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }));

  const headers = list.querySelectorAll('.cmd-group-heading');
  const indexLinks = index.querySelectorAll('a');
  const obs = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (en.isIntersecting) {
        indexLinks.forEach(a => a.classList.toggle('active', a.dataset.idx === en.target.dataset.idx));
      }
    });
  }, { rootMargin: '-15% 0px -75% 0px', threshold: 0 });
  headers.forEach(h => obs.observe(h));
  window.__cmdObserver = obs;
}

function paintEncyList(terms, query) {
  const q = (query || '').trim().toLowerCase();
  const filtered = q ? terms.filter(t => (t.term + ' ' + t.definition).toLowerCase().includes(q)) : terms;

  const list = document.getElementById('ency-list');
  const index = document.getElementById('ency-index');
  if (!list || !index) return;

  if (window.__encyObserver) { window.__encyObserver.disconnect(); window.__encyObserver = null; }

  if (!filtered.length) {
    list.innerHTML = `<div class="empty">Sin resultados para "${query}".</div>`;
    index.innerHTML = '';
    return;
  }

  const groups = {};
  filtered.forEach(t => { const l = encyLetterOf(t.term); (groups[l] = groups[l] || []).push(t); });
  const letters = Object.keys(groups).sort();

  list.innerHTML = letters.map(l => `
    <div class="ency-letter-group">
      <div class="ency-letter-heading" id="ency-letter-${l}" data-letter="${l}">${l}</div>
      <div class="ency-vlist">${groups[l].map(t => `
        <div class="ency-row">
          <b>${t.term}</b>
          <p>${t.definition}</p>
          <a class="src" data-open="${t.articleId}">De: ${t.articleTitle}</a>
        </div>
      `).join('')}</div>
    </div>
  `).join('');

  index.innerHTML = letters.map((l, i) => `<a href="#ency-letter-${l}" data-letter="${l}" class="${i === 0 ? 'active' : ''}">${l}</a>`).join('');

  list.querySelectorAll('[data-open]').forEach(el => el.addEventListener('click', () => { location.hash = '#/articulo/' + el.dataset.open; }));
  index.querySelectorAll('a').forEach(a => a.addEventListener('click', e => {
    e.preventDefault();
    const target = document.getElementById(`ency-letter-${a.dataset.letter}`);
    if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }));

  const headers = list.querySelectorAll('.ency-letter-heading');
  const indexLinks = index.querySelectorAll('a');
  const obs = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (en.isIntersecting) {
        indexLinks.forEach(a => a.classList.toggle('active', a.dataset.letter === en.target.dataset.letter));
      }
    });
  }, { rootMargin: '-15% 0px -75% 0px', threshold: 0 });
  headers.forEach(h => obs.observe(h));
  window.__encyObserver = obs;
}

document.getElementById('close-overlay').innerHTML = ICONS.close;
document.getElementById('close-overlay').addEventListener('click', () => { history.back(); });
document.addEventListener('keydown', e => { if (e.key === 'Escape') { const o=document.getElementById('overlay'); if (o.classList.contains('open')) history.back(); } });


/* ---------- wiring del modal de flashcards ---------- */
document.getElementById('flash-modal-close').innerHTML = ICONS.close;
document.getElementById('flash-modal-close').addEventListener('click', closeFlashModal);
document.getElementById('flash-modal').addEventListener('click', e => { if (e.target.id === 'flash-modal') closeFlashModal(); });
document.addEventListener('keydown', e => { if (e.key === 'Escape' && document.getElementById('flash-modal').classList.contains('open')) closeFlashModal(); });

/* ---------- spotlight search ---------- */
document.getElementById('spotlight-icon').innerHTML = ICONS.search;
let spotlightSel = 0;

function spotlightMatches(q) {
  q = (q || '').trim().toLowerCase();
  const list = visibleArticles();
  if (!q) {
    return list.slice().sort((a,b)=>(b.date_added||'').localeCompare(a.date_added||'')).slice(0, 6);
  }
  return list.filter(a => {
    const haystack = (a.title + ' ' + a.summary + ' ' + (a.key_points||[]).join(' ') + ' ' + (a.subsection||'')).toLowerCase();
    return haystack.includes(q);
  }).slice(0, 8);
}

function renderSpotlightResults(q) {
  const results = spotlightMatches(q);
  const out = document.getElementById('spotlight-results');
  spotlightSel = 0;
  if (!results.length) {
    out.innerHTML = `<div class="spotlight-empty">Sin resultados para "${q}".</div>`;
    return;
  }
  out.innerHTML = results.map((a, i) => {
    const sec = bySlug(a.section);
    return `<a class="spotlight-item ${i===0?'sel':''}" href="#/articulo/${a.id}" data-idx="${i}">
      <div class="icon">${sec ? ICONS[sec.icon] : ''}</div>
      <div class="meta"><b>${a.title}</b><span>${sec ? sec.name : a.section}${a.subsection ? ' · ' + a.subsection : ''}</span></div>
    </a>`;
  }).join('');
  out.querySelectorAll('.spotlight-item').forEach(el => el.addEventListener('click', closeSpotlight));
}

function openSpotlight() {
  document.getElementById('spotlight').classList.add('open');
  const input = document.getElementById('spotlight-input');
  input.value = '';
  renderSpotlightResults('');
  setTimeout(() => input.focus(), 10);
}
function closeSpotlight() {
  document.getElementById('spotlight').classList.remove('open');
}

document.getElementById('spotlight-input').addEventListener('input', e => renderSpotlightResults(e.target.value));
document.getElementById('spotlight').addEventListener('click', e => { if (e.target.id === 'spotlight') closeSpotlight(); });
document.getElementById('spotlight-input').addEventListener('keydown', e => {
  const items = Array.from(document.querySelectorAll('.spotlight-item'));
  if (!items.length) return;
  if (e.key === 'ArrowDown') {
    e.preventDefault();
    spotlightSel = Math.min(spotlightSel + 1, items.length - 1);
    items.forEach((it,i) => it.classList.toggle('sel', i === spotlightSel));
    items[spotlightSel].scrollIntoView({ block: 'nearest' });
  } else if (e.key === 'ArrowUp') {
    e.preventDefault();
    spotlightSel = Math.max(spotlightSel - 1, 0);
    items.forEach((it,i) => it.classList.toggle('sel', i === spotlightSel));
    items[spotlightSel].scrollIntoView({ block: 'nearest' });
  } else if (e.key === 'Enter') {
    e.preventDefault();
    items[spotlightSel].click();
  }
});
document.addEventListener('keydown', e => {
  if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); openSpotlight(); }
  else if (e.key === 'Escape' && document.getElementById('spotlight').classList.contains('open')) { closeSpotlight(); }
});

/* ---------- router ---------- */
function route() {
  const hash = location.hash || '#/';
  const overlay = document.getElementById('overlay');
  closeSpotlight();
  clearHeroTimer();
  const m = hash.match(/^#\/articulo\/(.+)$/);
  if (m) { renderArticleOverlay(decodeURIComponent(m[1])); return; }
  overlay.classList.remove('open');

  if (hash === '#/' || hash === '') { renderPortada(); return; }
  if (hash === '#/historial') { renderHistorial(); return; }
  if (hash === '#/enciclopedia') { renderEnciclopedia('terminos'); return; }
  if (hash === '#/enciclopedia/comandos') { renderEnciclopedia('comandos'); return; }
  const sm = hash.match(/^#\/(.+)$/);
  if (sm && bySlug(sm[1])) { renderSection(sm[1]); return; }
  renderPortada();
}
window.addEventListener('hashchange', route);
renderLiveKicker();
renderSubtitle();
renderTicker();
renderFooter();
route();
</script>
</body>
</html>
"""

html = (TEMPLATE
        .replace("__ARTICLES_JSON__", data_json)
        .replace("__COMMANDS_JSON__", commands_json)
        .replace("__SECTIONS_JSON__", sections_json)
        .replace("__ICONS_JSON__", icons_json)
        .replace("__ARTICLE_ICONS_JSON__", article_icons_json))

with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Built {OUT_FILE} with {len(articles)} articles across {len(SECTIONS)} sections")
