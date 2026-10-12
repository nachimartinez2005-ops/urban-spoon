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
