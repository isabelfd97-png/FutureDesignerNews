---
name: benchmark
description: >-
  Estructura un análisis de benchmarking competitivo — cómo resuelven distintos
  competidores un mismo patrón o problema de interfaz — con tabla comparativa y gap
  analysis, ahorrando el tiempo de organizar lo que se ha visto (no el de mirarlo). Úsala
  cuando Isabel quiera comparar cómo resuelven otros un problema concreto de diseño, y
  tenga capturas de pantalla, descripciones o material real de competidores que aportar.
---

# Benchmark — comparación competitiva estructurada

> Fuente: [Owl-Listener/designer-skills — ux-strategy](https://github.com/Owl-Listener/designer-skills)

Estructura una comparación de cómo distintos competidores resuelven un mismo patrón o
problema de interfaz, en vez del proceso manual de abrir Mobbin o apps reales y apuntar
cosas en un documento durante horas.

## ⚠️ Limitación real — léela antes de usar la skill

No hay acceso a capturas de pantalla de competidores en vivo ni a navegar por Mobbin de
forma autónoma. La skill funciona de dos formas honestas:

1. **Isabel aporta el material** (capturas de pantalla, descripciones de lo que ha visto) y
   el análisis se estructura sobre eso — este es el modo fiable, y el que hay que preferir
   siempre que sea posible.
2. **Isabel pide usar conocimiento general** de patrones conocidos de cierta app — esto
   puede estar desactualizado o ser genérico, porque no se ha mirado la versión actual de
   esa app. En este caso, **hay que advertirlo explícitamente** antes de dar el análisis,
   nunca presentarlo como si se acabara de mirar la app en directo.

Nunca prometas que esto sustituye por completo el tiempo de mirar las apps — ahorra el
tiempo de **estructurar** lo que Isabel ya ha visto o va recopilando, no el de mirarlas.

## Cuándo se activa

Isabel quiere comparar cómo resuelven otros un problema concreto de diseño (no "cómo es la
app entera de un competidor", sino un patrón específico: cómo comparan datos, cómo filtran,
cómo hacen onboarding...) y tiene o puede conseguir material real que aportar. También si
pide explícitamente `/benchmark [patrón a comparar]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Qué patrón concreto interesa comparar? (no "la app entera", algo específico)
- ¿El objetivo es inspiración para replicar lo que funciona, o detectar huecos que nadie
  cubre bien?

**2. Estructura la comparación en tabla** — una fila por dimensión relevante del patrón
(cómo se activa, cómo se visualiza, qué casos edge cubre), una columna por competidor.

**3. Cierra con un gap analysis** — qué hace ninguno de los competidores comparados, o qué
resuelven todos mal, como posible ventaja diferencial.

**4. Termina conectando el hallazgo con trabajo previo si existe** — por ejemplo, si hay un
`layers-conceptual-model` con una pregunta abierta, señala si el benchmark aporta un
precedente de mercado relevante para esa pregunta.

## Ejemplo

**Isabel escribe:**
> `/benchmark` cómo resuelven otras herramientas de marketing la comparación de campañas —
> te adjunto 3 capturas de Herramienta A, B y C

**Preguntas antes de construir:**
> Antes de comparar, dime:
> - ¿Qué patrón concreto te interesa? (¿la interacción de comparar, la visualización, el
>   filtrado?)
> - ¿Buscas inspiración para copiar lo que funciona, o detectar huecos que ninguna cubre
>   bien?

**Isabel responde:**
> La interacción de comparar dos campañas específicamente. Busco huecos que nadie cubre
> bien.

**Output final:**

> | | Herramienta A | Herramienta B | Herramienta C |
> |---|---|---|---|
> | Cómo se selecciona qué comparar | Checkbox en lista | Arrastrar a un "slot" de comparación | Dropdown de 2 campos |
> | Visualización | Barras lado a lado | Líneas superpuestas | Tabla de números |
> | Normaliza periodos distintos | No — asume mismo rango | Sí, automático | No aplica (tabla) |
>
> **Gap analysis:** ninguna de las tres deja claro qué pasa si se compara una campaña de 2
> semanas con una de 2 meses, salvo Herramienta B — posible hueco a favor si se resuelve
> bien.

**Recomendación final:**
> El patrón de Herramienta B (normalización automática de periodos) resuelve exactamente
> la pregunta pendiente que había en el `layers-conceptual-model` sobre comparar periodos
> distintos — hay un precedente de mercado de referencia para esa decisión.
