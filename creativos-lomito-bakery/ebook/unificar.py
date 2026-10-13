# -*- coding: utf-8 -*-
"""Fusiona el curso y los 4 bonos en PDF en UN solo archivo, con portada,
índice y marcadores.

Impultienda acepta un PDF o un link, no un ZIP. Este archivo es la opción
sin dependencias: todo menos la calculadora, que es una hoja de cálculo y
dentro de un PDF no calcularía nada.

Los números de página del índice se calculan leyendo los PDFs reales, no
se escriben a mano: así no se desincronizan cuando cambia un bono.
"""
import os
from pypdf import PdfWriter, PdfReader
import generar as G

OUT = "entregables"
PORTADA = 2                      # páginas de portada + índice
PARTES = [("01-Curso-Pasteleria-Canina-30-recetas", "Curso: las 30 recetas"),
          ("03-Bono-Guia-de-ingredientes",          "Bono 2 · Ingredientes seguros"),
          ("04-Bono-Plan-de-negocio",               "Bono 3 · Plan de negocio"),
          ("05-Bono-Plantillas-de-etiquetas",       "Bono 4 · Plantillas de etiquetas"),
          ("06-Bono-Porciones-y-soluciones",        "Bono 5 · Porciones y soluciones")]

# ── 1. leer los PDFs reales y calcular dónde arranca cada uno ──
lectores, inicio, cursor = [], [], PORTADA + 1
for nom, _ in PARTES:
    r = PdfReader(os.path.join(OUT, nom + ".pdf"))
    lectores.append(r)
    inicio.append(cursor)
    cursor += len(r.pages)
TOTAL = cursor - 1

# ── 2. portada e índice con esos números ──
FILAS = [("1", "Curso: las 30 recetas",          f"pág. {inicio[0]}"),
         ("2", "Calculadora de precios",          "archivo aparte"),
         ("3", "Guía de ingredientes seguros",   f"pág. {inicio[1]}"),
         ("4", "Plan de negocio desde casa",     f"pág. {inicio[2]}"),
         ("5", "Plantillas de etiquetas",        f"pág. {inicio[3]}"),
         ("6", "Porciones y soluciones",         f"pág. {inicio[4]}")]

def portada():
    p1 = G.pg("", f"""
      <div class="grow" style="display:flex;flex-direction:column;justify-content:center;padding:0 12mm">
        <div class="kick">Lomito Bakery</div>
        <div class="ttl serif" style="margin-top:4mm">Pastelería Canina<br>que Vende</div>
        <div class="lede" style="margin-top:5mm">
          30 recetas aprobadas, los costos reales de cada una y el precio al que
          se vende. El curso y sus 5 bonos en un solo archivo.
        </div>
        <div class="price" style="margin-top:9mm">
          <div class="big">Curso + 5 bonos · {TOTAL} páginas</div>
          <div class="sm">Edición 2026</div>
        </div>
      </div>
      <div class="pad fnote">Uso personal del comprador.</div>""")

    filas = "".join(
        f'<div class="row"><span><b>{n}.</b> {t}</span>'
        f'<span style="color:#7A6354">{p}</span></div>' for n, t, p in FILAS)

    p2 = G.pg("", f"""
      <div class="hdbar">QUÉ CONTIENE ESTE ARCHIVO</div>
      <div class="pad grow">
        <div class="card">{filas}</div>

        <div class="note" style="margin-top:6mm">
          <b>Sobre la calculadora</b><br>
          Es una hoja de cálculo, no un PDF: le escribís tus costos y te devuelve
          el precio de venta y tu margen. Por eso viaja como archivo separado
          — adentro de un PDF no podría calcular nada.
        </div>

        <div class="box" style="margin-top:5mm">
          <b>Cómo se usa el curso</b>
          Cada receta trae su costo aproximado, el precio al que se vende y el
          margen. Son precios de referencia en pesos mexicanos: cambia los
          costos por los de tu ciudad y multiplica por 5 para fijar tu precio.
        </div>

        <div class="warn" style="margin-top:5mm">
          Ninguna receta reemplaza al veterinario. Si tu perro tiene alergias,
          sobrepeso o una condición médica, consulta antes de darle premios caseros.
        </div>
      </div>
      <div class="pad fnote">lomitobakery.impultienda.ar</div>""")
    return [p1, p2]

G.render(portada(), "Pastelería Canina que Vende", "zz-portada-tmp")

# ── 3. unir ──
w = PdfWriter()
for p in PdfReader(os.path.join(OUT, "zz-portada-tmp.pdf")).pages:
    w.add_page(p)
for (nom, titulo), r, n in zip(PARTES, lectores, inicio):
    for p in r.pages:
        w.add_page(p)
    w.add_outline_item(titulo, n - 1)

dest = os.path.join(OUT, "Pasteleria-Canina-que-Vende-TODO-EN-UNO.pdf")
w.write(dest)
os.remove(os.path.join(OUT, "zz-portada-tmp.pdf"))

print(f"\n✓ {dest} · {TOTAL} págs · {os.path.getsize(dest)//1024} KB")
for (nom, titulo), n in zip(PARTES, inicio):
    print(f"    pág {n:>3}  {titulo}")
