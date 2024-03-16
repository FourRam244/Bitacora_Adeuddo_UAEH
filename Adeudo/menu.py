import tkinter as tk
from PIL import Image, ImageTk
from image_loader import ImageLoader
import generar
import consultar
import cancelar

class MenuPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Menú Principal")

        self.image_loader = ImageLoader()
        
        

        # Crear los widgets para los logotipos
        self.logo1_label = tk.Label(master, image=self.image_loader.get_logo1())
        self.logo1_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        self.logo2_label = tk.Label(master, image=self.image_loader.get_logo2())
        self.logo2_label.grid(row=0, column=1, sticky=tk.E, padx=10, pady=10)

        # Título del menú
        titulo_label = tk.Label(master, text="Préstamo de Equipo", font=("Helvetica", 20))
        titulo_label.grid(row=1, columnspan=2, pady=20)
        # Botones del menú
        button_frame = tk.Frame(master)
        button_frame.grid(row=2, columnspan=2)

        generar_button = tk.Button(button_frame, text="Generar Vale", command=self.abrir_generar, height=2, width=20, font=("Helvetica", 12))
        generar_button.grid(row=0, column=0, padx=10, pady=10)

        consultar_button = tk.Button(button_frame, text="Consultar Vale", command=self.abrir_consultar, height=2, width=20, font=("Helvetica", 12))
        consultar_button.grid(row=1, column=0, padx=10, pady=10)

        cancelar_button = tk.Button(button_frame, text="Cancelar Vale", command=self.abrir_cancelar, height=2, width=20, font=("Helvetica", 12))
        cancelar_button.grid(row=2, column=0, padx=10, pady=10)
        
    
    def abrir_generar(self):
        self.master.withdraw()  # Ocultar la ventana del menú principal
        generar_vale = generar.GenerarVale(self.master)  # Pasar la instancia de la ventana principal al generar vale
        generar_vale.menu_principal = self  # Pasar la instancia del menú principal a la ventana de generar vale
        generar_vale.root.protocol("WM_DELETE_WINDOW", generar_vale.on_closing)  # Configurar el evento de cierre en generar vale



    def abrir_consultar(self):
        self.master.withdraw()  # Ocultar la ventana del menú principal
        consultar_vale = consultar.ConsultarVale(self.master)  # Pasar la instancia de la ventana principal al generar vale
        consultar_vale.menu_principal = self  # Pasar la instancia del menú principal a la ventana de generar vale
        consultar_vale.root.protocol("WM_DELETE_WINDOW", consultar_vale.on_closing)  # Configurar el evento de cierre en generar vale

        

    def abrir_cancelar(self):
        self.master.withdraw()  # Ocultar la ventana del menú principal
        cancelar_vale = cancelar.CancelarVale(self.master)  # Pasar la instancia de la ventana principal al generar vale
        cancelar_vale.menu_principal = self  # Pasar la instancia del menú principal a la ventana de generar vale
        cancelar_vale.root.protocol("WM_DELETE_WINDOW", cancelar_vale.on_closing)  # Configurar el evento de cierre en generar vale


def main():
    root = tk.Tk()
    menu_principal = MenuPrincipal(root)
    root.mainloop()

if __name__ == "__main__":
    main()
