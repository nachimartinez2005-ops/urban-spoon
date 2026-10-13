# -*- coding: utf-8 -*-
"""Bono 5 del paquete: porciones, sustituciones y solución de problemas.

Se creó para completar 5 bonos sin pisar el contenido de los 3 upsells
(Pack Pasteles de Cumpleaños, Kit Vende en Redes, Pack Fechas que Venden),
que se venden aparte. Por eso no toca redes, calendario ni pasteles de
fiesta: resuelve las dudas de quien recién hornea.
"""
import generar as G

PESOS = [("2 – 5 kg", "Chihuahua, yorkie, pinscher", "1 a 2"),
         ("5 – 10 kg", "Poodle, schnauzer, salchicha", "2 a 3"),
         ("10 – 20 kg", "Beagle, cocker, bulldog francés", "3 a 4"),
         ("20 – 30 kg", "Labrador, border collie, husky", "4 a 6"),
         ("30 kg o más", "Pastor alemán, rottweiler, gran danés", "6 a 8")]

SUST = [("Harina de arroz", "Avena molida en la licuadora", "Misma cantidad"),
        ("Avena", "Harina de arroz", "Misma cantidad"),
        ("Plátano machacado", "Calabaza o camote cocido", "Misma cantidad"),
        ("Calabaza cocida", "Camote cocido", "Misma cantidad"),
        ("Huevo", "2 cucharadas de puré de plátano", "Por cada huevo"),
        ("Crema de cacahuate", "Aceite de coco", "La mitad: engrasa más"),
        ("Pollo cocido", "Hígado de pollo cocido", "Misma cantidad"),
        ("Zanahoria rallada", "Calabaza rallada", "Misma cantidad"),
        ("Yogur natural", "Puedes omitirlo", "Agrega 1 cda de agua")]

PROB = [("Quedaron blandas al día siguiente",
         "Les faltó secado. Devuélvelas al horno 10 minutos a 150 °C con la "
         "puerta entreabierta y déjalas enfriar por completo antes de guardar."),
        ("Se quemaron abajo pero arriba están crudas",
         "La charola está muy cerca del piso del horno. Súbela una rejilla y "
         "usa papel manteca."),
        ("Nunca endurecen",
         "La masa tiene demasiada humedad. Agrega avena de a 1 cucharada "
         "hasta que la masa no se pegue en los dedos."),
        ("Se desarman al cortarlas",
         "Masa demasiado seca. Agrega 1 cucharada de puré de plátano o "
         "calabaza y amasa de nuevo."),
        ("El betún de yogur no cuaja",
         "El yogur tiene mucho suero. Cuélalo 2 horas en un trapo limpio "
         "dentro del refrigerador, y enfría el pastel 1 hora antes de decorar."),
        ("Se pegan al molde",
         "Engrasa con aceite de coco o, mejor, usa papel manteca. Nunca "
         "desmoldes en caliente: espera 15 minutos."),
        ("Les salieron hongos antes de tiempo",
         "Se guardaron tibias. El calor hace vapor dentro del frasco. Enfría "
         "SIEMPRE al 100 % antes de cerrar el envase."),
        ("El perro no las quiere comer",
         "Suelen estar muy duras o sin olor. Caliéntalas 10 segundos antes de "
         "dárselas: el aroma es lo que las vuelve irresistibles.")]

MED = [("1 taza de avena", "90 g"), ("1 taza de harina de arroz", "160 g"),
       ("1 taza de puré de plátano", "240 g"), ("1 plátano mediano pelado", "100 g"),
       ("1 cucharada (cda)", "15 ml"), ("1 cucharadita (cdta)", "5 ml"),
       ("Horno 180 °C", "350 °F"), ("Horno 150 °C", "300 °F")]

def p_porciones():
    filas = "".join(
        f'<tr><td>{p}</td><td style="width:38%">{razas}</td>'
        f'<td style="width:22%;font-weight:800;text-align:center">{n}</td></tr>'
        for p, razas, n in PESOS)
    return G.pg("", f"""
      <div class="hdbar">CUÁNTO DARLE SEGÚN SU PESO</div>
      <div class="pad grow" style="display:flex;flex-direction:column">
        <div class="ttl2 serif">La regla del 10 %</div>
        <div class="lede" style="margin-top:2.5mm">
          Los premios nunca deben pasar del 10 % de lo que tu perro come en el día.
          El otro 90 % es su alimento normal.
        </div>
        <table class="tbl" style="margin-top:5mm">
          <tr style="background:#B5533C;color:#fff">
            <td style="color:#fff">Peso del perro</td>
            <td style="color:#fff;font-weight:700">Razas de ejemplo</td>
            <td style="color:#fff;font-weight:700;text-align:center">Galletas al día</td></tr>
          {filas}
        </table>
        <div class="note" style="margin-top:5mm">
          <b>OJO:</b> la tabla usa galletas chicas, de unos 5 gramos. Si las tuyas
          son del doble, da la mitad. Y si ese día le diste premios, reduce un poco
          su comida.
        </div>
        <div class="grow"></div>
        <div class="warn">
          Esto es una orientación, no una indicación médica. Si tu perro tiene
          sobrepeso, diabetes, alergias o cualquier condición, pregúntale a tu
          veterinario antes de darle premios caseros.
        </div>
      </div>""")

def p_sustituciones():
    filas = "".join(f'<tr><td>{a}</td><td>{b}</td>'
                    f'<td style="width:30%;font-size:7.5pt;color:#7A6354">{c}</td></tr>'
                    for a, b, c in SUST)
    return G.pg("", f"""
      <div class="hdbar">SI NO TIENES UN INGREDIENTE</div>
      <div class="pad grow" style="display:flex;flex-direction:column">
        <div class="ttl2 serif">Sustituciones seguras</div>
        <div class="lede" style="margin-top:2.5mm">
          Ninguna receta se cancela por un ingrediente que falta. Todos los
          cambios de esta tabla usan ingredientes aprobados del curso.
        </div>
        <table class="tbl" style="margin-top:5mm">
          <tr style="background:#B5533C;color:#fff">
            <td style="color:#fff">Si la receta pide</td>
            <td style="color:#fff;font-weight:700">Puedes usar</td>
            <td style="color:#fff;font-weight:700">Cantidad</td></tr>
          {filas}
        </table>
        <div class="grow"></div>
        <div class="warn">
          Nunca sustituyas por algo que no esté en la lista de ingredientes
          seguros del Bono 2. Un cambio “lógico” puede ser tóxico: la crema de
          cacahuate con xilitol y el chocolate son los dos errores más comunes.
        </div>
      </div>""")

def p_problemas():
    cajas = "".join(
        f'<div style="margin-bottom:3.2mm"><div style="font-size:8.6pt;font-weight:800;'
        f'color:#B5533C">{t}</div><div style="font-size:8pt;line-height:1.35;'
        f'margin-top:.6mm">{s}</div></div>' for t, s in PROB)
    return G.pg("", f"""
      <div class="hdbar">SI ALGO SALE MAL</div>
      <div class="pad grow" style="display:flex;flex-direction:column">
        <div class="ttl2 serif">Ocho problemas y su arreglo</div>
        <div class="lede" style="margin-top:2mm;margin-bottom:4mm">
          Ninguna tanda se tira. Casi todo tiene arreglo.
        </div>
        {cajas}
        <div class="grow"></div>
      </div>""")

def p_medidas():
    filas = "".join(f'<tr><td>{a}</td><td style="font-weight:800">{b}</td></tr>'
                    for a, b in MED)
    chk = ["Leí la receta completa antes de empezar",
           "Revisé que ningún ingrediente esté en la lista de prohibidos",
           "Precalenté el horno",
           "Puse papel manteca en la charola",
           "Dejé enfriar al 100 % antes de guardar",
           "Etiqueté con fecha de elaboración",
           "Anoté mi costo real en la calculadora"]
    return G.pg("", f"""
      <div class="hdbar">MEDIDAS Y LISTA DE CONTROL</div>
      <div class="pad grow" style="display:flex;flex-direction:column">
        <div class="ttl2 serif">Equivalencias</div>
        <table class="tbl" style="margin-top:4mm">{filas}</table>
        <div class="lbl" style="margin-top:6mm">ANTES DE CADA TANDA</div>
        <div class="card">
          {"".join(f'<div class="row"><span>☐ &nbsp;{c}</span></div>' for c in chk)}
        </div>
        <div class="grow"></div>
        <div class="note">
          <b>IMPRIME ESTA PÁGINA.</b> Las dos primeras tandas se arruinan casi
          siempre por saltarse uno de estos siete puntos.
        </div>
      </div>""")

def build():
    P = [G.pg("cvr", """
      <div class="kick">LOMITO BAKERY · BONO 5</div>
      <h1 class="serif" style="font-size:25pt">PORCIONES<span class="q" style="font-size:16pt">SUSTITUCIONES Y SOLUCIONES</span></h1>
      <div class="lede" style="margin-top:5mm">Cuánto darle, qué hacer si falta<br>un ingrediente y cómo salvar una tanda</div>
      <div class="hero" style="font-size:36pt">⚖️ 🔄 🔧</div>
      <div class="fnote" style="font-weight:700">Pastelería Canina que Vende · 2026</div>"""),
      p_porciones(), p_sustituciones(), p_problemas(), p_medidas()]
    G.render(P, "Porciones, sustituciones y soluciones", "06-Bono-Porciones-y-soluciones")

build()
