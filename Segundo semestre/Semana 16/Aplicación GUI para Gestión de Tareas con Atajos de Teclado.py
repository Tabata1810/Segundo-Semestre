import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("\u2728 Lista de Tareas \u2728")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f4f8")  # Fondo suave azul grisáceo

        self.tasks = []

        # --- Widgets ---
        self.entry = tk.Entry(root, font=("Arial", 14), bg="#ffffff", fg="#333333")
        self.entry.pack(pady=10, padx=10, fill=tk.X)
        self.entry.focus()

        self.button_frame = tk.Frame(root, bg="#f0f4f8")
        self.button_frame.pack(pady=5)

        self.add_button = tk.Button(self.button_frame, text="Agregar", bg="#4caf50", fg="white", activebackground="#45a049", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(self.button_frame, text="Completada", bg="#2196f3", fg="white", activebackground="#1e88e5", command=self.complete_task)
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Eliminar", bg="#f44336", fg="white", activebackground="#e53935", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        self.listbox = tk.Listbox(root, font=("Arial", 14), selectmode=tk.SINGLE, bg="#e3f2fd", fg="#333333", selectbackground="#90caf9")
        self.listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # --- Binds ---
        self.entry.bind("<Return>", lambda event: self.add_task())
        self.listbox.bind("<Delete>", lambda event: self.delete_task())
        self.listbox.bind("<d>", lambda event: self.delete_task())
        self.listbox.bind("<c>", lambda event: self.complete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text:
            self.tasks.append({"text": task_text, "completed": False})
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "\u26a0\ufe0f La tarea no puede estar vac\u00eda.")

    def complete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_listbox()
        else:
            messagebox.showinfo("Info", "\u2139\ufe0f Selecciona una tarea para completar.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showinfo("Info", "\u2139\ufe0f Selecciona una tarea para eliminar.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            text = task["text"]
            if task["completed"]:
                text = f"\u2705 {text}"
            else:
                text = f"\u23f3 {text}"
            self.listbox.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

