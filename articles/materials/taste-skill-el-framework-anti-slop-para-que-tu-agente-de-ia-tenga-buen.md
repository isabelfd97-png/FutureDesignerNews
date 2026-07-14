---
title: Taste Skill: el framework anti-slop para que tu agente de IA tenga buen gusto
url: https://www.tasteskill.dev/
section: materials
subsection: Skills anti-diseño-genérico
date_added: 2026-07-14
---

## De qué va
Taste Skill es un proyecto open-source que empaqueta, en forma de skills instalables, exactamente el problema que ya conoces de los '5 trucos para Claude Code' y de DESIGN.md: los agentes de IA por defecto tienden a generar frontends genéricos ('slop', en la jerga del proyecto) — mismos patrones, mismos colores por defecto, misma sensación de plantilla. En vez de escribir tú mismo las reglas anti-genéricas en un CLAUDE.md, Taste Skill te las da ya escritas y probadas, instalables con un solo comando (`npx skills add Leonxlnx/taste-skill`) en cualquier agente que soporte archivos SKILL.md: Claude Code, Cursor, Codex, Gemini CLI, v0, Lovable, entre otros.

No es una sola skill, son 13 pensadas para casos distintos: la principal genera interfaces con criterio general; hay variantes de estilo (minimalista, brutalista, 'soft' para interfaces calmadas y caras); una específica para auditar y rediseñar un proyecto ya existente en vez de partir de cero; una más estricta pensada para GPT/Codex; y una (`stitch-skill`) que exporta directamente en formato DESIGN.md, conectando con el artículo que ya guardaste sobre ese tema.

La versión 2 (experimental, ya el default) añade varias capas nuevas: el agente lee el brief antes de generar nada (a qué industria, para qué audiencia, qué tono), sabe cuándo te conviene un sistema de diseño real ya existente (Material, Fluent, Carbon, Polaris, Radix, shadcn, Tailwind oficial) en vez de inventar uno desde cero, aplica modo oscuro por defecto con la misma jerarquía en ambos temas, tiene un protocolo específico para rediseños (qué preservar, qué modernizar), y termina con un checklist obligatorio que el resultado tiene que pasar honestamente antes de entregarse.

## Por qué le importa a un product designer
Es la versión 'lista para instalar' de un problema que ya entiendes bien: sin guardrails explícitos, la IA genera diseño con cara de IA. La diferencia con escribir tu propio CLAUDE.md o DESIGN.md es que aquí alguien ya hizo el trabajo de investigar qué reglas funcionan, para qué casos, y las mantiene actualizadas (hay changelog y todo). Vale la pena tenerlo a mano como referencia de qué reglas concretas usar, aunque acabes escribiendo las tuyas propias adaptadas a tu marca.

## Ideas clave
- Taste Skill = skills open-source instalables con un comando para que agentes de IA dejen de generar frontends genéricos.
- 13 skills distintas para casos distintos, no una talla única: estilo visual, rediseño, exportar a DESIGN.md, etc.
- La v2 lee el brief, elige sistemas de diseño reales cuando toca, y pasa un checklist antes de entregar.
- Mismo problema que CLAUDE.md/DESIGN.md, pero empaquetado y mantenido por otros en vez de escrito desde cero.

## Para aprender
- **npx**: Un comando que descarga y ejecuta un paquete de código una sola vez, sin instalarlo permanentemente en tu ordenador — a diferencia de `npm install`, que sí lo deja instalado. Es la forma más rápida de 'probar' o 'añadir' algo como una skill sin montar nada a mano.
- **AI slop**: Término coloquial para el resultado genérico y de baja calidad que produce la IA cuando no se le dan suficientes límites o criterio: el mismo patrón visual repetido, colores por defecto, sensación de plantilla. Es lo contrario de lo que buscan guardrails como CLAUDE.md, DESIGN.md o Taste Skill.

---
Artículo original: https://www.tasteskill.dev/
