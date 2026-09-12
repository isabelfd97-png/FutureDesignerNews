---
name: build-chain
description: >-
  Diseña una cadena de prompts de varios pasos para una tarea compleja que un solo prompt
  no resuelve bien de una vez. Úsala cuando una tarea de IA tenga varias fases distintas
  (extraer datos → analizar → redactar) y convenga dividirla en pasos encadenados en vez de
  pedirlo todo en un único prompt monolítico.
---

# Build Chain — cadena de prompts de varios pasos

> Parte del plugin [`prompt-architecture`](../../plugins/prompt-architecture.md) — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)

Divide una tarea compleja en varios prompts encadenados, cada uno con una responsabilidad
clara, en vez de un único prompt monolítico que intenta hacerlo todo de golpe. Un prompt
que mezcla "extrae los datos relevantes, analízalos, y redacta un resumen" en un solo paso
suele fallar en alguna de las tres partes sin que sea fácil saber cuál — dividirlo en pasos
permite revisar y corregir cada fase por separado.

## Cuándo se activa

Una tarea de IA tiene varias fases claramente distintas (extracción, análisis, redacción,
validación) y conviene dividirla en una cadena en vez de un prompt único. También si pide
explícitamente `/build-chain [tarea compleja]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Cuáles son las fases naturales de esta tarea? (aunque sea a grandes rasgos)
- ¿Hay algún paso que ya sepas que falla o da resultados poco fiables en el prompt actual
  (si ya existe uno monolítico)?

**2. Divide la tarea en pasos**, cada uno con una única responsabilidad clara, y define qué
recibe cada paso de entrada (¿la salida del paso anterior, o datos originales?).

**3. Marca con ⚠️ cualquier punto donde el error de un paso se propagaría silenciosamente
al siguiente** — esos son los puntos donde conviene añadir una validación intermedia.

**4. Termina recomendando en qué paso empezar a depurar** si la cadena completa da
resultados incorrectos.

## Ejemplo

**Isabel escribe:**
> `/build-chain` generar el resumen de rendimiento de campaña — ahora mismo es un prompt
> único que a veces falla en algo distinto cada vez

**Preguntas antes de construir:**
> Antes de dividir la cadena, dime:
> - ¿Cuáles son las fases naturales de esta tarea?
> - ¿Sabes en qué falla el prompt actual — extrae mal los datos, analiza mal, o redacta
>   mal?

**Isabel responde:**
> No lo sé exactamente, a veces el resumen dice cosas que no cuadran con los números.

**Output final:**

> **Cadena propuesta:**
> 1. **Extracción** — de los datos crudos de la campaña, extraer solo las métricas
>    relevantes (formato estructurado, sin narrativa todavía).
> 2. **Análisis** — a partir de las métricas extraídas, identificar qué patrón explica el
>    resultado (sin escribir el resumen final todavía, solo el hallazgo).
> 3. **Redacción** — convertir el hallazgo del paso 2 en las 3 frases finales para el
>    usuario.
>
> ⚠️ **Punto de propagación silenciosa:** si el paso 1 extrae mal un número, el paso 3
> generará un resumen convincente pero basado en un dato incorrecto, sin que se note. Vale
> la pena mostrar el output del paso 1 (los datos extraídos) de forma visible, aunque sea
> solo para depuración.

**Recomendación final:**
> Empezar a depurar por el paso 1 (extracción) — como el fallo actual es "dice cosas que
> no cuadran con los números", lo más probable es que el problema esté ahí, no en la
> redacción final.
