---
title: CLAUDE.md: el proceso paso a paso para crear el tuyo
url: 
section: claude
subsection: Claude Code
date_added: 2026-08-18
---

## De qué va
Un workflow práctico (parte del curso "Claude Code for Designers") para crear tu propio CLAUDE.md: el archivo que Claude Code lee automáticamente al principio de cada sesión en un proyecto, y que le da el contexto que si no tendrías que repetir cada vez — qué es el proyecto, tus preferencias de diseño, cómo está organizado, y qué no tocar. La idea central: no lo escribas de memoria ni de golpe. Se construye respondiendo a una entrevista guiada, con reglas concretas sobre lo que hace que un CLAUDE.md funcione de verdad en vez de ser ruido que Claude acaba ignorando.

## Cuándo usar esto
- Ya has empezado a construir algo en Claude Code y los resultados se sienten demasiado genéricos.
- Estás montando una carpeta de proyecto nueva por primera vez.
- Quieres que Claude siga tus preferencias de diseño y el contexto del proyecto de forma consistente.
- Un compañero va a usar el mismo proyecto de Claude Code y necesita el mismo contexto compartido.

**Cuándo NO usarlo todavía:** si es tu primera vez con Claude Code, explora y construye algo primero. Monta el CLAUDE.md una vez tengas una idea de qué decisiones se repiten.

## Las reglas antes de escribir nada
- **40–80 líneas ideal, máximo ~150.** Se carga en cada sesión — demasiado largo y Claude empieza a "olvidar" lo del medio (context rot), o directamente lo ignora.
- **Es un índice, no una enciclopedia.** Mantenlo corto y señala a otros archivos para el detalle ("Para tokens → lee tokens.md") en vez de meterlo todo dentro.
- **Solo Markdown.** Es eficiente en tokens; un PDF gasta contexto solo en metadatos.
- **Qué + Por qué + Cómo.** Esa es la estructura mínima: qué es esto, por qué existe, cómo está organizado.
- **El sistema de diseño va aquí, no en una Skill.** Las Skills hay que invocarlas explícitamente; el CLAUDE.md se carga solo — resérvalo para lo que tiene que aplicar siempre.
- **No dupliques.** Si algo ya vive en otro archivo, señala hacia él — no lo copies dentro.

## Paso 1 — pega este prompt en Claude Code
Abre una sesión nueva de Claude Code en la carpeta de tu proyecto. Pon el modo de permisos en **Plan Mode**. Luego pega esto tal cual (está en inglés a propósito, es literalmente lo que le vas a dar a Claude):

```
I want you to help me create a CLAUDE.md file for this project.

CLAUDE.md is a system prompt that you will read at the start of every single conversation in this project. It should give you the context you need to do good work without me having to repeat myself — covering what this project is, why it exists, how it's structured, my design preferences, and any constraints.

Please interview me to gather what you need. Ask me questions one section at a time — don't dump everything at once. After each answer, ask any follow-up that would help you write that section better.

Once we've covered everything, draft the full CLAUDE.md file for my review. I'll then tell you what to adjust before we save it.

Ground rules for the file you'll create:
- Keep it between 40 and 80 lines. Maximum 150.
- Use markdown format only (no PDFs, no long prose blocks)
- Structure it with clear sections using ## headers
- If any section would get too long, don't write the full detail — instead write a short pointer: "For X detail — read [filename].md" and flag that we should create that file separately
- The file should cover: project overview, design preferences, architecture/structure, tone and content rules, and any known constraints
- End with a short "What NOT to do" section so you know what to avoid

Start by asking me about the project — what it is and who it's for.
```

## Paso 2 — responde a las preguntas de Claude
Claude va a ir sección por sección. Esto es lo que te va a preguntar en cada bloque — tenlo pensado antes de empezar para que la entrevista vaya rápido:

**Sobre el proyecto**
- ¿Qué es este proyecto, en una frase?
- ¿Para quién es?
- ¿Qué problema resuelve?
- ¿Cómo se ve el éxito?

**Sobre tus preferencias de diseño**
- ¿Cuál es el lenguaje visual? (minimalista, atrevido, editorial, desenfadado...)
- Tipografías, si ya las tienes decididas
- Enfoque de color (p. ej. "fondo oscuro, un solo color de acento, alto contraste")
- Sensación de espaciado (apretado, generoso, estructurado...)
- Estilo de animación (ninguna, sutil, expresiva...)
- Referencias — sitios, apps o sensaciones que te parecen acertadas

**Sobre la arquitectura**
- ¿Qué hay en esta carpeta? ¿Cómo está organizada?
- ¿Qué stack se está usando? (aunque sea a grandes rasgos — "Next.js + Tailwind", "HTML plano", "React")
- ¿Dónde viven las API keys / secretos? (p. ej. un archivo .env)
- ¿Hay archivos que Claude nunca debería tocar?

**Sobre el tono y el contenido**
- ¿Cuál es la voz de este producto? (profesional, cercana, directa, con filo...)
- ¿Hay palabras o expresiones que evitar?
- ¿Quién es quien lee/usa esto — cómo piensa y cómo habla?

**Sobre las restricciones**
- ¿Requisitos de compatibilidad de navegador?
- ¿Objetivos de rendimiento?
- ¿Estándares de accesibilidad?
- ¿Algo que ya esté decidido y no deba cambiarse?

## Paso 3 — revisa el borrador
Claude va a producir un borrador. Léelo y pregúntate:
- ¿Está por debajo de 150 líneas?
- ¿Se nota cada línea, o hay alguna que no echarías de menos si desapareciera?
- ¿La sección de preferencias de diseño es lo bastante concreta para guiar decisiones, o sigue siendo vaga?
- ¿Falta algo que siempre acabas repitiéndole a Claude?
- ¿Hay algo aquí que Claude no necesita saber en cada sesión?

Dile a Claude qué cambiar, siendo específico — algo como *"la sección de preferencias de diseño es demasiado vaga, añade que usamos 8px de espaciado base e Inter como tipografía principal"*, no un "mejóralo" genérico.

## Paso 4 — guárdalo
Cuando estés a gusto con el resultado, dile a Claude, tal cual:

```
Save this as CLAUDE.md in the root of this project folder.
```

Listo. A partir de ahí, cualquier sesión nueva en esa carpeta lo carga sola.

## Paso 5 — mantenlo vivo
Un CLAUDE.md tiene que crecer con el proyecto. Vuelve a él cuando:
- Has tomado una decisión de diseño que Claude sigue clavando mal.
- La estructura del proyecto ha cambiado de forma significativa.
- Has añadido un sistema de diseño o un archivo de tokens (añade un puntero a él).
- Has creado otros archivos de referencia que Claude debería conocer.

Si se acerca a las 150 líneas, divídelo: mueve la sección más larga a su propio archivo y sustitúyela por un puntero de una línea.

## La plantilla, lista para copiar
Esta es la forma a la que apuntas — Claude la rellenará con tus respuestas. Se queda en inglés a propósito: es literalmente lo que se pega dentro de tu CLAUDE.md.

```
# [Project Name]

## Project
[1–3 sentences: what it is, who it's for, what it's trying to do]

## Design Preferences
- Layout: [e.g. minimal, generous whitespace, single-column mobile-first]
- Typography: [font family, scale approach]
- Colour: [palette description, usage rules]
- Spacing: [base unit, rhythm]
- Interactions: [animation style, hover states]
- Mood / references: [1–2 references or vibes]

## Architecture
- Stack: [e.g. Next.js 15, Tailwind 4, TypeScript]
- Folder structure: [brief overview or pointer to a README]
- API keys: stored in `.env` — never commit this file
- Do not touch: [any files or folders that are off-limits]

## Design System
→ See `tokens.md` for colour, spacing, and type tokens
→ See `components.md` for component rules and variants
[Or write tokens inline if there's no separate file yet]

## Content & Tone
- Voice: [e.g. direct, warm, no jargon]
- Audience: [who they are, how they think]
- Avoid: [words, patterns, or tones that don't fit]

## Known Constraints
- [e.g. Must work offline / WCAG AA minimum / No external fonts]

## What NOT to Do
- Don't invent new design patterns — use what's already established
- Don't hardcode values — use tokens
- Don't change [X] without asking first
- [Any other guardrails specific to this project]
```

## Por qué le importa a un product designer
Esto es la versión de proyecto del DESIGN.md que ya viste: si DESIGN.md es tu sistema de diseño real puesto en un formato que la IA puede leer, CLAUDE.md es el resto del contexto del proyecto — quién es el usuario, cómo está organizado el código, qué tono usar, qué no tocar. Sin él, acabas repitiendo la misma información al principio de cada conversación nueva; con él, cualquiera que abra el proyecto (tú en tres meses, o un compañero) parte del mismo punto. Y como se actualiza igual que cualquier otro archivo del proyecto, es el sitio natural donde anotar una decisión de diseño en cuanto Claude la vuelve a acertar mal por segunda vez.

## Ideas clave
- CLAUDE.md se carga automáticamente al principio de cada sesión de Claude Code en ese proyecto — por eso tiene que ser corto (40–80 líneas ideal, 150 máximo).
- Se construye por entrevista, con un prompt de arranque concreto: le pides a Claude que te pregunte sección por sección, no que lo escriba de un tirón.
- Las preguntas cubren cinco bloques: proyecto, preferencias de diseño, arquitectura, tono/contenido y restricciones.
- Antes de guardar, revísalo con la checklist de longitud y especificidad — y dale a Claude feedback concreto, no genérico.
- Incluye una plantilla lista para copiar, que Claude rellena con tus respuestas.
- Se mantiene vivo: vuelve a él cuando Claude repita un error, cambie la estructura del proyecto, o crezca por encima de las 150 líneas (y entonces, divídelo).

## Para aprender
- **Context rot**: Cuando un archivo de contexto es tan largo que Claude empieza a "perder" o ignorar la información que está en medio, tratándola con menos peso que lo que está al principio o al final.
- **Plan Mode**: Un modo de permisos de Claude Code en el que Claude solo puede leer y proponer un plan, no editar archivos todavía — pensado para fases de diseño/entrevista antes de tocar nada.

---
Research propio de Isabel (sin fuente externa).
