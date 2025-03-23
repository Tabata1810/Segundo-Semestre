import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import locale

# Configurar el idioma local a español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

def agregar_evento():
    fecha = date_entry.get()
    hora = hora_entry.get()
    descripcion = descripcion_entry.get()
    if fecha and hora and descripcion:
        tree.insert('', 'end', values=(fecha, hora, descripcion))
        limpiar_campos()
    else:
        messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")

def eliminar_evento():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Selección vacía", "Por favor, seleccione un evento para eliminar.")
        return
    if messagebox.askyesno("Confirmación", "¿Está seguro de eliminar el evento seleccionado?"):
        tree.delete(selected_item)

def limpiar_campos():
    hora_entry.delete(0, tk.END)
    descripcion_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Agenda Personal")
root.configure(bg="#885b8a")

frame_input = ttk.Frame(root, padding="10")
frame_input.pack(fill=tk.X)

# Estilos
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12, "bold"), foreground="black")
style.configure("TButton", font=("Arial", 10, "bold"), background="#885b8a", foreground="black")
style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#f7bfd8", foreground="black")
style.configure("Treeview", background="#f7bfd8", foreground="black", rowheight=25, fieldbackground="#885b8a")

# Widgets de entrada
ttk.Label(frame_input, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
date_entry = DateEntry(frame_input, width=12, background='#885b8a', foreground='black', borderwidth=2,
                       date_pattern='dd/mm/yyyy', locale='es_ES')
date_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_input, text="Hora:").grid(row=0, column=2, padx=5, pady=5)
hora_entry = ttk.Entry(frame_input, width=10, font=("Arial", 12), foreground="#5D4157")
hora_entry.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(frame_input, text="Descripción:").grid(row=0, column=4, padx=5, pady=5)
descripcion_entry = ttk.Entry(frame_input, width=30, font=("Arial", 12), foreground="#5D4157")
descripcion_entry.grid(row=0, column=5, padx=5, pady=5)

# Botones
frame_buttons = ttk.Frame(root, padding="10")
frame_buttons.pack(fill=tk.X)

ttk.Button(frame_buttons, text="Agregar Evento", command=agregar_evento, style="TButton").pack(side=tk.LEFT, padx=5)
ttk.Button(frame_buttons, text="Eliminar Evento", command=eliminar_evento, style="TButton").pack(side=tk.LEFT, padx=5)
ttk.Button(frame_buttons, text="Salir", command=root.quit, style="TButton").pack(side=tk.RIGHT, padx=5)

# Treeview para mostrar los eventos
frame_tree = ttk.Frame(root, padding="10")
frame_tree.pack(fill=tk.BOTH, expand=True)

columns = ("Fecha", "Hora", "Descripción")
tree = ttk.Treeview(frame_tree, columns=columns, show='headings', style="Treeview")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(fill=tk.BOTH, expand=True)

root.mainloop()


