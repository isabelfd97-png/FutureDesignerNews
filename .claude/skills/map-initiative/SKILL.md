---
name: map-initiative
description: >-
  Mapea quién lidera — la IA o el usuario — en cada etapa de un flujo, y dónde se cede el
  control de uno a otro. Úsala cuando Isabel tenga un flujo con varias etapas que involucren
  IA y quiera ver de un vistazo si la iniciativa está bien repartida, o si hay etapas donde
  no está claro quién debería llevar la voz cantante.
---

# Map Initiative — mapa de iniciativa por etapa

> Parte del plugin [`model-interaction-design`](../../plugins/model-interaction-design.md) — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)

Construido sobre `mixed-initiative-flow`, pero aplicado a un flujo completo con varias
etapas — en vez de decidir la iniciativa una vez, la mapea etapa por etapa para detectar
inconsistencias (ej. la IA lidera al principio y de repente exige que el usuario tome las
riendas sin ninguna transición clara).

## Cuándo se activa

Isabel tiene un flujo de varias etapas que involucra IA en algún punto (o en varios) y
quiere ver de un vistazo cómo se reparte la iniciativa a lo largo de todo el flujo.
También si pide explícitamente `/map-initiative [flujo]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Cuáles son las etapas del flujo? (puede apoyarse en un `layers-interaction-flow` ya
  hecho)
- ¿Hay alguna etapa donde ya sospeches que la transición de control es abrupta?

**2. Para cada etapa, marca quién lidera** (IA / Usuario / Compartido) y cómo se transita a
la siguiente etapa.

**3. Marca con ⚠️ cualquier transición abrupta** — un salto de "IA lidera" a "Usuario
lidera" sin ninguna señal que lo anuncie.

**4. Termina recomendando dónde suavizar la transición más problemática.**

## Ejemplo

**Isabel escribe:**
> `/map-initiative` el flujo de comparar campañas con el asistente de IA integrado

**Preguntas antes de construir:**
> Antes de mapear, dime:
> - ¿Cuáles son las etapas del flujo?
> - ¿Hay alguna transición que ya sospeches que es abrupta?

**Isabel responde:**
> Etapas: propuesta del asistente → usuario confirma o corrige → asistente muestra la
> comparación → usuario decide. No he pensado en transiciones abruptas.

**Output final:**

> | Etapa | Lidera | Transición a la siguiente |
> |---|---|---|
> | Propuesta del asistente | IA | Espera confirmación explícita — clara |
> | Confirmar/corregir | Usuario | Vuelve a la IA una vez confirmado — clara |
> | Muestra la comparación | IA | ⚠️ Pasa directamente a esperar una decisión, sin
> anunciar que ahora el usuario debe actuar |
> | Decide | Usuario | — |

**Recomendación final:**
> La transición entre "Muestra la comparación" y "Decide" necesita una señal explícita de
> que ahora es turno del usuario (ej. un CTA claro tipo "¿Repetir esta campaña?") — ahora
> mismo el cambio de iniciativa es implícito y el usuario podría no darse cuenta de que se
> espera una acción suya.
