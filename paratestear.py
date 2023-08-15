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

import time

def actualizar_reloj():   
    ahora = time.strftime("%d-%m-%Y %H:%M:%S")
    etiqueta.config(text=ahora)
    ventana.after(1000, actualizar_reloj)  # Actualizar cada segundo

ventana = tk.Tk()
ventana.title("Reloj Digital")

etiqueta = tk.Label(ventana, font=("Helvetica", 48), fg="blue")
etiqueta.pack(padx=20, pady=20)

actualizar_reloj()  # Iniciar la actualización del reloj

ventana.mainloop()

""""
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
"""