---
name: journey-map
description: >-
  Construye un mapa de journey de usuario de principio a fin — etapas, touchpoints,
  emociones, pain points — y, sobre todo, una fila final de áreas de oportunidad concretas
  y accionables (lo que la mayoría de journey maps se saltan). Úsala cuando Isabel quiera
  entender un recorrido concreto (alguien consultando un dashboard, alguien creando algo
  desde cero) y detectar huecos de UX con los que se pueda trabajar ya, no solo documentar
  dónde hay dolor.
---

# Journey Map — de las etapas a la oportunidad

> Fuente: [Owl-Listener/designer-skills — design-research](https://github.com/Owl-Listener/designer-skills/tree/main/design-research)

Un journey map clásico documenta etapas, touchpoints, emociones y pain points — pero muchos
se quedan ahí, en "aquí el usuario sufre", sin dar el salto a "y qué hacemos con esto". Esta
skill obliga a terminar siempre con una fila de **áreas de oportunidad**: no repetir el
dolor con otras palabras, sino convertirlo en algo con lo que se pueda abrir trabajo mañana
mismo.

## Cuándo se activa

Isabel quiere mapear un recorrido concreto (alguien consultando un dashboard para tomar una
decisión, alguien creando una pieza nueva desde cero, etc.) y detectar huecos de UX
accionables. También si pide explícitamente "hazme un `/journey-map`" o "mapea el recorrido
de...".

No la actives para un recorrido demasiado amplio o vago ("todo el producto") — un journey
map sirve para **una decisión concreta**, no para todo de golpe. Si Isabel no ha acotado el
recorrido, pregúntale cuál quiere mapear antes de construir nada.

## Lo que necesitas antes de construirlo

Pide, en este orden:

1. **Quién es la persona** — aunque sea a ojo, o la `synthetic-persona` ya construida si
   existe una relevante.
2. **El objetivo del recorrido** — qué journey concreto se mapea. No es lo mismo "consulta
   el dashboard por primera vez" que "vuelve cada semana a revisar resultados" o "compara
   dos campañas para decidir cuál repetir".
3. **Las etapas reales**, aunque sea intuición de Isabel como diseñadora del propio
   producto — no hace falta research formal para esto.

Si además hay analytics reales, feedback recibido, o job stories ya construidas con
`layers-user-needs` / `layers-observed-behaviour`, úsalas como base en vez de inventar la
etapa correspondiente desde cero — evita duplicar trabajo ya hecho.

Si algo del recorrido no está verificado y es pura intuición, márcalo como tal (mismo
principio que `layers-observed-behaviour`) en vez de presentarlo con la misma confianza que
algo observado o medido.

## Cómo construir el mapa

Estructura en columnas (etapas) y filas:

- **Touchpoint** — dónde interactúa la persona con el producto en esa etapa.
- **Emoción** — cómo se siente en ese momento (breve, con matiz — no solo 🙂/🙁).
- **Pain point** — dónde se frustra, se pierde o se atasca.
- **Oportunidad** — la parte que no se puede saltar. Por cada pain point real, una
  oportunidad concreta y accionable, no una reformulación del problema. Si una etapa no
  tiene pain point, la fila de oportunidad puede quedar vacía — no la rellenes por rellenar.

## Ejemplo

Isabel: *"Mapéame el recorrido de alguien del equipo de marketing consultando el dashboard
de campañas para decidir si repetir una campaña."*

| Etapa | Llega al dashboard | Encuentra la campaña | Lee la gráfica | Decide |
|---|---|---|---|---|
| **Touchpoint** | Abre el dashboard tras cerrar la campaña | Busca la campaña en la lista | Mira la gráfica de métricas | Compara con la campaña anterior |
| **Emoción** | 😐 Neutral, entra por rutina | 🙂 La encuentra rápido | 😕 No está segura de qué eje mirar | 🤔 Duda si la comparación es válida |
| **Pain point** | — | — | Ejes sin etiquetar con claridad | No hay forma fácil de superponer dos campañas |
| **Oportunidad** | — | — | Etiquetar ejes con claridad | Añadir vista de comparación lado a lado entre campañas |

La fila de oportunidad es la que justifica la skill: cada pain point termina en algo
concreto y con lo que se podría trabajar directamente, no solo en un diagnóstico del
problema.
