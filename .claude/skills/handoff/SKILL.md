---
name: handoff
description: >-
  Genera el paquete completo de handoff a ingeniería — spec (measurements, behaviours,
  assets, states, edge cases) más un checklist de QA para verificar DESPUÉS de la
  implementación si lo construido coincide con el diseño. Úsala cuando Isabel entregue un
  diseño a desarrollo y quiera cerrar el círculo con una verificación posterior, no solo
  la especificación previa que ya cubre `design:design-handoff`.
---

# Handoff — spec + checklist de QA post-implementación

> Fuente: [Owl-Listener/designer-skills — design-ops](https://github.com/Owl-Listener/designer-skills/tree/main/design-ops)

## ⚠️ Relación con `design:design-handoff`

Esta skill se solapa parcialmente con `design:design-handoff` (ya disponible por
defecto). La parte de spec (measurements, behaviours, assets, states, edge cases) es
básicamente equivalente — si Isabel solo necesita la spec previa a construir, usar
`design-handoff` directamente. La parte genuinamente nueva es el **checklist de QA
posterior**: mientras la spec dice "qué construir", el checklist verifica "si lo
construido coincide de verdad con el diseño", una vez ya está implementado. Son dos
momentos distintos del mismo proceso: antes de construir, y después de construir.

## Las dos piezas

- **Spec de handoff** — measurements exactos, comportamientos esperados, assets
  necesarios, estados, y edge cases — el blueprint prescriptivo.
- **Checklist de QA** — lista de verificación para comprobar, ya con la feature construida,
  si cada medida, comportamiento y estado coincide con lo especificado. No es una lista
  genérica ("¿se ve bien?"), sino ítems concretos derivados directamente de la spec.

## Cuándo se activa

Isabel va a entregar un diseño a desarrollo y quiere el paquete completo — la spec y,
crucialmente, cómo verificar el resultado después. También si pide explícitamente
`/handoff [componente o pantalla]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Hay ya una spec de handoff hecha (con `design-handoff` u otra), o se construye desde
  cero aquí?
- ¿Quién hará la verificación de QA después — la propia Isabel, un QA dedicado, o el
  mismo ingeniero que lo construyó?

**2. Construye o reutiliza la spec** con measurements, comportamientos, assets, estados y
edge cases.

**3. Genera el checklist de QA a partir de la spec**, un ítem verificable por cada medida
o comportamiento específico — no genérico, sino derivado 1 a 1 de la spec anterior.

**4. Marca con ⚠️ cualquier ítem de la spec difícil de verificar objetivamente** (ej. un
comportamiento sujeto a interpretación) y sugiere cómo hacerlo verificable.

## Ejemplo

**Isabel escribe:**
> `/handoff` la vista de comparación de campañas — ya tengo la spec de measurements y
> estados, ahora quiero el checklist de QA también

**Preguntas antes de construir:**
> Antes del checklist, dime: ¿quién hará la verificación después — tú, un QA dedicado, o
> el mismo ingeniero?

**Isabel responde:**
> Yo misma la reviso antes de dar el visto bueno.

**Output final** (checklist derivado de la spec ya existente):

> - [ ] La leyenda mide exactamente 16px de padding respecto al borde de la gráfica
>       (spec: `space-md`)
> - [ ] Al comparar dos campañas con rangos de fechas distintos, se muestra el aviso de
>       normalización (spec: comportamiento definido en `layers-conceptual-model`)
> - [ ] El estado `partial` (una campaña cargada, otra no) muestra el skeleton solo en la
>       campaña pendiente, no en ambas
> - ⚠️ **Difícil de verificar objetivamente:** "el color debe transmitir claridad" — no es
>   verificable así; reformulado como: "el contraste del texto sobre el fondo cumple
>   mínimo 4.5:1 (WCAG AA)"

**Recomendación final:**
> Revisar primero los ítems que dependen de estados poco frecuentes (`partial`, error) —
> son los que más fácilmente se quedan sin probar antes de dar el visto bueno.
