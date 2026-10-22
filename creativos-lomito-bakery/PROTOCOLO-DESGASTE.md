# Protocolo de desgaste creativo

Creado el 2026-10-23, a pedido de Nacho: *"estate atento también por si hay
que renovar creativos"*. La idea es detectar desvíos contra una línea de base
medida, no opinar sobre si "se ve cansado".

---

## Línea de base de 15 B (16 al 22 de octubre)

Anuncio `15 B | negacion + 30 recetas` (`52533183939926`),
video `2497533197399959`, creative `1803041127501843`.

| Día | Gasto | Impr. | Alcance | Frec. | CTR | CPM | p25 | p75 | Thruplay | Ventas | LPV |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 16 | $3.30 | 337 | 299 | 1.127 | 2.97% | $9.79 | 33 | 15 | 27 | 1 | 3 |
| 17 | $12.31 | 824 | 690 | 1.194 | 5.34% | $14.94 | 104 | 40 | 79 | 0 | 29 |
| 18 | $19.22 | 1715 | 1444 | 1.188 | 3.97% | $11.21 | 263 | 108 | 207 | 1 | 30 |
| 19 | $14.50 | 1759 | 1476 | 1.192 | 3.24% | $8.24 | 201 | 75 | 160 | 2 | 30 |
| 20 | $16.04 | 1873 | 1582 | 1.184 | 3.63% | $8.56 | 237 | 103 | 184 | 1 | 25 |
| 21 | $17.42 | 2022 | 1777 | **1.138** | 3.76% | $8.62 | 325 | 133 | 255 | **3** | 39 |
| 22* | $9.46 | 931 | 816 | 1.141 | **4.73%** | $10.16 | 179 | 62 | 146 | — | 19 |

\* parcial

**Acumulado: $92.25 gastados, 9.461 impresiones en 7 días.**

### Diagnóstico al 23/10: NO hay fatiga
1. **La frecuencia BAJA mientras el gasto SUBE.** 1.192 el 19 con $14.50 →
   1.138 el 21 con $17.42. Meta encuentra gente nueva más rápido de lo que
   la consume. Es lo contrario de la saturación.
2. **El CTR no cae.** Piso el 19 (3.24%), subió tres días seguidos a 4.73%.
3. **9.461 impresiones es nada** para el mercado mexicano. No hay pozo
   secándose.

---

## Umbrales de acción

| Señal | Base | 🟡 Construir | 🔴 Cambiar ya |
|---|---|---|---|
| Frecuencia | 1.13–1.19 | **1.5** | **1.8** |
| CTR | 3.2–4.7% | 2 días < 2.8% | 3 días < 2.5% |
| Retención p75/p25 | 37–45% | 2 días < 32% | < 28% |
| CPA | $5.81–16.33 | 2 días > $15 | 3 días > $17 |

### El discriminador que importa
- **CPM sube + CTR aguanta** → la subasta se puso cara. NO es el creativo.
  No tocar nada.
- **CPM sube + CTR cae** → el video se está quemando. Acción.

Ejemplo real: el 22/10 el CPM subió de $8.62 a $10.16 con el CTR en 4.73%.
Es subasta, no desgaste. No se tocó nada.

### Retención p75/p25 — por qué este número
Es el único indicador **independiente de la entrega**: mide cuántos de los
que empezaron el video siguieron mirando. Si baja, el creativo perdió
fuerza aunque Meta siga entregando bien. Calcularlo como
`video_p75_watched_actions / video_p25_watched_actions`.

**Marcado al 23/10:** el 22 cayó a 34.6%, el valor más bajo de la serie.
Es día parcial y el rango viene siendo 37-45%, así que todavía es ruido.
Pero es el único número que se movió para el lado feo. **Vigilar.**

---

## Qué hacer en cada nivel

### 🟡 Amarillo — empezar a construir
No se cambia nada al aire. Se arranca el reemplazo **antes de necesitarlo**,
porque un video nuevo tarda ~1 día de trabajo más créditos de Higgsfield.
1. Generar el video nuevo (pipeline probado: sandbox Higgsfield → curl del
   CDN → Pillow para la caja del gancho → drawtext para subtítulos →
   media_upload → ads_creative_upload_media con upload_source URL).
2. Mantener el ÁNGULO ganador: negación específica y contable al principio,
   el dinero en segundo lugar. Lo que cambia es la ejecución, no el ángulo.
3. Dejarlo listo y pausado.

### 🔴 Rojo — cambiar
El reemplazo ya existe (se construyó en amarillo). Se lanza y se deja 15 B
corriendo en paralelo 2-3 días para comparar, no se apaga de golpe.

### Palanca gratis, siempre disponible antes que el video
**El copy no cuesta nada.** C y D ya están escritas en VARIACIONES-15B.md:
- C · negación de la inversión ("No necesitas horno industrial")
- D · negación del tiempo ("No te quita las tardes")
Entran cuando el presupuesto pase de ~$30/día, o antes si hace falta
refrescar sin gastar créditos.

**Orden de agotamiento: primero copy (gratis), después video (caro).**

---

## El riesgo que NO es fatiga: concentración

Un anuncio, un video, un ángulo. Si 15 B cae mañana por cualquier motivo
—rechazo de políticas, cambio de algoritmo, lo que sea— no hay nada atrás.
19 A y 20 B existen pero reciben el 5% del presupuesto y no juntan muestra.

**Esto es más urgente que la fatiga, porque la fatiga avisa y una caída no.**

Mitigación en curso: a mayor presupuesto, Meta debería aflojar la
exploración y A/B empezar a juntar impresiones. Revisar en cada cierre.

---

## Qué revisar en CADA cierre diario
1. Frecuencia del día contra la tabla.
2. CTR del día contra la tabla.
3. Retención p75/p25 del día.
4. CPM, cruzado con el CTR (ver el discriminador).
5. Impresiones acumuladas de A y B contra el corte de ~500.
