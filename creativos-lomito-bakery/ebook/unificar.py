# -*- coding: utf-8 -*-
"""Fusiona los 4 PDFs del paquete en UN solo archivo, con portada e índice.

Para Impultienda, que acepta un PDF o un link, pero no un ZIP.
Salida: entregables/Pasteleria-Canina-que-Vende-TODO-EN-UNO.pdf
"""
import os
from pypdf import PdfWriter, PdfReader
import generar as G

OUT = "entregables"
PARTES = ["01-Curso-Pasteleria-Canina-30-recetas",
          "03-Bono-Guia-de-ingredientes",
          "04-Bono-Plan-de-negocio",
          "05-Bono-Plantillas-de-etiquetas"]

def portada():
    p1 = G.pg("", f"""
      <div class="grow" style="display:flex;flex-direction:column;justify-content:center;padding:0 12mm">
        <div class="kick">Lomito Bakery</div>
        <div class="ttl serif" style="margin-top:4mm">Pastelería Canina<br>que Vende</div>
        <div class="lede" style="margin-top:5mm">
          30 recetas aprobadas, los costos reales de cada una y el precio al que
          se vende. Todo el paquete en un solo archivo.
        </div>
        <div class="price" style="margin-top:9mm">
          <div class="big">5 entregables · 88 páginas</div>
          <div class="sm">Curso completo + 4 bonos</div>
        </div>
      </div>
      <div class="pad fnote">Edición 2026. Uso personal del comprador.</div>""")

    filas = "".join(
        f'<div class="row"><span><b>{n}.</b> {t}</span><span style="color:#7A6354">{pg}</span></div>'
        for n, t, pg in [
            ("1", "Curso: las 30 recetas", "pág. 3"),
            ("2", "Calculadora de precios", "archivo aparte"),
            ("3", "Guía de ingredientes seguros", "pág. 75"),
            ("4", "Plan de negocio desde casa", "pág. 79"),
            ("5", "Plantillas de etiquetas", "pág. 84"),
        ])

    p2 = G.pg("", f"""
      <div class="hdbar">QUÉ CONTIENE ESTE ARCHIVO</div>
      <div class="pad grow">
        <div class="card">{filas}</div>

        <div class="note" style="margin-top:6mm">
          <b>Sobre la calculadora (entregable 2)</b><br>
          Es una hoja de cálculo, no un PDF: le escribís tus costos y te devuelve
          el precio de venta y tu margen. Por eso viaja como archivo separado
          — adentro de un PDF no podría calcular nada.
        </div>

        <div class="box" style="margin-top:5mm">
          <b>Cómo se usa el curso</b>
          Cada receta trae su costo aproximado, el precio al que se vende y el
          margen. Son precios de referencia en pesos mexicanos: cambiá los
          costos por los de tu ciudad y multiplicá por 5 para fijar tu precio.
        </div>

        <div class="warn" style="margin-top:5mm">
          Ninguna receta reemplaza al veterinario. Si tu perro tiene alergias,
          sobrepeso o una condición médica, consultá antes de darle premios caseros.
        </div>
      </div>
      <div class="pad fnote">lomitobakery.impultienda.ar</div>""")
    return [p1, p2]

G.render(portada(), "Pastelería Canina que Vende", "zz-portada-tmp")

w = PdfWriter()
for pg_ in PdfReader(os.path.join(OUT, "zz-portada-tmp.pdf")).pages:
    w.add_page(pg_)
total = 2
marcas = []
for nom in PARTES:
    r = PdfReader(os.path.join(OUT, nom + ".pdf"))
    marcas.append((nom, total + 1))
    for pg_ in r.pages:
        w.add_page(pg_)
    total += len(r.pages)

for nom, n in marcas:
    w.add_outline_item(nom[3:].replace("-", " "), n - 1)

dest = os.path.join(OUT, "Pasteleria-Canina-que-Vende-TODO-EN-UNO.pdf")
w.write(dest)
os.remove(os.path.join(OUT, "zz-portada-tmp.pdf"))
print(f"\n✓ {dest} · {total} págs · {os.path.getsize(dest)//1024} KB")
for nom, n in marcas:
    print(f"    pág {n:>3}  {nom}")
