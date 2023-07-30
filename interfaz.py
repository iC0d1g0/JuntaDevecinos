from tkinter import *
from tkinter import ttk
from registros import Prueba
from treeview import *
class Ventana(Frame) : 
    def __init__(self, master=None):
        super().__init__(master, width=850, height=460)
        self.master=master
        self.pack()
        self.tabla=VistaArbol(self,100,10,700)
        self.create_widgets()

    def registrar(self):
       
        self.objeto=Prueba()
        algo=lambda :self.objeto.getInfo()
        self.boton=Button(self.objeto.aver,text="Guardar",command=algo)
        self.boton.pack(side=BOTTOM)

    def aporte():
        pass
    def ver():
        pass
    def create_widgets(self):
        frame1= Frame(self, bg="#bfdaff")
        frame1.place(x=0, y=0, width=93, height=459)
        #Botones
        self.registro=Button(frame1, text="REGISTRO", bd=5, background="#1DE321", command=self.registrar)
        self.registro.place(x=10, y=10, width=80, height=30)

        self.actualizar=Button(frame1, text="EDITAR", bd=5, background="#2C91E3")
        self.actualizar.place(x=10, y=50, width=80, height=30)
        
        self.eliminar=Button(frame1, text="ELIMINAR", bd=5, background="#E35625")
        self.eliminar.place(x=10, y=95, width=80, height=30)

        self.aporte1=Button(frame1, text="APORTE", bd=5,background="#35E3CB")
        self.aporte1.place(x=10, y=140, width=80, height=30)

        self.ver1=Button(frame1, text="INFO.", bd=5)
        self.ver1.place(x=10, y=178, width=80, height=30)

        self.resumen=Button(frame1, text="RESUMEN", bd=5)
        self.resumen.place(x=10, y=225, width=80, height=30)

        self.exportar=Button(frame1, text="EXPORTAR", bd=5)
        self.exportar.place(x=10, y=270, width=80, height=30)

        self.refrescar=Button(frame1, text="Refresh", bd=5, command=self.refresh)
        self.refrescar.place(x=10, y=300, width=80, height=30)
        #Montor el TreeView
        
        
        #self.tabla.insert("", END, text="1", values=("Adderlis","Severino","24","N17","8293891045","100","2000.00"))
        
       
        #Insertando

    def refresh(self):
        #self.tabla.insertar("Adderlis","REYES","24","N17","8293891045","100","2000.00")
      pass  
      
       
        


def main():
    root=Tk()
    root.wm_title("JV. La Union Hace la Fuerza!")
    root.resizable(False, False)
    app=Ventana(root)
    app.mainloop()

if __name__ =='__main__': 
    main()
