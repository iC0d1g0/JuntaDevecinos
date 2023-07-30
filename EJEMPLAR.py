
#Funcion que se ejecuta automaticamente, 
#solo hay que llamar al objecto/clase.
def __str__(self):
    datos = self.consulta_paises()
    aux=""
    for row in datos:
        aux=aux+ str(row)+"\n"
    return aux

#consulta la tabla contries, y devuelve los datos consultados. 
def consulta_paises(self):
    cur=self.cnn.cursor()
    cur.execute("SELECT * FROM countries")
    datos=cur.fetchall()
    cur.close()
    return datos

def buscar_pais(self,Id):
    cur = self.cnn.cursor()
    sql="SELECT * FROM countries WHERE Id={}".format(id)
    cur.execute(sql)
    datos = cur.fetchone()
    cur.close()
    return datos
def inserta_pais(self,Id, Country,etc):
    cur=self.cnn.cursor()
    variables='ejemplo'
    sql='''INSERT INTO countries (campos de tabla)
        VALUES('{}' nombres de las variables')'''.format(variables)
    cur.execute(sql)
    n=cur.rowcount
    self.cnn.commit()
    cur.close()
    return n
