
from tkinter import *
from crud import *
from treeview import *
class Prueba:
    def __init__(self,columnas) -> None:
        venta=Tk()
        self.crud=Crud()
        self.columnas=self.crud.vistaColumnas(columnas)
        self.aver=venta
        venta.title="Prueba Objeto"
        venta.geometry('400x550')
        venta.resizable(False,False)
        venta.configure(background='#53FFFC')
        #
        self.registroslabel=Label(venta, text='REGISTRA AQUI UN NUEVO MIEMBRO!!')
        self.registroslabel.place(x=50, y=10)
        #Contenedor de botones y campos
        self.contenedor=Frame(venta,bd=5, bg='#53FFFC')
        self.contenedor.place(x=20,y=30)
        #Nombre y entrada
        #Resuelto en pocas lineas de codigo
        j=0
        obEntrada=[]
        labels=[]
        for i in self.columnas:
            self.nombrelabel=self.nombres_entradas('{}:'.format(i),0,j)
            self.nombre=Entry(self.contenedor, font=40)
            self.nombre.grid(column=1, row=j,padx=5, pady=5)

            labels.append(self.nombrelabel)
            obEntrada.append(self.nombre)
            
            j+=1
        self.label=labels
        self.obentrada=[i for i in obEntrada]
        self.obentrada[0].config(state='disable')
           

    def nombres_entradas(self,nombre,columna, fila):
        return Label(self.contenedor,text=nombre, font=20, bg='#53FFFC').grid(column=columna, row=fila, padx=5,pady=5)
     
    def editando(self,valores):
         #Crud.guardar(numero_casa1,nombre1,apellido1,mz1,telefono1)
        self.obentrada[0].config(state='normal')
        lista2=self.obentrada
        lista=[]
        cont=0
        for i in lista2:
            lista.append(i.insert(0,valores[cont]))
            
            cont+=1
        lista2[0].config(state='disable')
       
        return True
        #self.cerrar.config(state=NORMAL)
    def getEditar(self):
        lista2=self.obentrada
        lista=[]
        for i in lista2:
            lista.append(i.get())
            
        
        crud=Crud()
        crud.modificar(lista)
        
    def getInfo(self):
        
        #Crud.guardar(numero_casa1,nombre1,apellido1,mz1,telefono1)
        
        lista2=self.obentrada

        lista=[]
        for i in lista2:
            if i:
                lista.append(i.get())
                
        crud=Crud()
        crud.guardar(lista[1:],self.crud.tabla)

      


    def aportar(self, lista_valores):
        self.crud.guardar(lista_valores,'jv_aportes')

        pass

def registrar():
    venta=Tk()
    objeto=Prueba()
    algo=lambda :objeto.editando()
    boton=Button(objeto.aver,text="Guardar",command=algo)
    boton.pack(side=BOTTOM)
    venta.mainloop()


