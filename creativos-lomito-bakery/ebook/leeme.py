# -*- coding: utf-8 -*-
"""Genera 00-LEEME-PRIMERO.pdf: la hoja de bienvenida del paquete.

Estructura: 1 producto principal + 5 bonos. Los 3 upsells (Pack Pasteles
de Cumpleaños, Kit Vende en Redes, Pack Fechas que Venden) se venden
aparte y NO se nombran acá como si vinieran incluidos.
"""
import generar as G

PRINCIPAL = ("01", "Curso Pastelería Canina · 30 recetas", "PDF · 72 págs",
             "Las 30 recetas paso a paso, en 5 categorías. Cada una con su costo, "
             "su precio de venta, su margen, tamaños, conservación y 4 formas de venderla.")

BONOS = [("02", "Calculadora de precios", "Excel / Google Sheets",
          "Metés tus costos y te dice exactamente qué cobrar. Trae una segunda "
          "hoja con las 30 recetas y sus números."),
         ("03", "Guía de ingredientes seguros y prohibidos", "PDF · 4 págs",
          "Los 12 que sí y los 9 que nunca. Imprimible."),
         ("04", "Plan de negocio desde casa", "PDF · 5 págs",
          "La fórmula de precios, el empaque, de dónde salen tus primeros 10 "
          "pedidos y los mensajes para vender."),
         ("05", "Plantillas de etiquetas", "PDF · 5 págs",
          "Para imprimir, recortar y pegar en tus bolsitas."),
         ("06", "Porciones, sustituciones y soluciones", "PDF · 5 págs",
          "Cuánto darle según su peso, qué usar si falta un ingrediente y cómo "
          "salvar una tanda que salió mal.")]

PASOS = [("1", "Abrí el archivo <b>01</b> y andá directo a la Receta 01. Es la más "
               "fácil, la más barata y la que más se vende."),
         ("2", "Imprimí el archivo <b>03</b> y pegalo en tu refrigerador."),
         ("3", "Cuando quieras poner precios, abrí el <b>02</b> en Excel o Google "
               "Sheets y llená solo las celdas amarillas.")]

def ficha(n, t, f_, d, destacado=False):
    borde = "border:1.4pt solid #B5533C;" if destacado else ""
    return f'''<div style="padding:2.8mm 4mm;border-bottom:1pt solid var(--line);{borde}">
         <div style="display:flex;justify-content:space-between;align-items:baseline">
           <span style="font-size:9pt;font-weight:800"><span style="color:#B5533C">{n}</span> &nbsp;{t}</span>
           <span style="font-size:6.5pt;color:#7A6354;white-space:nowrap">{f_}</span></div>
         <div style="font-size:7.6pt;color:#7A6354;line-height:1.35;margin-top:.8mm">{d}</div>
       </div>'''

p1 = G.pg("", f"""
  <div class="hdbar">EMPEZÁ POR ACÁ</div>
  <div class="pad grow">
    <div class="kick">Lomito Bakery · Edición 2026</div>
    <div class="ttl2 serif" style="margin-top:2.5mm">Pastelería Canina que Vende</div>
    <div class="lede" style="margin-top:2.5mm">
      ¡Gracias por tu compra! Tu paquete son <b>6 archivos</b>: el curso y 5 bonos.
    </div>

    <div class="lbl" style="margin-top:6mm">TUS PRIMEROS 3 PASOS</div>
    {"".join(f'<div class="stp"><i>{n}</i><span>{t}</span></div>' for n, t in PASOS)}

    <div class="lbl" style="margin-top:5.5mm">EL CURSO</div>
    <div class="card">{ficha(*PRINCIPAL, destacado=True)}</div>

    <div class="lbl" style="margin-top:5mm">TUS 5 BONOS</div>
    <div class="card">{"".join(ficha(*b) for b in BONOS[:3])}</div>
  </div>
  <div class="pad fnote" style="padding-top:0">lomitobakery.impultienda.ar</div>""")

p2 = G.pg("", f"""
  <div class="hdbar">TUS 5 BONOS · CONTINUACIÓN</div>
  <div class="pad grow">
    <div class="card">{"".join(ficha(*b) for b in BONOS[3:])}</div>

    <div class="box" style="margin-top:6mm">
      <b>Un consejo para la primera semana</b>
      No intentes las 30 recetas. Elegí 3: una galleta, un pastel y un premio
      deshidratado. Con esas tres armás una bolsita, una caja de cumpleaños y
      un premio de entrenamiento, que es todo lo que te van a pedir al principio.
    </div>

    <div class="note" style="margin-top:5mm">
      <b>¿ALGO NO ABRE?</b> Respondé el correo con el que recibiste este paquete
      y te lo mandamos por otro medio. No te quedes sin tus archivos.
    </div>
  </div>
  <div class="pad" style="padding-top:0">
    <div class="warn">
      Estas recetas son premios y no sustituyen el alimento diario de tu mascota:
      no deben superar el 10 % de su alimentación. Consultá siempre al veterinario
      ante dudas, alergias o condiciones de salud.
    </div>
    <div class="fnote" style="margin-top:3.5mm">
      Precios sugeridos en pesos mexicanos. Tus ganancias dependen de tus costos,
      tu zona y tus ventas. &nbsp;·&nbsp; lomitobakery.impultienda.ar
    </div>
  </div>""")

G.render([p1, p2], "Empezá por acá · Pastelería Canina que Vende", "00-LEEME-PRIMERO")
