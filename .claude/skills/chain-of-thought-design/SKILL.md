---
name: chain-of-thought-design
description: >-
  Diseña cadenas de razonamiento paso a paso dentro de un prompt para producir mejores
  resultados en tareas complejas, en vez de pedir la respuesta final directamente. Úsala
  cuando una función de IA falle o dé resultados inconsistentes en tareas que requieren
  varios pasos de razonamiento, y quieras estructurar explícitamente esos pasos dentro del
  prompt.
---

# Chain-of-Thought Design

> Parte del plugin [`prompt-architecture`](../../plugins/prompt-architecture.md) — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)

Diseña la secuencia de razonamiento que un prompt le pide a la IA que siga paso a paso,
antes de dar la respuesta final — útil en tareas complejas donde pedir la respuesta
directa produce resultados inconsistentes o superficiales, pero pedir "primero identifica
X, luego evalúa Y, luego decide Z" mejora la calidad del resultado.

## Cuándo se activa

Una función de IA da resultados inconsistentes o poco fiables en tareas que requieren
varios pasos de razonamiento (comparar, priorizar, evaluar) y hace falta estructurar esos
pasos explícitamente en el prompt en vez de pedir la conclusión directa.
