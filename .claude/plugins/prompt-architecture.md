# Plugin: prompt-architecture

> Fuente: [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills) — plugin `prompt-architecture`
> Instalación original (fuera de este repo): `claude plugin install prompt-architecture@ai-design-skills`

## Qué es

Los prompts (system prompts, plantillas, cadenas de razonamiento) que corren por debajo de
una función de IA son ahora una **superficie de producto** — determinan directamente qué
hace y qué no hace esa función, igual que un componente de UI determina qué puede hacer un
usuario. Este plugin trata el diseño de esos prompts con la misma disciplina que el resto
del sistema de diseño: estructura, plantillas reutilizables, versionado, auditoría.

Las piezas viven como skills individuales en `.claude/skills/`, cada una marcada como
perteneciente a este plugin. Aquí solo se documenta el conjunto.

## Las 7 skills base (versión breve, ver cada `SKILL.md` para más detalle)

1. **system-prompt-structure** — anatomía de un system prompt efectivo: rol, contexto,
   restricciones, formato.
2. **template-design** — plantillas de prompt reutilizables y parametrizadas para salidas
   consistentes.
3. **chain-of-thought-design** — diseñar cadenas de razonamiento que producen mejores
   resultados.
4. **few-shot-patterns** — diseñar ejemplos que orienten el comportamiento de la IA.
5. **constraint-specification** — definir formato de salida, longitud, tono y límites de
   contenido dentro de un prompt.
6. **prompt-versioning** — gestionar iteraciones de un prompt, probar cambios, y rastrear
   qué funcionó.
7. **context-engineering** — decidir qué información entra en la ventana de contexto y en
   qué orden.

## Los 3 comandos (con ejemplo completo en su propio `SKILL.md`)

- **design-prompt** — crea un system prompt estructurado para una función de IA.
- **build-chain** — diseña una cadena de prompts de varios pasos para una tarea compleja.
- **audit-prompt** — evalúa un prompt ya existente por claridad, efectividad y edge cases.
