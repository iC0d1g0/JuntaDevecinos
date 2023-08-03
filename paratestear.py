from tkinter import *




venta=Tk()
venta.geometry('400x400')
entrada = Entry(venta, font=50)
entrada.place(x=30,y=20)
funcion=lambda :entrada.get()


def mifuncion():
    print(funcion())
boton=Button(venta,text="Info",bd=5,command=mifuncion)
boton.place(x=60, y=40)
venta.mainloop()
