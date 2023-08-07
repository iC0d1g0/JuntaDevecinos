import mysql.connector
from tkinter import *
from tkinter import messagebox
class Conexion: 

   #Se necesita corregir este objeto, que tenga la capacidad
   #de poder crear su propia base de datos, recibir los parametros a utilizar. 
   # tambien que se le indique el puerto al que se va a conectar. 
   #Esto permitira que la aplicacion se pueda ajustar a la necesidad del cliente sin 
   # que tenga acceso al codig. 
    try:
        cnn=mysql.connector.connect(host='127.0.0.1',
                                        port=3306,
                                        user='root',
                                        passwd='adderlis',
                                        database='adderlis')
    except Exception as ex:
        messagebox.showerror('Conexion Error',ex)
    
    
    def __init__(self) :
        
        
        try:
            self.info=self.cnn.get_server_info()
            print(self.info)
            self.fe=self.cnn.cursor()
          
        except Exception as ex:
            messagebox.showerror("Coneccion a base de datos", ex)
        finally:
            if self.cnn.is_connected():
                self.cnn.close()
                print("Conexion finalizada")
