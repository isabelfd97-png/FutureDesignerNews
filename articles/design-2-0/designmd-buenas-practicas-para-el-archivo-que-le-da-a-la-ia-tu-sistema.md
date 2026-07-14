---
title: DESIGN.md: buenas prácticas para el archivo que le da a la IA tu sistema de diseño
url: https://uxplanet.org/design-md-best-practices-c00325e8b23a
section: design-2-0
subsection: Design systems + IA
date_added: 2026-07-14
---

## De qué va
Nick Babich (el mismo autor de los '5 trucos para que Claude Code no te dé un diseño genérico') explica DESIGN.md: un archivo de texto plano que describe la identidad visual de tu producto y le da a un agente de IA contexto persistente y estructurado sobre cómo debe verse y sentirse. Nació en Google Stitch y se abrió como especificación, así que sirve igual en Claude Code, Cursor o cualquier otra herramienta de IA para diseño.

El archivo tiene dos capas: un frontmatter en YAML con el nombre del sistema de diseño y los design tokens (colores, tipografía, radios de esquina, spacing), y un cuerpo en Markdown que desarrolla marca, estilos y componentes conectando cada explicación con los tokens definidos arriba.

## DESIGN.md es el hermano de diseño de CLAUDE.md
Si ya viste el artículo de los 5 trucos anti-diseño-genérico, esto te va a sonar: CLAUDE.md son las reglas de comportamiento que le pones a Claude Code antes de generar nada (qué evitar, qué screenshot loop seguir). DESIGN.md es el complemento específico de diseño — en vez de reglas de proceso, es el sistema de diseño real (tus tokens, tu marca, tus componentes) puesto en un formato que la IA puede leer directamente en vez de inventar valores por defecto. Usados juntos, uno cubre el 'cómo te comportas' y el otro el 'con qué material trabajas'.

## Las 3 reglas para escribir un buen DESIGN.md
1. **Los tokens son decisiones, no solo variables.** Nombrar un color 'primary' no es solo ponerle nombre a un HEX, es definir qué rol cumple en la interfaz. Evita nombres por aspecto (`blue`, `gray-1`) y usa nombres por rol (`primary`, `surface-dim`, `border-subtle`, `radius-card`) — así la IA entiende la función, no solo el valor.
2. **Toda decisión necesita razonamiento.** La secuencia es: valor bruto (el HEX) → intención de uso (para qué sirve) → razonamiento (por qué) → límites (cuándo NO usarlo). Ese último punto —los límites— es el que más se olvida, y es justo el que evita que la IA use tu color de marca en sitios donde no toca.
3. **Los componentes se construyen encima de los tokens y el razonamiento.** No basta con describir el estado por defecto de un botón: hace falta cubrir default, hover, active, disabled, loading y focus, porque son justo los estados que una IA sin esa guía tiende a olvidar o inventar mal.

## Por qué le importa a un product designer
Esto es la versión escrita de algo que ya haces mentalmente al mantener un design system: nombrar por rol, justificar decisiones, cubrir todos los estados. La diferencia es que aquí ese criterio se pone en un archivo que la IA puede leer literalmente antes de generar nada, en vez de tener que repetírselo en cada prompt. Cuanto más se parezca tu DESIGN.md a cómo ya piensas un sistema de diseño, menos genérico va a salir lo que te construya Claude Code, Cursor o Stitch.

## Ideas clave
- DESIGN.md le da a la IA tu sistema de diseño real (tokens, marca, componentes) en vez de dejarle inventar estilos por defecto.
- Es el complemento de diseño del CLAUDE.md: uno cubre el comportamiento, el otro el material visual.
- Nombra los tokens por el rol que cumplen, no por su aspecto.
- Cada decisión necesita razonamiento, y sobre todo límites: cuándo NO usar algo.
- Los componentes deben cubrir todos los estados, no solo el default.

## Para aprender
- **YAML frontmatter**: Un bloque de configuración al principio de un archivo de texto, delimitado por '---', escrito en formato YAML (parecido al JSON pero con sangrado en vez de llaves). En DESIGN.md es donde van los design tokens; en las Skills de Claude es donde va el nombre y la descripción. Piénsalo como el panel de ajustes del archivo, separado del contenido narrativo de abajo.
- **Google Stitch**: Una herramienta de Google que genera UI a partir de un sistema de diseño, y donde nació el formato DESIGN.md. No hace falta usarla para aprovechar la idea: el formato se abrió como especificación reutilizable en cualquier herramienta de IA para diseño, incluido Claude Code.

---
Artículo original: https://uxplanet.org/design-md-best-practices-c00325e8b23a
