import os
from connection import *
from openpyxl import Workbook

class Excel: 
        conexion=Conexion.cnn
        cursor=conexion.cursor()
        cursor.execute(f"SELECT * FROM cliente")
        datos = cursor.fetchall()
        archivo_xlsx = f"C:/Users/{os.getenv('USERNAME')}/Desktop/Reporte_JV"
        def __init__(self,tabla)-> None:
           
            self.tabla=tabla

            archivo_xlsx=self.archivo_xlsx
            
            pass


        def exportar_db_a_xlsx(self):
            # Conectar a la base de datos
            """
            Llamar el objecto conexion
            """

            # Recuperar los datos de la tabla
        

            # Obtener los nombres de las columnas
            nombres_columnas = [descripcion[0] for descripcion in self.cursor.description]

            # Crear un nuevo libro de trabajo (Workbook)
            libro_trabajo = Workbook()
            hoja = libro_trabajo.active

            # Escribir los nombres de las columnas en la primera fila
            for columna_idx, columna_nombre in enumerate(nombres_columnas, start=1):
                hoja.cell(row=1, column=columna_idx, value=columna_nombre)

            # Escribir los datos en las filas siguientes
            for fila_idx, fila_datos in enumerate(self.datos, start=2):
                for columna_idx, valor in enumerate(fila_datos, start=1):
                    hoja.cell(row=fila_idx, column=columna_idx, value=valor)

            # Guardar el libro de trabajo en un archivo .xlsx
            self.conexion.close()
            
            compara=os.path.exists(self.archivo_xlsx+'.xlsx')
            
            if compara:
                contador=1
                self.archivo_xlsx+='_'
                while  os.path.exists(self.archivo_xlsx+str(contador)+'.xlsx'): 
                    contador+=1
                libro_trabajo.save(self.archivo_xlsx+str(contador)+'.xlsx')
            else:
                libro_trabajo.save(self.archivo_xlsx+'.xlsx')
                print(compara)
                    
                        

            # Cerrar la conexión
            

     
