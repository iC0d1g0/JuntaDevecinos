from tkinter import *
import os
from tkinter import messagebox
class Campos:
    def __init__(self) -> None:
        self.ventana=Tk()
        self.ventana.geometry('300x300')
        self.ventana.title('Crea aqui tu tabla y los campos')
        self.nombres=Label(self.ventana,text='NOMBRE DE LOS CAMPOS')
        self.nombres.pack()


        self.caja2=Frame(self.ventana)

        self.uno=Label(self.caja2,text='1.')
        self.uno.grid(column=0, row=0,padx=5, pady=5)

        self.uno=Label(self.caja2,text='2.')
        self.uno.grid(column=0, row=1,padx=5, pady=5)
        
        self.uno=Label(self.caja2,text='3.')
        self.uno.grid(column=0, row=2,padx=5, pady=5)

        self.uno=Label(self.caja2,text='4.')
        self.uno.grid(column=0, row=3,padx=5, pady=5)

        self.uno=Label(self.caja2,text='5.')
        self.uno.grid(column=0, row=4,padx=5, pady=5)

        self.caja2.place(x=50,y=20)


        self.caja=Frame(self.ventana)     

        #0
        self.entrada1=Entry(self.caja)
        self.entrada1.grid(column=0,row=0,padx=5, pady=5)
        #1
        self.entrada1=Entry(self.caja)
        self.entrada1.grid(column=0,row=1,padx=5, pady=5)
        #2
        self.entrada1=Entry(self.caja)
        self.entrada1.grid(column=0,row=2,padx=5, pady=5)
        #3
        self.entrada1=Entry(self.caja)
        self.entrada1.grid(column=0,row=3,padx=5, pady=5)
        #4
        self.entrada1=Entry(self.caja)
        self.entrada1.grid(column=0,row=4,padx=5, pady=5)



        self.caja.pack(side=TOP)
        self.boton=Button(self.ventana,text='Guardar tabla',command=self.guardar)
        self.boton.pack()
        




        self.ventana.mainloop()
    def guardar(self):
        if os.path.exists('./interfaz.py'):
            messagebox.showinfo('Bienvenido!!', 'Accediste a Jv CRUD')
            self.ventana.destroy()
            os.system('python interfaz.py')

if __name__=='__main__': 
    Campos()