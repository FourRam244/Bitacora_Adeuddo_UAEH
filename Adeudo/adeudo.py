import tkinter as tk
from tkinter import messagebox

class Vale:
    def __init__(self, equipo, cantidad, fecha, estado):
        self.equipo = equipo
        self.cantidad = cantidad
        self.fecha = fecha
        self.estado = estado

def generar_vale():
    equipo = equipo_entry.get()
    cantidad = int(cantidad_entry.get())
    fecha = fecha_entry.get()
    nuevo_vale = Vale(equipo, cantidad, fecha, "Prestado")
    vales.append(nuevo_vale)
    messagebox.showinfo("Generar Vale", "Vale generado correctamente.")

def consultar_vale():
    vale_info = ""
    for idx, vale in enumerate(vales):
        vale_info += f"Vale {idx+1}:\n"
        vale_info += f"Equipo: {vale.equipo}\n"
        vale_info += f"Cantidad: {vale.cantidad}\n"
        vale_info += f"Fecha: {vale.fecha}\n"
        vale_info += f"Estado: {vale.estado}\n\n"
    messagebox.showinfo("Consultar Vale", vale_info)

def cancelar_vale():
    consultar_vale()
    idx = int(cancelar_entry.get()) - 1
    if 0 <= idx < len(vales):
        vales[idx].estado = "Cancelado"
        messagebox.showinfo("Cancelar Vale", "Vale cancelado correctamente.")
    else:
        messagebox.showerror("Cancelar Vale", "Número de vale inválido.")

# Crear ventana principal
root = tk.Tk()
root.title("Sistema de Préstamo de Equipos")

# Crear variables para entrada de texto
equipo_entry = tk.Entry(root)
cantidad_entry = tk.Entry(root)
fecha_entry = tk.Entry(root)
cancelar_entry = tk.Entry(root)

# Etiquetas
tk.Label(root, text="Equipo:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="Cantidad:").grid(row=1, column=0, padx=5, pady=5)
tk.Label(root, text="Fecha (DD/MM/AAAA):").grid(row=2, column=0, padx=5, pady=5)
tk.Label(root, text="Número de vale a cancelar:").grid(row=4, column=0, padx=5, pady=5)

# Entradas de texto
equipo_entry.grid(row=0, column=1, padx=5, pady=5)
cantidad_entry.grid(row=1, column=1, padx=5, pady=5)
fecha_entry.grid(row=2, column=1, padx=5, pady=5)
cancelar_entry.grid(row=4, column=1, padx=5, pady=5)

# Botones
tk.Button(root, text="Generar Vale", command=generar_vale).grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")
tk.Button(root, text="Consultar Vale", command=consultar_vale).grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")
tk.Button(root, text="Cancelar Vale", command=cancelar_vale).grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Lista para almacenar vales
vales = []

root.mainloop()
