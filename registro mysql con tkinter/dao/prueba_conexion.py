import mysql.connector
from mysql.connector import Error

try:

    conexion= mysql.connector.connect(
        host='localhost', 
        port=3306, 
        user='root', 
        passwd='', 
        db='empresa'
    )

    if conexion.is_connected():
        print('conexion exitosa!!')
        
except Error as ex:
    print('error durante la conexion ', ex)