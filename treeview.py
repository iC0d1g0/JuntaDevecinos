from tkinter import ttk
from tkinter import *
class VistaArbol:
    def __init__(self,master, ladosx, altoy, ancho, alto,columnas):
        self.master=master
        self.nombre_columnas=columnas
        self.x=ladosx
        self.y=altoy
        self.width=ancho
        self.height=alto
        self.entrada=Entry(self.master)
        #tupla=["col1","col2","col3","col4","col5","col6","col7"]
        tupla=['col{}'.format(i+1) for i in range(len(self.nombre_columnas))]
        #nombres=['NOMBRE','APELLIDO','MZ','NO','TEL', 'APORTE','ACUMULADO']
        nombres=[i for i in self.nombre_columnas]
        self.grid=ttk.Treeview(self.master,columns=(tupla))
        self.grid.column("#0",width=50)
        self.grid.heading("#0",text="ID")
        #Logre reducir el codigo, utilizando solo 1 bucles for
        nom=0
        for i in tupla:
            self.grid.column(i,width=60,anchor=CENTER)
            self.grid.heading(i,text=nombres[nom],anchor=CENTER)
            nom+=1  
       
        self.grid.place(x=self.x,y=self.y,width=self.width,height=self.height)
    def insertar(self,b):
        #como insertar recive una tupla, o una lista
        self.grid.insert("", END, text=b[0], values=(b))


        
        """self.grid.column("col2",width=90,anchor=CENTER)
        self.grid.column("col3",width=60,anchor=CENTER)
        self.grid.column("col4",width=60,anchor=CENTER)
        self.grid.column("col5",width=90,anchor=CENTER)
        self.grid.column("col6",width=60,anchor=CENTER)
        self.grid.column("col7",width=60,anchor=CENTER)"""

        #Heading (Encabezado)       
        
        """self.grid.heading("col2",text="APELLIDO",anchor=CENTER)
        self.grid.heading("col3",text="MZ.",anchor=CENTER)
        self.grid.heading("col4",text="No.",anchor=CENTER)
        self.grid.heading("col5",text="TEL.",anchor=CENTER)
        self.grid.heading("col6",text="Aporte FIjo",anchor=CENTER)
        self.grid.heading("col7",text="ACUMULADO",anchor=CENTER)"""
        
        
    

