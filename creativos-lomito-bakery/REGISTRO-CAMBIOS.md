# Registro de cambios ejecutados en la cuenta

Cuenta: Ebooks Argentina (`1560224662043860`)
Campaña: Test ABO | Pastelería Canina | MX 10/10 (`52532697130726`)

---

## 2026-10-12 — PASO 1: cortar placements basura + arreglar edad

### Hallazgos previos a la ejecución

1. **La edad real no era 25-60.** Los conjuntos se llaman `MX 25-60` pero tenían
   `age_min: 18, age_max: 65` con `targeting_automation.advantage_audience: 1`.
   Advantage+ Audience trata el rango de edad como sugerencia y lo ignora.
   Se estaba comprando tráfico de 18-65.

2. **8 conjuntos con $6/día cada uno.** Fragmentación extrema: con CPA ~$7 cada
   conjunto hace <1 conversión/día y nunca sale de la fase de aprendizaje
   (Meta necesita ~50 conversiones/semana por conjunto).

3. **CJ3 gastó $13.01 con 0 ventas** — 19% del gasto total en un ángulo muerto.

### Cambios aplicados

**Targeting nuevo (idéntico en los 5 conjuntos conservados):**
```json
{
  "age_min": 25,
  "age_max": 60,
  "geo_locations": { "countries": ["MX"],
                     "location_types": ["frequently_in","home","recent"] },
  "publisher_platforms": ["facebook", "instagram"],
  "facebook_positions": ["feed"],
  "instagram_positions": ["reels"],
  "device_platforms": ["mobile", "desktop"],
  "targeting_automation": { "advantage_audience": 0 }
}
```

`page_types` resultante: `["desktopfeed", "instagramreels", "mobilefeed"]`
Eliminados: Audience Network (classic + rewarded_video), WhatsApp Status,
Threads, Stories FB/IG, FB Reels, IG Feed, Marketplace, Search, instream video,
right column, profile feeds, biz_disco, notifications.

| Conjunto | ID | Acción | Estado final |
|---|---|---|---|
| CJ1 \| V1 Problema | `52532697234526` | Placements + edad | ✅ ACTIVE |
| CJ2 \| V2 Negocio | `52532697322726` | Placements + edad + **reactivado** | ✅ ACTIVE |
| CJ5 \| V5 Pastel | `52532697375926` | Placements + edad | ✅ ACTIVE |
| CJ6 \| V5 Pastel copy ganancia | `52532940160526` | Placements + edad | ✅ ACTIVE |
| CJ7 \| V1 Problema copy extra | `52532940166926` | Placements + edad | ✅ ACTIVE |
| CJ3 \| V3 Notas | `52532697353726` | **PAUSADO** ($13.01 / 0 ventas) | ⏸️ PAUSED |
| CJ4 \| V4 Carrusel | `52532697365526` | ya estaba pausado | ⏸️ PAUSED |
| CJ6 Pastel - Copia | `52532939754326` | sin tocar ($0 gastado) | ⏸️ PAUSED |

**Presupuesto diario: $30/día antes → $30/día después.** Se cambió el perdedor
(CJ3) por el segundo mejor (CJ2, CPA $9.90 con upsell = ROAS 1.39). Exposición neutra.

### Notas técnicas

- Meta fuerza `status: PAUSED` al editar un conjunto activo
  (`status_forced_to_paused: true`). Los tres afectados (CJ1, CJ2, CJ5) se
  reactivaron con `ads_activate_entity` → confirmado `status: ACTIVE`.
- Los 5 anuncios quedaron en `PENDING_REVIEW`: editar el targeting dispara
  revisión nueva de Meta. Normal, se aprueban en minutos u horas.
- `is_draft: false` en todas las respuestas → los cambios fueron a los objetos
  en vivo, no a un borrador.

### Qué monitorear en 48-72h

| Métrica | Esperado | Alarma |
|---|---|---|
| CTR | **BAJA** de ~5% a ~2-3% (se van los clics basura) | — |
| CPM | Sube algo (menos inventario disponible) | **+40% o más** |
| CPA | **BAJA** hacia ~$7 | se mantiene >$12 |
| Ventas/día | Sube | baja con CPM alto |

**Plan de contingencia:** si el CPM sube más de 40% y el CPA no baja, agregar de
vuelta solo `instagram_positions: ["stream"]` (Feed de Instagram). Con $6/día por
conjunto, restringir demasiado puede encarecer el alcance.

**No mirar el CTR para decidir.** Decidir solo por CPA.

### Pendiente (próximos pasos del plan)

- Paso 4-8: arreglar `fbp` (35.5%) y verificar los 3 upsells
- Paso 9-12: repackagear a 50+ recetas, precio en titular, escalera de upsells
- Paso 18: consolidar los conjuntos (la fragmentación de $6/día sigue sin resolverse)

---

## 2026-10-12 (segunda tanda) — Correcciones y reasignación de presupuesto

### Bug encontrado y corregido 🚨
**CJ2 tenía el conjunto ACTIVO pero el anuncio `2 video neg` PAUSADO.**
Un conjunto activo con el anuncio apagado no entrega nada: ocupaba lugar en la
estructura sin poder vender. Activado (`ads_activate_entity` sobre el ad).

> Regla: para que un anuncio se entregue, los TRES niveles tienen que estar
> activos — campaña, conjunto Y anuncio.

### Reasignación de presupuesto

Hallazgo: **CJ5 y CJ6 usan el mismo video** ("V5 Pastel", `video_id` 1063090180100392
y 1954647015494680 del mismo material). La diferencia está en el CTA:

| | CTA | Efecto |
|---|---|---|
| CJ5 (creativo `1954647015494680`) | `SEE_DETAILS` | no precalifica |
| CJ6 (creativo `1404693651814835`) | **`BUY_NOW`** | precalifica el clic ✅ |

Se pausó CJ5 y se conserva CJ6: mismo asset, mejor CTA, copy más nuevo.

| Conjunto | Antes | Ahora | Razón |
|---|---|---|---|
| CJ1 \| V1 Problema | $6 | **$10** | mejor CPA ($6.43), 2 de 4 ventas |
| CJ2 \| V2 Negocio | $6 | **$8** | 2º mejor (CPA $9.90 con upsell, ROAS 1.39) |
| CJ6 \| copy ganancia | $6 | $6 | sin datos, CTA BUY_NOW, merece test |
| CJ7 \| copy ingreso extra | $6 | $6 | sin datos, CTA BUY_NOW, merece test |
| CJ5 \| V5 Pastel | $6 | **PAUSADO** | duplicado de CJ6 con peor CTA |

**Total: $30/día antes → $30/día ahora.** Misma exposición, inclinada a lo que funciona.

### Estado final verificado

```
🟢 CJ1 | V1 Problema          $10/día   anuncio ACTIVE
🟢 CJ2 | V2 Negocio            $8/día   anuncio ACTIVE (reparado)
🟢 CJ6 | copy ganancia         $6/día   anuncio ACTIVE
🟢 CJ7 | copy ingreso extra    $6/día   anuncio ACTIVE
⏸️ CJ3 | V3 Notas              pausado  ($13.01 / 0 ventas)
⏸️ CJ4 | V4 Carrusel           pausado  ($8.33 / 0 ventas)
⏸️ CJ5 | V5 Pastel             pausado  (duplicado de CJ6)
⏸️ CJ6 Pastel - Copia          pausado  ($0 gastado)
```

`ads_get_errors` sobre la campaña: **sin errores de entrega.**
Los 4 anuncios activos pasaron revisión de Meta.

### Lo que queda SIN resolver en Meta (a propósito)

**Consolidación (Paso 18).** Siguen siendo 4 conjuntos separados, ninguno con
volumen para salir de aprendizaje. Es el próximo cambio estructural grande.
**Se difiere ~72h a propósito:** hoy ya se cambiaron placements y presupuestos;
consolidar ahora reiniciaría el aprendizaje antes de tener un solo dato limpio
bajo la configuración nueva.

**Retargeting (Paso 20).** Evaluado y descartado por ahora: con ~118 clics
limpios históricos, el público de carrito abandonado es demasiado chico para
que Meta lo entregue (necesita ~1.000 personas). Vuelve a la mesa cuando haya
volumen.

---

# TRABAJO PENDIENTE EN IMPULTIENDA (no tengo acceso)

> El checkout de Lomito Bakery está en **Impultienda**. No hay conector, así que
> esto es manual. **Acá está el 70% de la ganancia que queda** — más que
> cualquier cosa que se pueda tocar en el administrador de anuncios.

## 1. El pixel pierde 2 de cada 3 visitas 🔴 PRIORIDAD MÁXIMA

**Diagnóstico:** `PageView` tiene cobertura de `fbp` del **35.5%**.
`Purchase` está impecable (EMQ 9.3, email/teléfono/external_id al 100%) → la
integración de servidor de Impultienda funciona bien. El agujero está en el
**navegador**, en la página de aterrizaje.

**Qué hacer:**
- Verificar que el pixel `1712126017302327` esté cargado en **TODAS** las páginas:
  aterrizaje, checkout, upsells y página de gracias. No solo en el checkout.
- Que cargue en el `<head>`, **antes** del contenido.
- Si hay banner de cookies, que **no bloquee** el pixel hasta aceptar.
- Si la landing y el checkout están en dominios distintos, pasar `fbclid` y
  `_fbp` en la URL del botón de compra.

**Qué ganás:** recuperás ~31% del ingreso que hoy Meta no ve. Y más importante:
el algoritmo deja de optimizar con 4 de 6 conversiones.

## 2. Los upsells están mal ordenados 🟠

**Evidencia:** de 6 compradores, 1 solo tomó upsell, y tomó **el más barato
($4.90)**. Ninguno tomó los de $5.90.

**Qué hacer:**
- Verificar **en qué orden** se muestran. Si el de $4.90 aparece primero,
  invertirlo: **$5.90 primero, $4.90 como downsell** si rechaza.
- Verificar que los dos upsells de **$5.90 disparen `Purchase`** con su valor
  real. El de $4.90 ya dispara (se reconstruyó desde el ROAS reportado).
- Confirmar que el flujo de upsell **se le muestra a todos** los compradores.
  Un take rate de 17% puede no ser take rate bajo: puede ser que no se ofrezca.

**Qué ganás:** con 35% de toma a $5.57 promedio, el AOV sube de $9.72 a $10.85.
Son $1.13 más de CPA que podés pagar por cada cliente.

## 3. El precio no paga el tráfico 🟠

| | Precio | Recetas |
|---|---|---|
| **Lomito Bakery** | **$8.90** | **15** |
| Infinity Cursos (MX) | ~$10.80 | 50 + App |
| CloudPets | **$17** | — |
| Dogtor Patitas | — | 70 |

Sos **el más barato y el que menos ofrece**. CloudPets tiene el doble de margen
para pagar el mismo clic.

**Qué hacer:**
- Repackagear: `15 recetas` → **`Curso + App + 50 recetas`**. No hace falta
  escribir 35 recetas nuevas: contá variantes, tamaños, versiones sin horno,
  para gato. Tus 5 bonos YA son el "curso".
- Subir a **$14.90** (o testear $11.90 primero si da miedo).

**Qué ganás:** el CPA que podés pagar salta de **$9.72 a $16.85**. Es la
diferencia entre perder plata y escalar.

---

## Lo que necesito para seguir con los anuncios

**La URL exacta del checkout de Impultienda.** Los creativos de video actuales
no exponen el `link_url` por API, y sin esa URL no puedo crear los anuncios
nuevos con el copy que precalifica (precio en el titular, "50 recetas",
"desde cero"). No la invento: un link mal puesto quema presupuesto mandando
gente a la nada.

---

## 2026-10-12 (tercera tanda) — 3 anuncios nuevos con copy que precalifica

URL de destino recibida: `https://lomitobakery.impultienda.ar/checkout`

> ⚠️ **No se pudo verificar la página.** La política de red de este entorno
> devuelve 403 al intentar abrirla (mismo bloqueo que el CDN de Higgsfield).
> No se sabe si `/checkout` es página de venta o formulario de pago directo.
> **Por eso los 3 anuncios se dejaron PAUSADOS**: si los creativos actuales
> apuntan a una página de venta y estos van directo al pago, la conversión
> se hunde. Verificar el destino en la vista previa antes de activar.

### Creativos creados

Todos sobre los **videos ya probados** (no se gastó un crédito en material nuevo),
con `BUY_NOW` y el **precio en el titular** — que es el arreglo directo al
problema del clic basura.

| Creativo | ID | Video | Titular |
|---|---|---|---|
| NEW-A Precio + desde cero | `1064418276589580` | `2513584822498079` (ganador) | `Pastelería canina desde cero · $8.90` |
| NEW-B Negación curiosidad | `1867866977717409` | `2149988429061612` (CJ2) | `Ninguna receta lleva estos 5 · $8.90` |
| NEW-C Fin de semana | `2136004643971775` | `2513584822498079` (ganador) | `Empieza a vender este fin de semana` |

Ángulos modelados de la competencia:
- **NEW-A** → Gaston Aguirre ("desde cero", 29 ads) + CloudPets (precio en titular)
- **NEW-B** → CloudPets ("Ninguna receta lleva estos 5 · US$17") + el ángulo
  $21→$85 que ya ganó en CJ2 (ROAS 1.39)
- **NEW-C** → Barkery en casa (25 días activo) y Mariana Rojas ("fin de semana")

Copy en español de México (manteniendo "pícale", "lomitos", "colonia" del
original). Todos declaran **"ebook digital de $8.90 USD"** en el cuerpo:
quien hace clic ya sabe que se paga y cuánto.

### Anuncios creados (PAUSADOS) — todos en CJ1, el mejor conjunto

| Anuncio | ID | Estado |
|---|---|---|
| 8 NEW-A \| precio en titular + desde cero | `52533177900326` | ⏸️ PAUSED |
| 9 NEW-B \| negación curiosidad + precio | `52533177911326` | ⏸️ PAUSED |
| 10 NEW-C \| inmediatez fin de semana | `52533177917726` | ⏸️ PAUSED |

Se pusieron en **CJ1** (`52532697234526`, $10/día) a propósito: compiten contra
el ganador `1 v prob.` bajo el mismo público, mismos placements y mismo
aprendizaje. Es la única comparación limpia posible.

`conversion_domain` configurado en `lomitobakery.impultienda.ar` en los tres.

### Antes de activarlos — 1 verificación obligatoria

1. Abrir la vista previa de `8 NEW-A` y **tocar el botón «Comprar»**.
2. ¿Llega al mismo lugar que tus anuncios actuales?
   - **Sí** → activar los 3.
   - **No** (los actuales van a una página de venta) → avisar y se cambia
     el `link_url` de los 3 creativos.

### Nota sobre el precio en el copy

Los 3 anuncios dicen **$8.90 USD** porque es el precio real de hoy.
**Si se sube el precio a $14.90 (recomendado), hay que rehacer estos 3
creativos** — los creativos de Meta son inmutables, no se pueden editar.
Conviene decidir el precio primero y después activarlos.
