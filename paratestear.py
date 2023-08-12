"""import subprocess


def is_mysql_installed():
    try:
        subprocess.run(["mysql", "--version"],shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

hola=is_mysql_installed()
if hola:
    print("MySQL está instalado en esta PC.")
else:
    print("MySQL no está instalado en esta PC.")
"""


import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tree = ttk.Treeview(root)
tree["columns"] = ("Name", "Age", "Location")

# Ocultar la columna #0
tree.column("#0", width=0)

# Configurar las columnas restantes
tree.heading("#1", text="Name")
tree.heading("#2", text="Age")
tree.heading("#3", text="Location")

# Insertar datos de ejemplo
tree.insert("", "end", text="", values=("John Doe", 25, "New York"))
tree.insert("", "end", text="", values=("Jane Smith", 30, "Los Angeles"))

tree.pack()

root.mainloop()
