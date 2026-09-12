---
name: market-scan
description: >-
  Análisis de entorno macro combinando cuatro marcos clásicos de estrategia de negocio:
  SWOT (fortalezas/debilidades/oportunidades/amenazas), PESTLE (factores
  Político/Económico/Social/Tecnológico/Legal/Medioambiental), Porter's Five Forces
  (rivalidad, proveedores, compradores, sustitutos, nuevos entrantes) y Ansoff Matrix
  (opciones de crecimiento). Úsala en momentos de alto impacto pero poco frecuentes: antes
  de una reunión de planificación donde se decide qué se prioriza, para defender una
  inversión de diseño grande con argumentos de negocio, al proponer una iniciativa nueva
  que quieres que se tome en serio desde el principio, o preparándote para hablar del
  posicionamiento de una empresa en una entrevista de trabajo. No es una skill de uso diario
  — es para los momentos donde importa tener un asiento en la mesa de decisión de negocio.
---

# Market Scan — SWOT + PESTLE + Porter's + Ansoff en un solo análisis

> Fuente: [phuryn/pm-skills — pm-product-strategy](https://github.com/phuryn/pm-skills)

Combina cuatro marcos clásicos de estrategia de negocio en un único análisis de entorno
macro. A diferencia de las skills orientadas a features (`discover`,
`opportunity-solution-tree`...), esta no ayuda a decidir qué construir — ayuda a entender
el contexto de mercado y competitivo en el que se toma esa decisión.

## Los cuatro marcos

1. **SWOT** — Fortalezas y Debilidades (internas al producto/equipo) + Oportunidades y
   Amenazas (externas, de mercado).
2. **PESTLE** — factores macro: Político, Económico, Social, Tecnológico, Legal,
   Medioambiental. No mira el producto, mira el mundo alrededor.
3. **Porter's Five Forces** — posición competitiva dentro de la industria: rivalidad entre
   competidores, poder de negociación de proveedores, poder de negociación de compradores,
   amenaza de sustitutos, amenaza de nuevos entrantes.
4. **Ansoff Matrix** — opciones de crecimiento: si lo que se plantea es penetración de
   mercado, desarrollo de producto, desarrollo de mercado, o diversificación.

## Cuándo se activa

Es una skill de uso poco frecuente pero de alto impacto — no para decisiones semanales.
Úsala cuando:
- Isabel se prepara para una reunión de planificación donde se decide qué se prioriza a
  nivel de negocio, no solo de producto.
- Quiere defender una inversión de diseño grande con argumentos de mercado/competencia, no
  solo de experiencia de usuario.
- Propone ella misma una iniciativa nueva y quiere que se tome en serio desde el principio.
- Se prepara para hablar del posicionamiento de una empresa (la suya o una a la que
  aspira) en una entrevista de trabajo.

También si pide explícitamente `/market-scan [contexto]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir** — con cuatro marcos encadenados hace falta más
contexto que en las skills sueltas, pero pide solo lo mínimo imprescindible:
- ¿En qué sector/industria opera la empresa?
- ¿Hay competidores directos ya haciendo algo parecido, o sería pionero?
- ¿Es para los mismos clientes actuales, o se buscarían clientes nuevos?

**2. Construye los cuatro marcos en orden** (SWOT → PESTLE → Porter's → Ansoff). En
PESTLE, no fuerces los 6 factores si alguno no tiene impacto real detectado — dilo
explícitamente en vez de rellenar por rellenar.

**3. Marca con ⚠️ cualquier punto que dependa de información que Isabel no ha confirmado**
(ej. temas legales/privacidad, competidores que podrían existir sin que ella lo sepa).

**4. Termina con una recomendación**: cuál de los puntos ⚠️ es más urgente resolver antes
de avanzar, y por qué cambiaría la decisión si resultara distinto a lo asumido.

## Ejemplo

**Isabel escribe:**
> `/market-scan` mi empresa se plantea lanzar la feature de comparación automática de
> campañas como producto independiente, no solo como parte del dashboard actual

**Preguntas antes de construir:**
> Antes del análisis completo, dime:
> - ¿En qué sector/industria opera vuestra empresa?
> - ¿Sabes si hay competidores directos ya haciendo esto como producto separado, o sería
>   pionero?
> - ¿Sería para los mismos clientes que ya tenéis, o buscaríais clientes nuevos?

**Isabel responde:**
> Somos una empresa de marketing tech, vendemos software a equipos de marketing. Hay un
> par de herramientas sueltas de analítica de campañas en el mercado, pero ninguna con
> recomendación automática de "qué repetir". Sería para los mismos clientes que ya
> tenemos.

**Output final:**

> **1. SWOT**
> - Fortalezas: ya se tienen los datos de campañas de los clientes actuales — ventaja de
>   datos frente a un competidor nuevo.
> - Debilidades ⚠️: sin experiencia previa vendiendo un producto separado (siempre ha sido
>   parte del paquete).
> - Oportunidades: nadie más ofrece "recomendación automática", solo analítica pasiva.
> - Amenazas: un competidor grande podría copiarlo rápido si funciona bien.
>
> **2. PESTLE** (solo factores relevantes)
> - Tecnológico: viable ya con los datos actuales.
> - Legal ⚠️: a confirmar — comparar campañas entre clientes distintos podría tocar
>   cláusulas de privacidad de datos, según cómo se entrene la recomendación.
> - Político, Económico, Social, Medioambiental: sin impacto directo detectado.
>
> **3. Porter's Five Forces**
> - Rivalidad: baja por ahora (nadie hace justo esto).
> - Poder de compradores: alto — son los propios clientes actuales, pueden no pagar el
>   extra si no ven valor claro.
> - Amenaza de sustitutos: alta — Excel manual sigue siendo gratis y "suficiente" para
>   muchos.
> - Amenaza de nuevos entrantes: media — la ventaja de datos protege un tiempo, no para
>   siempre.
>
> **4. Ansoff Matrix**
> - Encaja como **desarrollo de producto** (nuevo producto, mismos clientes) — la opción
>   de menor riesgo de las cuatro, porque no hay que conseguir clientes nuevos.

**Recomendación final:**
> El punto más urgente a resolver antes de avanzar es el ⚠️ Legal (privacidad de datos
> entre clientes) — si eso bloquea la recomendación automática, cambia el diseño del
> producto entero. Es más barato aclararlo ahora que después de construir.
