---
title: Meta abre Astryx, su design system interno, y ya funciona en Figma Make
url: https://www.linkedin.com/posts/achyut-khanpara_designsystems-figmamake-uxdesign-share-7480456616299917312-4U0C/
section: figma-freebies
subsection: Figma Make
date_added: 2026-07-12
---

## De qué va
Meta ha abierto el código de Astryx, su design system interno usado en más de 13.000 apps durante 8 años. Achyut Khanpara probó si funciona dentro de Figma Make: basta con pedirle que instale los paquetes `@astryxdesign/core` y `@astryxdesign/theme-neutral` desde npm y que construya una pantalla con sus componentes, sin instalación manual. Funciona, pero todavía en beta: hay que esperar algún error intermedio antes de que el resultado se asiente.

## Por qué le importa a un product designer
Más allá de los componentes, lo interesante es que Astryx sale de fábrica con un CLI y un servidor MCP pensados para que agentes de IA lo lean directamente, no solo desarrolladores. Es una pista de hacia dónde van los design systems: no solo documentados para humanos, sino estructurados para que la IA los use como fuente de verdad al generar UI.

## Ideas clave
- Astryx es el design system interno de Meta (13.000+ apps, 8 años), ahora open source.
- Se instala en Figma Make con un prompt, tirando del paquete público de npm.
- Aún en beta: genera output real pero con algún error mid-generación.
- Se puede personalizar (colores, spacing, comportamiento) por lenguaje natural, sin tocar código.
- Lo importante no es el kit de componentes, es el CLI + MCP: diseñado para que los agentes de IA lo consuman directamente.

## Para aprender
- **CLI (Command Line Interface)**: Una forma de controlar un programa escribiendo comandos de texto en vez de hacer clic en botones — es la 'interfaz' que usan desarrolladores (y ahora agentes de IA) para instalar y manejar herramientas como Astryx. Piénsalo como el equivalente en código a un menú de opciones, pero escrito.
- **Servidor MCP (Model Context Protocol)**: Un protocolo que permite que un agente de IA se conecte directamente a una herramienta o base de datos y la use, en vez de que un humano tenga que ir explicándole cómo hacerlo cada vez. Piénsalo como un 'enchufe universal' entre la IA y el software que ya existe — es lo que permite que Figma Make 'entienda' Astryx sin que nadie le enseñe manualmente.
- **npm (registro de paquetes)**: Un catálogo público enorme donde desarrolladores publican piezas de código reutilizable ('paquetes'), como Astryx, para que cualquiera pueda instalarlas con un comando en vez de construirlas desde cero. Es parecido a una librería de plugins, pero para código.

---
Artículo original: https://www.linkedin.com/posts/achyut-khanpara_designsystems-figmamake-uxdesign-share-7480456616299917312-4U0C/
