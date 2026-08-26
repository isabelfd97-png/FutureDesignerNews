---
name: add-article
description: Guarda un artículo o post (LinkedIn, blog, noticia) en el repo de aprendizaje de Isabel ("The Future Designer"), un sitio tipo periódico en "10 Articles and news" de su escritorio. Úsala SIEMPRE que diga "guárdame este artículo", "añade esto al repo", "guarda este post de LinkedIn", "archívalo", o pegue un link (sobre todo LinkedIn) pidiendo procesarlo/resumirlo. También si pega texto ya copiado pidiendo guardarlo. Isabel es senior product designer, no ingeniera, y la skill detecta jerga técnica (CLI, MCP, API, LLM...) y genera un glosario en lenguaje llano, guardable en "Enciclopedia". Lee el contenido (extensión de Chrome si hace falta login), extrae lo interesante, escribe una nota en Markdown con imágenes si las hay, la guarda en la sección correcta y regenera index.html.
---

# Add Article — repo de aprendizaje de Isabel

Isabel es senior product designer aprendiendo IA. Tiene un repo personal tipo periódico
(carpeta `10 Articles and news` en su escritorio) donde cada artículo que le interesa se
convierte en una nota corta en Markdown, clasificada por sección. Esta skill automatiza ese
proceso completo: leer el artículo → analizarlo → escribirlo en limpio → guardarlo en el
ordenador → regenerar el sitio.

No te limites a resumir: el objetivo es que la nota final sea *mejor* que el artículo
original para repasar rápido — capta la idea, por qué importa para un product designer
trabajando con IA, y dos o tres puntos que se puedan recordar sin releer nada.

## Dónde vive el proyecto

Todo el proyecto está en la carpeta conectada del escritorio de Isabel, normalmente
`~/Desktop/10 Articles and news`. Si no tienes acceso a esa carpeta en la sesión actual,
pide acceso con la herramienta de conectar carpeta antes de continuar — no improvises otra
ubicación.

Estructura relevante dentro de esa carpeta:

```
data/articles.json          <- índice maestro (una entrada por artículo)
articles/<sección>/<id>.md  <- el markdown real de cada artículo
images/<id>/                <- imágenes descargadas de ese artículo (si las hay)
build_repo.py                <- regenera index.html a partir de articles.json
scripts/save_article.py      <- helper que esta skill usa para guardar todo de una vez
index.html                   <- el sitio final, se regenera solo
```

Si `scripts/save_article.py` no existe todavía en el proyecto del usuario, cópialo desde
`scripts/save_article.py` (el que viene con esta skill) a la carpeta del proyecto antes de
usarlo.

## Las 6 secciones fijas

El sitio tiene siempre estas 6 secciones (no inventes otras salvo que Isabel lo pida
explícitamente):

| slug | nombre | de qué va |
|---|---|---|
| `design-2-0` | Design 2.0 | Cómo cambia la disciplina del diseño en la era de la IA: nuevos flujos, nuevas habilidades, principios de diseño en general (no específicos de una herramienta) |
| `claude` | Claude | Guías, features y forma de trabajar específicas de Claude: agentes, contexto, límites de uso, Claude Code |
| `figma` | Figma | Novedades, plugins y funciones de Figma, incluido lo que toca IA dentro de la propia herramienta (ej. Figma Make) |
| `engineering` | Engineering | Cómo colaborar mejor con developers: procesos, cultura, expectativas y lenguaje común |
| `ai` | AI | IA en general más allá de Claude: fundamentos, modelos, terminología de referencia |
| `materials` | Materials | Skills, plantillas, repos u otros recursos descargables que vienen incluidos en el propio artículo, listos para usar |

Algunos artículos pueden encajar en más de una a primera vista — usa esta guía rápida: si el
artículo es sobre todo una guía o feature *de Claude* (Claude Code, Claude Agents, Projects...),
va en `claude` aunque hable de IA en general. Si es sobre todo una idea o técnica *de diseño*
que resulta que se aplica con IA (principios, crítica de producto, cómo cambia el oficio), va
en `design-2-0` aunque mencione Claude de pasada. Si el artículo trae o enlaza un recurso
descargable concreto (una skill empaquetada, una plantilla de Figma, un repo de GitHub) y ESE
recurso es el motivo principal por el que Isabel lo guarda —no solo una idea que explica—, va
en `materials`, aunque también toque Claude o Figma de fondo: la pregunta clave es si lo que
importa es "usar esto" o "entender esto". Si dudas entre dos secciones, pregúntale a Isabel en
vez de forzar una — igual que con el contenido (Paso 4.5), mejor confirmar que adivinar mal una
clasificación que luego hay que deshacer.

Dentro de cada sección puedes usar cualquier `subsection` (texto libre, ej. "Fundamentos de
ML", "Design systems", "Prompting avanzado") — créala libremente según encaje el artículo,
no hace falta que exista de antemano.

## Paso 1 — Leer el artículo

- **Si Isabel pega texto directamente**: usa ese texto, no hace falta abrir nada.
- **Si pega un link**: intenta primero un fetch normal. Muchas páginas (y casi siempre
  LinkedIn) están detrás de login o se renderizan por JavaScript y el fetch normal vuelve
  vacío — en ese caso usa la extensión de Claude in Chrome (`navigate` a la URL, luego
  `get_page_text` para el texto y `read_page` o una captura para localizar imágenes). Si la
  extensión no está conectada, dile a Isabel que la conecte o que pegue el texto a mano —
  no inventes contenido que no has visto.
- Para posts de LinkedIn en concreto: el texto del post suele estar en las primeras líneas
  del `get_page_text`, seguido de comentarios — quédate solo con el post original del autor,
  ignora comentarios y sugerencias de LinkedIn.

## Paso 2 — Analizar y decidir la clasificación

Decide:
- **section**: la sección de la tabla de arriba que mejor encaje.
- **subsection**: una etiqueta corta y concreta del tema (2-4 palabras).
- **title**: si el artículo no tiene un título claro (típico en posts de LinkedIn), escribe
  uno tú, corto y directo, en el tono de un titular de periódico.
- **summary**: 1-2 frases que capten la idea central. Esto es lo que se ve en las tarjetas
  del sitio, así que tiene que enganchar y ser autoexplicativo.
- **key_points**: 3-5 bullets con lo que de verdad merece la pena recordar. No parafrasees
  cada frase del original — prioriza. Si el artículo es largo, es mejor perderse detalles
  que ahogar la idea principal.
- **content_md**: la nota completa en Markdown (ver formato abajo). Aquí sí puedes
  desarrollar un poco más que en el summary, pero sigue siendo una nota de repaso, no una
  traducción literal del artículo — reescribe con tus palabras, no copies párrafos enteros.

## Paso 2.5 — Glosario para aprender

Isabel es senior product designer, no ingeniera — está aprendiendo IA y código sobre la
marcha. Muchos artículos que guarda vienen cargados de jerga técnica (CLI, servidor MCP,
API, LLM, embeddings, npm, endpoint, repo, fine-tuning...) que ella no domina todavía y que
si no se explica, le corta el ritmo de lectura o la deja con la sensación de haberse perdido
algo importante.

Cada vez que proceses un artículo, repasa el texto buscando términos técnicos que probablemente
le resulten nuevos a alguien con perfil de diseño (no de ingeniería). Para cada uno, escribe
una definición corta (1-2 frases), en lenguaje llano, conectada si es posible con algo que
ella sí conoce del mundo del producto/diseño — la idea es que sirva como una tarjeta de
estudio, no una definición de manual.

No inventes términos que no aparecen en el artículo, y no expliques cosas obvias o que ya
maneja un product designer (no hace falta explicar "Figma" o "prototipo", por ejemplo). Si
el artículo no tiene jerga relevante, deja el glosario vacío — no fuerces entradas.

Guarda esto en un campo `glossary`, una lista de objetos `{"term": "...", "definition": "..."}`.
En el sitio, cada término aparece al final del artículo con un botón de "me gusta": si a
Isabel le interesa un término, lo guarda en una sección aparte llamada **Enciclopedia**, así
que las definiciones deben poder leerse solas, sin depender del contexto del artículo
original.

Ejemplo de una entrada de glosario buena:
```json
{"term": "Servidor MCP (Model Context Protocol)", "definition": "Un protocolo que permite que un agente de IA se conecte directamente a una herramienta o base de datos y la use, en vez de que un humano tenga que ir explicándole cómo hacerlo cada vez. Piénsalo como un 'enchufe universal' entre la IA y el software que ya existe."}
```

## Paso 3 — Imágenes

Si el artículo/post tiene imágenes relevantes (no avatares, no logos de LinkedIn, no
iconos de UI), reúne hasta 2-3 URLs de imagen. `scripts/save_article.py` las descarga y las
deja referenciadas en el markdown automáticamente — tú solo pasas las URLs. Si no hay
imágenes claras o relevantes, no fuerces nada; muchos artículos no las necesitan.

## Paso 4 — Formato del content_md

No fuerces siempre los mismos tres headers ("De qué va" / "Por qué le importa" / "Ideas
clave") — esa plantilla fija aplana artículos que no encajan en tres cajones iguales
(pasos concretos, ejemplos, código, una comparativa, una sola idea sin mucho desarrollo) y
hace que se pierda contenido real por encajarlo a la fuerza. La estructura de la nota tiene
que salir del propio artículo, no al revés.

Lo único obligatorio es que en algún punto de la nota quede claro **por qué le importa a
un product designer trabajando con IA** — no hace falta que sea su propio header si ya
queda tejido en el texto. A partir de ahí, usa el formato que mejor sirva a lo que trae el
artículo:

- Si el artículo da pasos o un proceso → una lista numerada o headers por paso, no un
  párrafo que los resuma.
- Si compara opciones o trade-offs → una tabla corta.
- Si trae código, comandos o plantillas → consérvalos en bloques de código, no los
  parafrasees en prosa.
- Si es una idea única sin mucho desarrollo → un par de párrafos sueltos, sin headers
  postizos solo para rellenar una estructura.
- Si el artículo mezcla varias cosas (una idea + un proceso + un ejemplo) → usa headers
  libres que reflejen esas partes, con los nombres que tengan sentido para ese contenido
  concreto.

Sigue reescribiendo con tus palabras, no traduzcas ni copies párrafos enteros del original
— pero prioriza no perder nada sustancial (pasos, reglas, listas, ejemplos, plantillas)
sobre que la nota quede visualmente uniforme con las demás. Si dudas si algo cabe o merece
su propia sección, pregúntale a Isabel antes de decidir tú qué se queda fuera (ver también
Paso 4.5).

No incluyas tú el enlace al original ni las imágenes dentro de este texto —
`save_article.py` añade las imágenes arriba y el enlace original al final automáticamente.

## Paso 3.5 — Materiales incluidos (solo para artículos de la sección `materials`)

Los artículos de `materials` no se leen como los de las demás secciones: Isabel no quiere un
muro de prosa explicando cada recurso, quiere poder escanear rápido qué hay y copiar lo que
necesite. Por eso, cuando `section` sea `materials`, además del `content_md` normal (que aquí
debe quedarse en un párrafo corto de contexto, no en la explicación completa), rellena un
campo `materials`: una lista de objetos, uno por cada recurso concreto que el artículo incluya
(una skill, una plantilla, un repo, un paquete...).

Cada objeto admite:
- **name** (obligatorio): nombre del recurso, corto.
- **tag** (opcional): una etiqueta de 1-2 palabras (ej. "Principal", "Visual style", "Legacy").
- **description** (opcional): 1 frase de qué hace, no un párrafo.
- **install** (opcional): el comando exacto para instalarlo/usarlo, si existe (ej. `npx skills add ...`). Se muestra en el sitio como un bloque de código que Isabel puede copiar con un clic.
- **url** (opcional): link directo a ese recurso concreto (no el artículo general, el recurso en sí si tiene su propia página).

Ejemplo:
```json
"materials": [
  {
    "name": "taste-skill v2 (experimental)",
    "tag": "Principal",
    "description": "Lee el brief, infiere la dirección de diseño correcta y evita interfaces con cara de plantilla.",
    "install": "npx skills add Leonxlnx/taste-skill --skill design-taste-frontend",
    "url": "https://github.com/Leonxlnx/taste-skill/tree/main/skills/taste-skill"
  }
]
```

Si un artículo de `materials` no trae recursos individuales claramente diferenciables (por
ejemplo, es un solo archivo o plantilla sin variantes), no fuerces la lista — un solo objeto
en `materials` está bien, o incluso ninguno si de verdad no aporta (aunque eso sería raro para
esta sección en concreto).

## Paso 4.5 — Revisar si el contenido necesita más contexto

Antes de guardar, relee el `content_md` que acabas de escribir con ojo crítico, como si
fueras Isabel repasándolo dentro de unas semanas sin memoria fresca del artículo original.
Algunos artículos (sobre todo los técnicos o los que dan por hecho conocimiento previo) dejan
huecos que un resumen fiel al original no cubre: mencionan una herramienta sin decir para qué
sirve, dan un dato suelto sin el porqué, o asumen un contexto que Isabel, como diseñadora
aprendiendo IA, no tiene todavía.

Si detectas que la nota se queda coja en algún punto y una explicación extra (un par de
frases, un ejemplo, una analogía con diseño) la haría más útil para repasar más adelante, no
la añadas directamente. En vez de eso, para antes de llamar a `save_article.py` y pregúntale
a Isabel qué te parece añadir, por ejemplo:

> "Antes de guardarlo: creo que valdría la pena añadir una explicación sobre [X], porque el
> artículo lo menciona sin desarrollarlo y puede que se pierda al repasar esto más adelante.
> ¿Te parece bien que lo añada, o lo dejo tal cual está?"

Si el artículo ya es autoexplicativo y no ves ningún hueco real, no hace falta preguntar nada
— sigue directo al Paso 5. La idea no es añadir contexto por sistema en cada artículo, sino
detectar cuándo de verdad hace falta y confirmarlo con ella antes de tocar el archivo final.

## Paso 5 — Guardar

Llama a `scripts/save_article.py` pasándole un JSON (por stdin o `--data-file`) con este
esquema. **Importante**: `save_article.py` se ejecuta con la herramienta de shell/bash, y
el shell suele ver las carpetas del usuario montadas en una ruta distinta a la que usan
Read/Write/Edit (algo como `/sessions/<id>/mnt/10 Articles and news`). Usa esa ruta de
shell en `project_dir`, no la ruta tipo `/Users/.../Desktop/...` — si no la conoces, revisa
las instrucciones de mapeo de rutas de shell de tu entorno actual antes de llamar al script.

```json
{
  "project_dir": "<ruta del proyecto TAL COMO LA VE EL SHELL, no la ruta de Finder>",
  "title": "...",
  "url": "https://...",
  "section": "ia-claude",
  "subsection": "...",
  "summary": "...",
  "key_points": ["...", "..."],
  "content_md": "## De qué va\n...",
  "image_urls": ["https://...jpg"],
  "glossary": [
    {"term": "...", "definition": "..."}
  ],
  "materials": [
    {"name": "...", "tag": "...", "description": "...", "install": "...", "url": "..."}
  ]
}
```

Ejemplo de invocación:

```bash
python3 scripts/save_article.py --data-file /tmp/article.json
```

El script se encarga de: generar un id único (slug del título), descargar y guardar
imágenes en `images/<id>/`, escribir `articles/<sección>/<id>.md`, añadir la entrada a
`data/articles.json`, y ejecutar `build_repo.py` para regenerar `index.html`. Es idempotente
respecto al `id` — si lo vuelves a llamar con el mismo título, actualiza la entrada en vez
de duplicarla.

Si algo falla (por ejemplo una imagen no se puede descargar), el script sigue adelante sin
esa imagen — no dejes que un fallo de imagen bloquee el guardado del artículo.

## Borrado definitivo (cuando Isabel te lo pida desde el chat)

En el sitio, la fila de un artículo en Historial se puede mandar a la papelera y desde ahí
restaurar o "eliminar definitivamente". El botón de eliminar definitivo no puede tocar el
disco por sí solo (el sitio es HTML estático) — por eso muestra un aviso pidiéndole a Isabel
que te lo confirme aquí, con una frase tipo `Elimina definitivamente el artículo: "<título>"
(id: <id>)`.

Cuando recibas ese mensaje (o cualquier petición equivalente de borrar un artículo del
repo), usa `scripts/delete_article.py`, que viene junto a `save_article.py`:

```bash
python3 scripts/delete_article.py --project-dir "<ruta del proyecto vista por el shell>" --id <article-id>
```

Esto borra la entrada de `data/articles.json`, el `.md` correspondiente y su carpeta de
imágenes si existe, y regenera `index.html`. Si no tienes el `id` a mano, puedes leer
`data/articles.json` y buscarlo por título.

## Paso 6 — Confirmar

Cuando termine, dile a Isabel en qué sección quedó el artículo y comparte el `index.html`
actualizado (con la herramienta de presentar archivos). Sé breve — ella puede abrir el sitio
y verlo, no hace falta que describas la nota entera en el chat.
