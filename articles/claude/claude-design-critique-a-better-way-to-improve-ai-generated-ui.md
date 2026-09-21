---
title: Claude Design Critique: A Better Way to Improve AI-Generated UI
url: https://uxplanet.org/claude-design-critique-a-better-way-to-improve-ai-generated-ui-7efa1064bf8a
section: practica
subsection: Claude para diseñadores
date_added: 2026-08-26
---

**Nota importante:** este artículo describe un proceso de 4 fases útil como punto de partida, pero con dos límites que conviene tener en cuenta al aplicarlo: (1) el "fix" de cada fase se aplica en bloque, sin que el diseñador triage por severidad qué issues merece la pena arreglar; y (2) no hay ningún paso que re-verifique que una fase no deshace lo que arregló la anterior — se asume que la IA "ya lo sabe", pero nunca se comprueba. Detalle en las anotaciones subrayadas del texto.

## De qué va

Design critique es un paso integral en el proceso de diseño — la mejor manera de mejorar la calidad de lo que creas. Tradicionalmente era un ejercicio manual hecho por un diseñador o un equipo de diseño, pero cada vez más equipos empiezan a practicar un proceso de crítica asistido por IA: le pides a la IA que analice el diseño en detalle e identifique los problemas subyacentes. Claude Design es, según el autor, una de las herramientas más potentes para este tipo de trabajo.

Aunque la crítica de diseño parece una tarea sencilla para herramientas de IA, un buen flujo de trabajo en Claude Design debería ser mucho más estructurado que "revisa este diseño y dime qué está mal".

En el artículo, Nick Babich comparte su proceso de crítica de diseño asistido por IA con Claude Design, junto con los prompts que usa.

## Ejecutar una crítica por especialistas con IA

Según el autor, lo más importante del proceso de crítica de Claude Design es que sea un proceso **estructurado**. En vez de pedir una única crítica enorme, ejecuta 4 pases enfocados, en un orden específico.

El producto de ejemplo que usa para todo el artículo: una app bancaria móvil sencilla para iOS creada con Claude Design, usando el design system **IBM Carbon** como base.

## Fase 1: Crítica de accesibilidad

El autor cree firmemente que un audit de accesibilidad debería ser la fase #1 del proceso de crítica. Cuando el diseño es accesible para los usuarios, ya tienes una base sólida sobre la que construir el resto del diseño.

Prompt que usa para el audit de a11y en Claude Design:

```
Review this interface for accessibility issues including contrast, touch targets, focus order, semantic hierarchy and reliance on color.
```

El prompt se da directamente en el chat. Para las 4 fases de crítica, el autor usa **Opus 5 con High effort** — dice que es el equilibrio ideal entre una crítica en profundidad y un consumo de tokens aceptable.

En un par de minutos, Claude Design genera una lista de problemas de accesibilidad del diseño.

Lo que le gusta de este output es que se puede usar como input para el siguiente paso: pedirle a Claude que arregle los problemas encontrados. El prompt que usa para eso es simplemente:

```
fix issues you've identified
```

Lo que más valora del comportamiento de Claude Design es que, al trabajar sobre la lista de defectos a corregir, introduce los cambios uno a uno, dándote la oportunidad de revisar cada cambio y evaluar el resultado antes de que continúe.

Si comparas el resultado generado con el diseño original, el texto queda más legible y fácil de leer. La IA también corrige otros detalles sutiles, como el espaciado.

## Fase 2: Crítica de jerarquía visual

Una vez arreglados los problemas básicos de a11y, la jerarquía visual es lo siguiente en la lista.

La jerarquía visual define la estructura de la pantalla (cómo se colocan el contenido y los elementos funcionales en pantalla determina qué ven los usuarios primero, segundo, tercero...), y por eso tiene un impacto directo en la UX.

Para esta fase de crítica con IA, el autor quiere cambiar el foco: de la apariencia visual de la pantalla a su diseño funcional. El prompt que usa:

```
Ignore whether the UI looks attractive. Evaluate whether visual hierarchy correctly reflects the importance of information and actions.
```

Igual que en la fase anterior, Claude Design nombra todos los problemas de jerarquía visual. Con ese informe, se le puede pedir a Claude que arregle los problemas señalados.

El resultado que genera Claude Design juega con colores y contraste (pero sin romper las reglas de accesibilidad, porque la IA ya sabe qué es un diseño accesible) y con el espaciado. En conjunto, la pantalla principal de la app queda más limpia.

## Fase 3: Crítica de contenido

El orden en que se ejecuta el audit de contenido puede parecer contraintuitivo — al fin y al cabo, el contenido es lo que define la experiencia, no al revés. Pero tras trabajar bastante tiempo con Claude Design, el autor se dio cuenta de que la IA necesita un contexto adecuado desde el principio para poder generar un buen diseño. Por "contexto" se refiere a dos cosas:

- El **design system** (en su caso, IBM Carbon)
- Un **spec** que defina la arquitectura de información y los objetivos de negocio

Si le das esas dos cosas, Claude genera un diseño adecuado que luego se puede refinar. Por eso la crítica de contenido no trata tanto de encontrar problemas críticos en el diseño, sino de un pulido final del trabajo — si le diste a la IA un buen contexto desde el principio, el contenido ya debería ser bastante bueno.

Prompt que usa para la crítica de contenido:

```
Review the interface copy. Identify labels that are ambiguous, overly technical, unnecessarily long or don't clearly describe the consequence of an action.
```

Igual que en las fases anteriores, obtiene un informe que señala todos los problemas de contenido, y puede pedir a Claude que los arregle con un prompt de seguimiento ("fix issues you've found"). Según el autor, Claude refina el copy: añade detalles importantes y elimina información irrelevante.

## Fase 4: Crítica de diseño de interacción

La crítica y refinamiento del diseño de interacción es la fase final del proceso. En este punto ya deberías tener un diseño accesible, con buena jerarquía visual y un copy de UX relevante. Toca refinar el diseño añadiendo los estados interactivos que falten.

Prompt que usa para esta fase:

```
Evaluate only interactions and user states. Look for missing hover, focus, loading, empty, error, success and disabled states.
```

El autor hace una aclaración: su prompt menciona el estado "hover" para un diseño mobile (técnicamente, en móvil no hay hover). Es porque usa un prompt unificado tanto para apps web como móviles, pero según él esto no supone un problema para Claude, que trata el hover como el estado "pressed" para los controles funcionales.

---
Artículo original: https://uxplanet.org/claude-design-critique-a-better-way-to-improve-ai-generated-ui-7efa1064bf8a
