---
title: Los diseñadores gastan los límites de uso de Claude más rápido que nadie: por qué y cómo arreglarlo
url: https://yummy-design-sprint.notion.site/Designers-hit-Claude-s-usage-limits-faster-than-anyone-Here-s-why-and-exactly-how-to-fix-it-33562791470980b78c4bc906178bc83f
section: ia-claude
subsection: Claude para diseñadores
date_added: 2026-07-12
---

## De qué va
Una guía de Yummy Labs sobre por qué los diseñadores queman los límites de uso de Claude más rápido que casi cualquier otro perfil, y qué hacer para arreglarlo sin dejar de trabajar bien.

## El problema de fondo
Cada mensaje que envías a Claude reprocesa TODA la conversación anterior. El mensaje número 30 cuesta como si volvieras a enviar del 1 al 30 juntos. Por eso pedir "hazlo un poco más grande" cinco veces seguidas, cada una en su propio mensaje, es tan caro: cada ronda relee todo lo anterior.

## Las dos cosas que gastan tu límite
- **Coste por token**: lo que cuesta cada token contra tu límite, según el modelo. La misma conversación en Opus cuesta 5 veces más que en Sonnet.
- **Consumo (burn)**: cuántos tokens gastas por tus propios hábitos — subir un PDF entero cuando podrías pegar el markdown, dejar que Claude escriba 500 palabras cuando necesitabas una frase, o mantener una conversación 30 mensajes cuando deberías haber empezado una nueva en el mensaje 10.

El coste es el multiplicador, el consumo es el volumen. Reducir uno se nota; reducir los dos hace que dejes de tocar el límite.

## Los planes, en cifras
Todos comparten el mismo cupo entre claude.ai, Claude Code, la app de escritorio y Cowork — una sesión intensa de Claude Code por la mañana deja menos mensajes disponibles en el chat por la tarde.

- **Free**: ~40 mensajes cortos al día — para probarlo, no para trabajar en serio.
- **Pro (20$/mes)**: ~44.000 tokens por ventana de 5 horas — bien para aprender, ajustado para diseño pesado.
- **Max5 (100$/mes)**: ~88.000 tokens — cómodo para trabajo diario de diseño.
- **Max20 (200$/mes)**: ~220.000 tokens — usuarios intensivos, varios proyectos a la vez.

## Por qué los diseñadores gastan tan rápido
- **La iteración visual en bucle**: "hazlo más grande" → "mejor más pequeño" → "¿lo centras?" → "el color no cuadra". Cada una de estas peticiones minúsculas reprocesa toda la conversación; en el mensaje 10 ya estás pagando por reenviar los 9 anteriores cada vez.
- **El impuesto de las herramientas MCP**: cada conector que tienes activo carga su definición en cada mensaje, lo uses o no. Sin herramientas: 0 tokens de más. Solo Figma MCP: ~4.000 tokens (~10% del cupo Pro antes de escribir nada). 4 herramientas conectadas: ~7.000 tokens (~16%). Una instalación pesada (5+ herramientas): hasta 55.000 tokens, capaz de superar todo tu cupo.
- **El error de selección en Figma**: seleccionar toda la página en vez de solo el componente en el que trabajas. Un componente suelto: 2.000-10.000 tokens. La página entera: 200.000+ tokens. Una diferencia de 20 a 100 veces.
- **El modelo equivocado para la tarea**: usar Opus para retoques de copy cuando Sonnet resuelve el 98% de las tareas de diseño con un 80% menos de coste.

## Diez situaciones típicas que queman el límite
La guía repasa diez escenarios concretos —iterar visualmente, construir un componente con retoques pequeños, usar Figma MCP, subir los mismos archivos una y otra vez, compartir mockups para revisión, pedir feedback de diseño, investigar y hacer brainstorming, tener conectores MCP siempre activos, usar el modelo equivocado, y dejar el extended thinking siempre encendido— y para cada uno da la versión cara y la versión barata de hacerlo.

## ¿Se puede entrenar a Claude para ser eficiente en tokens? Sí, con una Skill
Se puede crear un archivo SKILL.md que le indique a Claude que sea consciente de los tokens: por ejemplo, que constriña sus respuestas, que pida confirmación antes de generar mucho texto, o que use el modelo adecuado por defecto. Una Skill es un archivo de instrucciones que Claude lee y sigue automáticamente, así que "entrenas" un comportamiento una vez en vez de repetirlo en cada conversación. Y no es solo para eficiencia: crear Skills para las cosas que repites constantemente hace que Claude acierte a la primera en vez de necesitar cinco rondas de correcciones.

## La parte incómoda: los prompts vagos también gastan
Usar Claude mucho puede volvernos perezosos al escribir, y un prompt perezoso sale caro: si no das las specs por adelantado (padding, fuentes, colores, spacing), Claude tiene que adivinar, tú corriges, y cada corrección reprocesa todo lo anterior. El arreglo es pensar antes de escribir, no después.

## La chuleta rápida
Antes de empezar una sesión: ¿tienes Sonnet seleccionado (no Opus)?, ¿extended thinking apagado para tareas simples?, ¿solo los conectores MCP que necesitas activos?, ¿el contenido reutilizable ya está en Project Knowledge? Durante el trabajo: junta el feedback y mándalo en un solo mensaje, da las specs por adelantado, constriñe la respuesta ("máximo 3 puntos"), recorta las imágenes sin piedad. Empieza una conversación nueva al terminar una tarea, cada 15-20 mensajes, o al cambiar a un tema no relacionado.

## Ideas clave
- Cada mensaje reprocesa toda la conversación: cuanto más larga, más caro cada turno nuevo.
- El coste depende del modelo (Opus vs Sonnet) y el consumo depende de tus hábitos (qué subes, cuánto dejas escribir a Claude, cuándo empiezas de cero).
- Seleccionar solo el componente en Figma MCP en vez de la página entera puede ahorrar hasta 100 veces los tokens.
- Los conectores MCP activos cobran un peaje en cada mensaje aunque no los uses ese turno — desconecta los que no necesites.
- Una Skill puede 'entrenar' a Claude a ser eficiente o a acertar a la primera en tareas repetitivas, sin tener que repetir instrucciones cada vez.

## Para aprender
- **Rate limit / ventana de uso**: El cupo de tokens que tienes disponible dentro de una ventana de tiempo (por ejemplo, 5 horas), según tu plan. Se comparte entre todas las formas de usar Claude —chat, Claude Code, la app de escritorio, Cowork— así que gastarlo en un sitio deja menos disponible en los demás.
- **Extended thinking**: Un modo en el que Claude 'piensa' de forma más extendida antes de responder, útil para tareas complejas, pero que cuesta bastantes tokens de más (unos 32.000 por petición) incluso en tareas sencillas donde no hace falta. Apagarlo para preguntas simples ahorra buena parte del cupo.
- **Modelo (Opus vs Sonnet)**: Las distintas 'versiones' de Claude que puedes elegir para una conversación. Opus es más potente pero cuesta unas 5 veces más tokens que Sonnet por el mismo trabajo; para la mayoría de tareas de diseño, Sonnet da un resultado prácticamente igual de bueno a una fracción del coste.
- **Skill (archivo SKILL.md)**: Un archivo de instrucciones que Claude lee y aplica automáticamente sin que tengas que repetirlas cada vez — por ejemplo, para que sea más breve por defecto, o para que resuelva bien una tarea que sueles pedirle. Es la forma de 'enseñarle' un comportamiento de una vez, en lugar de corregirlo conversación tras conversación.

---
Artículo original: https://yummy-design-sprint.notion.site/Designers-hit-Claude-s-usage-limits-faster-than-anyone-Here-s-why-and-exactly-how-to-fix-it-33562791470980b78c4bc906178bc83f
