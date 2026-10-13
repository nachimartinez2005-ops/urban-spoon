# Mail post-compra con upsell · Lomito Bakery

Se dispara automáticamente después de cada compra, desde Impultienda.
Reemplaza al upsell post-compra que **no se muestra** en el checkout: ese
canal vendió 0 de 6. El mail, en cambio, llega al instante y a bandeja
principal (verificado el 12/10 con una compra de prueba).

## Criterio

**Una sola oferta arriba, no tres.** Tres botones compiten entre sí y la
persona no elige ninguno. Las otras dos van al pie, en una línea, para
quien las busque.

**Primero el Pack de Cumpleaños**, por tres razones:
1. Es el más barato ($4,90): la barrera más baja justo después de pagar.
2. Ya está validado como order bump dentro del checkout.
3. Tiene el mejor argumento: un smash cake se vende a $350-380 contra los
   $70 de una bolsita de galletas. El retorno se explica en una frase.

Los otros dos son herramientas de venta — valen más para quien ya empezó
a vender, no para quien todavía no horneó nada. Ese es el mail de la
semana siguiente, no el de hoy.

---

## ASUNTO

```
Tus 30 recetas están acá — y algo más antes de que empieces 🐾
```

## CUERPO

Hola [nombre]:

Tu paquete completo está acá: **https://drive.google.com/drive/folders/1m9AR-DTdqJrfxcfv4Ji0SsxcTpZ0eq_k**

Abrí primero el archivo **00** y andá directo a la **Receta 01**. Es la más
fácil, la más barata y la que más se vende: te cuesta $25 hacerla y la
vendés a $70.

---

**Una cosa más, solo por hoy**

Cuando empieces a recibir pedidos, la mayoría van a ser para cumpleaños.
Es la ocasión en que la gente gasta sin pensarlo: **un smash cake se vende
entre $350 y $380**, contra los $70 de una bolsita de galletas.

**🎂 Pack Pasteles de Cumpleaños — $4,90**

5 pasteles y postres de fiesta paso a paso: smash cake, pastel salado de
pollo, pastel de calabaza de dos pisos, pastel con forma de hueso y donas
glaseadas. Con betunes seguros para perro.

Con **un solo** pastel de cumpleaños que vendas, ya lo recuperaste 70 veces.

👉 **AGREGAR A MI PAQUETE — $4,90**
https://lomitobakery.impultienda.ar/checkout?p=3e559482-2689-41d8-a4f0-7f6cc47f88cd

Se suma a tu carpeta al instante, sin volver a cargar tus datos.

---

*¿Ya sabés hornear y lo que te falta es vender?*
*📱 Kit Vende en Redes ($5,90) — https://lomitobakery.impultienda.ar/checkout?p=4299c3a2-a25a-42d2-8d5b-87e5f6f9d216*
*📅 Pack Fechas que Venden ($5,90) — https://lomitobakery.impultienda.ar/checkout?p=3e5e4caa-821c-435b-be78-20a60ecd595e*

Cualquier duda, respondeme este mismo correo — lo leo yo.

Gracias por confiar,
**Lomito Bakery**

---

## Antes de activarlo

- [ ] Cambiar `[nombre]` por la variable de nombre que use Impultienda.
- [ ] Verificar que los 5 pasteles que listo del Pack sean los que
      realmente trae. Los tomé de la descripción del order bump del
      checkout; si adentro hay otros, corregí la lista.
- [ ] Probar los 3 links: cada uno tiene que abrir su checkout con el
      precio correcto.
- [ ] Confirmar que "Mensajes que venden" y "Calendario de ventas" ya NO
      estén dentro del producto principal. Son el contenido de los dos
      upsells de $5,90: si se entregan gratis, nadie los compra.
