# -*- coding: utf-8 -*-
"""Genera la Calculadora de precios (bono 2) en XLSX con fórmulas reales."""
import os, re
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.comments import Comment
from recetas import R, CATEGORIAS

OUT = "entregables/02-Bono-Calculadora-de-precios.xlsx"

TERRA, MINT, BROWN = "B5533C", "9FD5BA", "3B2B20"
CREAM, YELL = "FDF3E3", "FFF2B2"
AZUL, NEGRO, VERDE = "0000FF", "000000", "008000"

F = lambda **k: Font(name="Arial", **k)
thin = Side(style="thin", color="D9C9B3")
box = Border(left=thin, right=thin, top=thin, bottom=thin)

wb = Workbook()

# ══════════════════════ HOJA 1 · CALCULADORA ══════════════════════
ws = wb.active
ws.title = "Calculadora"
ws.sheet_view.showGridLines = False

ws["A1"] = "CALCULADORA DE PRECIOS"
ws["A1"].font = F(size=18, bold=True, color=BROWN)
ws["A2"] = "Pastelería Canina que Vende · Lomito Bakery · Bono 1 de 5"
ws["A2"].font = F(size=10, color="7A6354")

ws["A4"] = "CÓMO SE USA"
ws["A4"].font = F(size=11, bold=True, color=TERRA)
inst = [
    "1.  Llena SOLO las celdas amarillas (columnas B a F). El resto se calcula solo.",
    "2.  La fila 9 es un ejemplo ya cargado: la receta 01 del curso. No la borres, úsala de guía.",
    "3.  Escribe tus costos reales de TU ciudad. Los del curso son de referencia.",
    "4.  El multiplicador x5 es el que usa el curso: reproduce sus precios y su margen del 80 %.",
    "     Usa 5.5 o 6 si entregas a domicilio. Nunca bajes de 4.",
]
for i, t in enumerate(inst, 5):
    ws.cell(i, 1, t).font = F(size=9.5, color=BROWN)

ws["A11"] = "Azul = lo escribes tú     ·     Negro = lo calcula la hoja"
ws["A11"].font = F(size=9, italic=True, color="7A6354")

HDR = ["Producto", "Costo ingredientes", "Costo empaque POR BOLSITA", "Rinde (piezas)",
       "Piezas por bolsita", "Multiplicador", "Costo por pieza", "Ingredientes por bolsita",
       "COSTO POR BOLSITA", "PRECIO SUGERIDO", "Tu ganancia", "Margen"]
HROW = 13
for j, h in enumerate(HDR, 1):
    c = ws.cell(HROW, j, h)
    c.font = F(size=9, bold=True, color="FFFFFF")
    c.fill = PatternFill("solid", fgColor=TERRA)
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    c.border = box
ws.row_dimensions[HROW].height = 34

FIRST, LAST = HROW + 1, HROW + 20
EJEMPLO = ["Galletas de plátano y avena (ejemplo)", 25, 6, 30, 10, 5.0]

for r in range(FIRST, LAST + 1):
    es_ej = (r == FIRST)
    for j in range(1, 7):
        c = ws.cell(r, j, EJEMPLO[j - 1] if es_ej else None)
        c.font = F(size=10, color=AZUL, italic=es_ej)
        c.fill = PatternFill("solid", fgColor=YELL)
        c.border = box
        if j in (2, 3): c.number_format = '$#,##0.00'
        if j == 6: c.number_format = '0.0"x"'
    # G costo total · H costo por pieza · I costo por bolsita · J precio · K ganancia · L margen
    ws.cell(r, 7, f"=IFERROR(B{r}/D{r},\"\")")
    ws.cell(r, 8, f"=IFERROR(G{r}*E{r},\"\")")
    ws.cell(r, 9, f"=IFERROR(H{r}+C{r},\"\")")
    ws.cell(r, 10, f"=IFERROR(ROUND(I{r}*F{r}/5,0)*5,\"\")")
    ws.cell(r, 11, f"=IFERROR(J{r}-I{r},\"\")")
    ws.cell(r, 12, f"=IFERROR(K{r}/J{r},\"\")")
    for j in range(7, 13):
        c = ws.cell(r, j)
        c.font = F(size=10, color=NEGRO, bold=(j == 10))
        c.border = box
        c.number_format = '0.0%' if j == 12 else '$#,##0.00'
        if j == 10:
            c.fill = PatternFill("solid", fgColor=MINT)
            c.number_format = '$#,##0'

ws.cell(FIRST, 1).comment = Comment(
    "Fila de ejemplo tomada de la Receta 01 del curso:\n"
    "$25 de ingredientes por tanda, $6 de empaque por bolsita,\n"
    "rinde 30 galletas, "
    "bolsita de 10 piezas. Dato del propio ebook.", "Lomito Bakery")
ws.cell(HROW, 6).comment = Comment(
    "5.0 es el multiplicador que usa el curso.\n"
    "Verificado contra las 30 recetas: reproduce sus precios\n"
    "y su margen del 80 %. Usa 5.5-6 si entregas a domicilio.", "Lomito Bakery")

# ─── Bloque: cuántas bolsitas para recuperar la inversión ───
rr = LAST + 3
ws.cell(rr, 1, "¿CUÁNTO FALTA PARA RECUPERAR LO QUE INVERTISTE?").font = F(size=11, bold=True, color=TERRA)
ws.cell(rr + 1, 1, "Lo que gastaste (curso, ingredientes, empaque, moldes)").font = F(size=10, color=BROWN)
inv = ws.cell(rr + 1, 4, 500)
inv.font = F(size=10, color=AZUL, bold=True)
inv.fill = PatternFill("solid", fgColor=YELL)
inv.number_format = '$#,##0'
inv.border = box
inv.comment = Comment("Cámbialo por lo que gastaste de verdad.\nEl valor de ejemplo es $500 MXN.", "Lomito Bakery")

ws.cell(rr + 2, 1, "Bolsitas que tienes que vender (según la fila de ejemplo)").font = F(size=10, color=BROWN)
cel = ws.cell(rr + 2, 4, f"=IFERROR(ROUNDUP(D{rr+1}/K{FIRST},0),\"\")")
cel.font = F(size=12, bold=True, color=NEGRO)
cel.fill = PatternFill("solid", fgColor=MINT)
cel.border = box
cel.number_format = '0'

ws.cell(rr + 4, 1, "Nota: todos los montos están en pesos mexicanos (MXN). "
                   "Los costos del curso son de referencia; usa los de tu ciudad.").font = F(size=8.5, italic=True, color="7A6354")

for col, w in zip("ABCDEFGHIJKL", [34, 15, 13, 13, 14, 12, 12, 13, 14, 16, 12, 10]):
    ws.column_dimensions[col].width = w
ws.freeze_panes = f"A{FIRST}"

# ══════════════════════ HOJA 2 · MIS 30 RECETAS ══════════════════════
w2 = wb.create_sheet("Mis 30 recetas")
w2.sheet_view.showGridLines = False
w2["A1"] = "LAS 30 RECETAS DEL CURSO"
w2["A1"].font = F(size=16, bold=True, color=BROWN)
w2["A2"] = "Costos y precios de referencia que ya trae cada receta. Úsalos como punto de partida."
w2["A2"].font = F(size=9.5, color="7A6354")

H2 = ["#", "Categoría", "Receta", "Costo aprox.", "Precio de venta", "Margen", "Nueva"]
for j, h in enumerate(H2, 1):
    c = w2.cell(4, j, h)
    c.font = F(size=9, bold=True, color="FFFFFF")
    c.fill = PatternFill("solid", fgColor=TERRA)
    c.alignment = Alignment(horizontal="center", vertical="center")
    c.border = box

num = lambda s: float(re.sub(r"[^\d.]", "", s) or 0)
for i, r in enumerate(R, 5):
    vals = [r["n"], CATEGORIAS[r["cat"]][0].title(), r["titulo"],
            num(r["costo"]), num(r["venta"].split("·")[-1]), num(r["margen"]) / 100,
            "Nueva" if r["nuevo"] else ""]
    for j, v in enumerate(vals, 1):
        c = w2.cell(i, j, v)
        c.font = F(size=9.5, color=BROWN, bold=(j == 7 and v == "Nueva"))
        c.border = box
        if j in (4, 5): c.number_format = '$#,##0'
        if j == 6: c.number_format = '0%'
        if j == 7 and v == "Nueva":
            c.fill = PatternFill("solid", fgColor=MINT)
    if i % 2 == 0:
        for j in range(1, 8):
            if not (j == 7 and vals[6] == "Nueva"):
                w2.cell(i, j).fill = PatternFill("solid", fgColor=CREAM)

tot = len(R) + 5
w2.cell(tot, 3, "Promedio").font = F(size=10, bold=True, color=BROWN)
for j, col in [(4, "D"), (5, "E"), (6, "F")]:
    c = w2.cell(tot, j, f"=AVERAGE({col}5:{col}{tot-1})")
    c.font = F(size=10, bold=True, color=NEGRO)
    c.number_format = '0%' if j == 6 else '$#,##0'
    c.border = box
    c.fill = PatternFill("solid", fgColor=MINT)

for col, w in zip("ABCDEFG", [5, 22, 40, 13, 16, 10, 9]):
    w2.column_dimensions[col].width = w
w2.freeze_panes = "A5"

os.makedirs("entregables", exist_ok=True)
wb.save(OUT)
print(f"✓ {OUT} · {os.path.getsize(OUT)//1024} KB · 2 hojas")
