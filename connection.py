import mysql.connector
class Conexion: 
    cnn=mysql.connector.connect(host='127.0.0.1',
                                        port=3306,
                                        user='root',
                                        passwd='adderlis',
                                        database='adderlis')
    def __init__(self) -> None:
        try:
            self.info=self.cnn.get_server_info()
            print(self.info)
            self.fe=self.cnn.cursor()
            """    data = [
                    ('Jane','555-001'),
                    ('Joe', '555-001'),
                    ('John', '555-003')
                    ]
            stmt = "INSERT INTO employee (nombre, telefono) VALUES (%s,%s)"
            fe.executemany(stmt, data)
            cnn.commit()
            """
        except Exception as ex:
            print(ex)
        finally:
            if self.cnn.is_connected():
                self.cnn.close()
                print("Conexion finalizada")