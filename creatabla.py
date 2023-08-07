
from crud import *
class Tabla(Crud): 
    def __init__(self):
        super().__init__()
        self.cursor=self.conexion.cursor()

    def creatabla(self,nombretabla):
        
        self.cursor.execute('CREATE {} '.format(nombretabla))