
from tkinter import *
from crud import *
from treeview import *
class Prueba:
    def __init__(self) -> None:
        venta=Tk()
        self.aver=venta
        venta.title="Prueba Objeto"
        venta.geometry('650x170')
        venta.resizable(False,False)
        venta.configure(background='#53FFFC')
        #
        self.registroslabel=Label(venta, text='REGISTRA AQUI UN NUEVO MIEMBRO!!')
        self.registroslabel.place(x=50, y=10)
        #Contenedor de botones y campos
        self.contenedor=Frame(venta,bd=5, bg='#53FFFC')
        self.contenedor.place(x=20,y=30)

        #Nombre y entrada
        self.nombrelabel=self.nombres_entradas("NOMBRE:",0,0)
        self.nombre=Entry(self.contenedor, font=40)
        self.nombre.grid(column=1, row=0,padx=5, pady=5)
        #Apellido y entrada
        
        self.apellidolabel=self.nombres_entradas("Apellido:",2,0)
        self.apellido=Entry(self.contenedor, font=40)
        self.apellido.grid(column=3, row=0,padx=5, pady=5)
    
        #
        self.telefonolabel=self.nombres_entradas("Telefono/Cel.:",2,1)
        self.telefono=Entry(self.contenedor, font=40)
        self.telefono.grid(column=3, row=1,padx=5, pady=5)

        #manzana
        self.manzanalabel=self.nombres_entradas("Manzana",0,2)
        self.manzana=Entry(self.contenedor, font=40)
        self.manzana.grid(column=1, row=2,padx=5, pady=5)
        #Los 
        
        self.numero_casalabel=self.nombres_entradas("No. Casa",0,1)
        self.numero_casa=Entry(self.contenedor, font=40)    
        self.numero_casa.grid(column=1, row=1,padx=5, pady=5)
        
        self.cerrar=Button(venta,text="CERRAR",bd=5,command=venta.destroy,state=DISABLED)
        self.cerrar.place(x=365,y=138)
   
    def nombres_entradas(self,nombre,columna, fila):
        return Label(self.contenedor,text=nombre, font=20, bg='#53FFFC').grid(column=columna, row=fila, padx=5,pady=5)
        
        """        
        """
    def getInfo(self):
        
        #Crud.guardar(numero_casa1,nombre1,apellido1,mz1,telefono1)
       
        lista=[self.numero_casa.get(),self.nombre.get(),self.apellido.get(),self.manzana.get(),self.telefono.get()]
        crud=Crud()
        crud.guardar(lista)

        
        print("guardado")
        self.cerrar.config(state=NORMAL)
        



"""def registrar():
    venta=Tk()
    objeto=Prueba()
    algo=lambda :objeto.getInfo()
    boton=Button(objeto.aver,text="Guardar",command=algo)
    boton.pack(side=BOTTOM)
    venta.mainloop()

if __name__=='__main__':
    registrar()"""
    