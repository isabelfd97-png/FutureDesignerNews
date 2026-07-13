import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE, "data", "articles.json")
OUT_FILE = os.path.join(BASE, "index.html")

with open(DATA_FILE, encoding="utf-8") as f:
    articles = json.load(f)

SECTIONS = [
    {
        "slug": "figma-freebies",
        "name": "Figma & Freebies",
        "desc": "Tips, plugins, plantillas y recursos gratuitos para sacarle más partido a Figma.",
        "icon": "layers",
    },
    {
        "slug": "ia-claude",
        "name": "IA & Claude",
        "desc": "Novedades de IA en general y de Claude en particular: modelos, features, casos de uso.",
        "icon": "chip",
    },
    {
        "slug": "terminologia-tecnica",
        "name": "Terminología Técnica",
        "desc": "Conceptos y palabras técnicas explicados en claro, para no perderte en una conversación de IA o de código.",
        "icon": "book",
    },
    {
        "slug": "hablar-con-ingenieros",
        "name": "Hablar con Ingenieros",
        "desc": "Cómo colaborar mejor con developers: procesos, cultura, expectativas y lenguaje común.",
        "icon": "chat-code",
    },
]

ICONS = {
    "chip": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="7" y="7" width="10" height="10" rx="1"/><path d="M9 7V3M12 7V3M15 7V3M9 21v-4M12 21v-4M15 21v-4M7 9H3M7 12H3M7 15H3M21 9h-4M21 12h-4M21 15h-4"/></svg>',
    "layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"><path d="M12 2 3 7l9 5 9-5-9-5Z"/><path d="M3 12l9 5 9-5"/><path d="M3 17l9 5 9-5"/></svg>',
    "chat-code": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M21 15a2 2 0 0 1-2 2H8l-4 4V5a2 2 0 0 1 2-2h13a2 2 0 0 1 2 2v10Z"/><path d="M9 10 7 12l2 2M15 10l2 2-2 2"/></svg>',
    "eye": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M1 12s4-7 11-7 11 7 11 7-4 7-11 7-11-7-11-7Z"/><circle cx="12" cy="12" r="3"/></svg>',
    "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M4 20V10M11 20V4M18 20v-7"/><path d="M2 20h20"/></svg>',
    "wrench": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M14.7 6.3a4 4 0 0 1-5.4 5.4L4 17l3 3 5.3-5.3a4 4 0 0 1 5.4-5.4L21 6l-3-3-3.3 3.3Z"/></svg>',
    "flame": '<svg viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M12 2c1 3-2 4-2 7a3 3 0 0 0 6 0c0-1-0.5-2-1-2 2 0 4 2 4 5.5A7 7 0 1 1 8 12.5C8 9 9 6 12 2Z"/></svg>',
    "trash": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M3 6h18M8 6V4a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v2m2 0-1 14a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1L5 6h14Z"/></svg>',
    "close": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 4l16 16M20 4 4 20"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "history": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7.5v5l3.2 1.9"/></svg>',
    "search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>',
    "restore": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/></svg>',
    "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M4 4.5A2.5 2.5 0 0 1 6.5 2H20v17H6.5A2.5 2.5 0 0 0 4 21.5v-17Z"/><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 20.5s-7.5-4.6-10-9.3C.4 7.9 2 4.5 5.4 4c2-.3 3.8.6 4.9 2.3.8 1.2 1.7 1.2 2.5 0C13.8 4.6 15.6 3.7 17.6 4c3.4.5 5 3.9 3.4 7.2-2.5 4.7-9 9.3-9 9.3Z"/></svg>',
    "heart-filled": '<svg viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M12 20.5s-7.5-4.6-10-9.3C.4 7.9 2 4.5 5.4 4c2-.3 3.8.6 4.9 2.3.8 1.2 1.7 1.2 2.5 0C13.8 4.6 15.6 3.7 17.6 4c3.4.5 5 3.9 3.4 7.2-2.5 4.7-9 9.3-9 9.3Z"/></svg>',
    "star": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"><path d="M12 2.5l2.9 6.2 6.6.7-5 4.6 1.4 6.6L12 17.9l-5.9 3.7 1.4-6.6-5-4.6 6.6-.7L12 2.5Z"/></svg>',
    "star-filled": '<svg viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M12 2.5l2.9 6.2 6.6.7-5 4.6 1.4 6.6L12 17.9l-5.9 3.7 1.4-6.6-5-4.6 6.6-.7L12 2.5Z"/></svg>',
}

data_json = json.dumps(articles, ensure_ascii=False)
sections_json = json.dumps(SECTIONS, ensure_ascii=False)
icons_json = json.dumps(ICONS, ensure_ascii=False)

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
  .mono { font-family: 'Space Mono', monospace; }

  /* ---- Masthead ---- */
  header.masthead { padding: 48px 24px 0; border-bottom: 4px solid var(--ink); position: relative; }
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
    font-weight: 400; font-size: 74px; letter-spacing: -2px;
    margin: 22px 0 10px; text-align: center; text-transform: uppercase; line-height: .92;
  }
  h1.title span { display: inline-block; opacity: 0; transform: translateY(18px) rotate(-1deg); animation: riseIn .55s cubic-bezier(.2,.8,.2,1) forwards; }
  h1.title span:nth-child(odd) { color: var(--accent); }
  @keyframes riseIn { to { opacity: 1; transform: translateY(0) rotate(0); } }

  .subtitle {
    color: var(--ink); font-size: 14px; text-align: center; margin-bottom: 40px;
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
  .ticker-track { display: inline-block; padding: 8px 0; animation: scrollTicker 34s linear infinite; }
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
    padding: 0 36px;
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
  .dict-badge {
    flex: none; display: flex; align-items: center; gap: 5px; font-family: 'Space Mono', monospace;
    font-size: 9.5px; letter-spacing: .5px; text-transform: uppercase; color: var(--accent);
  }
  .dict-badge svg { width: 14px; height: 14px; }

  /* ---- Enciclopedia ---- */
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

  /* ---- Front page (portada) ---- */
  .frontpage-top { display: grid; grid-template-columns: 1.7fr 1fr; gap: 22px; margin-top: 6px; align-items: start; }
  .frontpage-top.single-col { grid-template-columns: 1fr; }

  /* ---- Títulos de columna (portada) ---- */
  .fp-col { display: flex; flex-direction: column; min-height: 0; }
  .fp-col-title {
    font-family: 'Space Mono', monospace; font-size: 10.5px; letter-spacing: 2px; text-transform: uppercase; color: #fff;
    background: var(--accent); display: inline-block; padding: 4px 10px; font-weight: 700; margin-bottom: 14px; width: fit-content;
  }

  /* ---- Hero carousel (5 estrellas) ---- */
  .hero-carousel { position: relative; height: 520px; }
  .hc-slide {
    height: 100%; opacity: 0; transform: translateY(8px);
    transition: opacity .38s ease, transform .38s ease;
  }
  .hc-slide.in { opacity: 1; transform: translateY(0); }
  .hc-slide.out { opacity: 0; transform: translateY(-8px); transition: opacity .2s ease, transform .2s ease; }
  .hc-slide .fp-hero { height: 100%; display: flex; flex-direction: column; }
  .hc-slide .fp-hero .fp-img, .hc-slide .fp-hero .fp-noimg { height: 260px; flex: none; }
  .hc-slide .fp-hero .fp-body { flex: 1; min-height: 0; overflow: hidden; }
  .hc-slide .fp-hero h2 { display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
  .hc-slide .fp-hero p { display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
  .hc-arrow {
    position: absolute; top: 50%; transform: translateY(-50%); width: 38px; height: 38px;
    border: 2px solid var(--ink); background: var(--bg); display: flex; align-items: center; justify-content: center;
    cursor: pointer; color: var(--ink); z-index: 2;
  }
  .hc-arrow:hover { background: var(--accent); border-color: var(--accent); color: #fff; }
  .hc-arrow svg { width: 15px; height: 15px; }
  .hc-arrow.left { left: -18px; }
  .hc-arrow.left svg { transform: scaleX(-1); }
  .hc-arrow.right { right: -18px; }
  .hc-dots { position: absolute; bottom: 14px; left: 50%; transform: translateX(-50%); display: flex; gap: 6px; z-index: 2; }
  .hc-dot { width: 7px; height: 7px; border-radius: 50%; background: rgba(255,255,255,.6); border: 1px solid var(--ink); padding: 0; }
  .hc-dot.on { background: var(--accent); border-color: var(--accent); }

  /* ---- 4 y 3 estrellas: columna derecha ---- */
  .fp-secondary-col { display: flex; flex-direction: column; min-height: 520px; }
  .fp-secondary-list { display: flex; flex-direction: column; gap: 14px; }
  .fp-card.fp-wide { display: flex; align-items: stretch; flex: none; position: relative; }
  .fp-card.fp-wide .fp-img, .fp-card.fp-wide .fp-noimg { width: 130px; flex: none; border-bottom: none; border-right: 2px solid var(--ink); min-height: 130px; }
  .fp-card.fp-wide .fp-noimg svg { width: 32px; }
  .fp-card.fp-wide .fp-body { display: flex; flex-direction: column; flex: 1 1 auto; min-width: 0; padding: 14px 16px; gap: 7px; justify-content: center; }
  .fp-card.fp-wide h3 { margin: 0; font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 15px; line-height: 1.3; }
  .fp-card.fp-wide p { margin: 0; font-size: 12px; line-height: 1.45; color: var(--muted); }
  .fp-card.fp-wide .tag-row { display: flex; align-items: center; gap: 8px; }
  .fp-pagination { flex: none; display: flex; align-items: center; justify-content: center; gap: 14px; margin-top: 12px; }
  .pg-btn { border: 2px solid var(--ink); background: var(--bg); width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; cursor: pointer; color: var(--ink); }
  .pg-btn svg { width: 13px; height: 13px; }
  .pg-btn.left svg { transform: scaleX(-1); }
  .pg-btn:hover:not(:disabled) { background: var(--accent); border-color: var(--accent); color: #fff; }
  .pg-btn:disabled { opacity: .3; cursor: default; }
  .pg-count { font-family: 'Space Mono', monospace; font-size: 11px; color: var(--muted); }

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

  /* ---- Empty states de portada ---- */
  .fp-empty-hero {
    height: 520px; border: 2px dashed var(--ink); display: flex; flex-direction: column; align-items: center; justify-content: center;
    gap: 14px; text-align: center; padding: 40px; color: var(--muted);
  }
  .fp-empty-hero .fp-empty-icon { width: 38px; height: 38px; opacity: .35; }
  .fp-empty-hero .fp-empty-icon svg { width: 100%; height: 100%; }
  .fp-empty-hero p { margin: 0; font-size: 14px; line-height: 1.6; }
  .fp-empty-row { padding: 22px 0; color: var(--muted); font-style: italic; font-size: 13.5px; }

  /* ---- Divisoria + secciones por categoría (2/1/sin valorar) ---- */
  .fp-divider { border: none; border-top: 3px solid var(--ink); margin: 40px 0 0; }
  .tier-section { margin-top: 36px; }
  .rail-wrap { position: relative; display: flex; align-items: center; gap: 6px; }
  .rail-wrap .rail { flex: 1; }
  .rail-arrow {
    flex: none; width: 30px; height: 30px; border: 2px solid var(--ink); background: var(--bg);
    display: flex; align-items: center; justify-content: center; cursor: pointer; color: var(--ink);
  }
  .rail-arrow svg { width: 13px; height: 13px; }
  .rail-arrow.left svg { transform: scaleX(-1); }
  .rail-arrow:hover { background: var(--accent); border-color: var(--accent); color: #fff; }
  .rail-arrow.hidden { visibility: hidden; }

  @media (max-width: 760px) {
    .frontpage-top { grid-template-columns: 1fr; }
    .hc-arrow { display: none; }
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
    .frontpage-top { gap: 16px; }
  }

  @media (max-width: 760px) {
    h1.title { font-size: 46px; letter-spacing: -1.5px; margin: 18px 0 8px; }
    .subtitle { font-size: 12.5px; margin-bottom: 26px; }

    nav.sections a { padding: 12px 14px; font-size: 11px; }
    nav.sections .hist-link { padding: 0 14px; }
    .streak-nav { padding: 0 12px; }
    .streak-tooltip { left: auto; right: -10px; }

    .frontpage-top { grid-template-columns: 1fr; }
    .fp-col-title { font-size: 12px; }
    .hero-carousel { height: auto; min-height: 0; }
    .hc-slide { position: relative; }
    .hc-slide .fp-hero .fp-img, .hc-slide .fp-hero .fp-noimg { height: 200px; }
    .hc-slide .fp-hero .fp-body { overflow: visible; }
    .fp-hero h2 { font-size: 26px; }
    .fp-hero p { font-size: 13.5px; }
    .fp-hero.no-media .fp-body { padding: 26px 22px; gap: 10px; }
    .fp-hero.no-media h2 { font-size: 30px; }
    .fp-hero.no-media p { font-size: 14px; }
    .hc-arrow { display: none; }

    .fp-secondary-col { min-height: 0; }
    .fp-card.fp-wide { flex-direction: column; }
    .fp-card.fp-wide .fp-img, .fp-card.fp-wide .fp-noimg {
      width: 100%; height: 150px; min-height: 0; border-right: none; border-bottom: 2px solid var(--ink);
    }

    .rail .card { flex: 0 0 78vw; }
    .grid { grid-template-columns: 1fr; }

    .section-hero { flex-direction: column; align-items: flex-start; gap: 10px; }
    .section-hero h2 { font-size: 26px; }

    .art-title { font-size: 30px; }
    .art-body p, .art-body ul { font-size: 15px; }
    .overlay-inner { padding: 60px 18px 80px; }

    .ency-layout { flex-direction: column; gap: 8px; }
    .ency-index {
      position: static; flex-direction: row; flex-wrap: wrap; max-height: none;
      justify-content: flex-start; gap: 2px 8px; padding: 10px 0; border-bottom: 1px solid #e5e5e5; margin-bottom: 10px;
      transform: none; top: auto; right: auto; background: transparent;
    }

    table.hist { min-width: 520px; }

    .spotlight, .ticker-modal { padding-top: 8vh; }
  }

  @media (max-width: 480px) {
    .wrap { padding: 0 14px; }
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

/* ---------- front page (editorial layout) ---------- */
function fpCardOpen(a) {
  const sec = bySlug(a.section);
  return `<span class="tag">${sec ? sec.name : a.section}${a.subsection ? ' · ' + a.subsection : ''}</span>`;
}

function fpMediaHtml(a, sec) {
  if (a.images && a.images.length) return `<img class="fp-img" src="${a.images[0]}" alt="" loading="lazy">`;
  return `<div class="fp-noimg">${sec ? ICONS[sec.icon] : ''}</div>`;
}

function fpHeroHtml(a) {
  const img = (a.images && a.images.length) ? `<img class="fp-img" src="${a.images[0]}" alt="" loading="lazy">` : '';
  return `<a class="fp-card fp-hero ${img ? '' : 'no-media'}" href="#/articulo/${a.id}">
    ${ratingBadgeHtml(a, 'overlay')}
    ${img}
    <div class="fp-body">
      ${fpCardOpen(a)}
      <h2>${truncate(a.title, 85)}</h2>
      <p>${truncate(a.summary, 135)}</p>
      <div class="date mono">${a.date_added || '—'}</div>
    </div>
  </a>`;
}

function fpWideHtml(a) {
  const sec = bySlug(a.section);
  const img = fpMediaHtml(a, sec);
  return `<a class="fp-card fp-wide" href="#/articulo/${a.id}">
    ${img}
    <div class="fp-body">
      <div class="tag-row"><span class="tag">${sec ? sec.name : a.section}</span>${ratingBadgeHtml(a, 'inline')}</div>
      <h3>${truncate(a.title, 58)}</h3>
      <p>${truncate(a.summary, 100)}</p>
    </div>
  </a>`;
}

/* ---------- hero carousel (5 estrellas) ---------- */
const heroState = { items: [], index: 0, timer: null };

function renderHeroCarousel(items) {
  heroState.items = items;
  heroState.index = 0;
  paintHero(true);
  resetHeroTimer();
  const wrap = document.getElementById('hero-carousel');
  if (wrap) {
    wrap.addEventListener('mouseenter', () => clearInterval(heroState.timer));
    wrap.addEventListener('mouseleave', resetHeroTimer);
  }
}

function paintHero(instant) {
  const wrap = document.getElementById('hero-carousel');
  if (!wrap) return;
  const existing = wrap.querySelector('.hc-slide');

  const doRender = () => {
    const a = heroState.items[heroState.index];
    const multi = heroState.items.length > 1;
    const dots = multi ? heroState.items.map((_, i) => `<span class="hc-dot ${i === heroState.index ? 'on' : ''}"></span>`).join('') : '';
    wrap.innerHTML = `
      <div class="hc-slide">${fpHeroHtml(a)}</div>
      ${multi ? `
        <button class="hc-arrow left" id="hc-prev" title="Anterior">${ICONS.arrow}</button>
        <button class="hc-arrow right" id="hc-next" title="Siguiente">${ICONS.arrow}</button>
        <div class="hc-dots">${dots}</div>
      ` : ''}
    `;
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        const s = wrap.querySelector('.hc-slide');
        if (s) s.classList.add('in');
      });
    });
    if (multi) {
      document.getElementById('hc-prev').addEventListener('click', () => heroStep(-1));
      document.getElementById('hc-next').addEventListener('click', () => heroStep(1));
    }
  };

  if (existing && !instant) {
    existing.classList.remove('in');
    existing.classList.add('out');
    setTimeout(doRender, 200);
  } else {
    doRender();
  }
}

function heroStep(dir) {
  heroState.index = (heroState.index + dir + heroState.items.length) % heroState.items.length;
  paintHero();
  resetHeroTimer();
}

function resetHeroTimer() {
  clearInterval(heroState.timer);
  if (heroState.items.length > 1) {
    heroState.timer = setInterval(() => heroStep(1), 10000);
  }
}

/* ---------- 4 estrellas: columna secundaria paginada ---------- */
const secState = { items: [], page: 0, pageSize: 3 };

function renderSecondaryColumn(items) {
  secState.items = items;
  secState.page = 0;
  paintSecondary();
}

function paintSecondary() {
  const wrap = document.getElementById('fp-secondary-out');
  if (!wrap) return;
  const { items, page, pageSize } = secState;
  const totalPages = Math.ceil(items.length / pageSize);
  const start = page * pageSize;
  const pageItems = items.slice(start, start + pageSize);
  wrap.innerHTML = `
    <div class="fp-secondary-list">${pageItems.map(fpWideHtml).join('')}</div>
    ${totalPages > 1 ? `
      <div class="fp-pagination">
        <button class="pg-btn left" id="sec-prev" ${page === 0 ? 'disabled' : ''}>${ICONS.arrow}</button>
        <span class="pg-count">${page + 1} / ${totalPages}</span>
        <button class="pg-btn" id="sec-next" ${page === totalPages - 1 ? 'disabled' : ''}>${ICONS.arrow}</button>
      </div>
    ` : ''}
  `;
  if (totalPages > 1) {
    document.getElementById('sec-prev').addEventListener('click', () => { secState.page = Math.max(0, secState.page - 1); paintSecondary(); });
    document.getElementById('sec-next').addEventListener('click', () => { secState.page = Math.min(totalPages - 1, secState.page + 1); paintSecondary(); });
  }
}

/* ---------- 2 / 1 / sin valorar: agrupados por sección real, siempre visibles ---------- */
function sectionRowHtml(sec, items) {
  const railId = `rail-sec-${sec.slug}`;
  const body = items.length
    ? `<div class="rail-wrap">
        <button class="rail-arrow left hidden" data-rail-prev="${railId}">${ICONS.arrow}</button>
        <div class="rail" id="${railId}">${items.map(cardHtml).join('')}</div>
        <button class="rail-arrow right hidden" data-rail-next="${railId}">${ICONS.arrow}</button>
      </div>`
    : `<div class="fp-empty-row">Todavía no hay artículos en ${sec.name}.</div>`;
  return `<div class="tier-section">
    <div class="subsection-title">${sec.name}</div>
    ${body}
  </div>`;
}

function bottomSectionsHtml(leftover) {
  const ratings = getRatings();
  let html = '<hr class="fp-divider">';
  SECTIONS.forEach(sec => {
    const items = leftover.filter(a => a.section === sec.slug).sort((x, y) => {
      const rx = ratings[x.id] || 0, ry = ratings[y.id] || 0;
      if (ry !== rx) return ry - rx;
      return (y.date_added || '').localeCompare(x.date_added || '');
    });
    html += sectionRowHtml(sec, items);
  });
  return html;
}

function heroEmptyStateHtml() {
  return `<div class="fp-empty-hero">
    <div class="fp-empty-icon">${ICONS.star}</div>
    <p>Aún no tienes artículos destacados.<br>Valora con 3★ o más para que entren en el ranking.</p>
  </div>`;
}

function secondaryEmptyStateHtml() {
  return `<div class="fp-empty-hero">
    <div class="fp-empty-icon">${ICONS.star}</div>
    <p>Todavía no hay más artículos en el ranking.</p>
  </div>`;
}

function setupRailArrows(id) {
  const track = document.getElementById(id);
  const prev = document.querySelector(`[data-rail-prev="${id}"]`);
  const next = document.querySelector(`[data-rail-next="${id}"]`);
  if (!track || !prev || !next) return;
  function update() {
    const overflow = track.scrollWidth > track.clientWidth + 2;
    prev.classList.toggle('hidden', !overflow || track.scrollLeft <= 2);
    next.classList.toggle('hidden', !overflow || track.scrollLeft >= track.scrollWidth - track.clientWidth - 2);
  }
  prev.addEventListener('click', () => track.scrollBy({ left: -320, behavior: 'smooth' }));
  next.addEventListener('click', () => track.scrollBy({ left: 320, behavior: 'smooth' }));
  track.addEventListener('scroll', update);
  window.addEventListener('resize', update);
  update();
}


/* ---------- ranking con decaimiento: puntuación + antigüedad ---------- */
const RANK_HALF_LIFE_DAYS = 14; // cada 14 días, el "peso" de la puntuación se reduce a la mitad

function ageDaysOf(a) {
  const t = Date.parse(a.date_added);
  if (isNaN(t)) return 0;
  return Math.max(0, (Date.now() - t) / 86400000);
}

function articleScore(a, ratings) {
  const r = ratings[a.id] || 0;
  if (r <= 0) return 0;
  return r * Math.pow(2, -ageDaysOf(a) / RANK_HALF_LIFE_DAYS);
}

/* ---------- pages ---------- */
function renderPortada() {
  renderNav('');
  clearInterval(heroState.timer);
  const list = visibleArticles();
  const main = document.getElementById('main');

  if (!list.length) {
    main.innerHTML = `<div class="empty">Todavía no hay artículos.</div>`;
    return;
  }

  const ratings = getRatings();
  const rateOf = a => ratings[a.id] || 0;

  const HERO_SLOTS = 3;
  const SECONDARY_SLOTS = 6;

  // solo compiten por el ranking los artículos valorados con 3★ o más;
  // el resto (1★, 2★ o sin valorar) siempre va a las secciones de abajo
  const ranked = list.filter(a => rateOf(a) >= 3)
    .map(a => ({ a, score: articleScore(a, ratings) }))
    .sort((x, y) => y.score - x.score || (y.a.date_added || '').localeCompare(x.a.date_added || ''))
    .map(x => x.a);

  const hero = ranked.slice(0, HERO_SLOTS);
  const secondary = ranked.slice(HERO_SLOTS, HERO_SLOTS + SECONDARY_SLOTS);
  const overflow = ranked.slice(HERO_SLOTS + SECONDARY_SLOTS);
  const leftover = list.filter(a => rateOf(a) <= 2).concat(overflow);

  const hasHero = hero.length > 0;
  const hasSecondary = secondary.length > 0;

  const heroColHtml = `<div class="fp-col">
    <div class="fp-col-title">Top artículos</div>
    ${hasHero ? `<div class="hero-carousel" id="hero-carousel"></div>` : heroEmptyStateHtml()}
  </div>`;
  const secondaryColHtml = `<div class="fp-col">
    <div class="fp-col-title">También destacados</div>
    ${hasSecondary ? `<div class="fp-secondary-col"><div id="fp-secondary-out"></div></div>` : secondaryEmptyStateHtml()}
  </div>`;

  const topHtml = `<div class="frontpage-top">${heroColHtml}${secondaryColHtml}</div>`;

  main.innerHTML = `${topHtml}${bottomSectionsHtml(leftover)}`;

  if (hasHero) renderHeroCarousel(hero);
  if (hasSecondary) renderSecondaryColumn(secondary);
  SECTIONS.forEach(sec => { const id = `rail-sec-${sec.slug}`; if (document.getElementById(id)) setupRailArrows(id); });
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

function renderHistorial() {
  renderNav('historial');
  const hidden = getHidden();
  const deleted = getDeleted();
  const list = ARTICLES.filter(a => !deleted.includes(a.id))
    .sort((x,y)=>(y.date_added||'').localeCompare(x.date_added||''));
  const main = document.getElementById('main');
  main.innerHTML = `
    <div class="section-hero"><div><h2>Historial</h2><p>Todo lo que has ido añadiendo, con fecha. Manda a la papelera lo que ya no te interese, y desde ahí restáuralo o bórralo del todo.</p></div></div>
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
    <div class="art-tag">${sec ? sec.name : a.section}${a.subsection ? ' · ' + a.subsection : ''}</div>
    <h1 class="art-title">${a.title}</h1>
    <div class="art-meta mono">Añadido el ${a.date_added || '—'}</div>
    ${ratingHtml(a)}
    <div class="art-body">${mdToHtml(a.content_md || a.summary)}</div>
    ${glossaryHtml(a)}
    <div class="art-original"><a href="${a.url}" target="_blank" rel="noopener">Leer el artículo original ${ICONS.arrow}</a></div>
  `;
  inner.querySelectorAll('[data-term-key]').forEach(btn => btn.addEventListener('click', () => {
    const nowLiked = toggleLikedTerm(btn.dataset.termKey);
    btn.classList.toggle('liked', nowLiked);
    btn.innerHTML = nowLiked ? ICONS['heart-filled'] : ICONS.heart;
  }));
  wireRating(a.id);
  overlay.classList.add('open');
  window.scrollTo(0,0);
}

function encyLetterOf(term) {
  let l = (term || '?').trim().charAt(0).toUpperCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  return /[A-Z]/.test(l) ? l : '#';
}

function renderEnciclopedia() {
  renderNav('enciclopedia');
  const main = document.getElementById('main');
  const liked = getLikedTerms();
  const terms = [];
  ARTICLES.forEach(a => {
    (a.glossary || []).forEach((g, idx) => {
      const key = termKey(a.id, idx);
      if (a.dictionary || liked.includes(key)) terms.push({ ...g, articleId: a.id, articleTitle: a.title });
    });
  });
  terms.sort((x, y) => x.term.localeCompare(y.term, 'es', { sensitivity: 'base' }));

  main.innerHTML = `
    <div class="section-hero"><div><h2>Enciclopedia</h2><p>Los términos que te ha interesado guardar, con su definición y de dónde salieron.</p></div></div>
    <div id="ency-out"></div>
  `;
  const out = document.getElementById('ency-out');
  if (!terms.length) {
    out.innerHTML = `<div class="empty">Aún no has guardado ningún término. Dale a ${ICONS.heart} en los términos nuevos que veas dentro de un artículo.</div>`;
    return;
  }

  out.innerHTML = `
    <div class="ency-search-row">${ICONS.search}<input type="text" id="ency-search" placeholder="Buscar en la Enciclopedia..." autocomplete="off"></div>
    <div class="ency-layout">
      <div class="ency-list" id="ency-list"></div>
      <div class="ency-index" id="ency-index"></div>
    </div>
  `;
  document.getElementById('ency-search').addEventListener('input', e => paintEncyList(terms, e.target.value));
  paintEncyList(terms, '');
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
        .replace("__ICONS_JSON__", icons_json))

with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Built {OUT_FILE} with {len(articles)} articles across {len(SECTIONS)} sections")
