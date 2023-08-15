import mysql.connector
from tkinter import *
from tkinter import messagebox
from dotenv import load_dotenv
import os

class Conexion: 
    #cargo la variable de entonno desde el archivo .env
    load_dotenv()
    host=os.getenv('HOST')
    port=os.getenv('PORT')
    user=os.getenv('USER')
    passwd=os.getenv('PASSWD')
    database=os.getenv('DATABASE')
    tabla=os.getenv('TABLA')


   #Se necesita corregir este objeto, que tenga la capacidad
   #de poder crear su propia base de datos, recibir los parametros a utilizar. 
   # tambien que se le indique el puerto al que se va a conectar. 
   #Esto permitira que la aplicacion se pueda ajustar a la necesidad del cliente sin 
   # que tenga acceso al codig. 
    try:
        cnn=mysql.connector.connect(database=database,port=port,user=user,passwd=passwd,host=host)
    except Exception as ex:
        messagebox.showerror('Conexion Error',ex)
    
    
    def __init__(self) :
        
        try:
            self.info=self.cnn()
           
            self.fe=self.cnn.cursor()
        
        except Exception as ex:
            messagebox.showerror("Coneccion a base de datos", ex)

        finally:
            if self.cnn.is_connected():
                self.cnn.close()
                
