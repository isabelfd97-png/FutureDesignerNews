---
name: layers-user-needs
description: >-
  Elicita y prioriza necesidades de usuario en formato job story ("Cuando [situación],
  quiero [motivación], para poder [resultado]") a partir de una idea vaga o una queja
  general, y devuelve oportunidades priorizadas listas para decidir qué construir. Úsala
  cuando Isabel tiene una idea de feature poco definida ("quiero añadir X pero no sé qué
  debería tener"), cuando parte de una queja u observación general de usuarios (suya o
  ajena) y quiere convertirla en algo accionable, o cuando quiere evitar saltar directo a
  "solución plausible" sin haber verificado cuál es el problema real.
---

# Layers User Needs — de queja vaga a oportunidades priorizadas

> Fuente: [jamiemill/layers-skills](https://github.com/jamiemill/layers-skills)

El error más común al diseñar una feature nueva es saltar directo a la solución ("necesita
tarjetas, filtros y un buscador") sin haber verbalizado cuál es la necesidad real. Esa
solución suena razonable porque sigue patrones conocidos, pero no hay garantía de que
resuelva el problema correcto. Esta skill fuerza a pasar primero por el formato **job
story** antes de proponer nada.

## Formato job story

> **Cuando** [situación/contexto en la que está el usuario], **quiero** [motivación],
> **para poder** [resultado que busca].

Se empieza por la *situación*, no por "el usuario quiere" ni por un rol/persona — eso evita
estereotipar y mantiene el foco en el contexto real que dispara la necesidad.

## Cuándo se activa

Isabel propone una idea de feature o gráfica nueva sin tener claro qué debería incluir, o
parte de una queja/observación general (suya, de su equipo, de usuarios) que quiere
convertir en algo accionable. También si pide explícitamente "hazme un
`/layers-user-needs`" o "sácame job stories de esto".

No la actives si Isabel ya trae la necesidad claramente especificada y solo quiere ejecutar
— para eso no hace falta este paso de elicitación.

## Paso 1 — Elicita antes de asumir

Si el input de Isabel es vago (una queja general, una idea sin contexto), no saltes directo
a job stories inventadas. Haz 1-3 preguntas concretas para afinar, por ejemplo:
- ¿Quién va a mirar/usar esto en la práctica — el usuario final, o alguien internamente
  revisando resultados?
- ¿Qué decisión tomará esa persona después de verlo?
- ¿Hay una situación concreta (un momento, un disparador) en la que esto surge?

No inventes el "cuándo" ni el "para poder" sin tener con qué sustentarlos — job stories
inventadas de la nada son tan inútiles como "los usuarios quieren un dashboard".

## Paso 2 — Escribe las job stories

Con las respuestas, redacta 1-3 job stories en el formato exacto de arriba. Sé específica:
el "cuándo" debe describir una situación reconocible, no una generalidad ("cuando uso la
gráfica" no vale; "cuando cierra una campaña y necesita decidir si repetirla" sí).

## Paso 3 — Prioriza como oportunidades

Convierte cada job story en una oportunidad concreta (qué se podría construir), y ordénalas
por lo accionable que son ahora mismo:
- 🔴 Alta — resuelve directamente la necesidad, barato de construir ya.
- 🟡 Media — ayuda, pero es más trabajo o depende de lo anterior.
- ⚪ Baja / a validar — plausible pero sin señal suficiente todavía; no construir sin
  validar primero.

No conviertas automáticamente la primera idea que tenías en la prioridad alta solo porque
era la idea original — la prioridad sale de qué tan directamente ataca la job story, no de
qué tan familiar suena.

## Ejemplo completo — creando algo nuevo desde cero

Isabel: *"Quiero crear una gráfica nueva de métricas de uso de campañas para los usuarios,
pero no sé bien qué debería mostrar."*

Preguntas de elicitación:
- ¿Quién va a mirar esta gráfica — el propio usuario final, o el equipo de marketing
  revisando resultados?
- ¿Qué decisión tomarán después de verla?

Isabel responde: *"La mira el equipo de marketing, y quieren decidir qué campaña repetir el
mes que viene."*

**Job stories:**
1. Cuando el equipo de marketing cierra una campaña, quiere compararla con campañas
   anteriores similares, para poder decidir si repetirla el próximo mes.
2. Cuando ve una caída brusca en el uso durante una campaña, quiere saber en qué momento y
   canal ocurrió, para poder diagnosticar la causa antes de la siguiente campaña.

**Oportunidades priorizadas:**
- 🔴 Alta: gráfica comparativa de rendimiento entre campañas (no solo la evolución de una
  sola campaña aislada).
- 🟡 Media: anotaciones en la línea temporal marcando eventos relevantes (lanzamiento,
  cambio de canal).
- ⚪ Baja / a validar: desglose por canal dentro de cada campaña — más trabajo, sin señal
  todavía de que haga falta ese nivel de detalle.

Contraste con no usar la skill: sin este paso, la respuesta habría saltado directo a "un
gráfico de líneas con filtros por fecha" — plausible, pero sin verificar qué decisión debía
soportar la gráfica.
