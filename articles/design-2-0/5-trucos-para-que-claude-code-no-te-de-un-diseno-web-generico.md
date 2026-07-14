---
title: 5 trucos para que Claude Code no te dé un diseño web genérico
url: https://uxplanet.org/5-tips-to-prevent-generic-web-design-in-claude-code-7cc044760453
section: ia-claude
subsection: Prompting avanzado
date_added: 2026-07-13
---

## De qué va
El artículo parte de un experimento simple: pedirle a Claude Code una landing page con un prompt suelto da un resultado funcional pero con "cara de plantilla genérica". El autor, Nick Babich, propone que el problema no es el modelo sino la falta de contexto — y da 5 ajustes concretos, todos centrados en el archivo `CLAUDE.md` (el archivo de instrucciones que Claude lee al empezar a trabajar en un proyecto), para que el resultado se acerque a un diseño con personalidad real.

## Por qué le importa a un product designer
Esto es justo el tipo de "prompting de sistema" que marca la diferencia entre usar Claude como generador de plantillas o como un colaborador que respeta tu criterio visual. Si alguna vez generas UI con Claude Code (o ves a un ingeniero hacerlo y quieres opinar sobre el resultado), estas guardrails son literalmente una versión en texto de lo que tú ya defines en un design system: paleta propia, tipografía con jerarquía, estados de interacción obligatorios, nada de sombras y grises por defecto.

## Ideas clave
- El CLAUDE.md es el equivalente a un brief de marca: cuanto más específico, menos "IA genérica" sale.
- La skill 'frontend-design' hay que pedirla explícitamente — no se activa sola.
- El screenshot loop (generar → capturar → comparar con referencia → corregir, mínimo 2 rondas) es la técnica que más mejora el resultado final, más que el prompt inicial.
- Las "Anti-Generic Design Guardrails" son básicamente una lista de anti-patrones de Tailwind/React que cualquier diseñador reconocería como "lo de siempre": bg-white + shadow-md + rounded-lg.

## Para aprender
- **CLAUDE.md**: Un archivo de texto que pones en la carpeta de tu proyecto y que Claude lee automáticamente al empezar a trabajar en él. Es como el brief que le darías a alguien nuevo en el equipo: objetivos, stack técnico, y reglas que quieres que respete siempre.
- **Skill (de Claude)**: Un paquete de instrucciones específicas que le enseña a Claude a hacer bien una tarea concreta (como diseñar frontend). Se activa a demanda — hay que pedírsela, no se usa sola por defecto. Piénsalo como un 'modo experto' que puedes encender.
- **Tailwind CSS**: Un sistema de utilidades para escribir estilos en código (en vez de un archivo CSS aparte, se aplican clases cortas directamente en el HTML/JSX, como 'bg-white' o 'shadow-md'). Muy usado en desarrollo web moderno; su problema es que, sin personalizar, todo el mundo acaba con la misma pinta 'de fábrica'.
- **JSX**: La forma de escribir código en React que mezcla HTML y lógica de programación en el mismo archivo. Es lo que ves si abres el código de una interfaz hecha con React: se parece a HTML pero dentro de JavaScript.
- **Design tokens**: Los valores base de un sistema de diseño (colores, tipografías, espaciados) guardados como variables con nombre propio, en vez de usar valores sueltos. Es el mismo concepto que los 'styles' o 'variables' que ya usas en Figma, pero aplicado directamente en el código.

---
Artículo original: https://uxplanet.org/5-tips-to-prevent-generic-web-design-in-claude-code-7cc044760453
