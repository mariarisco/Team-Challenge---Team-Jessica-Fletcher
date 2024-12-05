#import pandas as pd
import sqlite3
import pandas as pd

# Conectamos con la base de datos chinook.db
connection = sqlite3.connect("almacen.db")

# Obtenemos un cursor que utilizaremos para hacer las queries
cursor= connection.cursor()

def sql_query(query):

    # Ejecuta la query
    cursor.execute(query) 

    # Almacena los datos de la query 
    ans = cursor.fetchall()

    # Obtenemos los nombres de las columnas de la tabla
    names = [description[0] for description in cursor.description]

    return pd.DataFrame(ans,columns=names)

query =  "SELECT * FROM Piezas"
cursor.execute(query)

"""

query =
SELECT *
FROM Proveedores

sql_query(query)
"""