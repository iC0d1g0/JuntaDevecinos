from connection import *
from tkinter import messagebox

class Crud: 

    def __init__(self):
        self.conexion=Conexion.cnn

    def guardar(self, id, nombre, apellido, direccion, telefono):
        if id == "" or nombre == "" or apellido == "" or direccion == "" or telefono == "":
            return messagebox.showerror("Error", "No se permiten campos vacios")
        else:
            self.cursor=self.conexion.cursor()
            self.cursor.execute(f"INSERT INTO cliente (CI, nombre, appellido, direccion, telefono) VALUES ('{id}', '{nombre}', '{apellido}', '{direccion}', '{telefono}')")
            self.conexion.commit() # commit para guardar los datos
            self.cursor.close()
        return messagebox.showinfo("Informacion", "Datos guardados correctamente")
        
    def elminar(self, id):
        """Elimina un registro de la base de datos si existe. En caso de que no exista, muestra un mensaje de error."""
        if id == "":
            messagebox.showerror("Error", "No se permiten campos vacios")
        else:
            #si existe el registro, se elimina
            if self.existe(id):
                """Preguntar si desea eliminar el registro"""
                if messagebox.askyesno("Eliminar", "¿Desea eliminar el registro?"):
                    self.cursor=self.conexion.cursor()
                    self.cursor.execute(f"DELETE FROM cliente WHERE CI = {id}")
                    self.conexion.commit()
                    self.cursor.close()
                    messagebox.showinfo("Informacion", "Datos eliminados correctamente")
            else:
                messagebox.showerror("Error", "No existe el registro")

    def existe(self, id):
        """Retorna True si existe el registro, False en caso contrario."""
        self.cursor=self.conexion.cursor()
        self.cursor.execute(f"SELECT * FROM cliente WHERE CI = {id}")
        datos = self.cursor.fetchall()
        self.cursor.close()
        return len(datos) != 0

    def modificar(self, id, nombre, apellido, direccion, telefono):
        if id == "" or nombre == "" or apellido == "" or direccion == "" or telefono == "":
            messagebox.showerror("Error", "No se permiten campos vacios")
        else:
            self.cursor=self.conexion.cursor()
            self.cursor.execute(f"UPDATE cliente SET CI = '{id}', nombre = '{nombre}', appellido = '{apellido}', direccion = '{direccion}', telefono = '{telefono}' WHERE CI = {id}")
            self.conexion.commit()
            self.cursor.close()
            messagebox.showinfo("Informacion", "Datos modificados correctamente")
        
    def leer(self):
        self.cursor=self.conexion.cursor()
        self.cursor.execute("SELECT * FROM cliente")
        datos = self.cursor.fetchall()
        self.cursor.close()
        # messagebox.showinfo("Informacion", "Datos cargados correctamente")
        return datos
    
    
    

"""if __name__=='__main__':
    os.system("cls")
    crud=Crud()
    crud.elminar('333232')"""
