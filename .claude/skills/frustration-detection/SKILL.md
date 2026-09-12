---
name: frustration-detection
description: >-
  Detecta señales de frustración del usuario en texto — mayúsculas, densidad de
  puntuación, repetición, latencia entre mensajes — y define cómo debería adaptarse la IA
  antes de que el usuario abandone. Úsala cuando Isabel diseñe una interacción de IA donde
  la frustración acumulada sea un riesgo real de abandono, y quiera definir qué señales
  vigilar y qué hacer al detectarlas.
---

# Frustration Detection

> Parte del plugin [`model-interaction-design`](../../plugins/model-interaction-design.md) — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)

Define qué señales textuales indican que un usuario se está frustrando con una interacción
de IA (mayúsculas, puntuación repetida "???", repetir la misma pregunta con otras
palabras, respuestas cada vez más cortas y cortantes, tiempo creciente entre mensajes) y
qué debería hacer el sistema al detectarlas — antes de que la persona simplemente cierre la
conversación sin decir por qué.

## Cuándo se activa

Isabel diseña una interacción de IA donde el abandono por frustración es un riesgo real
(soporte, un asistente que puede fallar en entender), y quiere definir señales de alerta
concretas y una respuesta (ej. ofrecer escalar a un humano, simplificar la pregunta,
reconocer explícitamente la dificultad) en vez de dejarlo sin cubrir.
