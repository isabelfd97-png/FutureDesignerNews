---
name: layers-domain
description: >-
  Extrae ("cosecha") el vocabulario real que ya usa un equipo — en conversaciones, tickets,
  documentos — y detecta dónde PM, diseño e ingeniería usan la misma palabra para cosas
  distintas (o palabras distintas para la misma cosa), usando el concepto de bounded context.
  Úsala cuando Isabel tenga texto real de conversaciones de equipo y sospeche que hay lío de
  vocabulario, o cuando una reunión se haya descarrilado porque dos personas estaban de
  acuerdo en las palabras pero no en lo que significan. Alimenta a `layers-conceptual-model`
  con el choque ya detectado, en vez de construir el modelo desde cero.
---

# Layers Domain — cosecha de sustantivos y choques de vocabulario

> Fuente: [jamiemill/layers-skills](https://github.com/jamiemill/layers-skills)

A diferencia de `layers-conceptual-model` (que construye el modelo preguntando
directamente), esta skill **extrae** el vocabulario que ya existe en conversaciones reales
del equipo — Slack, tickets, documentos — y detecta dónde distintas personas (PM, diseño,
ingeniería) usan la misma palabra con significados distintos, o palabras distintas para lo
mismo. Usa el concepto de **bounded context** (Domain-Driven Design): que una palabra
signifique cosas distintas en partes distintas de la organización es normal — el problema
es no saber que está pasando.

## Cuándo se activa

Isabel tiene texto real de conversaciones de equipo (no una pantalla en blanco) y sospecha
que hay líos de vocabulario, o una reunión se ha descarrilado porque dos personas parecían
de acuerdo en las palabras pero no en el significado. También si pide explícitamente "hazme
un `/layers-domain`".

Es el paso que típicamente va **antes** de `layers-conceptual-model`: primero se cosecha el
vocabulario real y se detecta el choque, luego se construye el modelo limpio ya resuelto.
No la actives si Isabel está diseñando algo desde cero sin conversaciones previas que
analizar — para eso ya está `layers-conceptual-model` directamente.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de analizar.** Con el texto que Isabel aporte, pregunta:
   - De qué equipos son las personas que escriben (para saber si el choque es entre
     PM/diseño/ingeniería o dentro del mismo equipo).
   - Si ya sospecha de alguna palabra concreta que dé problemas, además de la que
     mencionó.

**2. Cosecha los sustantivos importantes** del texto real aportado — no inventes términos
   que no aparezcan literalmente.

**3. Para cada sustantivo relevante, compara cómo lo usa cada persona/equipo.** Si hay
   choque real (mismo término, significado distinto) o sospecha de sinónimo fantasma
   (términos distintos que podrían ser la misma cosa), márcalo explícitamente con ⚠️ y
   describe el choque concreto, no solo "hay confusión".

**4. Termina con una recomendación concreta** de qué aclarar primero y con quién, antes de
   pasar a construir el modelo conceptual completo con `layers-conceptual-model`.

## Ejemplo

**Isabel escribe:**
> `/layers-domain` en las últimas reuniones sobre campañas, no sé si todos entendemos
> "segmento" igual. Aquí tienes trozos de 3 hilos de Slack: [pega texto]

**Preguntas antes de construir:**
> Antes de analizarlo, dos cosas rápidas:
> 1. ¿De qué equipos son las personas que escriben en estos hilos?
> 2. ¿Hay alguna palabra concreta, aparte de "segmento", que ya sospeches que da
>    problemas?

**Isabel responde:**
> Son PM y un ingeniero. Y sí, "audiencia" también me da mala espina

**Output final:**

> **Cosecha de sustantivos — Campañas**
>
> - **Segmento** — usado por PM como "grupo de usuarios con un filtro aplicado en tiempo
>   real". Usado por ingeniería como "tabla precalculada que se actualiza cada 24h". ⚠️
>   Choque real: PM cree que es dinámico, ingeniería lo construyó como snapshot diario.
> - **Audiencia** — usado indistintamente como sinónimo de "Segmento" por PM, pero
>   ingeniería nunca usa esta palabra. ⚠️ Posible sinónimo fantasma: ¿son la misma cosa con
>   dos nombres, o dos cosas distintas que casualmente se confunden?

**Recomendación final:**
> Antes de seguir con el modelo conceptual completo (`layers-conceptual-model`), aclarar
> con ingeniería si "Segmento" es en tiempo real o snapshot diario — esto cambia lo que la
> pantalla puede prometer mostrar.
