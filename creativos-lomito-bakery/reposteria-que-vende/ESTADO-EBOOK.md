# Estado de producción del ebook — Repostería que Vende

Última actualización: 2026-10-22

## Dónde están las páginas

Las imágenes generadas viven en el sandbox de Higgsfield, en `/home/user/rqv/`,
con el nombre `r<receta>p<página>.png` (ej. `r14p2.png`). **El sandbox se
recicla**: si faltan archivos, se vuelven a bajar de
`https://d8j0ntlcm91z4.cloudfront.net/user_3JcSeMkIKAC7oEjAohA9u5GlXaz/<archivo>.png`
o se regeneran con los prompts de abajo.

## Avance

| Bloque | Páginas | Estado |
|---|---|---|
| Receta 01 | 3 | lista |
| Recetas 02-05 | 12 | listas |
| Recetas 06-09 | 12 | listas |
| Recetas 10-13 | 12 | listas |
| Recetas 14-17 | 12 | listas |
| Recetas 18-20 | 9 | listas |
| **Total** | **60 de 103** | |

Faltan 43 páginas: recetas 21 a 30 (30 páginas) + portada, índice/bienvenida,
5 separadores de categoría, 4 páginas de sistema de negocio y cierre (13).

## Modelo y parámetros (esto ya costó créditos de más, no cambiarlo)

- Modelo correcto: **`nano_banana_2_1`** con **`resolution: "2k"`**.
- `nano_banana_2` **no existe**: el servidor cae en silencio a
  `nano_banana_flash` y devuelve 848×1264, la mitad de resolución. Pasó el
  22/10 y hubo que regenerar 24 páginas.
- Toda página buena mide **1696×2528**. Verificar siempre el tamaño antes de
  dar un lote por bueno.
- El batch tira 429 (`rate_limit_reached`) cuando se mandan 10-12 juntas:
  reenviar las que rebotan, no hay cargo por las fallidas.

## Cláusula antidefectos (va en todos los prompts)

> ALL TEXT STRICTLY IN SPANISH, no English words anywhere, every label spelled
> correctly, no duplicated labels, no repeated words.

Sin ella salió "CHFRIADO POR G REFRIIGORADOR" y "Chill Time" en la receta 01.
Con ella, cero defectos de idioma en 60 páginas. Igual revisar: la 15 p3 salió
con la etiqueta "Masa de chocolate" duplicada y hubo que rehacerla.

## Estructura de cada receta (3 páginas)

1. **Portada**: foto del postre, badge de número, nivel/rinde/tiempo/
   conservación/costo, y el botón "SE VENDE EN $X MXN".
2. **Receta técnica**: ingredientes numerados + pasos en tarjetas + CLAVE +
   CONSEJO.
3. **Armado y venta**: ilustración con llamadas, tabla de costo y precio por
   presentación, 4 ocasiones de venta, leyenda, y la barra de margen.

## Qué falta antes de vender

- Terminar las 43 páginas y armar el PDF.
- Landing (copia de `landing-lomito-bakery.html` con el contenido cambiado).
- Creativos con el ángulo de negación de 15 B.
- **De Nacho**: crear la 2da tienda en Impultienda con el nombre *Repostería
  que Vende*, compartir el pixel `1712126017302327`, subir el PDF y hacer una
  **compra de prueba real** de punta a punta.
