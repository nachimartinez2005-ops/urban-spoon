# Mail post-compra con upsell · Repostería que Vende

Se dispara automáticamente después de cada compra, desde Impultienda.

## Por qué el mail y no el checkout

En Lomito el upsell del checkout **no se muestra**: ese canal vendió **0 de
6**. El mail, en cambio, llega al instante y a bandeja principal (verificado
el 12/10 con una compra de prueba).

Así que acá se arranca al revés que en Lomito: **el mail es el canal
principal de upsell desde el día uno**, no el parche. Si más adelante el
bump del checkout aparece y funciona, se suma; no se reemplaza.

## Criterio

**Una sola oferta arriba, no tres.** Tres botones compiten entre sí y la
persona no elige ninguno. Las otras dos van al pie, en una línea, para quien
las busque.

**Primero Pastelería de Fiesta**, por las mismas tres razones que en Lomito:

1. Es el más barato ($6,70): la barrera más baja justo después de pagar.
2. Es de **producción**, no de venta. Sirve a quien todavía no vendió nada,
   que es exactamente quien acaba de comprar.
3. Tiene el mejor argumento, y se explica en una frase: el mismo horno que
   hace un pastel de $380 hace uno de evento de $1.600.

Vende en Redes y Fechas que Venden son herramientas de venta: valen más para
quien ya empezó. Ese es el mail de la semana siguiente, no el de hoy.

---

## ASUNTO

```
Tus 30 recetas están acá — y una cosa más antes de que empieces 🍰
```

## CUERPO

Hola [nombre]:

Tu paquete completo está acá: **[LINK DE LA CARPETA]**

Abre primero el archivo **00** y ve directo a la **Receta 01**, la gelatina
de mosaico. Es la más barata del libro, no lleva horno y tiene el mejor
margen: te cuesta $38 y se vende en $220.

Son 7 archivos. El que más te va a servir el primer día es la
**calculadora**: pon ahí los precios de tu súper y te dice qué cobrar.

---

**Una cosa más, y te dejo.**

En el curso hay siete pasteles. Todos son pasteles de casa: se cobran entre
$280 y $450.

Pero cuando alguien hace una fiesta no pide un pastel de casa. Pide uno de
dos pisos, o de número, o temático. Y eso se cobra **$1.600**.

Mismo horno. Misma cocina. Otro precio.

**Pastelería de Fiesta** trae los cinco pasteles de evento que no están en
el curso, cómo se sostiene uno de dos pisos para que no se te caiga en el
camino, y cómo cotizar una mesa de postres completa en vez de cobrarla
pieza por pieza.

👉 **[BOTÓN: Agregarlo por $6,70]**

Con un solo pastel de evento vendido lo recuperas más de doscientas veces.

---

Cualquier cosa me escribes por acá.

[tu nombre]

---

*¿Ya vendiendo y quieres más? También están **Vende en Redes** (15
publicaciones listas y cómo fotografiar tus postres) y **Fechas que Venden**
(el calendario mexicano con cuándo abrir pedidos en cada fecha), $7,90 cada
uno.*

---

## Notas de implementación

- **El link de la carpeta va antes que el upsell.** Lo que compró primero,
  siempre. Un mail que arranca vendiendo otra cosa quema la confianza del
  que acaba de pagar.
- El botón del upsell apunta al link de pago del producto *Pastelería de
  Fiesta* en Impultienda, no a la tienda.
- **La receta 01 que se nombra tiene que coincidir con el ebook.** Es la
  gelatina de mosaico: $38 de costo, $220 de precio, 83% de margen, el más
  alto del libro. Verificado contra la página 9 del PDF.
- El mail de la semana siguiente (con los otros dos upsells) todavía no está
  escrito. Se escribe cuando haya al menos una compra real, para saber si
  esta gente abre los mails.
