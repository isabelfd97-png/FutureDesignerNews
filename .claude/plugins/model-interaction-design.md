# Plugin: model-interaction-design

> Fuente: [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills) — plugin `model-interaction-design`
> Instalación original (fuera de este repo): `claude plugin install model-interaction-design@ai-design-skills`

## Qué es

A diferencia de una skill suelta, un **plugin** agrupa varias skills y comandos que
trabajan juntos sobre un mismo dominio — en este caso, cómo se comportan las interacciones
entre humanos y una IA: quién lleva la iniciativa en cada momento, cómo se revela lo que la
IA sabe hacer, qué pasa cuando hay un malentendido, cómo se detecta que el usuario se está
frustrando.

Es el marco de fondo para diseñar cualquier producto con IA (un asistente, un chat, una
función generativa) sin que la experiencia salga "quebradiza" — cada parte resuelta de
forma distinta, sin una decisión consciente de diseño detrás.

Las piezas de este plugin viven en este repo como skills individuales en
`.claude/skills/`, cada una marcada como perteneciente a este plugin. Aquí solo se
documenta el conjunto.

## Las 8 skills base (versión breve, ver cada `SKILL.md` para más detalle)

1. **conversation-patterns** — turn-taking, secuencias de reparación, estructura de
   diálogo.
2. **mixed-initiative-flow** — cuándo lidera la IA y cuándo el usuario, y cómo se cede el
   control.
3. **progressive-disclosure** — revelar la capacidad de la IA gradualmente.
4. **multimodal-orchestration** — coordinar texto, imagen, voz y uso de herramientas en
   una misma interacción.
5. **context-window-design** — diseñar en torno a límites de tokens, memoria y
   persistencia de la conversación.
6. **generative-ui** — interfaces donde la IA genera componentes de UI dinámicamente.
7. **feedback-loops** — corrección del usuario, pulgar arriba/abajo, edición inline,
   señales de refuerzo.
8. **frustration-detection** — detectar frustración del usuario por señales de texto y
   adaptar antes de que abandone.

## Los 3 comandos (con ejemplo completo en su propio `SKILL.md`)

- **design-conversation** — diseña un flujo de conversación humano-IA completo.
- **audit-interaction** — evalúa una interacción IA ya existente contra las taxonomías de
  las 8 skills base.
- **map-initiative** — mapea quién lidera (IA o usuario) en cada etapa de un flujo.
