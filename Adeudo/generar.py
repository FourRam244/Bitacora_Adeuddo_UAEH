import tkinter as tk
from image_loader import ImageLoader
from PIL import Image, ImageTk, ImageDraw
from PIL import ImageFont
from tkcalendar import DateEntry  # Importamos el widget de calendario
import menu
import tempfile
import os
import barcode
from barcode import Code39
from barcode.writer import ImageWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import qrcode

contador_folios = 12345

class GenerarVale:
    def __init__(self, menu_principal):
        self.menu_principal = None 
        self.folio_counter = self.cargar_folio()  # Cargar el contador de folio

        self.root = tk.Toplevel()
        self.root.title("Generar Vale")
        self.root.iconbitmap("logo4.ico")
        # Obtener las dimensiones de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular las coordenadas para la ventana centrada en la parte superior
        window_width = 390  # Ancho deseado de la ventana
        window_height = 705  # Alto deseado de la ventana
        x = (screen_width - window_width) // 2
        y = 50  # Altura deseada desde la parte superior de la pantalla

        # Establecer las coordenadas para la ventana
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.image_loader = ImageLoader()

        self.logo1_label = tk.Label(self.root, image=self.image_loader.get_logo1())
        self.logo1_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        self.logo2_label = tk.Label(self.root, image=self.image_loader.get_logo2())
        self.logo2_label.grid(row=0, column=1, sticky=tk.E, padx=10, pady=10)

        titulo_label = tk.Label(self.root, text="Préstamo de Equipo", font=("Helvetica", 20))
        titulo_label.grid(row=1, columnspan=2, pady=20)

        datos_solicitante_label = tk.Label(self.root, text="Datos del Solicitante", font=("Helvetica", 14, "bold"))
        datos_solicitante_label.grid(row=2, column=0, columnspan=2, pady=(10, 5))

        self.nombre_label = tk.Label(self.root, text="Nombre:")
        self.nombre_label.grid(row=3, column=0, sticky='w')
        self.nombre_entry = tk.Entry(self.root)
        self.nombre_entry.grid(row=3, column=1)
        self.nombre_entry.bind('<KeyRelease>', self.validar_campos)

        self.dependencia_label = tk.Label(self.root, text="Dependencia:")
        self.dependencia_label.grid(row=4, column=0, sticky='w')
        self.dependencia_entry = tk.Entry(self.root)
        self.dependencia_entry.grid(row=4, column=1)
        self.dependencia_entry.bind('<KeyRelease>', self.validar_campos)

        self.num_empleado_label = tk.Label(self.root, text="Num. Empleado:")
        self.num_empleado_label.grid(row=5, column=0, sticky='w')
        self.num_empleado_entry = tk.Entry(self.root)
        self.num_empleado_entry.grid(row=5, column=1)
        self.num_empleado_entry.bind('<KeyRelease>', self.validar_campos)

        self.telefono_ext_label = tk.Label(self.root, text="Teléfono/Ext:")
        self.telefono_ext_label.grid(row=6, column=0, sticky='w')
        self.telefono_ext_entry = tk.Entry(self.root)
        self.telefono_ext_entry.grid(row=6, column=1)
        self.telefono_ext_entry.bind('<KeyRelease>', self.validar_campos)

        self.correo_label = tk.Label(self.root, text="Correo Institucional:")
        self.correo_label.grid(row=7, column=0, sticky='w')
        self.correo_entry = tk.Entry(self.root)
        self.correo_entry.grid(row=7, column=1)
        self.correo_entry.bind('<KeyRelease>', self.validar_campos)

        datos_equipo_label = tk.Label(self.root, text="Datos del Equipo", font=("Helvetica", 14, "bold"))
        datos_equipo_label.grid(row=8, column=0, columnspan=2, pady=(20, 5))

        self.nombre_equipo_label = tk.Label(self.root, text="Nombre:")
        self.nombre_equipo_label.grid(row=9, column=0, sticky='w')
        self.nombre_equipo_entry = tk.Entry(self.root)
        self.nombre_equipo_entry.grid(row=9, column=1)
        self.nombre_equipo_entry.bind('<KeyRelease>', self.validar_campos)

        self.modelo_label = tk.Label(self.root, text="Modelo:")
        self.modelo_label.grid(row=10, column=0, sticky='w')
        self.modelo_entry = tk.Entry(self.root)
        self.modelo_entry.grid(row=10, column=1)
        self.modelo_entry.bind('<KeyRelease>', self.validar_campos)

        self.marca_label = tk.Label(self.root, text="Marca:")
        self.marca_label.grid(row=11, column=0, sticky='w')
        self.marca_entry = tk.Entry(self.root)
        self.marca_entry.grid(row=11, column=1)
        self.marca_entry.bind('<KeyRelease>', self.validar_campos)

        self.num_serie_label = tk.Label(self.root, text="Num. Serie:")
        self.num_serie_label.grid(row=12, column=0, sticky='w')
        self.num_serie_entry = tk.Entry(self.root)
        self.num_serie_entry.grid(row=12, column=1)
        self.num_serie_entry.bind('<KeyRelease>', self.validar_campos)

        self.num_inventario_label = tk.Label(self.root, text="No. Inventario:")
        self.num_inventario_label.grid(row=13, column=0, sticky='w')
        self.num_inventario_entry = tk.Entry(self.root)
        self.num_inventario_entry.grid(row=13, column=1)
        self.num_inventario_entry.bind('<KeyRelease>', self.validar_campos)
        
        
        self.fecha_salida_label = tk.Label(self.root, text="Fecha de Salida:")
        self.fecha_salida_label.grid(row=14, column=0, sticky='w')
        self.fecha_salida_entry = DateEntry(self.root, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.fecha_salida_entry.grid(row=14, column=1)

        self.fecha_entrega_label = tk.Label(self.root, text="Fecha de Entrega:")
        self.fecha_entrega_label.grid(row=15, column=0, sticky='w')
        self.fecha_entrega_entry = DateEntry(self.root, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.fecha_entrega_entry.grid(row=15, column=1)

        responsables = ["Juan Daniel Ramírez Zamora", "Jose Manuel Fernandez Ramírez", "Otro"]
        self.responsable_nombre_label = tk.Label(self.root, text="Responsable:")
        self.responsable_nombre_label.grid(row=17, column=0, sticky='w')
        self.responsable_nombre_option = tk.StringVar(self.root)
        self.responsable_nombre_option.set(responsables[0])
        self.responsable_nombre_menu = tk.OptionMenu(self.root, self.responsable_nombre_option, *responsables,command=self.habilitar_otro)
        self.responsable_nombre_menu.grid(row=17, column=1)
        
        
        self.otro_responsable_label = tk.Label(self.root, text="Otro Responsable:")
        self.otro_responsable_label.grid(row=18, column=0, sticky='w')
        self.otro_responsable_entry = tk.Entry(self.root, state='disabled')
        self.otro_responsable_entry.grid(row=18, column=1)

        self.guardar_button = tk.Button(self.root, text="Guardar", command=self.guardar_y_generar_ticket, state='disabled')
        self.guardar_button.grid(row=19, columnspan=2, pady=20)
        
    def habilitar_otro(self, responsable):
        if responsable == "Otro":
            self.otro_responsable_entry.config(state='normal')
        else:
            self.otro_responsable_entry.config(state='disabled')
            self.otro_responsable_entry.delete(0, tk.END)

    def on_closing(self):
        self.root.destroy()  # Cerrar la ventana de generar vale
        if self.menu_principal:
            self.menu_principal.master.deiconify()  # Mostrar la ventana del menú principal nuevamente
            
            
    def validar_campos(self, event):
        if all([
            self.nombre_entry.get(),
            self.dependencia_entry.get(),
            self.num_empleado_entry.get(),
            self.telefono_ext_entry.get(),
            self.correo_entry.get(),
            self.nombre_equipo_entry.get(),
            self.modelo_entry.get(),
            self.marca_entry.get(),
            self.num_serie_entry.get(),
            self.num_inventario_entry.get(),
        ]):
            if self.responsable_nombre_option.get() != "Otro" or self.otro_responsable_entry.get():
                self.guardar_button.config(state='normal')
            else:
                self.guardar_button.config(state='disabled')
        else:
            self.guardar_button.config(state='disabled')
            
            

            
    def cargar_folio(self):
        try:
            with open("folio.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 1

    def guardar_folio(self, folio):
        with open("folio.txt", "w") as file:
            file.write(str(folio))
            

            
            
    def guardar_y_generar_ticket(self):
        # Obtener datos del formulario
        datos_solicitante = {
            "Nombre": self.nombre_entry.get(),
            "Dependencia": self.dependencia_entry.get(),
            "Num. Empleado": self.num_empleado_entry.get(),
            "Teléfono/Ext": self.telefono_ext_entry.get(),
            "Correo Institucional": self.correo_entry.get()
        }

        datos_equipo = {
            "Nombre": self.nombre_equipo_entry.get(),
            "Modelo": self.modelo_entry.get(),
            "Marca": self.marca_entry.get(),
            "Num. Serie": self.num_serie_entry.get(),
            "No. Inventario": self.num_inventario_entry.get(),
            "Fecha de Salida": self.fecha_salida_entry.get(),
            "Fecha de Entrega": self.fecha_entrega_entry.get()
        }

        responsable_nombre = self.responsable_nombre_option.get()
        
        if responsable_nombre == "Otro":
            responsable_nombre = self.otro_responsable_entry.get()
                

        # Generar el folio
        folio = self.folio_counter  # Usar el folio actual

        qr_data = f"Folio: {folio}\nSolicitante: {datos_solicitante['Nombre']}\nResponsable: {responsable_nombre}"
        qr_code = self.generar_qr(qr_data)
        barcode_path = self.generar_codigo_barras(str(folio))
        generar_ticket(datos_solicitante, datos_equipo, responsable_nombre, folio, qr_code, barcode_path)

      # Generar el ticket en formato PDF
        generar_ticket_pdf(datos_solicitante, datos_equipo, responsable_nombre, folio, qr_code, barcode_path)


        # Incrementar el contador de folio para el próximo uso
        self.folio_counter += 1
        self.guardar_folio(self.folio_counter)

        # Cerrar la ventana de generar vale
        self.root.destroy()
        # Mostrar la ventana del menú principal nuevamente
        self.menu_principal.master.deiconify()
        
    
    def generar_qr(self, data):
        qr = qrcode.make(data)
        qr_path = os.path.join(os.path.dirname(__file__), "Archivos", "qr_code.png")
        qr.save(qr_path)
        return qr_path

    def generar_codigo_barras(self, data):
       # Generar el código de barras en formato PNG
        code = Code39(data, writer=ImageWriter())
        # Obtener la ruta completa para guardar el archivo de código de barras
        barcode_path = os.path.join(os.path.dirname(__file__), "Archivos", "barcode")
        code.save(barcode_path)
        return barcode_path
    
def mostrar_ticket(folio):
    ticket_window = tk.Toplevel()
    ticket_window.title("Ticket Generado")
    ticket_window.iconbitmap("logo4.ico")
    
    
    ticket_image_path = f"./Archivos/{folio}.png"

    ticket_image = Image.open(ticket_image_path)
    ticket_photo = ImageTk.PhotoImage(ticket_image)
    ticket_label = tk.Label(ticket_window, image=ticket_photo)
    ticket_label.image = ticket_photo
    ticket_label.pack()
def generar_ticket(datos_solicitante, datos_equipo, responsable_nombre, folio, qr_code, barcode_path):
    ticket_image = Image.new("RGB", (400, 600), (255, 255, 255))
    ticket_draw = ImageDraw.Draw(ticket_image)
    font = ImageFont.truetype("arial.ttf", 12)

    # Datos del Solicitante
    ticket_draw.text((10, 10), "Datos del Solicitante:", fill=(0, 0, 0), font=font)
    y_offset = 30
    for key, value in datos_solicitante.items():
        ticket_draw.text((10, y_offset), f"{key}: {value}", fill=(0, 0, 0), font=font)
        y_offset += 20

    # Datos del Equipo
    ticket_draw.text((10, y_offset), "Datos del Equipo:", fill=(0, 0, 0), font=font)
    y_offset += 20
    for key, value in datos_equipo.items():
        ticket_draw.text((10, y_offset), f"{key}: {value}", fill=(0, 0, 0), font=font)
        y_offset += 20

    # Responsable
    ticket_draw.text((10, y_offset), f"Responsable: {responsable_nombre}", fill=(0, 0, 0), font=font)
    y_offset += 20

    # Folio
    ticket_draw.text((10, y_offset), f"Folio: {folio}", fill=(0, 0, 0), font=font)
    y_offset += 20

    # Código QR
    qr_image = Image.open("./Archivos/qr_code.png")
    qr_image = qr_image.resize((100, 100))  # Ajusta el tamaño del código QR según lo necesites
    ticket_image.paste(qr_image, (10, y_offset))
    y_offset += qr_image.size[1] + 20

    # Código de barras
    barcode_image = Image.open("./Archivos/barcode.png")
    barcode_image = barcode_image.resize((200, 50))  # Ajusta el tamaño del código de barras según lo necesites
    ticket_image.paste(barcode_image, (10, y_offset))

    ticket_path = f"./Archivos/{folio}.png"

    ticket_image.save(ticket_path)

    mostrar_ticket(folio)

def generar_ticket_pdf(datos_solicitante, datos_equipo, responsable_nombre, folio, qr_code, barcode_path):
    # Crear un lienzo PDF
    ticket_pdf_path =  f"./Archivos/PDFs/{folio}.pdf"
    c = canvas.Canvas(ticket_pdf_path, pagesize=letter)

    # Definir el contenido del ticket en el lienzo PDF
    c.drawString(100, 750, "Ticket de Préstamo de Equipo")
    c.drawString(100, 730, f"Folio: {folio}")
    c.drawString(100, 710, f"Datos del Solicitante:")
    y_offset = 690
    for key, value in datos_solicitante.items():
        c.drawString(120, y_offset, f"{key}: {value}")
        y_offset -= 20

    c.drawString(100, y_offset, f"Datos del Equipo:")
    y_offset -= 20
    for key, value in datos_equipo.items():
        c.drawString(120, y_offset, f"{key}: {value}")
        y_offset -= 20

    c.drawString(100, y_offset, f"Responsable: {responsable_nombre}")

    # Agregar el código QR al PDF
    c.drawInlineImage("./Archivos/qr_code.png", 100, y_offset - 120, width=100, height=100)

    # Agregar el código de barras al PDF
    c.drawInlineImage("./Archivos/barcode.png", 100, y_offset - 200, width=200, height=50)

    # Guardar el lienzo PDF
    c.save()


def main():
    root = tk.Tk()
    generar_ticket_button = tk.Button(root, text="Generar Ticket", command=generar_ticket)
    generar_ticket_button.pack()
    root.mainloop()

if __name__ == "__main__":
    main()