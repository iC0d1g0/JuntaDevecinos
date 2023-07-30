
from tkinter import *
from guardadb import *
from treeview import *
class Prueba:
    def __init__(self) -> None:
        venta=Tk()
        self.aver=venta
        venta.title="Prueba Objeto"
        #
        self.nombrelabel=Label(venta,text="NOMBRE")
        self.nombrelabel.pack()
        self.nombre=Entry(venta)
        self.nombre.pack(side=TOP)
        #
        self.apellidolabel=Label(venta,text="Apellido")
        self.apellidolabel.pack()
        self.apellido=Entry(venta)
        self.apellido.pack(side=TOP)
        #
        self.mzlabel=Label(venta,text="Manzana")
        self.mzlabel.pack()
        self.mz=Entry(venta)
        self.mz.pack(side=TOP)
        #
        self.numero_casalabel=Label(venta,text="Numero de casa")
        self.numero_casalabel.pack()
        self.numero_casa=Entry(venta)
        self.numero_casa.pack(side=TOP)
        #
        self.telefonolabel=Label(venta,text="Numero de telefono")
        self.telefonolabel.pack()
        self.telefono=Entry(venta)
        self.telefono.pack(side=TOP)
        
        self.cerrar=Button(venta,text="CERRAR",command=venta.destroy,state=DISABLED)
        self.cerrar.pack(side=BOTTOM)
        
    def getInfo(self):
        nombre1=self.nombre.get()
        apellido1=self.apellido.get()
        mz1=self.mz.get()
        numero_casa1=self.numero_casa.get()
        telefono1=self.telefono.get()

        guardado=GuardaDB(nombre1,apellido1,mz1,numero_casa1,telefono1)


        guardado.guarda_db()
        print("guardado")
        self.cerrar.config(state=NORMAL)
        


    
    
