---
name: audit-prompt
description: >-
  Evalúa un prompt ya existente por claridad, efectividad y edge cases, detectando
  ambigüedades que podrían producir resultados inconsistentes. Úsala cuando Isabel tenga un
  prompt en producción que a veces falla o da resultados irregulares, y quiera un
  diagnóstico estructurado en vez de reescribirlo a ciegas por prueba y error.
---

# Audit Prompt — auditoría de un prompt existente

> Parte del plugin [`prompt-architecture`](../../plugins/prompt-architecture.md) — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)

Audita un prompt real ya en uso, buscando ambigüedades en las instrucciones, falta de
restricciones explícitas, o edge cases no contemplados — en vez de iterar a ciegas
cambiando frases sueltas por prueba y error cuando algo falla.

## Cuándo se activa

Isabel tiene un prompt en producción que da resultados inconsistentes o falla en casos
concretos, y quiere un diagnóstico estructurado de por qué. También si pide explícitamente
`/audit-prompt [prompt a evaluar]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿En qué casos concretos falla o da resultados raros? (ejemplos reales, si los hay)
- ¿El prompt tiene restricciones explícitas de formato/tono/contenido, o depende del
  comportamiento por defecto del modelo?

**2. Revisa el prompt buscando:**
- Instrucciones ambiguas (que se puedan interpretar de más de una forma razonable)
- Restricciones que faltan y que explicarían los fallos reportados
- Edge cases no contemplados (entradas vacías, datos incompletos, casos límite)

**3. Marca cada hallazgo con severidad** (🔴 explica directamente el fallo reportado / 🟡
riesgo real pero no confirmado / ⚪ mejora menor).

**4. Termina recomendando el cambio más urgente**, priorizando lo que explique
directamente el problema que Isabel reportó.

## Ejemplo

**Isabel escribe:**
> `/audit-prompt` este prompt a veces da un resumen que dice "excelente rendimiento"
> cuando los datos son mediocres: [pega el prompt]

**Preguntas antes de construir:**
> Antes de auditar, dime: ¿tienes un ejemplo real de una entrada donde falló así?

**Isabel responde:**
> Sí, tengo uno guardado, te lo paso.

**Output final:**

> 🔴 **Sin restricción de tono ligado a los datos:** el prompt no especifica que el tono
> debe reflejar el resultado real (positivo solo si los datos lo respaldan) — el modelo
> por defecto tiende a sonar positivo salvo que se le indique lo contrario explícitamente.
> Esto explica directamente el caso que compartiste.
>
> 🟡 **Sin edge case para datos mediocres/ambiguos:** el prompt cubre "buen rendimiento" y
> "mal rendimiento" en los ejemplos, pero no un caso intermedio — el modelo probablemente
> redondea hacia el ejemplo más parecido que tiene, que puede ser el positivo.

**Recomendación final:**
> Añadir una restricción explícita: "el tono debe reflejar objetivamente los números, sin
> inclinarse hacia positivo por defecto" y un ejemplo few-shot de un caso mediocre para
> cubrir el punto 🟡 — el 🔴 es la corrección más urgente porque explica directamente el
> fallo reportado.
