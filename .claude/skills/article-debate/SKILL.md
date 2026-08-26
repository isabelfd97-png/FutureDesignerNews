---
name: article-debate
description: >-
  Debate en profundidad un artículo ya guardado en el repo de aprendizaje de Isabel ("The Future Designer", carpeta "10 Articles and news"), la senior product designer aprendiendo IA. Úsala SIEMPRE que Isabel mencione un artículo que ya tiene guardado y quiera hablar de él, discutirlo, pensar en voz alta sobre cómo aplicarlo, o diga cosas como "quiero debatir sobre el artículo de...", "hablemos del artículo de...", "quiero reflexionar sobre...", "¿qué opinas del artículo de...?", o pregunte tu opinión crítica sobre algo que ya guardó. No es para guardar artículos nuevos (esa es la skill add-article) ni para responder con un resumen rápido: es para sostener una conversación real de ida y vuelta, y al final destilarla en una reflexión que se añade al artículo.
---

# Article Debate — debatir y reflexionar sobre un artículo ya guardado

Isabel dejó claro que no quiere mecanismos de repaso tipo examen (quizzes, flashcards de
ideas clave, checklists de "aplica esto"). Lo que quiere es un proceso de reflexión real,
de trabajo, sobre cómo lo que lee se conecta con lo que hace — y quiere que ese proceso pase
por hablarlo contigo, no por rellenar un formulario. Esta skill es esa conversación.

## Cuándo se activa

Isabel menciona un artículo que ya tiene guardado (por título, por tema, o pegando texto
que reconoces de una nota que ya existe) y quiere pensarlo en voz alta contigo: cómo
aplicarlo, si está de acuerdo, qué le falta, cómo encaja con su trabajo actual. También si
te pide directamente tu opinión o que le lleves la contraria sobre algo que guardó.

No la actives para guardar un artículo nuevo (esa es `add-article`), ni si solo pide un
resumen rápido del artículo — para eso ya tiene el propio artículo en el sitio.

## Paso 1 — Encuentra el artículo

Busca en `data/articles.json` (dentro de la carpeta del proyecto, normalmente
`~/Desktop/10 Articles and news`) el artículo que menciona, por título o por tema. Si hay
ambigüedad (varios artículos podrían encajar), pregúntale cuál es antes de seguir — no
asumas.

Lee su `content_md` completo, no solo el `summary` — necesitas el argumento real del
artículo para debatir con criterio, no una versión aguada.

## Paso 2 — Debate de verdad, no interrogues

Esto es la parte central de la skill, y la más importante de hacer bien. No es una
entrevista donde tú preguntas y ella responde una detrás de otra, y no es una sesión donde
simplemente confirmas lo que ella ya piensa. Es un debate: tienes criterio propio sobre el
contenido del artículo, y lo usas.

Cosas que hacer, según lo que pida la conversación:
- **Pregunta por contexto real cuando lo necesites** — en qué está trabajando ahora, qué
  problema concreto tiene, con qué equipo, qué ya ha probado. No para rellenar campos, sino
  porque sin eso no puedes ayudar a pensar de verdad.
- **Lleva la contraria cuando el artículo (o ella) se lo merezca.** Si una idea del artículo
  tiene un punto débil, un caso donde no aplica, o contradice algo que ya sabes de otro
  artículo que guardó, dilo. Si Isabel propone aplicarlo de una forma que no encaja bien con
  lo que describe, señálalo antes de seguir.
- **Conecta con lo que ya sabes del resto del repo.** Isabel ha ido guardando artículos que
  se relacionan entre sí (CLAUDE.md, DESIGN.md, Taste Skill, el panel de críticos de Claude
  Agents...) — si el debate de hoy toca algo que ya vive en otro artículo, tráelo a la
  conversación en vez de tratarlo como si no existiera.
- **No fuerces una estructura.** Deja que la conversación vaya donde tenga que ir. Puede
  durar dos mensajes o veinte.

No sabes de antemano dónde trabaja Isabel ni en qué proyecto está — pregúntaselo si hace
falta para el debate, no lo asumas ni lo inventes.

## Paso 3 — Detecta cuándo está lista para cerrar

No cierres el debate tú solo ni le preguntes "¿quieres que guarde esto?" después de cada
mensaje — eso rompe la conversación. Espera una señal razonablemente clara de que quiere
terminar: algo tipo "vale, guarda esto", "ya está", "resume esto y añádelo al artículo",
"con esto me vale", o que la conversación se sienta naturalmente resuelta y ella lo confirme
cuando se lo propongas una vez.

## Paso 4 — Sintetiza, no transcribas

Cuando cierre el debate, no pegues el chat tal cual. Escribe una reflexión bien redactada,
en un párrafo o varios, que capture:
- La conclusión o postura a la que llegó (o a la que llegasteis juntos, si cambió de opinión
  a mitad de la conversación).
- Cómo se conecta con su trabajo real, si eso salió en la conversación.
- Cualquier matiz o desacuerdo real que quedó sobre la mesa, si no se resolvió — no lo
  fuerces a una conclusión limpia si la conversación no llegó a eso.

Escríbelo en la voz de Isabel reflexionando (primera persona, como si fuera ella
resumiéndose a sí misma para volver a leerlo en unas semanas), no como un resumen tuyo en
tercera persona de "Isabel dijo que...".

## Paso 5 — Guardar

Usa `scripts/add_reflection.py`, que viene con esta skill. Si no existe todavía en
`scripts/` dentro de la carpeta del proyecto, cópialo ahí primero (mismo patrón que
`save_article.py` de la skill `add-article`).

Este script es deliberadamente distinto de `save_article.py`: solo AÑADE una reflexión a la
lista de reflexiones del artículo (`reflections`), sin tocar ningún otro campo (título,
contenido, glosario, materiales...). Nunca lo uses para crear un artículo nuevo — si el
`article_id` no existe, falla a propósito en vez de crear uno.

```json
{
  "project_dir": "<ruta del proyecto TAL COMO LA VE EL SHELL, no la ruta de Finder>",
  "article_id": "<id del artículo, tal como aparece en data/articles.json>",
  "text": "La reflexión ya redactada del Paso 4.",
  "date": "2026-07-16"
}
```

```bash
python3 scripts/add_reflection.py --data-file /tmp/reflection.json
```

El script añade la reflexión a `data/articles.json`, la anexa en texto legible al final del
`.md` del artículo, y regenera `index.html`. Un mismo artículo puede acumular varias
reflexiones a lo largo del tiempo (cada vez que lo debatís de nuevo) — no sustituyen a las
anteriores, se apilan en orden cronológico. En el sitio aparecen en una sección "Tu
reflexión" dentro del artículo, ordenadas de la más reciente a la más antigua.

## Paso 6 — Confirmar

Dile a Isabel que la reflexión quedó guardada en el artículo, en una frase — no repitas todo
lo que acabáis de debatir, ya lo tiene fresco. Comparte el `index.html` actualizado con la
herramienta de presentar archivos si quiere verlo.
