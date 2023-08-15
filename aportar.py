from tkinter import *
from tkinter import messagebox
import time
from crud import *
class AportarView: 
    def __init__(self, clave):
        self.ventana=Tk()
        self.ventana.geometry('500x140')
        self.ventana.title('Aportes')
        self.ventana.resizable(False,False)
        caja_box=Frame(self.ventana)
        caja_box.pack(padx=10,pady=10)
        self.Id_usuario=Label(caja_box,text='Clave de Usuario: '); self.idEntry=Entry(caja_box)
        self.Id_usuario.grid(column=0,row=0); self.idEntry.grid(column=1,row=0)
        self.fecha=Label(caja_box,text='Fecha: '); self.fechaEntry=Entry(caja_box)
        self.fecha.grid(column=0, row=1); self.fechaEntry.grid(column=1, row=1)
        self.hora=Label(caja_box,text='Hora: '); self.horaEntry=Entry(caja_box)
        self.hora.grid(column=0,row=2); self.horaEntry.grid(column=1, row=2)
        self.aporte=Label(caja_box,text='Ingrese el Aporte aqui:'); self.aporteEntry=Entry(caja_box)
        self.aporte.grid(column=0,row=3); self.aporteEntry.grid(column=1, row=3)
        self.guardardb=Button(self.ventana,text='Aportar',command=self.setGuardar)
        self.guardardb.pack()
        self.getfecha_hora(clave)
        #Entradas:
        
        self.ventana.mainloop()
    
    def getfecha_hora(self,id):
        
        ahora = time.strftime("%H:%M:%S")
        fecha=time.strftime('%d-%m-%Y ')
        self.idEntry.insert(0,id)
        self.horaEntry.insert(0,ahora)
        self.fechaEntry.insert(0,fecha)
        self.fechaEntry.config(state='disabled')
        self.horaEntry.config(state='disabled')
        self.idEntry.config(state='disabled')
          

   
    def setGuardar(self): 
        crud=Crud()
        lista_entradas=[self.idEntry.get(),
                        self.aporteEntry.get(),
                        self.fechaEntry.get(),
                        self.horaEntry.get(),
               
               ]
        if lista_entradas[1].isdigit() and lista_entradas[1] != '0' :
            crud.guardar(lista_entradas,'jv_aportes')
        else:
            messagebox.showwarning('Alerta','Entrada incorrecta, prueba solo numeros')



