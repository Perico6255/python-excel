import tkinter as tk
from tkinter import messagebox
from userManager import userManager


class MiApp:
    def __init__(self, root):
        self.users = userManager()
        self.root = root
        self.root.title("Registro de usuario")

        self.label = tk.Label(root, text="Name:")
        self.label.pack(pady=10)

        # Entrada de texto
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack(pady=10)

        # Botón Pick In
        self.btn_pickin = tk.Button(root, text="Pick In", command=self.pick_in)
        self.btn_pickin.pack(side=tk.LEFT, padx=10)

        # Botón Pick Out
        self.btn_pickout = tk.Button(root, text="Pick Out", command=self.pick_out)
        self.btn_pickout.pack(side=tk.LEFT, padx=10)

        # Botón Export
        self.btn_export = tk.Button(root, text="Export", command=self.export)
        self.btn_export.pack(side=tk.LEFT, padx=10)

    def pick_in(self):
        nombre = self.entry_nombre.get()
        if self.users.check(nombre):
            messagebox.showinfo("Error", "nombre ya en uso")
        else:
            messagebox.showinfo("pick in", "correcto")
            self.users.pickin(nombre)


    def pick_out(self):
        nombre = self.entry_nombre.get()
        if self.users.check(nombre):
            messagebox.showinfo("pick out", "correcto")
            self.users.pickout(nombre)
        else:
            messagebox.showinfo("Error", "nombre no encontrado")

    def export(self):
        self.users.save()

if __name__ == "__main__":
    root = tk.Tk()
    app = MiApp(root)
    root.mainloop()
