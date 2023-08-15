from tkinter import *
from tkinter import ttk
from registros import Prueba
from treeview import *
from exportar import *
from crud import *
from aportar import AportarView
class Ventana(Frame) :
    def __init__(self, master=None):
        super().__init__(master, width=850, height=460)
        self.crud=Crud()
        self.master=master
        self.pack()
        nombres_columnas=self.crud.vistaColumnas(self.crud.tabla)
        self.tabla=VistaArbol(self,100,20,700,430,nombres_columnas)
        self.tabla.grid['selectmode']='browse' #Esta linea es para desabilitar que se seleccionen mas de un elemento
        
        self.create_widgets()

    def setTablaFiltrar(self):
        self.vista=Tk()
        self.vista.title('Resumen de APortes')
        self.vista.geometry('625x450')
        nombres_columnas=self.crud.vistaColumnas('jv_aportes')
        self.verResumen=VistaArbol(self.vista,100,20,500,400,nombres_columnas)
        self.verResumen.grid['selectmode']='browse'
        frame2=Frame(self.vista)
        frame2.place(x=600,y=0, width=20, height=450)
        sb=Scrollbar(frame2,orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)
        self.verResumen.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.verResumen.grid.yview)

    def getResumen(self): 
        self.setTablaFiltrar()
        buton=Button(self.vista,text='Total', command=self.getTotal)
        buton.place(x=15, y=100)
        exportar = lambda: Excel('jv_aportes')
        buton2=Button(self.vista, text='Exportar', command=exportar)
        buton2.place(x=15, y=120)
        datos=self.crud.leer('jv_aportes')
        
        for row in datos: 
            
            self.verResumen.insertar(row)

        
    def getInfoUsuario(self):
        selected=self.tabla.grid.focus()
        clave=self.tabla.grid.item(selected,'text')
        valores=self.tabla.grid.item(selected,'values')
        print(clave)
        if clave != '':
            datos=self.crud.buscar_db(clave,'jv_aportes')
            
            if datos != []:
                self.setTablaFiltrar()
                
                print(datos)
                for row in datos:
                    self.verResumen.insertar(row)
            else:
                messagebox.showinfo('No ha aportado','{} no ha hecho aportes'.format(valores))
            
        else: 
            messagebox.showwarning('Alerta','Para ver la info de un usuario favor selecionarlo')
    def getTotal(self): 
        datos =self.crud.sumarcolumnas('aporte','jv_aportes')
        total=''
        for to in datos:
            for t in to:
                total=t
        print(total)
        messagebox.showinfo('Total', 'Total de aportes: {}'.format(total))
    
    def llenarDatos(self): 
        datos=self.crud.leer()
        for row in datos: 
            self.tabla.insertar(row)
           

    def guardar(self):
        self.objeto.getInfo()
        self.refresh()
        
    def registrar(self):
        self.objeto=Prueba(self.crud.tabla)
        
        self.boton=Button(self.objeto.aver,text="Guardar",bd=5,command=self.guardar)
        self.boton.pack(side=BOTTOM)

    def ayudamodificar(self,valores):
        self.objeto=Prueba(self.crud.tabla)
        if self.objeto.editando(valores):
            boton=Button(self.objeto.aver,text="Modificar",bd=5, command=lambda:self.objeto.getEditar())
            boton.pack(side=BOTTOM)



    def exportar(self):
        mi_tabla=self.crud.tabla
        Excel(mi_tabla)
    
    def modificar(self):
        selected=self.tabla.grid.focus()
        clave=self.tabla.grid.item(selected,'text')
        
        valores=self.tabla.grid.item(selected,'values')#Obetengo una tupla con los valores
        if clave:
            if messagebox.askokcancel('modificar', 'seguro que quieres "Modificar": {}'.format(' '.join(valores))):
                 valores =list(valores)
                 valores.insert(0,str(clave))
                 self.ayudamodificar(valores)
                
        else: 
            messagebox.showwarning('Error', 'Preciona el boton "Refrescar", y luego seleciona un elemento para editarlo')         
                 
        #self.refresh()  
        

    def aporte(self):
        #1>en aporte leo la clave o id del usuario selecionado
        selected=self.tabla.grid.focus()
        clave=self.tabla.grid.item(selected,'text')
        valores=self.tabla.grid.item(selected,'values')
        
        #2> EN caso que no selecionen nada
        if clave=='':
            messagebox.showwarning('Alerta!!', 'Seleciona un miembro para hacer el aporte')

        else:
            
            AportarView(clave)
    


    def eliminar(self):
        selected=self.tabla.grid.focus()
        clave=self.tabla.grid.item(selected,'text')
        valores=self.tabla.grid.item(selected,'values')
     
        if clave:
            if messagebox.askokcancel('modificar', 'seguro que quieres eliminar: {}'.format(' '.join(valores))):
                
                if self.crud.elminar(clave):
                    messagebox.showwarning('Albertensia', 'Acabas de eliminar: {}'.format(' '.join(valores)))

                else:
                    messagebox.showerror('ERROR','NO ES POSIBLE ELIMINAR ELEMENTO, ERROR 404')
            else:
                pass
        else: 
            messagebox.showerror('Eliminar','No selecionaste ningun elemento!')
        self.refresh()


    def buscar(self):
        pass

    


    def create_widgets(self):
        frame1= Frame(self, bg="#bfdaff")
        frame1.place(x=0, y=0, width=93, height=459)

        frame2=Frame(self)
        frame2.place(x=800,y=0, width=20, height=459)
        sb=Scrollbar(frame2,orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)
        self.tabla.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.tabla.grid.yview)

        #Botones
        self.registro=Button(frame1, text="REGISTRO", bd=5, background="#1DE321", command=self.registrar)
        self.registro.place(x=10, y=10, width=80, height=30)
        
        self.actualizar=Button(frame1, text="EDITAR", bd=5, background="#2C91E3",command=self.modificar)
        self.actualizar.place(x=10, y=50, width=80, height=30)
        
        self.eliminar=Button(frame1, text="ELIMINAR", bd=5, background="#E35625",command=self.eliminar)
        self.eliminar.place(x=10, y=95, width=80, height=30)

        self.aporte1=Button(frame1, text="APORTE", bd=5,background="#35E3CB", command=self.aporte)
        self.aporte1.place(x=10, y=140, width=80, height=30)

        self.ver1=Button(frame1, text="INFO.", bd=5,command=self.getInfoUsuario)
        self.ver1.place(x=10, y=178, width=80, height=30)

        self.resumen=Button(frame1, text="RESUMEN", bd=5, command=self.getResumen)
        self.resumen.place(x=10, y=225, width=80, height=30)

        self.exportar=Button(frame1, text="EXPORTAR", bd=5,command=self.exportar)
        self.exportar.pack(side=BOTTOM)

        self.refrescar=Button(frame1, text="Refresh", bd=5, command=self.refresh)
        self.refrescar.place(x=10, y=300, width=80, height=30)


        #Buscador de elementos para filtrar la tabla
        #Se colocará un imput coon un botón

        #input
        self.entryBuscar=Entry(frame2)
        #self.entryBuscar.

        self.buscar=Button(frame2, text="Buscar", bd=5, command=self.buscar)
        self.buscar.place(x=300, y=10, width=80, height=30)
        #Montor el TreeView
        
        
        #self.tabla.insert("", END, text="1", values=("Adderlis","Severino","24","N17","8293891045","100","2000.00"))
        
       
        #Insertando

    def refresh(self):
        #self.tabla.insertar("Adderlis","REYES","24","N17","8293891045","100","2000.00")
        for item in self.tabla.grid.get_children():
            self.tabla.grid.delete(item)

        self.llenarDatos()


def main():
    root=Tk()
    root.wm_title("JV. La Union Hace la Fuerza!")
    root.resizable(False, False)
    app=Ventana(root)
    app.mainloop()

if __name__ =='__main__': 
    main()
