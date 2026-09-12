---
name: strategy
description: >-
  Construye un Product Strategy Canvas completo de 9 secciones — visión, propuesta de valor
  (JTBD), segmento objetivo, modelo de negocio, monetización, go-to-market, panorama
  competitivo, métricas clave y defensibilidad. Úsala cuando Isabel (o su equipo) necesite
  responder en serio "¿cuál es la estrategia aquí?" para una línea de producto o feature
  nueva, no una idea suelta. Documento pesado — pensado para contexto de equipo/empresa, no
  para decisiones pequeñas de una sola pantalla o feature aislada.
---

# Strategy — Product Strategy Canvas de 9 secciones

> Fuente: [phuryn/pm-skills — pm-product-strategy](https://github.com/phuryn/pm-skills)

A diferencia del resto de skills de esta colección (que trabajan sobre una oportunidad o
feature concreta), esta construye el documento de estrategia de producto completo — el que
respondería en serio a "¿cuál es la estrategia de esto?" cuando lo pregunta un director de
producto o un manager, no solo "¿qué construimos primero?".

## Las 9 secciones

1. **Visión** — hacia dónde va el producto, de forma inspiradora y creíble.
2. **Propuesta de valor** — framework JTBD en 6 partes: quién se beneficia, por qué lo
   necesita, su situación actual, cómo se resuelve, el resultado, qué alternativas
   consideraría.
3. **Segmento objetivo** — a quién se construye esto, basado en research/personas.
4. **Modelo de negocio** — cómo se crea, entrega y captura valor.
5. **Estrategia de monetización** — cómo genera ingresos, validado con experimentos.
6. **Go-to-market** — canales, mensaje, cómo se lanza y adquieren clientes.
7. **Panorama competitivo** — posicionamiento frente a competidores directos e indirectos
   (usa Porter's Five Forces).
8. **Métricas clave** — cómo se mide el éxito, ligado a la visión.
9. **Defensibilidad** — qué hace que no se pueda copiar fácilmente (efecto red, coste de
   cambio, marca, datos...).

## Cuándo se activa

Isabel (o su equipo) va a lanzar o proponer una línea de producto o feature con peso real —
no una feature pequeña o una iteración visual — y necesita un documento de estrategia
serio. Es una skill pesada para contexto de equipo/empresa; no tiene sentido para
decisiones pequeñas de una sola pantalla, ni para un proyecto personal sin modelo de
negocio propio.

También si pide explícitamente `/strategy [idea de producto]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir.** No completes las 9 secciones a partir de una frase —
pide lo mínimo imprescindible para no inventar:
- ¿Quién paga por esto — es una feature dentro de algo que ya se vende, o algo nuevo con
  precio propio?
- ¿Ya se sabe contra quién compite (aunque sea "lo hacen a mano hoy"), o parte de cero?
- ¿Hay alguna métrica ya marcada como objetivo, o también parte de cero?

**2. Construye las 9 secciones** con lo que Isabel aportó, usando criterio razonable para
completar el resto — pero **marca con ⚠️ cada sección donde no había información real** de
base (ej. Defensibilidad y Monetización suelen quedar con huecos grandes en una feature
interna sin modelo de negocio propio). No inventes una respuesta convincente sin dejar
claro que es una suposición, no un dato aportado.

**3. Termina señalando qué secciones ⚠️ convendría validar o decidir con el equipo antes de
tratar el documento como definitivo.**

## Ejemplo

**Isabel escribe:**
> `/strategy` mi equipo va a lanzar una nueva línea: comparación automática de campañas
> con recomendación de cuál repetir

**Preguntas antes de construir:**
> Antes del canvas completo, dime lo que ya sepas:
> - ¿Quién paga por esto — es una feature dentro de un producto que ya vendéis, o algo
>   nuevo con precio propio?
> - ¿Ya sabéis contra quién compite esto hoy (aunque sea "lo hacen a mano en Excel")?
> - ¿Hay alguna métrica ya marcada como objetivo, o parte de cero?

**Isabel responde:**
> Es una feature dentro del producto que ya vendemos, sin precio propio. Hoy la gente lo
> hace comparando manualmente en Excel/Sheets. No hay métrica todavía.

**Output final (resumido):**
> 1. **Visión** — [construida con criterio a partir del contexto dado]
> 2. **Propuesta de valor (JTBD)** — [construida]
> 3. **Segmento objetivo** — [construida]
> 4. **Modelo de negocio** ⚠️ — sin dato aportado; se asume que no cambia el modelo del
>    producto principal, a confirmar.
> 5. **Monetización** ⚠️ — no aplica directamente (feature sin precio propio); marcar como
>    n/a en vez de inventar un modelo de precio.
> 6. **Go-to-market** — [construida, apoyada en que ya hay usuarios del producto principal]
> 7. **Panorama competitivo** — Excel/Sheets como "competidor" actual (manual).
> 8. **Métricas clave** ⚠️ — no hay ninguna definida todavía; propuesta preliminar a
>    validar con el equipo.
> 9. **Defensibilidad** ⚠️ — sin dato suficiente para evaluar; requiere más contexto de
>    negocio.

**Recomendación final:**
> Antes de tratar este canvas como definitivo, cerrar con el equipo las secciones ⚠️
> (Modelo de negocio, Métricas clave, Defensibilidad) — son las que más cambiarían el
> documento si aparece información nueva.
