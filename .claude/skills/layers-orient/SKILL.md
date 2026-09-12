---
name: layers-orient
description: >-
  Diagnóstico que audita un proyecto de diseño a través de siete capas de decisión —
  estrategia, alcance, modelo conceptual, estructura, interacción, layout y superficie
  visual — y señala en cuál está el verdadero cuello de botella. Úsala cuando Isabel no sabe
  por dónde empezar con un diseño, dice cosas como "esto no me convence pero no sé qué le
  pasa", "creo que necesito rediseñar X", o cuando quiere evitar pulir visualmente algo cuyo
  problema real está más arriba (en el modelo conceptual o la estructura). Casi siempre
  revela que el trabajo se estaba haciendo en la capa equivocada.
---

# Layers Orient — diagnóstico de las 7 capas de decisión

> Fuente: [jamiemill/layers-skills](https://github.com/jamiemill/layers-skills)

Antes de tocar nada visual, esta skill obliga a preguntarse en qué capa vive realmente el
problema. La tentación natural es saltar directo al layout o al color ("esta pantalla se ve
mal"), pero muchas veces el problema real está dos o tres capas más abajo — y arreglar lo
visual sin resolver eso primero es maquillar algo que habrá que rehacer.

## Las 7 capas (de más abstracta a más concreta)

1. **Estrategia** — qué problema resuelve el proyecto y para quién.
2. **Alcance** — qué entra y qué se queda fuera.
3. **Modelo conceptual** — cómo se organiza la información en la cabeza del usuario (¿esto
   es un feed?, ¿una revista con secciones?, ¿una colección?).
4. **Estructura** — cómo se navega, qué lleva a qué.
5. **Interacción** — cómo se comporta cada elemento (clic, scroll, hover...).
6. **Layout / composición** — dónde va cada cosa en la pantalla.
7. **Superficie visual** — color, tipografía, sombras, el "look" final.

## Cuándo se activa

Isabel pide un diagnóstico general de un diseño, no sabe por dónde empezar, o propone
rediseñar algo concreto (una gráfica, una pantalla, un componente) sin haber verificado que
el problema esté ahí. También si dice explícitamente "hazme un `/layers-orient`" o "audita
las capas".

No la actives para pedidos de feedback puntual y acotado sobre algo ya bien definido (para
eso están otras skills de crítica de diseño) — esta es para cuando el problema aún no está
localizado.

## Cómo hacer el diagnóstico

Recorre las 7 capas en orden, de arriba a abajo, para el proyecto o la parte del proyecto
que Isabel señale. Para cada capa:

- Marca si está resuelta (✅), es ambigua o floja (⚠️), o directamente no existe (❌).
- Si una capa está en ⚠️ o ❌, **detente ahí** — las capas siguientes dependen de esa
  decisión y no se pueden evaluar con criterio hasta que se resuelva.
- Sé concreta: no digas "el modelo conceptual es confuso", di *qué* dos modelos se están
  mezclando y *qué síntoma* produce eso más abajo.

Termina siempre con:
1. Un **diagnóstico de una frase**: en qué capa está el cuello de botella real.
2. **1-2 preguntas concretas** para desbloquear esa capa — no una lista larga, las mínimas
   necesarias para poder seguir bajando.

No sigas bajando de capa tú sola dando por hecho las respuestas. Espera a que Isabel
responda antes de continuar el diagnóstico hacia las capas inferiores.

## Ejemplo — iterando algo que ya existe

Isabel: *"Quiero iterar el estilo visual de esta gráfica de métricas de campaña, no me
convence."*

Respuesta esperada (resumida):

> 1. Estrategia ✅ — el dashboard existe para que el equipo de marketing decida qué
>    campañas repetir. Clara.
> 2. Alcance ✅ — claro qué métricas entran.
> 3. **Modelo conceptual ⚠️** — la gráfica actual mezcla dos propósitos: a veces se lee como
>    *evolución en el tiempo de una campaña* (línea continua) y a veces como *comparación
>    entre campañas distintas* (varias líneas superpuestas sin distinguirse bien). El
>    usuario no sabe si debe leerla como tendencia o como comparación.
> 4-7. No evaluables hasta resolver el punto 3.
>
> **Diagnóstico:** el problema no es el estilo visual de la gráfica, es que no se ha
> decidido si su función principal es mostrar tendencia o comparación.
>
> **Preguntas:**
> - ¿Quieres que el equipo compare campañas entre sí, o vea la evolución de una campaña
>   concreta en el tiempo?
> - ¿Hay una acción que deban tomar al ver un pico o una caída, o es solo informativo?

Solo tras responder eso tendría sentido bajar a estructura, interacción, layout y, ya al
final, al estilo visual concreto que Isabel quería iterar.
