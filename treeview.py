from tkinter import ttk
from tkinter import *

## Conclusion, no mostrar
# que el ID almacene el valor del primer elemento, y la primera columna
# como es auto generada, que no se inserte.. 
###################################################################################################
#crea la vista de las tablas en la ventana tkinter
#Ya ha sido modificado y resumido!! reducido a mas de la mitad del codiog!
#recive una lista de nombres por parametros
###################################################################################################
class VistaArbol:
    def __init__(self,master, ladosx, altoy, ancho, alto,columnas):
        self.master=master
        self.nombre_columnas=columnas #Esto es una lista de columnas
        self.x=ladosx
        self.y=altoy
        self.width=ancho
        self.height=alto
        
        #col_positions=["col1","col2","col3","col4","col5","col6","col7"]
        col_positions=['{}{}'.format('col',i) for i in range(len(self.nombre_columnas)-1)]
        
        #nombres=['NOMBRE','APELLIDO','MZ','NO','TEL', 'APORTE','ACUMULADO']
        nombres=[i for i in self.nombre_columnas]
        #Este self.grid guarda el objeto de la clase ttk llamado Treview
        #RECIBE UN MASTER, Y UNA TUPLA INDICANDO LOS NOMBRES DE LAS COLUMNAS. 
        #OJO: no el label, si no las posiciones por ejemplo: Col1, col2, etc..

        self.grid=ttk.Treeview(self.master,columns=(col_positions))#me salto la primera posicion
        #La primera psoicion por defecto en el treeview es #0, 
        self.grid.place(x=self.x,y=self.y,width=self.width,height=self.height)

        
        #Logre reducir el codigo, utilizando solo 1 bucles for
        self.grid.column('#0',width=0)
        self.grid.heading('#0',text=nombres[0],anchor=CENTER)
        nom=1
        for i in col_positions:
            
            self.grid.column(i,width=0,anchor=CENTER)
            self.grid.heading(i,text=nombres[nom],anchor=CENTER)
            nom+=1  
       
    def insertar(self,b):
        #como insertar recive una col_positions, o una lista
        self.grid.insert("", END, text=b[0], values=(b[1:]))






"""
        elf.grid.column("#0",width=50)
        self.grid.column("col1",width=90,anchor=CENTER)
        self.grid.column("col2",width=90,anchor=CENTER)
        self.grid.column("col3",width=60,anchor=CENTER)
        self.grid.column("col4",width=60,anchor=CENTER)
        self.grid.column("col5",width=90,anchor=CENTER)
        self.grid.column("col6",width=60,anchor=CENTER)
        self.grid.column("col7",width=60,anchor=CENTER)"""

        #Heading (Encabezado)       
        #s
        #
        
"""
        self.grid.heading("#0",text="ID")
        self.grid.heading("col1",text="APELLIDO",anchor=CENTER)
        self.grid.heading("col2",text="APELLIDO",anchor=CENTER)
        self.grid.heading("col3",text="MZ.",anchor=CENTER)
        self.grid.heading("col4",text="No.",anchor=CENTER)
        self.grid.heading("col5",text="TEL.",anchor=CENTER)
        self.grid.heading("col6",text="Aporte FIjo",anchor=CENTER)
        self.grid.heading("col7",text="ACUMULADO",anchor=CENTER)"""
        
        
    

