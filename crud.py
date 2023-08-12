from connection import *
from tkinter import messagebox

class Crud: 

    def __init__(self):
        try:
            self.conexion=Conexion.cnn
            self.tabla=Conexion.tabla
        except Exception as ex:
            messagebox.showerror('Conexion Error', ex)

    # Obtener los nombres de las columnas
    def vistaColumnas(self):
        self.cursor=self.conexion.cursor()
        self.cursor.execute("SELECT * FROM {}".format(self.tabla))
        self.datos=self.cursor.fetchall()
        
        nombres_columnas = [descripcion[0] for descripcion in self.cursor.description]
        return nombres_columnas #Devuelve la lista de nombres de las columnas de la base de datos
    
    """ def guardar(self, id, nombre, apellido, direccion, telefono):
        if id == "" or nombre == "" or apellido == "" or direccion == "" or telefono == "":
            return messagebox.showerror("Error", "No se permiten campos vacios")
        else:
            self.cursor=self.conexion.cursor()
            conviertetupla=self.vistaColumnas() #Utilizamos la lista de columnas en la vase de datos
            self.cursor.execute(f"INSERT INTO cliente ({','.join(conviertetupla)}) VALUES ('{id}', '{nombre}', '{apellido}', '{direccion}', '{telefono}')")
            self.conexion.commit() # commit para guardar los datos
            self.cursor.close()
        return messagebox.showinfo("Informacion", "Datos guardados correctamente")"""
    def guardar(self, values):
        if any(value == "" for value in values):
            return messagebox.showerror("Error", "No se permiten campos vacíos")
        else:
            self.cursor = self.conexion.cursor()
            column_names = self.vistaColumnas()
            placeholders = ', '.join(['%s'] * len(column_names[1:]))#crea una cadena solo usando %s, %s, %s...
            #Esto lo uso para posteriormente reemplazar los %s con los valores reales.
            query = f"INSERT INTO {self.tabla} ({','.join(column_names[1:])}) VALUES ({placeholders})"
            self.cursor.execute(query, values)
            self.conexion.commit()
            self.cursor.close()
        return messagebox.showinfo("Información", "Datos guardados correctamente")
    #Necesito reparar la funcion Elimiar, para que reciva por parametro una lista de 
    #elementos, como lo hace la funcion modificar. 
    def elminar(self, id):
        nombre_columna=self.vistaColumnas()
        """Elimina un registro de la base de datos si existe. En caso de que no exista, muestra un mensaje de error."""
        if id == "":
            messagebox.showerror("Error", "No se permiten campos vacios")
        else:
            #si existe el registro, se elimina
            if self.existe(id):
                """Preguntar si desea eliminar el registro"""
                #if messagebox.askyesno("Eliminar", "¿Desea eliminar el registro?"):
                self.cursor=self.conexion.cursor()
                try:
                    self.cursor.execute(f"DELETE FROM {self.tabla} WHERE {nombre_columna[0]} = {id}")
                    self.conexion.commit()
                    return True
                except Exception as ex:
                    messagebox.showerror('Error','{}'.format(ex))
                    #return False
                finally:

                    self.cursor.close()
                    #messagebox.showinfo("Informacion", "Datos eliminados correctamente")
            else:
                #messagebox.showerror("Error", "No existe el registro")
                return False

    def existe(self, id):
        """Retorna True si existe el registro, False en caso contrario."""
        nombre_columna=self.vistaColumnas()
        self.cursor=self.conexion.cursor()
        self.cursor.execute(f"SELECT * FROM {self.tabla} WHERE {nombre_columna[0]} = {id}")
        datos = self.cursor.fetchall()
        self.cursor.close()
        return len(datos) != 0
    
    def modificar(self, values):
        if len(values) < 2 or any(value == "" for value in values[1:]):
            return messagebox.showerror("Error", "Se requiere al menos un valor no vacío y el identificador")
        else:
            self.cursor = self.conexion.cursor()
            column_names = self.vistaColumnas()
            id_column = column_names[0]  # Tomamos el nombre de la primera columna como el identificador
            set_clause = ', '.join(f"{col} = %s" for col in column_names[1:])
            query = f"UPDATE {self.tabla} SET {set_clause} WHERE {id_column} = %s"
            self.cursor.execute(query, values[1:] + [values[0]])  # Valores sin el identificador, luego agregamos el identificador
            self.conexion.commit()
            self.cursor.close()
        return messagebox.showinfo("Información", "Datos modificados correctamente")

    """def modificar(self, id, nombre, apellido, direccion, telefono):
        if id == "" or nombre == "" or apellido == "" or direccion == "" or telefono == "":
            messagebox.showerror("Error", "No se permiten campos vacios")
        else:
            self.cursor=self.conexion.cursor()
            self.cursor.execute(f"UPDATE cliente SET CI = '{id}', nombre = '{nombre}', appellido = '{apellido}', direccion = '{direccion}', telefono = '{telefono}' WHERE CI = {id}")
            self.conexion.commit()
            self.cursor.close()
            messagebox.showinfo("Informacion", "Datos modificados correctamente")"""
        
    def leer(self):
        self.cursor=self.conexion.cursor()
        self.cursor.execute("SELECT * FROM {}".format(self.tabla))
        datos = self.cursor.fetchall()
        print(datos)
        self.cursor.close()
        # messagebox.showinfo("Informacion", "Datos cargados correctamente")
        return datos
    
    
    

"""if __name__=='__main__':
    os.system("cls")
    crud=Crud()
    crud.elminar('333232')"""
