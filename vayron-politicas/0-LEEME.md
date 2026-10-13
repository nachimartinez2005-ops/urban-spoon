# Políticas legales de Vayron — instrucciones

El conector de Shopify no tiene permiso de escritura sobre politicas legales
(`write_legal_policies`), así que estas hay que pegarlas a mano. Son 5 minutos.

## Dónde van

Shopify Admin → **Configuración → Políticas**

| Archivo | Campo de Shopify |
|---|---|
| `1-devoluciones.txt` | Política de reembolsos |
| `2-envios.txt` | Política de envío |
| `3-terminos.txt` | Términos del servicio |
| `4-contacto.txt` | Información de contacto |

Abrí el campo, pegá el contenido del archivo tal cual y guardá. Son texto plano:
los títulos van en MAYÚSCULAS para que funcionen como encabezados sin formato.

## Antes de publicar

1. En `3-terminos.txt` hay dos `[COMPLETAR]`: razón social / nombre y apellido,
   y CUIT. Son obligatorios para operar como vendedor.
2. Verificá que el domicilio (Belgrano 893, Quilmes) sea el correcto para
   publicar. Lo tomé de los datos ya cargados en tu Política de Privacidad.

## Botón de Arrepentimiento (obligatorio)

La Resolución 424/2020 exige que esté **visible y accesible desde la home**,
no solo dentro de una política. Pasos:

1. Shopify Admin → **Tienda online → Navegación → Menú de pie de página**
2. Agregá un ítem con el nombre exacto **"Botón de Arrepentimiento"**
3. Enlazalo a la Política de reembolsos (`/policies/refund-policy`)

Lo mismo con un ítem **"Defensa del Consumidor"** que enlace a:
`https://www.argentina.gob.ar/produccion/defensadelconsumidor/formulario`

## Aviso

Estos textos son una base sólida y alineada con la Ley 24.240, la Res. 424/2020
y la Ley 25.326, pero no son asesoramiento legal. Si el volumen de la tienda
crece, que un abogado los revise.
