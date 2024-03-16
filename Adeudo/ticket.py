from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import barcode

def generar_ticket(datos_solicitante, datos_equipo, responsable_nombre):
    c = canvas.Canvas("ticket.pdf", pagesize=letter)

    # Agregar texto al ticket
    c.drawString(100, 750, "Folio: 123456")
    c.drawString(100, 730, f"Responsable: {responsable_nombre}")

    # Agregar datos del solicitante
    y = 700
    for clave, valor in datos_solicitante.items():
        c.drawString(100, y, f"{clave}: {valor}")
        y -= 20

    # Agregar datos del equipo
    y -= 20
    for clave, valor in datos_equipo.items():
        c.drawString(100, y, f"{clave}: {valor}")
        y -= 20

    # Generar código de barras (ejemplo utilizando EAN13)
    codigo_barras = barcode.get_barcode_class('ean13')
    codigo = codigo_barras('1234567890128')
    codigo_filename = 'codigo_barras.png'
    codigo.write(codigo_filename)

    # Agregar código de barras al ticket
    c.drawImage(codigo_filename, 100, 100)

    c.save()
