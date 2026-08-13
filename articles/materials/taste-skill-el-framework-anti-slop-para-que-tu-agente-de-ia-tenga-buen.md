---
title: Taste Skill: el framework anti-slop para que tu agente de IA tenga buen gusto
url: https://www.tasteskill.dev/
section: materials
subsection: Skills anti-diseño-genérico
date_added: 2026-07-14
---

## De qué va
Taste Skill empaqueta, en forma de skills instalables, el mismo problema que ya conoces de los '5 trucos para Claude Code' y de DESIGN.md: por defecto, los agentes de IA tienden a generar frontends genéricos ('slop', en la jerga del proyecto). En vez de escribir tú las reglas anti-genéricas a mano, aquí vienen ya escritas y mantenidas, listas para instalar en cualquier agente compatible con archivos SKILL.md.

## Por qué le importa a un product designer
Es la versión 'lista para instalar' de un criterio que ya tienes: sin guardrails explícitos, la IA genera diseño con cara de IA. La diferencia con tu propio CLAUDE.md o DESIGN.md es que aquí alguien más ya investigó qué reglas funcionan para qué casos, y las mantiene actualizadas (tiene changelog). Vale la pena tenerlo como referencia de qué reglas concretas usar, aunque acabes adaptando las tuyas a tu propia marca.

## Materiales incluidos
- **taste-skill** (Principal · v2) — Lee el brief, infiere la dirección de diseño correcta y evita interfaces con cara de plantilla. Usa sistemas de diseño reales cuando toca y pasa un checklist antes de entregar.
  - Instalar: `npx skills add Leonxlnx/taste-skill --skill design-taste-frontend`
  - Link: https://github.com/Leonxlnx/taste-skill/tree/main/skills/taste-skill
- **taste-skill-v1** (Legacy) — La v1 original, conservada para proyectos que dependen de su comportamiento exacto. Úsala solo si v2 rompe algo específico.
  - Instalar: `npx skills add Leonxlnx/taste-skill --skill design-taste-frontend-v1`
  - Link: https://github.com/Leonxlnx/taste-skill/tree/main/skills/taste-skill-v1
- **gpt-tasteskill** (GPT / Codex) — Variante más estricta para modelos de GPT y Codex, con más variación de layout y dirección de movimiento.
  - Instalar: `npx skills add Leonxlnx/taste-skill --skill gpt-tasteskill`
  - Link: https://github.com/Leonxlnx/taste-skill/tree/main/skills/gpt-tasteskill
- **image-to-code-skill** (Image-first) — Genera referencias visuales primero, las analiza en profundidad, y luego implementa el frontend siguiéndolas de cerca.
  - Instalar: `npx skills add Leonxlnx/taste-skill --skill image-to-code-skill`
  - Link: https://github.com/Leonxlnx/taste-skill/tree/main/skills/image-to-code-skill
- **redesign-skill** (Auditoría) — Para proyectos existentes que necesitan una auditoría visual seria y un rediseño más limpio, no partir de cero.
  - Instalar: `npx skills add Leonxlnx/taste-skill --skill redesign-skill`
  - Link: https://github.com/Leonxlnx/taste-skill/tree/main/skills/redesign-skill
- **soft-skill** (Estilo visual) — Interfaces calmadas y de aspecto caro: contraste suave, mucho whitespace, movimiento fluido.
  - Instalar: `npx skills add Leonxlnx/taste-skill --skill soft-skill`
  - Link: https://github.com/Leonxlnx/taste-skill/tree/main/skills/soft-skill
- **output-skill** (Ejecución) — Evita resultados a medias: bloquea placeholders, secciones saltadas o trabajo sin terminar.
  - Instalar: `npx skills add Leonxlnx/taste-skill --skill output-skill`
  - Link: https://github.com/Leonxlnx/taste-skill/tree/main/skills/output-skill
- **minimalist-skill** (Estilo visual) — UI de producto editorial y limpia: color contenido, estructura marcada, jerarquía más ajustada.
  - Instalar: `npx skills add Leonxlnx/taste-skill --skill minimalist-skill`
  - Link: https://github.com/Leonxlnx/taste-skill/tree/main/skills/minimalist-skill
- **brutalist-skill** (Estilo visual) — Lenguaje visual mecánico y duro: tipografía suiza, estructura cruda, contraste marcado.
  - Instalar: `npx skills add Leonxlnx/taste-skill --skill brutalist-skill`
  - Link: https://github.com/Leonxlnx/taste-skill/tree/main/skills/brutalist-skill
- **stitch-skill** (Exportar) — Reglas de diseño semánticas compatibles con Google Stitch, con un formato extra de exportación a DESIGN.md.
  - Instalar: `npx skills add Leonxlnx/taste-skill --skill stitch-skill`
  - Link: https://github.com/Leonxlnx/taste-skill/tree/main/skills/stitch-skill
- **imagegen-frontend-web** (Image gen) — Imágenes de referencia de nivel 'premium' para webs: dirección de arte fuerte, tipografía, spacing, disciplina anti-slop.
  - Instalar: `npx skills add Leonxlnx/taste-skill --skill imagegen-frontend-web`
  - Link: https://github.com/Leonxlnx/taste-skill/tree/main/skills/imagegen-frontend-web
- **imagegen-frontend-mobile** (Image gen) — Conceptos de pantallas móviles y flujos completos, con jerarquía limpia y consistencia entre pantallas.
  - Instalar: `npx skills add Leonxlnx/taste-skill --skill imagegen-frontend-mobile`
  - Link: https://github.com/Leonxlnx/taste-skill/tree/main/skills/imagegen-frontend-mobile
- **brandkit** (Image gen) — Imágenes resumen de brand kit: conceptos de logo, sistema de color, tipografía y mockups.
  - Instalar: `npx skills add Leonxlnx/taste-skill --skill brandkit`
  - Link: https://github.com/Leonxlnx/taste-skill/tree/main/skills/brandkit

## Para aprender
- **npx**: Un comando que descarga y ejecuta un paquete de código una sola vez, sin instalarlo permanentemente en tu ordenador — a diferencia de `npm install`, que sí lo deja instalado. Es la forma más rápida de 'probar' o 'añadir' algo como una skill sin montar nada a mano.
- **AI slop**: Término coloquial para el resultado genérico y de baja calidad que produce la IA cuando no se le dan suficientes límites o criterio: el mismo patrón visual repetido, colores por defecto, sensación de plantilla. Es lo contrario de lo que buscan guardrails como CLAUDE.md, DESIGN.md o Taste Skill.

---
Artículo original: https://www.tasteskill.dev/
