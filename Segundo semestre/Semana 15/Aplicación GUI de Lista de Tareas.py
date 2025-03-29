import tkinter as tk
from tkinter import messagebox

def agregar_tarea(event=None):
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "No puedes agregar una tarea vacía.")

def completar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(indice)
        lista_tareas.delete(indice)
        lista_tareas.insert(indice, f"[✔] {tarea}")
    except IndexError:
        messagebox.showwarning("Error", "Selecciona una tarea para marcar como completada.")

def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except IndexError:
        messagebox.showwarning("Error", "Selecciona una tarea para eliminar.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Administrador de Tareas")
ventana.geometry("620x480")
ventana.config(bg="#aa5ab8")

# Estilos
titulo = tk.Label(ventana, text="Mis Tareas", font=("Verdana", 18, "bold"), bg="#aa5ab8")
titulo.pack(pady=10)

entrada_tarea = tk.Entry(ventana, width=45, font=("Verdana", 12))
entrada_tarea.pack(pady=5)
entrada_tarea.bind("<Return>", agregar_tarea)

marco_botones = tk.Frame(ventana, bg="#aa5ab8")
marco_botones.pack(pady=5)

btn_agregar = tk.Button(marco_botones, text="Agregar", bg="#2196F3", fg="white", font=("Verdana", 11, "bold"), command=agregar_tarea)
btn_agregar.grid(row=0, column=0, padx=5)

btn_completar = tk.Button(marco_botones, text="Completada", bg="#4CAF50", fg="white", font=("Verdana", 11, "bold"), command=completar_tarea)
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(marco_botones, text="Eliminar", bg="#F44336", fg="white", font=("Verdana", 11, "bold"), command=eliminar_tarea)
btn_eliminar.grid(row=0, column=2, padx=5)

lista_tareas = tk.Listbox(ventana, width=55, height=15, font=("Verdana", 12), selectbackground="#B0BEC5")
lista_tareas.pack(pady=10)

ventana.mainloop()

