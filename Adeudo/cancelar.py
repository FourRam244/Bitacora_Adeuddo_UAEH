import tkinter as tk
from image_loader import ImageLoader
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import menu
import consultar
import cancelar


class CancelarVale:
    def __init__(self,master):
        self.master = master
        self.root = tk.Toplevel()
        self.root.title("Cancelar Vale")
        self.root.iconbitmap("logo4.ico")
        self.menu_principal = None 
        
        # Obtener las dimensiones de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular las coordenadas para la ventana centrada en la parte superior
        window_width = 400  # Ancho deseado de la ventana
        window_height = 900  # Alto deseado de la ventana
        x = (screen_width - window_width) // 2
        y = 50  # Altura deseada desde la parte superior de la pantalla

        # Establecer las coordenadas para la ventana
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.image_loader = ImageLoader() 

        # Crear los widgets para los logotipos
        self.logo1_label = tk.Label(self.root, image=self.image_loader.get_logo1())
        self.logo1_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        self.logo2_label = tk.Label(self.root, image=self.image_loader.get_logo2())
        self.logo2_label.grid(row=0, column=1, sticky=tk.E, padx=10, pady=10)


        # Título del menú
        titulo_label = tk.Label(self.root, text="Consultar Vale", font=("Helvetica", 20))
        titulo_label.grid(row=1, columnspan=2, pady=20)
        
        # Campos de texto para los datos del solicitante
        self.nombre_label = tk.Label(self.root, text="Numero de Folio:")
        self.nombre_label.grid(row=3, column=0, sticky='w')
        self.nombre_entry = tk.Entry(self.root)
        self.nombre_entry.grid(row=3, column=1)
        
        # Botón para guardar los datos
        guardar_button = tk.Button(self.root, text="Consulta", command=self.consultar_vale)  # Vincula el botón al método consultar_vale
        guardar_button.grid(row=4, columnspan=2, pady=20)
        # Botón para guardar los datos
        guardar_button = tk.Button(self.root, text="Cancelar",command=self.cancelar_consulta)  # Vincula el botón al método consultar_vale
        guardar_button.grid(row=25, columnspan=2, pady=20)
        
        # Label para mostrar la imagen del vale
        self.vale_image_label = tk.Label(self.root)
        self.vale_image_label.grid(row=5, columnspan=2)
    
    def consultar_vale(self):
        folio = self.nombre_entry.get()  # Obtén el número de folio del campo de entrada
        image_path = f"./Archivos/{folio}.png"  # Ruta de la imagen basada en el número de folio
    
        if os.path.exists(image_path):
            # Cargar la imagen y mostrarla en el Label
            image = Image.open(image_path)
            image.thumbnail((350, 600))  # Redimensionar la imagen para ajustarla al Label
            photo = ImageTk.PhotoImage(image)
            self.vale_image_label.config(image=photo)
            self.vale_image_label.image = photo  # Guardar una referencia a la imagen para evitar que sea eliminada por el recolector de basura
        else:
            # Mostrar un mensaje de error si la imagen no existe
            self.vale_image_label.config(text="Vale no encontrado")
            
    def cancelar_consulta(self):
        # Limpiar el campo de entrada del número de folio y restablecer la imagen a vacío
        folio = self.nombre_entry.get()  # Obtén el número de folio del campo de entrada
        ticket_image_path = f"./Archivos/{folio}.png"
        os.remove(ticket_image_path)
        self.nombre_entry.delete(0, tk.END)
        self.vale_image_label.config(image=None)
        messagebox.showinfo("Cancelación Exitosa", "La cancelación se realizó con éxito.")


    def on_closing(self):
        self.root.destroy()  # Cerrar la ventana de generar vale
        if self.menu_principal:
            self.menu_principal.master.deiconify()  # Mostrar la ventana del menú principal nuevamente
def main():
    root = tk.Tk()
    cancelar_vale = CancelarVale(root)
    root.mainloop()

if __name__ == "__main__":
    main()
