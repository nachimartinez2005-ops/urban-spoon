# Estado de producción del ebook — Repostería que Vende

Última actualización: 2026-10-22

## Dónde están las páginas

Las imágenes generadas viven en el sandbox de Higgsfield, en `/home/user/rqv/`,
con el nombre `r<receta>p<página>.png` (ej. `r14p2.png`). **El sandbox se
recicla**: si faltan archivos, se vuelven a bajar de
`https://d8j0ntlcm91z4.cloudfront.net/user_3JcSeMkIKAC7oEjAohA9u5GlXaz/<archivo>.png`
o se regeneran con los prompts de abajo.

## Avance

**El ebook está terminado: 102 páginas, PDF armado.**

| Bloque | Páginas |
|---|---|
| Portada, bienvenida e índice | 3 |
| 5 separadores de categoría | 5 |
| 30 recetas × 3 páginas | 90 |
| Precio, clientes, primera semana y cierre | 4 |
| **Total** | **102** |

PDF: `reposteria-que-vende.pdf`, 30 MB, 102 páginas, 1272×1896 por página
(equivale a 150 ppp en media carta). Queda en el sandbox de Higgsfield en
`/home/user/rqv/` y subido como media `f5c20122-4d80-48cd-88a1-5becb197c183`.

### El PDF se arma así

ImageMagick tiene el coder de PDF bloqueado por política y `pip install` no
tiene permisos de escritura, así que el armado va con un escritor de PDF en
Python puro que embebe los JPEG con `DCTDecode`. El script está en el
historial de la sesión; si hay que rehacerlo, el orden de páginas vive en
`/home/user/rqv/orden.txt`.

## Defectos que hubo que corregir

| Página | Qué salió mal |
|---|---|
| Receta 01 p3 | Texto inventado en inglés y mal escrito |
| Receta 15 p3 | La etiqueta "Masa de chocolate" dos veces |
| Receta 23 p3 | La etiqueta "Papel encerado" dos veces |
| Receta 24 p2 | El paso 1 pedía azúcar que no estaba en los ingredientes |
| Índice | **Inventó ocho recetas que no existen** (red velvet, croissants, macarons). Hubo que pasarle la lista exacta y prohibirle agregar nada |
| Portada | "EDICIÓN 2026" repetido, y decía 103 páginas cuando son 102 |

La lección: el modelo respeta el formato pero rellena el contenido si lo
dejás. Toda página con una lista hay que dictársela entera.

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
Con ella, cero defectos de idioma en las 102 páginas. Lo que la cláusula no
evita es que invente contenido: para eso hay que dictarle la lista completa.

## Estructura de cada receta (3 páginas)

1. **Portada**: foto del postre, badge de número, nivel/rinde/tiempo/
   conservación/costo, y el botón "SE VENDE EN $X MXN".
2. **Receta técnica**: ingredientes numerados + pasos en tarjetas + CLAVE +
   CONSEJO.
3. **Armado y venta**: ilustración con llamadas, tabla de costo y precio por
   presentación, 4 ocasiones de venta, leyenda, y la barra de margen.

## Qué falta antes de vender

- Landing (copia de `landing-lomito-bakery.html` con el contenido cambiado).
- Creativos con el ángulo de negación de 15 B.
- **De Nacho**: crear la 2da tienda en Impultienda con el nombre *Repostería
  que Vende*, compartir el pixel `1712126017302327`, subir el PDF y hacer una
  **compra de prueba real** de punta a punta.
