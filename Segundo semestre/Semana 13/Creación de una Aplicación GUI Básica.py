import tkinter as tk
from tkinter import messagebox

def agregar_dato(event=None):
    dato = entrada_texto.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entrada_texto.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

def limpiar_datos(event=None):
    lista_datos.delete(0, tk.END)

def limpiar_seleccion():
    seleccion = lista_datos.curselection()
    for index in reversed(seleccion):
        lista_datos.delete(index)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Administrador de Datos")
ventana.geometry("550x600")  # Ventana más grande
ventana.configure(bg="#2C3E50")  # Fondo oscuro

# Estilos
fuente_titulo = ("Comic Sans MS", 16, "bold")
fuente_texto = ("Verdana", 12)
color_boton = "#3498DB"
color_boton_texto = "white"

# Etiqueta y campo de texto
etiqueta = tk.Label(ventana, text="Ingrese un dato:", font=fuente_titulo, bg="#2C3E50", fg="white")
etiqueta.pack(pady=10)

entrada_texto = tk.Entry(ventana, font=fuente_texto, width=40, bg="#ECF0F1", fg="#2C3E50")
entrada_texto.pack(pady=5)
entrada_texto.bind("<Return>", agregar_dato)  # Agregar funcionalidad de Enter

# Botón para agregar datos
boton_agregar = tk.Button(ventana, text="Agregar", font=fuente_texto, bg=color_boton, fg=color_boton_texto, command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar datos
tk.Label(ventana, text="Datos ingresados:", font=fuente_titulo, bg="#2C3E50", fg="white").pack(pady=10)
lista_datos = tk.Listbox(ventana, selectmode=tk.MULTIPLE, font=fuente_texto, height=10, width=50, bg="#ECF0F1", fg="#2C3E50")
lista_datos.pack(pady=5, fill=tk.BOTH, expand=True)

# Botones para limpiar datos
boton_limpiar_todo = tk.Button(ventana, text="Limpiar Todo", font=fuente_texto, bg="#E74C3C", fg=color_boton_texto, command=limpiar_datos)
boton_limpiar_todo.pack(pady=5)
ventana.bind("<Control-l>", limpiar_datos)  # Agregar funcionalidad de Ctrl+L

boton_limpiar_seleccion = tk.Button(ventana, text="Eliminar Seleccionados", font=fuente_texto, bg="#F39C12", fg="black", command=limpiar_seleccion)
boton_limpiar_seleccion.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
