# -*- coding: utf-8 -*-
"""Genera las miniaturas de catálogo de los dos bonos nuevos.

La miniatura es la tapa real del PDF, montada sobre un lienzo 4:5 en la
paleta de la marca. Así lo que ve el comprador en el catálogo es
exactamente la tapa del archivo que descarga.
"""
import subprocess, os
from PIL import Image, ImageFilter

W, H = 1080, 1350                      # 4:5, el formato de las tarjetas
CREAM = (253, 243, 227)
SOMBRA = (59, 43, 32)

BONOS = [("04-Bono-Plan-de-negocio", "plan-de-negocio"),
         ("06-Bono-Porciones-y-soluciones", "porciones-y-soluciones")]

for pdf, salida in BONOS:
    tmp = f"portadas/_{salida}"
    subprocess.run(["pdftoppm", "-f", "1", "-l", "1", "-r", "300", "-png",
                    f"entregables/{pdf}.pdf", tmp], check=True)
    tapa = Image.open(f"{tmp}-1.png").convert("RGB")

    # la tapa ocupa el 72 % del alto del lienzo
    alto = int(H * 0.72)
    ancho = int(tapa.width * alto / tapa.height)
    tapa = tapa.resize((ancho, alto), Image.LANCZOS)

    lienzo = Image.new("RGB", (W, H), CREAM)
    x, y = (W - ancho) // 2, (H - alto) // 2

    # sombra suave para que la tapa se lea como un libro sobre la mesa
    sombra = Image.new("RGB", (W, H), CREAM)
    caja = Image.new("RGB", (ancho + 18, alto + 18), SOMBRA)
    sombra.paste(caja, (x - 9, y - 1))
    sombra = sombra.filter(ImageFilter.GaussianBlur(22))
    lienzo = Image.blend(lienzo, sombra, 0.30)

    lienzo.paste(tapa, (x, y))
    dest = f"portadas/portada-{salida}.png"
    lienzo.save(dest, quality=95)
    os.remove(f"{tmp}-1.png")
    print(f"✓ {dest} · {lienzo.size[0]}x{lienzo.size[1]} · {os.path.getsize(dest)//1024} KB")
