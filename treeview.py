from tkinter import ttk
from tkinter import *
class VistaArbol:
    def __init__(self,master, ladosx, altoy, ancho):
        self.master =master
        self.x=ladosx
        self.y=altoy
        self.width=ancho
        self.entrada=Entry(self.master)
        
        self.grid=ttk.Treeview(self.master,columns=("col1","col2","col3","col4","col5","col6","col7"))
        self.grid.column("#0",width=50)
        self.grid.column("col1",width=60,anchor=CENTER)
        self.grid.column("col2",width=90,anchor=CENTER)
        self.grid.column("col3",width=60,anchor=CENTER)
        self.grid.column("col4",width=60,anchor=CENTER)
        self.grid.column("col5",width=90,anchor=CENTER)
        self.grid.column("col6",width=60,anchor=CENTER)
        self.grid.column("col7",width=60,anchor=CENTER)

        #Heading (Encabezado)
        self.grid.heading("#0",text="ID")
        self.grid.heading("col1",text="NOMBRE",anchor=CENTER)
        self.grid.heading("col2",text="APELLIDO",anchor=CENTER)
        self.grid.heading("col3",text="MZ.",anchor=CENTER)
        self.grid.heading("col4",text="No.",anchor=CENTER)
        self.grid.heading("col5",text="TEL.",anchor=CENTER)
        self.grid.heading("col6",text="Aporte FIjo",anchor=CENTER)
        self.grid.heading("col7",text="ACUMULADO",anchor=CENTER)
        self.grid.place(x=self.x,y=self.y,width=self.width)

    def insertar(self,a,b,c,d,e,f):
        self.grid.insert("", END, text="1", values=(a,b,c,d,e,f))

