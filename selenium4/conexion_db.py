import os
from pymysql import Connection
from dataclasses import dataclass, field
from typing import Any



def abrir_conexion():
    credenciales = {
        "host": os.environ['MYSQL_HOST']
        "user": os.environ['MYSQL_USER'],
        "database": os.environ['MYSQL_DATABASE'],
        "password": os.environ['MYSQL_PASSWORD'],
        "port": 3307,
    }
    
    conexion = Connection(**credenciales)
    
    return conexion
    


@dataclass
class ConexionSQL

    conexion: Any = field(default_factory=abrir_conexion)

    def ejecutar_query(self, query, commit=False, respuesta=True, valores=None):
        
        cursor = self.conexion.cursor()

        if valores:
            cursor.execute(query, valores)
        else:
            cursor.execute(query)
            
        if respuesta:
              
            return list(cursor.fetchall())
        
        if commit:
            
            self.conexion.commit()


# query = "SHOW DATABASES;"

# query = "CREATE TABLE condusef (valor VARCHAR(15), enganche VARCHAR(10), plazos VARCHAR(5), opcion VARCHAR(20))"

# query = "INSERT INTO condusef (name, address) VALUES (%s, %s, %s, %s )"
# val = ("10000000", "2000000", "36", "tasa")



