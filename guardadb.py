

class GuardaDB:
    def __init__(self,nombre,apellido,mz,numero_casa,telefono) -> None:
       self.nombre=nombre
       self.apellido=apellido
       self.mz=mz
       self.numero_casa=numero_casa
       self.telefono=telefono
    def guarda_db(self):
        self.nombre
        self.apellido
        self.mz
        self.numero_casa
        self.telefono
        print(self.nombre,
        self.apellido,
        self.mz,
        self.numero_casa,
        self.telefono)
        listas=[self.nombre,
                            self.apellido,
                            self.mz,
                            self.numero_casa,
                            self.telefono]
        with open('basedeprueba.txt', 'w') as f:
                 for i in listas:
                    f.write(i+'\n')
        f.close()
        print("listo")