
from tkinter import *
from crud import *
from treeview import *
class Prueba:
    def __init__(self) -> None:
        venta=Tk()
        self.crud=Crud()
        self.columnas=self.crud.vistaColumnas()
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
        for i in self.columnas:
            self.nombrelabel=self.nombres_entradas('{}:'.format(i),0,j)
            self.nombre=Entry(self.contenedor, font=40)
            self.nombre.grid(column=1, row=j,padx=5, pady=5)
           
                
            obEntrada.append(self.nombre)
            print(self.columnas)
            j+=1
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
            print(valores[cont])
            cont+=1
        lista2[0].config(state='disable')
        print(lista)
        return True
        #self.cerrar.config(state=NORMAL)
    def getEditar(self):
        lista2=self.obentrada
        lista=[]
        for i in lista2:
            lista.append(i.get())
            print(lista)
        
        crud=Crud()
        crud.modificar(lista)
        
    def getInfo(self):
        
        #Crud.guardar(numero_casa1,nombre1,apellido1,mz1,telefono1)
        
        lista2=self.obentrada

        lista=[]
        for i in lista2:
            if i:
                lista.append(i.get())
                print(lista)
        
        
        crud=Crud()
        crud.guardar(lista[1:])

        
        print("guardado")

def registrar():
    venta=Tk()
    objeto=Prueba()
    algo=lambda :objeto.editando()
    boton=Button(objeto.aver,text="Guardar",command=algo)
    boton.pack(side=BOTTOM)
    venta.mainloop()

if __name__=='__main__':
    registrar()

"""#Apellido y entrada
        
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
        self.numero_casa.grid(column=1, row=1,padx=5, pady=5)"""