import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE, "data", "articles.json")
OUT_FILE = os.path.join(BASE, "index.html")

with open(DATA_FILE, encoding="utf-8") as f:
    articles = json.load(f)

SECTIONS = [
    {
        "slug": "design-2-0",
        "name": "Design 2.0",
        "desc": "Cómo está cambiando la disciplina del diseño en la era de la IA: nuevos flujos, nuevas habilidades, principios que siguen mandando.",
        "icon": "design-2-0",
    },
    {
        "slug": "claude",
        "name": "Claude",
        "desc": "Guías, features y forma de trabajar específicas de Claude: agentes, contexto, límites de uso, Claude Code.",
        "icon": "claude",
    },
    {
        "slug": "figma",
        "name": "Figma",
        "desc": "Novedades, plugins y funciones de Figma, incluido todo lo que toca IA dentro de la propia herramienta.",
        "icon": "layers",
    },
    {
        "slug": "engineering",
        "name": "Engineering",
        "desc": "Cómo colaborar mejor con developers: procesos, cultura, expectativas y lenguaje común.",
        "icon": "chat-code",
    },
    {
        "slug": "ai",
        "name": "AI",
        "desc": "Conceptos e IA en general, más allá de Claude: fundamentos, modelos, terminología de referencia.",
        "icon": "chip",
    },
    {
        "slug": "materials",
        "name": "Materials",
        "desc": "Skills, plantillas, repos y otros recursos descargables que vienen incluidos en un artículo, listos para usar.",
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
PIXEL12 = {'close': ['##........##', '###......###', '.###....###.', '..###..###..', '...######...', '....####....', '....####....', '...######...', '..###..###..', '.###....###.', '###......###', '##........##'], 'check': ['............', '............', '...........#', '..........##', '.........##.', '#.......##..', '##.....##...', '.##...##....', '..##.##.....', '...###......', '....#.......', '............'], 'trash': ['...######...', '..#......#..', '.##########.', '..#.####.#..', '..#.####.#..', '..#.####.#..', '..#.####.#..', '..#.####.#..', '..#.####.#..', '..#.####.#..', '..#......#..', '...######...'], 'restore': ['............', '............', '....####.##.', '...#....#.#.', '..#......#..', '..#.........', '..#.........', '..#.........', '...#........', '....####....', '............', '............'], 'star': ['.....#......', '....###.....', '....#.#.....', '............', '.##.....##..', '##.......##.', '.##.....##..', '............', '....#.#.....', '....###.....', '.....#......', '............'], 'star-filled': ['.....#......', '....###.....', '....###.....', '....###.....', '.#########..', '###########.', '.#########..', '....###.....', '....###.....', '....###.....', '.....#......', '............'], 'edit': ['.........##.', '........####', '.......###..', '......###...', '.....###....', '....###.....', '...###......', '..###.......', '.###........', '.##.........', '.#..........', '.##.........'], 'link': ['............', '....#.......', '..#####.....', '..#...#.....', '.##...#.....', '..#...#.#...', '..#########.', '......#...#.', '.....##...#.', '......#...#.', '......####..', '............'], 'cards': ['............', '....#######.', '....#.....#.', '....#.....#.', '.#######..#.', '.#..#..#..#.', '.#..#..#..#.', '.#..#######.', '.#.....#....', '.#.....#....', '.#######....', '............'], 'eye': ['............', '....####....', '..##....##..', '.#........#.', '#....##....#', '#...####...#', '#...####...#', '#....##....#', '.#........#.', '..##....##..', '....####....', '............'], 'chart': ['............', '............', '.........###', '.........###', '.........###', '.....###.###', '.....###.###', '.....###.###', '.###.###.###', '.###.###.###', '.###.###.###', '############'], 'wrench': ['............', '..###.......', '.##.##......', '...###......', '...###......', '...####.....', '.....###....', '......###...', '.......###..', '........###.', '.........###', '..........#.']}

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

# Ilustración pixel-art única por artículo (16x16, más detallada), pensada para el tema concreto de cada uno.
# Los artículos futuros sin entrada aquí caen al icono por keyword/sección (pixelIconFor en JS).
ARTICLE_ICONS_ROWS = {'aprendizaje-por-refuerzo-basico': ['................', '................', '.....######.....', '...##......###..', '...#........#...', '......####...#..', '.....##..##.....', '.....#.##.#.....', '.....#.##.#.....', '.....##..##.....', '..#...####......', '...#........#...', '..###......##...', '.....######.....', '................', '................'], 'meta-abre-astryx-su-design-system-interno-y-ya-funciona-en-figma-make': ['.........####...', '.........####...', '.....########...', '..###########...', '..#.#####.......', '..#######.......', '......#####.....', '....##.....#....', '...#........##..', '..#############.', '..#...........#.', '..#.#########.#.', '..#...........#.', '..#############.', '................', '................'], 'claude-agents-que-son-y-como-crear-uno': ['....#...........', '....#...........', '#########.......', '#.......#.......', '#.##.##.#.......', '#.##.##.#.......', '#.##.##.#.......', '#.......#.......', '#.#####.#...#...', '#########.#####.', '.........#######', '.........##...##', '........###...##', '.........##...##', '.........#######', '..........#####.'], 'donde-va-realmente-tu-contexto-de-diseno-en-claude': ['................', '................', '..############..', '..#.##.....#.#..', '..#..........#..', '..############..', '................', '..############..', '..#.##.....#.#..', '..#..........#..', '..############..', '................', '..############..', '..#.##.....#.#..', '..#..........#..', '..############..'], 'los-disenadores-gastan-los-limites-de-uso-de-claude-mas-rapido-que-nad': ['................', '................', '................', '................', '.############...', '.####...#...#...', '.####..#....###.', '.####..#....###.', '.####.####..###.', '.####...#...###.', '.####...#...#...', '.############...', '................', '................', '................', '................'], 'diccionario-de-ia-para-disenadores': ['...........#....', '...........#....', '.......####.#...', '....###.#.###...', '..##....#....##.', '..#.....#.....#.', '..#.#########.#.', '..#.....#.....#.', '..#.#########.#.', '..#.....#.....#.', '..#.#########.#.', '..#.....#.....#.', '..###...#...###.', '.....#######....', '................', '................'], '5-trucos-para-que-claude-code-no-te-de-un-diseno-web-generico': ['................', '################', '#.#.#.#..#####.#', '#..............#', '################', '#..............#', '#......##......#', '#......##......#', '#....######....#', '#...########...#', '#....######....#', '#......##......#', '#......##......#', '################', '................', '................']}
ARTICLE_ICONS = {aid: pixel_svg(rows) for aid, rows in ARTICLE_ICONS_ROWS.items()}

# Icono de "varita mágica" para el empty state de Últimas entradas (todo revisado / limpio)
ICONS['wand'] = pixel_svg(['............', '............', '.......##...', '......####..', '......####..', '.......##...', '......#.....', '.....#......', '...##.......', '...#........', '..#.........', '.#..........'])

data_json = json.dumps(articles, ensure_ascii=False)
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
  .top-bar { display: flex; align-items: center; justify-content: center; gap: 12px; }

  .live {
    display: flex; align-items: center; gap: 8px;
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
    margin: 14px 0 6px; text-align: center; text-transform: uppercase; line-height: .92;
  }
  h1.title span { display: inline-block; opacity: 0; transform: translateY(18px) rotate(-1deg); animation: riseIn .55s cubic-bezier(.2,.8,.2,1) forwards; }
  h1.title span:nth-child(odd) { color: var(--accent); }
  @keyframes riseIn { to { opacity: 1; transform: translateY(0) rotate(0); } }

  .subtitle {
    color: var(--ink); font-size: 13px; text-align: center; margin-bottom: 18px;
    font-weight: 500;
  }
  .subtitle .phrase { color: var(--muted); font-style: italic; font-weight: 400; }

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
  .ticker span.item { font-family: 'Space Mono', monospace; font-size: 12px; letter-spacing: .5px; padding: 0 22px; color: var(--muted); }
  .ticker span.item b { color: var(--ink); font-weight: 700; }
  .ticker span.item.empty-msg { color: var(--ink); font-weight: 700; }
  .ticker.empty-state .ticker-track { animation: none; padding: 8px 22px; }
  @keyframes scrollTicker { from { transform: translateX(0); } to { transform: translateX(-50%); } }

  .ticker-badge {
    position: absolute; top: -30px; left: 18px; width: 76px; height: 76px;
    z-index: 3; pointer-events: none; display: flex; align-items: center; justify-content: center;
    animation: burstWiggle 2.6s ease-in-out infinite;
  }
  .ticker-badge svg.burst { position: absolute; inset: 0; width: 100%; height: 100%; overflow: visible; }
  .ticker-badge span {
    position: relative; transform: rotate(5deg);
    font-family: 'Space Mono', monospace; font-size: 10.5px; font-weight: 700;
    letter-spacing: .5px; text-transform: uppercase; color: #fff; text-align: center; line-height: 1.15;
  }
  @keyframes burstWiggle {
    0%, 100% { transform: rotate(-9deg); }
    50% { transform: rotate(-3deg); }
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
    display: flex; align-items: stretch;
    flex-wrap: nowrap;
  }
  .links-wrap { flex: 1; min-width: 0; display: flex; align-items: stretch; position: relative; }
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
  nav.sections .hist-link {
    display: flex; align-items: center; gap: 6px; border-left: 2px solid var(--ink);
    padding: 0 18px; font-family: 'Space Mono', monospace; font-size: 11px; letter-spacing: 1px;
    text-transform: uppercase; text-decoration: none; color: var(--ink); font-weight: 700;
  }
  nav.sections .hist-link svg { width: 15px; height: 15px; }
  nav.sections .hist-link:hover { color: var(--accent); }
  nav.sections .hist-link.active { color: var(--accent); }
  nav.sections .hist-link.icon-only { padding: 0 20px; }
  nav.sections .hist-link.icon-only svg { width: 18px; height: 18px; }

  .nav-icon-btn {
    flex: none; display: flex; align-items: center; justify-content: center;
    border: none; border-right: 2px solid var(--ink); background: transparent;
    color: var(--ink); cursor: pointer; padding: 0 18px;
  }
  .nav-icon-btn svg { width: 16px; height: 16px; }
  .nav-icon-btn:hover { color: var(--accent); }

  .streak-nav {
    position: relative; display: flex; align-items: center; gap: 5px; border-left: 2px solid var(--ink);
    padding: 0 16px; font-family: 'Space Mono', monospace; font-size: 11px; letter-spacing: .5px;
    color: var(--muted); cursor: default;
  }
  .streak-nav svg { width: 13px; height: 13px; color: var(--accent); }
  .streak-nav:hover { color: var(--ink); }
  .streak-tooltip {
    position: absolute; top: calc(100% + 10px); right: 0; background: var(--ink); color: #fff;
    padding: 10px 14px; font-family: 'Space Mono', monospace; font-size: 11px; line-height: 1.5;
    white-space: nowrap; opacity: 0; pointer-events: none; transform: translateY(-4px);
    transition: opacity .15s ease, transform .15s ease; z-index: 20;
  }
  .streak-tooltip::after {
    content: ""; position: absolute; bottom: 100%; right: 16px; border: 6px solid transparent;
    border-bottom-color: var(--ink);
  }
  .streak-tooltip .tt-phrase { color: var(--accent); }
  .streak-nav:hover .streak-tooltip { opacity: 1; transform: translateY(0); pointer-events: auto; }

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
  /* ---- Nota propia (artículo) ---- */
  .art-note { margin-top: 32px; padding: 18px 20px; background: rgba(255,90,31,0.05); border: 2px dashed var(--accent); }
  .art-note h4 { display: flex; align-items: center; gap: 8px; margin: 0 0 6px; font-family: 'Space Mono', monospace; font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase; color: var(--accent); }
  .art-note h4 svg { width: 14px; height: 14px; }
  .note-hint { margin: 0 0 10px; font-size: 12.5px; color: var(--muted); line-height: 1.5; }
  .art-note textarea {
    width: 100%; min-height: 84px; resize: vertical; border: 2px solid var(--ink); background: var(--bg);
    font-family: 'Space Grotesk', sans-serif; font-size: 14.5px; line-height: 1.5; color: var(--ink);
    padding: 10px 12px; outline: none;
  }
  .art-note textarea:focus { border-color: var(--accent); }
  .note-status { font-family: 'Space Mono', monospace; font-size: 10.5px; color: var(--accent); height: 14px; margin-top: 6px; }

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
  .flash-yes { background: var(--ink); color: #fff; }
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
  .section-hero { display: flex; align-items: center; gap: 16px; padding: 30px 0 10px; }
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

  /* ---- Fila superior: titular manda, últimas entradas es columna pequeña ---- */
  .front-top { display: grid; grid-template-columns: 2.3fr 1fr; gap: 26px; align-items: start; margin-top: 4px; }
  .front-top.no-lead { display: block; }
  .front-lead .fp-hero .fp-img { height: 320px; }
  .front-lead .fp-hero .fp-body { padding: 20px 22px; gap: 8px; }
  .front-lead .fp-hero h2 { font-size: 36px; }
  .front-lead .fp-hero p { font-size: 15px; }
  .front-briefs-col .front-label { margin-top: 0; }

  /* ---- Controles del carrusel de 5★ (debajo del titular) ---- */
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
    width: 9px; height: 9px; border-radius: 50%; background: #ddd; border: 2px solid var(--ink);
    padding: 0; cursor: pointer;
  }
  .lead-dot.on { background: var(--accent); border-color: var(--accent); }

  /* ---- Titular sin imagen: icono de sección, sin bloque gris ---- */
  .lead-icon { width: 52px; height: 52px; color: var(--ink); margin-bottom: 4px; image-rendering: pixelated; }
  .lead-icon svg { width: 100%; height: 100%; shape-rendering: crispEdges; }

  /* ---- Apuntes (los 2 siguientes más recientes), en fila debajo ---- */
  .front-picks { display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; margin-top: 14px; }
  .picks-subsection:first-of-type .subsection-title { margin-top: 20px; }
  .front-pick {
    display: flex; gap: 0; text-decoration: none; color: var(--ink); height: 96px;
    border: 2px solid var(--ink); position: relative; transition: border-color .15s ease;
  }
  .front-pick:hover { border-color: var(--accent); }
  .front-pick:hover h3 { color: var(--accent); }
  .front-pick .fp-img, .front-pick .fp-noimg { width: 96px; flex: none; border-right: 2px solid var(--ink); object-fit: cover; height: 100%; }
  .front-pick .fp-noimg { display: flex; align-items: center; justify-content: center; background: #f2f2f2; }
  .front-pick .fp-noimg svg { width: 26px; height: 26px; color: var(--ink); opacity: .5; }
  .front-pick .pick-body { padding: 10px 14px; display: flex; flex-direction: column; justify-content: center; gap: 5px; min-width: 0; }
  .front-pick .pick-tag { font-family: 'Space Mono', monospace; font-size: 9px; letter-spacing: .6px; text-transform: uppercase; color: var(--accent); font-weight: 700; }
  .front-pick h3 {
    margin: 0; font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 14.5px; line-height: 1.28;
    display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; transition: color .15s ease;
  }

  /* ---- Empty state de "Últimas entradas" ---- */
  .briefs-empty {
    border: 2px dashed var(--ink); padding: 26px 18px; text-align: center;
    display: flex; flex-direction: column; align-items: center; gap: 10px; min-height: 180px; justify-content: center;
  }
  .briefs-empty-icon { width: 26px; height: 26px; color: var(--accent); opacity: .55; }
  .briefs-empty-icon svg { width: 100%; height: 100%; }
  .briefs-empty p { margin: 0; font-size: 13px; line-height: 1.5; font-weight: 700; color: var(--ink); }
  .briefs-empty .briefs-empty-sub { font-weight: 400; color: var(--muted); font-size: 12px; }

  /* ---- Breves: columna angosta, título en varias líneas ---- */
  .front-briefs { border-top: 3px solid var(--ink); }
  .brief-row {
    display: flex; flex-direction: column; align-items: flex-start; gap: 7px; padding: 13px 2px; border-bottom: 1px solid #ddd;
    text-decoration: none; color: var(--ink);
  }
  .brief-row:hover { background: rgba(255,90,31,0.06); }
  .brief-row:hover .brief-title { color: var(--accent); }
  .brief-stamp {
    flex: none; font-family: 'Space Mono', monospace; font-size: 9px; font-weight: 700; letter-spacing: .8px; text-transform: uppercase;
    border: 2px solid var(--ink); padding: 4px 8px; background: var(--bg); transform: rotate(-3deg);
    transition: background .18s ease, color .18s ease, border-color .18s ease;
  }
  .brief-row:nth-child(3n+2) .brief-stamp { transform: rotate(2deg); }
  .brief-row:nth-child(3n) .brief-stamp { transform: rotate(-1.5deg); }
  .brief-row:hover .brief-stamp {
    background: var(--accent); border-color: var(--accent); color: #fff;
    animation: stampWiggle .45s ease;
  }
  @keyframes stampWiggle {
    0% { transform: rotate(-3deg) scale(1); }
    35% { transform: rotate(-9deg) scale(1.1); }
    65% { transform: rotate(6deg) scale(1.1); }
    100% { transform: rotate(-2deg) scale(1.05); }
  }
  .brief-title {
    width: 100%; font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 14px; line-height: 1.32;
    display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; transition: color .15s ease;
  }
  .brief-meta { display: flex; align-items: center; gap: 10px; }
  .brief-date { font-size: 10.5px; color: var(--muted); }

  /* ---- Paginación de "Últimas entradas" ---- */
  .brief-pagination { display: flex; align-items: center; justify-content: center; gap: 10px; margin-top: 14px; }
  .brief-pg-arrow {
    border: 2px solid var(--ink); background: var(--bg); width: 26px; height: 26px; flex: none;
    display: flex; align-items: center; justify-content: center; cursor: pointer; color: var(--ink);
  }
  .brief-pg-arrow svg { width: 11px; height: 11px; }
  .brief-pg-arrow.left svg { transform: scaleX(-1); }
  .brief-pg-arrow:hover:not(:disabled) { background: var(--accent); border-color: var(--accent); color: #fff; }
  .brief-pg-arrow:disabled { opacity: .3; cursor: default; }
  .brief-pg-nums { display: flex; gap: 6px; }
  .brief-pg-num {
    border: 2px solid var(--ink); background: var(--bg); width: 26px; height: 26px; flex: none;
    display: flex; align-items: center; justify-content: center; cursor: pointer; color: var(--ink);
    font-family: 'Space Mono', monospace; font-size: 11px; font-weight: 700;
  }
  .brief-pg-num:hover { border-color: var(--accent); color: var(--accent); }
  .brief-pg-num.active { background: var(--ink); border-color: var(--ink); color: #fff; }

  /* ---- Mini rating badge (miniaturas) ---- */
  .mini-rating { display: flex; align-items: center; gap: 3px; font-family: 'Space Mono', monospace; font-size: 11px; font-weight: 700; }
  .mini-rating svg { width: 11px; height: 11px; }
  .mini-rating.overlay { position: absolute; top: 8px; right: 8px; background: rgba(10,10,10,.75); color: #fff; padding: 3px 7px; z-index: 2; }
  .mini-rating.overlay svg { color: var(--accent); }
  .mini-rating.overlay.muted svg { color: rgba(255,255,255,.4); }
  .mini-rating.overlay.muted span { color: rgba(255,255,255,.65); }
  .mini-rating.inline { color: var(--accent); }
  .mini-rating.inline svg { color: var(--accent); }
  .mini-rating.inline.muted, .mini-rating.inline.muted svg { color: var(--muted); }

  @media (max-width: 760px) {
    .front-top { grid-template-columns: 1fr; }
    .front-lead .fp-hero .fp-img { height: 180px; }
    .front-lead .fp-hero h2 { font-size: 23px; }
    .front-picks { grid-template-columns: 1fr; }
    .front-pick { height: 76px; }
    .front-pick .fp-img, .front-pick .fp-noimg { width: 64px; }
    .brief-title { font-size: 14px; }
    .brief-meta { gap: 8px; }
    .brief-date { display: none; }
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

  /* ---- Grid / cards ---- */
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 18px; margin-top: 14px; }
  .card {
    position: relative; background: var(--bg); border: 2px solid var(--ink);
    padding: 20px; display: flex; flex-direction: column; gap: 10px; cursor: pointer;
    transition: transform .15s ease, box-shadow .15s ease, border-color .15s ease, color .15s ease;
    text-decoration: none;
  }
  .card:hover { color: var(--accent); border-color: var(--accent); transform: translate(-5px,-5px); box-shadow: 6px 6px 0 var(--ink); }
  .card .icon { width: 22px; height: 22px; }
  .card .icon svg { width: 100%; height: 100%; }
  .tag { display: inline-block; font-family: 'Space Mono', monospace; font-size: 10px; letter-spacing: 1.2px; color: var(--accent); border: 1px solid var(--accent); padding: 3px 9px; width: fit-content; font-weight: 700; text-transform: uppercase; }
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
  .overlay-inner { max-width: 720px; margin: 0 auto; padding: 60px 24px 100px; }
  .overlay .close-btn { position: fixed; top: 20px; right: 24px; width: 36px; height: 36px; border: 2px solid var(--ink); background: var(--bg); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 41; }
  .overlay .close-btn:hover { background: var(--accent); border-color: var(--accent); color: #fff; }
  .overlay .close-btn svg { width: 16px; height: 16px; }
  .art-icon { width: 46px; height: 46px; color: var(--ink); margin-bottom: 10px; }
  .art-icon svg { width: 100%; height: 100%; shape-rendering: crispEdges; }
  .art-tag { font-family: 'Space Mono', monospace; font-size: 10.5px; letter-spacing: 1.4px; text-transform: uppercase; color: var(--accent); font-weight: 700; }
  .art-title { font-family: 'Archivo Black', sans-serif; font-weight: 400; font-size: 42px; line-height: 1.05; margin: 10px 0 6px; letter-spacing: -1px; opacity: 0; transform: translateY(10px); animation: riseIn .5s ease forwards .1s; }
  .art-meta { font-family: 'Space Mono', monospace; font-size: 11.5px; color: var(--muted); border-bottom: 1px solid #ddd; padding-bottom: 18px; margin-bottom: 20px; }
  .art-body h2 { font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 21px; margin: 26px 0 8px; }
  .art-body p { font-size: 16px; line-height: 1.7; margin: 0 0 14px; }
  .art-body ul { font-size: 15.5px; line-height: 1.7; padding-left: 22px; }
  .art-body strong { background: linear-gradient(transparent 60%, rgba(255,90,31,.3) 60%); }
  .art-figure { margin: 22px 0; }
  .art-figure img { width: 100%; height: auto; display: block; border: 2px solid var(--ink); filter: grayscale(100%) contrast(1.05); }
  .art-figure figcaption { font-family: 'Space Mono', monospace; font-size: 11px; color: var(--muted); margin-top: 6px; }
  .card .thumb { width: 100%; height: 130px; object-fit: cover; border: 2px solid var(--ink); filter: grayscale(100%) contrast(1.05); margin-bottom: 4px; }
  .card:hover .thumb { border-color: var(--accent); }
  .art-original { margin-top: 40px; padding-top: 18px; border-top: 3px solid var(--ink); }
  .art-original a { display: inline-flex; align-items: center; gap: 8px; text-decoration: none; font-weight: 700; text-transform: uppercase; font-size: 12.5px; letter-spacing: .5px; font-family: 'Space Mono', monospace; }
  .art-original a:hover { color: var(--accent); }
  .art-original a svg { width: 16px; height: 16px; }

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
    h1.title { font-size: 46px; letter-spacing: -1.5px; margin: 18px 0 8px; }
    .subtitle { font-size: 12.5px; margin-bottom: 26px; }

    nav.sections a { padding: 12px 14px; font-size: 11px; }
    nav.sections .hist-link { padding: 0 14px; }
    .streak-nav { padding: 0 12px; }
    .streak-tooltip { left: auto; right: -10px; }

    .fp-hero h2 { font-size: 26px; }
    .fp-hero p { font-size: 13.5px; }
    .fp-hero.no-media .fp-body { padding: 26px 22px; gap: 10px; }
    .fp-hero.no-media h2 { font-size: 30px; }
    .fp-hero.no-media p { font-size: 14px; }

    .rail .card { flex: 0 0 78vw; }
    .grid { grid-template-columns: 1fr; }

    .section-hero { flex-direction: column; align-items: flex-start; gap: 10px; }
    .section-hero h2 { font-size: 26px; }

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

    h1.title { font-size: 34px; }
    .subtitle { font-size: 11.5px; }

    nav.sections .hist-link:not(.icon-only) { padding: 0 10px; font-size: 9.5px; }
    .streak-nav { padding: 0 8px; }
    .streak-nav span { display: none; } /* solo la llama, sin el número de días */

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
      <div class="live" id="live-kicker"></div>
    </div>
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
  <div class="overlay-inner" id="overlay-inner"></div>
</div>

<div class="toast" id="toast"></div>

<div class="ticker-modal" id="ticker-modal">
  <div class="ticker-modal-panel">
    <div class="ticker-modal-header">
      <h3>Artículos nuevos sin valorar</h3>
      <button class="close-btn-sm" id="ticker-modal-close"></button>
    </div>
    <div class="ticker-modal-list" id="ticker-modal-list"></div>
  </div>
</div>

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
const SECTIONS = __SECTIONS_JSON__;
const ICONS = __ICONS_JSON__;
const ARTICLE_ICONS = __ARTICLE_ICONS_JSON__;

function bySlug(slug) { return SECTIONS.find(s => s.slug === slug); }

/* one-off: resetea todas las puntuaciones a 0 (todos los artículos vuelven a ser "nuevos") */
if (!localStorage.getItem('ratingsResetTeleprompter')) {
  localStorage.removeItem('articleRatings');
  localStorage.setItem('ratingsResetTeleprompter', '1');
}

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

/* ---------- dynamic greeting ---------- */
function renderSubtitle() {
  const el = document.getElementById('subtitle');
  const h = new Date().getHours();
  let greeting, phrase;
  if (h >= 5 && h < 12) { greeting = 'Buenos días'; phrase = 'un café, una idea nueva y a por el día.'; }
  else if (h >= 12 && h < 20) { greeting = 'Buenas tardes'; phrase = 'pausa entre reuniones para alimentar la curiosidad.'; }
  else { greeting = 'Buenas noches'; phrase = 'el mejor momento para desconectar leyendo algo que sí interesa.'; }
  el.innerHTML = `${greeting}, Isabel — <span class="phrase">${phrase}</span>`;
}

/* ---------- ticker: solo artículos nuevos sin valorar ---------- */
function unratedArticles() {
  const ratings = getRatings();
  return visibleArticles()
    .filter(a => (ratings[a.id] || 0) === 0)
    .sort((x, y) => (y.date_added || '').localeCompare(x.date_added || ''));
}

function renderTicker() {
  const wrap = document.getElementById('ticker');
  const track = document.getElementById('ticker-track');
  const badge = document.getElementById('ticker-badge');
  if (badge && !badge.dataset.filled) {
    const pts = "50,4 62.6,19.5 82.5,17.5 80.5,37.4 96,50 80.5,62.6 82.5,82.5 62.6,80.5 50,96 37.4,80.5 17.5,82.5 19.5,62.6 4,50 19.5,37.4 17.5,17.5 37.4,19.5";
    badge.innerHTML = `<svg class="burst" viewBox="0 0 100 100"><polygon points="${pts}" fill="var(--accent)" stroke="none"/></svg><span>¡Nuevo!</span>`;
    badge.dataset.filled = '1';
  }
  if (ARTICLES.length === 0) { wrap.style.display = 'none'; return; }
  wrap.style.display = '';
  const items = unratedArticles();
  if (!items.length) {
    wrap.classList.add('empty-state');
    track.innerHTML = `<span class="item empty-msg">¡Estás al día! Añade más artículos para saber más.</span>`;
    return;
  }
  wrap.classList.remove('empty-state');
  const build = () => items.map(a => {
    const sec = bySlug(a.section);
    return `<span class="item"><b>${sec ? sec.name : ''}</b> — ${a.title}</span>`;
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

/* ---------- ratings (0-5 estrellas) ---------- */
function getRatings() { try { return JSON.parse(localStorage.getItem('articleRatings') || '{}'); } catch(e) { return {}; } }
function setRatingValue(id, value) {
  const r = getRatings();
  if (value <= 0) { delete r[id]; } else { r[id] = value; }
  localStorage.setItem('articleRatings', JSON.stringify(r));
}
function getRatingValue(id) { return getRatings()[id] || 0; }

function ratingHtml(a) {
  const current = getRatingValue(a.id);
  const stars = [1,2,3,4,5].map(n => {
    const icon = n <= current ? ICONS['star-filled'] : ICONS.star;
    return `<button class="star-btn ${n <= current ? 'on' : ''}" data-star="${n}" title="${n} estrella${n===1?'':'s'}">${icon}</button>`;
  }).join('');
  return `<div class="art-rating"><span class="rlabel">Tu valoración</span><div class="stars" id="art-stars">${stars}</div></div>`;
}

function wireRating(articleId) {
  const wrap = document.getElementById('art-stars');
  if (!wrap) return;
  const btns = Array.from(wrap.querySelectorAll('.star-btn'));
  function paint(value) {
    btns.forEach(b => {
      const n = Number(b.dataset.star);
      b.classList.toggle('on', n <= value);
      b.innerHTML = n <= value ? ICONS['star-filled'] : ICONS.star;
    });
  }
  btns.forEach(btn => {
    const n = Number(btn.dataset.star);
    btn.addEventListener('mouseenter', () => paint(n));
    btn.addEventListener('mouseleave', () => paint(getRatingValue(articleId)));
    btn.addEventListener('click', () => {
      const current = getRatingValue(articleId);
      const next = current === n ? 0 : n; // clicar la misma estrella la quita
      setRatingValue(articleId, next);
      paint(next);
      renderTicker();
    });
  });
}

/* ---------- notas propias por artículo ---------- */
function getArticleNotes() { try { return JSON.parse(localStorage.getItem('articleNotes') || '{}'); } catch(e) { return {}; } }
function setArticleNote(id, text) {
  const notes = getArticleNotes();
  if (!text || !text.trim()) { delete notes[id]; } else { notes[id] = text; }
  localStorage.setItem('articleNotes', JSON.stringify(notes));
}

function noteHtml(a) {
  const val = getArticleNotes()[a.id] || '';
  return `<div class="art-note">
    <h4>${ICONS.edit} Tu nota</h4>
    <p class="note-hint">Escribe en tus palabras qué te llevas de esto, o cómo lo aplicarías. Se guarda solo, en tu navegador.</p>
    <textarea id="art-note-input" placeholder="Ej: esto me sirve para justificar el rediseño del onboarding...">${val}</textarea>
    <div class="note-status" id="art-note-status"></div>
  </div>`;
}

function wireNote(articleId) {
  const input = document.getElementById('art-note-input');
  const status = document.getElementById('art-note-status');
  if (!input) return;
  let t = null;
  input.addEventListener('input', () => {
    clearTimeout(t);
    status.textContent = '';
    t = setTimeout(() => {
      setArticleNote(articleId, input.value);
      status.textContent = 'Guardado ✓';
      clearTimeout(window.__noteStatusTimer);
      window.__noteStatusTimer = setTimeout(() => { status.textContent = ''; }, 1800);
    }, 500);
  });
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
function openTickerModal() {
  document.getElementById('ticker-modal').classList.add('open');
  renderTickerModalList();
}
function closeTickerModal() {
  document.getElementById('ticker-modal').classList.remove('open');
}

function paintTmStars(btns, value) {
  btns.forEach(b => {
    const n = Number(b.dataset.star);
    b.classList.toggle('on', n <= value);
    b.innerHTML = n <= value ? ICONS['star-filled'] : ICONS.star;
  });
}

function renderTickerModalList() {
  const list = document.getElementById('ticker-modal-list');
  if (!list) return;
  const items = unratedArticles();
  if (!items.length) {
    list.innerHTML = `<div class="empty" style="padding:40px 20px;">¡Estás al día! Añade más artículos para saber más.</div>`;
    return;
  }
  list.innerHTML = items.map(a => {
    const sec = bySlug(a.section);
    return `<div class="tm-row" data-id="${a.id}">
      <a class="tm-title" data-open="${a.id}">
        <span class="tag">${sec ? sec.name : a.section}</span>
        <h4>${a.title}</h4>
      </a>
      <div class="tm-stars" data-rate-id="${a.id}">
        ${[1, 2, 3, 4, 5].map(n => `<button class="star-btn" data-star="${n}" title="${n} estrella${n === 1 ? '' : 's'}">${ICONS.star}</button>`).join('')}
      </div>
    </div>`;
  }).join('');

  list.querySelectorAll('[data-open]').forEach(el => el.addEventListener('click', () => {
    closeTickerModal();
    location.hash = '#/articulo/' + el.dataset.open;
  }));

  list.querySelectorAll('.tm-stars').forEach(starsWrap => {
    const id = starsWrap.dataset.rateId;
    const btns = Array.from(starsWrap.querySelectorAll('.star-btn'));
    btns.forEach(btn => {
      const n = Number(btn.dataset.star);
      btn.addEventListener('mouseenter', () => paintTmStars(btns, n));
      btn.addEventListener('mouseleave', () => paintTmStars(btns, 0));
      btn.addEventListener('click', e => {
        e.preventDefault();
        e.stopPropagation();
        setRatingValue(id, n);
        renderTicker();
        const row = starsWrap.closest('.tm-row');
        row.classList.add('tm-row-out');
        setTimeout(renderTickerModalList, 240);
      });
    });
  });
}

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

/* ---------- streak (junto a Historial, con tooltip) ---------- */
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
function streakPhrase(streak) {
  if (streak === 0) return 'Hoy es un buen día para empezar.';
  if (streak < 3) return 'Vas calentando motores.';
  if (streak < 7) return 'Buena racha, no la sueltes.';
  return 'Racha en llamas — sigue así.';
}

/* ---------- nav ---------- */
function renderNav(active) {
  const nav = document.getElementById('section-nav');
  const items = [{slug:'', name:'Portada'}].concat(SECTIONS.map(s=>({slug:s.slug,name:s.name})));
  const links = items.map(it => {
    const href = it.slug ? `#/${it.slug}` : '#/';
    const cls = (active === it.slug) ? 'active' : '';
    return `<a href="${href}" class="${cls}">${it.name}</a>`;
  }).join('');
  const histCls = active === 'historial' ? 'active' : '';
  const encyCls = active === 'enciclopedia' ? 'active' : '';
  const streak = computeStreak();
  const streakHtml = `<div class="streak-nav">${ICONS.flame}<span>${streak}d</span>
    <div class="streak-tooltip">${streak} día${streak===1?'':'s'} seguidos<br><span class="tt-phrase">${streakPhrase(streak)}</span></div>
  </div>`;
  nav.innerHTML = `
    <button class="nav-icon-btn" id="nav-search-btn" title="Buscar">${ICONS.search}</button>
    <div class="links-wrap">
      <button class="links-arrow left hidden" id="links-prev" title="Ver anteriores">${ICONS.arrow}</button>
      <div class="links" id="nav-links">${links}</div>
      <button class="links-arrow right hidden" id="links-next" title="Ver más">${ICONS.arrow}</button>
    </div>
    <a href="#/enciclopedia" class="hist-link ${encyCls}">Enciclopedia</a>
    ${streakHtml}
    <a href="#/historial" class="hist-link icon-only ${histCls}" title="Historial">${ICONS.history}</a>`;
  document.getElementById('nav-search-btn').addEventListener('click', openSpotlight);
  setupLinksScroll();
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
function mdToHtml(md) {
  if (!md) return '';
  const lines = md.replace(/\r/g,'').split('\n');
  let html = '';
  let inList = false;
  const inlineFmt = (s) => s
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    .replace(/\[(.+?)\]\((.+?)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
  lines.forEach(line => {
    const l = line.trim();
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
  });
  if (inList) html += '</ul>';
  return html;
}

/* ---------- mini rating badge (miniaturas) ---------- */
function ratingBadgeHtml(a, variant) {
  const r = getRatingValue(a.id);
  const inner = r > 0 ? `${ICONS['star-filled']}<span>${r}</span>` : `${ICONS.star}<span>—</span>`;
  const cls = `mini-rating ${variant} ${r === 0 ? 'muted' : ''}`;
  return `<div class="${cls}">${inner}</div>`;
}

/* ---------- card rendering ---------- */
function cardHtml(a) {
  const sec = bySlug(a.section);
  const thumb = (a.images && a.images.length) ? `<img class="thumb" src="${a.images[0]}" alt="" loading="lazy">` : '';
  return `<a class="card" href="#/articulo/${a.id}" data-id="${a.id}">
    ${ratingBadgeHtml(a, 'overlay')}
    ${thumb}
    <div class="icon">${sec ? ICONS[sec.icon] : ''}</div>
    <span class="tag">${sec ? sec.name : a.section}${a.subsection ? ' · ' + a.subsection : ''}</span>
    <h3>${a.title}</h3>
    <p>${a.summary}</p>
    <div class="date">Añadido: ${a.date_added || '—'}</div>
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
  'design-2-0': 'px-brain',
  'claude': 'px-robot',
  'figma': 'px-palette',
  'engineering': 'px-chat',
  'ai': 'px-chip',
  'materials': 'px-box',
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
    ${ratingBadgeHtml(a, 'overlay')}
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

/* ---------- artículo principal: carrusel de los 5★ ---------- */
const leadState = { items: [], index: 0, timer: null };

function renderLead(items) {
  leadState.items = items;
  leadState.index = 0;
  paintLead();
  resetLeadTimer();
}

function paintLead() {
  const wrap = document.getElementById('front-lead-out');
  if (!wrap || !leadState.items.length) return;
  const a = leadState.items[leadState.index];
  const multi = leadState.items.length > 1;
  const dots = multi ? leadState.items.map((_, i) => `<button class="lead-dot ${i === leadState.index ? 'on' : ''}" data-dot="${i}"></button>`).join('') : '';
  wrap.innerHTML = `
    ${leadHtml(a)}
    ${multi ? `
      <div class="lead-controls">
        <button class="lead-arrow left" id="lead-prev" title="Anterior">${ICONS.arrow}</button>
        <div class="lead-dots">${dots}</div>
        <button class="lead-arrow right" id="lead-next" title="Siguiente">${ICONS.arrow}</button>
      </div>
    ` : ''}
  `;
  if (multi) {
    document.getElementById('lead-prev').addEventListener('click', () => leadStep(-1));
    document.getElementById('lead-next').addEventListener('click', () => leadStep(1));
    wrap.querySelectorAll('[data-dot]').forEach(d => d.addEventListener('click', () => {
      leadState.index = Number(d.dataset.dot); paintLead(); resetLeadTimer();
    }));
    wrap.addEventListener('mouseenter', () => clearInterval(leadState.timer));
    wrap.addEventListener('mouseleave', resetLeadTimer);
  }
}

function leadStep(dir) {
  leadState.index = (leadState.index + dir + leadState.items.length) % leadState.items.length;
  paintLead();
  resetLeadTimer();
}

function resetLeadTimer() {
  clearInterval(leadState.timer);
  if (leadState.items.length > 1) leadState.timer = setInterval(() => leadStep(1), 10000);
}

function frontPickHtml(a) {
  const sec = bySlug(a.section);
  const img = (a.images && a.images.length) ? `<img class="fp-img" src="${a.images[0]}" alt="" loading="lazy">` : `<div class="fp-noimg">${articleIconSvg(a)}</div>`;
  return `<a class="front-pick" href="#/articulo/${a.id}">
    ${img}
    <div class="pick-body">
      <span class="pick-tag">${sec ? sec.name : a.section}</span>
      <h3>${truncate(a.title, 70)}</h3>
    </div>
  </a>`;
}

function midRatedGroupsHtml(midRated) {
  let html = '';
  SECTIONS.forEach(sec => {
    const items = midRated.filter(a => a.section === sec.slug);
    if (!items.length) return;
    html += `<div class="picks-subsection">
      <div class="subsection-title">${sec.name}</div>
      <div class="front-picks">${items.map(frontPickHtml).join('')}</div>
    </div>`;
  });
  return html;
}

function briefsEmptyStateHtml() {
  return `<div class="briefs-empty">
    <div class="briefs-empty-icon">${ICONS['wand']}</div>
    <p>¡Estás al día! Ya has valorado todo lo que tienes guardado.</p>
    <p class="briefs-empty-sub">Añade un artículo nuevo para que la portada vuelva a moverse.</p>
  </div>`;
}

function briefRowHtml(a) {
  const sec = bySlug(a.section);
  return `<a class="brief-row" href="#/articulo/${a.id}">
    <span class="brief-stamp">${sec ? sec.name : a.section}</span>
    <span class="brief-title">${a.title}</span>
    <span class="brief-meta">${ratingBadgeHtml(a, 'inline')}<span class="brief-date mono">${a.date_added || '—'}</span></span>
  </a>`;
}

/* ---------- "últimas entradas": paginado de 3 en 3 ---------- */
const briefsState = { items: [], page: 0, pageSize: 3 };

function renderBriefs(items) {
  briefsState.items = items;
  briefsState.page = 0;
  paintBriefs();
}

function paintBriefs() {
  const wrap = document.getElementById('front-briefs-out');
  if (!wrap) return;
  const { items, page, pageSize } = briefsState;
  const totalPages = Math.ceil(items.length / pageSize);
  const start = page * pageSize;
  const pageItems = items.slice(start, start + pageSize);
  wrap.innerHTML = `
    <div class="front-briefs">${pageItems.map(briefRowHtml).join('')}</div>
    ${totalPages > 1 ? `
      <div class="brief-pagination">
        <button class="brief-pg-arrow left" id="briefs-prev" ${page === 0 ? 'disabled' : ''}>${ICONS.arrow}</button>
        <div class="brief-pg-nums">${Array.from({ length: totalPages }, (_, i) =>
          `<button class="brief-pg-num ${i === page ? 'active' : ''}" data-pg="${i}">${i + 1}</button>`
        ).join('')}</div>
        <button class="brief-pg-arrow right" id="briefs-next" ${page === totalPages - 1 ? 'disabled' : ''}>${ICONS.arrow}</button>
      </div>
    ` : ''}
  `;
  if (totalPages > 1) {
    document.getElementById('briefs-prev').addEventListener('click', () => { briefsState.page = Math.max(0, briefsState.page - 1); paintBriefs(); });
    document.getElementById('briefs-next').addEventListener('click', () => { briefsState.page = Math.min(totalPages - 1, briefsState.page + 1); paintBriefs(); });
    wrap.querySelectorAll('[data-pg]').forEach(btn => btn.addEventListener('click', () => { briefsState.page = Number(btn.dataset.pg); paintBriefs(); }));
  }
}

/* ---------- pages ---------- */
function renderPortada() {
  renderNav('');
  clearInterval(leadState.timer);
  const list = visibleArticles();
  const main = document.getElementById('main');

  if (!list.length) {
    main.innerHTML = `<div class="empty">Todavía no hay artículos.</div>`;
    return;
  }

  const ratings = getRatings();
  const rateOf = a => ratings[a.id] || 0;
  const byDateDesc = (x, y) => (y.date_added || '').localeCompare(x.date_added || '');

  // artículo principal: tus 5★, en carrusel si hay varias
  const fiveStars = list.filter(a => rateOf(a) === 5).sort(byDateDesc);
  // últimas entradas: todo lo que aún no has valorado
  const unrated = list.filter(a => rateOf(a) === 0).sort(byDateDesc);
  // más artículos: lo valorado con menos de 5★
  const midRated = list.filter(a => { const r = rateOf(a); return r > 0 && r < 5; }).sort(byDateDesc);

  const hasLead = fiveStars.length > 0;

  main.innerHTML = `
    <div class="front-top ${hasLead ? '' : 'no-lead'}">
      ${hasLead ? `<div class="front-lead" id="front-lead-out"></div>` : ''}
      <div class="front-briefs-col">
        <div class="front-label">Últimas entradas</div>
        ${unrated.length ? `<div id="front-briefs-out"></div>` : briefsEmptyStateHtml()}
      </div>
    </div>
    ${midRated.length ? `
      <div class="front-divider"><span class="front-label">Más artículos</span></div>
      ${midRatedGroupsHtml(midRated)}
    ` : ''}
  `;

  if (hasLead) renderLead(fiveStars);
  if (unrated.length) renderBriefs(unrated);
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
  const { list, subsections, activeSub } = sectionState;
  const byDate = (x, y) => (y.date_added || '').localeCompare(x.date_added || '');
  let html = '';

  if (activeSub === null) {
    const groups = subsections.length ? subsections : [null];
    groups.forEach(sub => {
      const items = list.filter(a => (a.subsection || null) === sub).sort(byDate);
      if (items.length === 0) return;
      if (sub) html += `<div class="subsection-title">${sub}</div>`;
      html += railHtml(items);
    });
    if (subsections.length) {
      const rest = list.filter(a => !a.subsection).sort(byDate);
      if (rest.length) html += `<div class="subsection-title">Otros</div>${railHtml(rest)}`;
    }
  } else if (activeSub === '__otros__') {
    const items = list.filter(a => !a.subsection).sort(byDate);
    html = items.length ? railHtml(items) : `<div class="empty">No hay artículos aquí.</div>`;
  } else {
    const items = list.filter(a => a.subsection === activeSub).sort(byDate);
    html = items.length ? railHtml(items) : `<div class="empty">No hay artículos aquí.</div>`;
  }

  wrap.innerHTML = html;
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
  inner.innerHTML = `
    <div class="art-icon">${articleIconSvg(a)}</div>
    <div class="art-tag">${sec ? sec.name : a.section}${a.subsection ? ' · ' + a.subsection : ''}</div>
    <h1 class="art-title">${a.title}</h1>
    <div class="art-meta mono">Añadido el ${a.date_added || '—'}</div>
    ${ratingHtml(a)}
    <div class="art-body">${mdToHtml(a.content_md || a.summary)}</div>
    ${glossaryHtml(a)}
    ${noteHtml(a)}
    <div class="art-original"><a href="${a.url}" target="_blank" rel="noopener">Leer el artículo original ${ICONS.arrow}</a></div>
    ${relatedHtml(a)}
  `;
  inner.querySelectorAll('[data-term-key]').forEach(btn => btn.addEventListener('click', () => {
    const nowLiked = toggleLikedTerm(btn.dataset.termKey);
    btn.classList.toggle('liked', nowLiked);
    btn.innerHTML = nowLiked ? ICONS['heart-filled'] : ICONS.heart;
  }));
  wireRating(a.id);
  wireNote(a.id);
  overlay.classList.add('open');
  window.scrollTo(0,0);
}

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

function renderEnciclopedia() {
  renderNav('enciclopedia');
  const main = document.getElementById('main');
  const terms = buildEncyTerms();

  main.innerHTML = `
    <div class="section-hero"><div><h2>Enciclopedia</h2><p>Los términos que te ha interesado guardar, con su definición y de dónde salieron.</p></div></div>
    <div id="ency-out"></div>
  `;
  const out = document.getElementById('ency-out');
  if (!terms.length) {
    out.innerHTML = `<div class="empty">Aún no has guardado ningún término. Dale a ${ICONS.heart} en los términos nuevos que veas dentro de un artículo.</div>`;
    return;
  }

  const due = termsDue(terms);
  out.innerHTML = `
    <div class="ency-toolbar">
      <div class="ency-search-row">${ICONS.search}<input type="text" id="ency-search" placeholder="Buscar en la Enciclopedia..." autocomplete="off"></div>
      <button class="review-btn" id="ency-review-btn">${ICONS.cards} Repasar${due.length ? ` (${due.length})` : ''}</button>
    </div>
    <div class="ency-layout">
      <div class="ency-list" id="ency-list"></div>
      <div class="ency-index" id="ency-index"></div>
    </div>
  `;
  document.getElementById('ency-search').addEventListener('input', e => paintEncyList(terms, e.target.value));
  document.getElementById('ency-review-btn').addEventListener('click', () => openFlashModal(terms));
  paintEncyList(terms, '');

  if (window.__pendingReviewOpen) {
    window.__pendingReviewOpen = false;
    openFlashModal(terms);
  }
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

/* ---------- wiring del teleprompter clicable ---------- */
document.getElementById('ticker').addEventListener('click', openTickerModal);
document.getElementById('ticker-modal-close').innerHTML = ICONS.close;
document.getElementById('ticker-modal-close').addEventListener('click', closeTickerModal);
document.getElementById('ticker-modal').addEventListener('click', e => { if (e.target.id === 'ticker-modal') closeTickerModal(); });
document.addEventListener('keydown', e => { if (e.key === 'Escape' && document.getElementById('ticker-modal').classList.contains('open')) closeTickerModal(); });

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
  const m = hash.match(/^#\/articulo\/(.+)$/);
  if (m) { renderArticleOverlay(decodeURIComponent(m[1])); return; }
  overlay.classList.remove('open');

  if (hash === '#/' || hash === '') { renderPortada(); return; }
  if (hash === '#/historial') { renderHistorial(); return; }
  if (hash === '#/enciclopedia') { renderEnciclopedia(); return; }
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
        .replace("__SECTIONS_JSON__", sections_json)
        .replace("__ICONS_JSON__", icons_json)
        .replace("__ARTICLE_ICONS_JSON__", article_icons_json))

with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Built {OUT_FILE} with {len(articles)} articles across {len(SECTIONS)} sections")
