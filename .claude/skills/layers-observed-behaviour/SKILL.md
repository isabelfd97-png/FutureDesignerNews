---
name: layers-observed-behaviour
description: >-
  Convierte notas de investigación de usuarios (entrevistas, comentarios, observaciones) en
  job stories con una etiqueta de confianza — 🟢 Observado, 🟡 Inferido, 🔴 Asumido — que
  separa lo que se vio literalmente de lo que se interpretó o se dio por hecho. Úsala cuando
  Isabel tiene notas o comentarios reales de gente (reviews de un equipo, feedback de
  usuarios) y quiere sacar conclusiones sin colar suposiciones propias como si fueran datos
  verificados.
---

# Layers Observed Behaviour — separar lo visto de lo asumido

> Fuente: [jamiemill/layers-skills](https://github.com/jamiemill/layers-skills)

Es fácil, al escribir notas de investigación, mezclar sin darse cuenta una observación real
con una interpretación propia. "El usuario no entendía el dashboard, así que prefiere
interfaces simples" tiene una parte vista (no entendía el dashboard) y una parte inventada
(prefiere interfaces simples) que puede ser cierta o no. Esta skill obliga a separarlas
explícitamente antes de construir nada sobre esas conclusiones.

## Cuándo se activa

Isabel trae notas, comentarios o transcripciones reales (feedback de una review de equipo,
comentarios de usuarios, notas de una conversación) y quiere convertirlas en necesidades
accionables. También si pide explícitamente "hazme un `/layers-observed-behaviour`" o
"sepárame lo observado de lo asumido".

Es prima de `layers-user-needs` (mismo formato job story), pero se usa cuando **ya hay
material de investigación real** de por medio — `layers-user-needs` sirve para partir de
una idea o queja vaga sin necesariamente tener notas escritas.

## Paso 1 — Lee el material tal cual, sin resumir de más

Pide o usa el texto original de las notas/comentarios. No trabajes sobre un resumen que ya
hayas hecho tú antes — el resumen es precisamente donde se cuelan las inferencias sin
marcar.

## Paso 2 — Extrae job stories con etiqueta de confianza

Por cada necesidad que salga del material, escribe la job story en el formato ya conocido
("Cuando..., quiero..., para poder...") y etiquétala:

- 🟢 **Observado** — está dicho o mostrado literalmente en el material. Cita la fuente
  (la frase o el comentario concreto).
- 🟡 **Inferido** — es una lectura razonable de lo observado, pero implica un salto lógico.
  Explica cuál es el salto.
- 🔴 **Asumido** — no está respaldado por el material, es una suposición previa (tuya o de
  Isabel) que se coló. Dilo explícitamente y no la trates como base sólida.

No conviertas automáticamente una frase vaga o aislada ("creo que la gente en general...")
en un 🟢. Si Isabel misma usó palabras como "creo que" o "en general" al describir lo que
vio, eso ya es una señal de que es 🟡 o 🔴, no 🟢.

## Paso 3 — Marca qué se puede actuar ya y qué necesita validarse

Las 🟢 son sólidas para actuar. Las 🟡 sirven para orientar pero conviene contrastarlas. Las
🔴 no deberían usarse para justificar una decisión de producto sin validarlas primero —
dilo explícitamente si Isabel parece a punto de construir algo apoyándose solo en una 🔴.

## Ejemplo completo — iterando algo que ya existe

Isabel trae esta nota: *"En la review de la gráfica de campañas, dos personas del equipo
dijeron que no entendían qué eje era cuál. Uno comentó que prefería ver barras en vez de
líneas. Creo que en general a la gente no le gustan los gráficos de líneas."*

**Job story 1** 🟢 Observado — Cuando alguien del equipo mira la gráfica, quiere que los
ejes estén etiquetados con claridad, para poder leerla sin tener que preguntar. (Basado en
el comentario literal de dos personas sobre no entender qué eje era cuál.)

**Job story 2** 🟡 Inferido — Cuando alguien compara campañas, quiere ver barras en vez de
líneas, para poder distinguir valores discretos más fácilmente. (Una persona lo pidió
directamente, pero es una preferencia individual, no confirmada en el resto del equipo.)

**Job story 3** 🔴 Asumido — "a la gente en general no le gustan los gráficos de líneas" —
generalización de Isabel a partir de un solo comentario. No construir sobre esto sin
confirmarlo con más gente del equipo.

Contraste con no usar la skill: sin separar la confianza, las tres frases habrían salido con
el mismo peso ("el equipo prefiere barras y no le gustan las líneas"), colando una
suposición como si fuera un hecho verificado por todo el equipo.
