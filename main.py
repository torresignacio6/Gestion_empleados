import mysql.connector
from mysql.connector import Error 
from bd import bd

def ejecutar_consulta():
    try:
        conexion = bd() 
        if conexion:
            cursor = conexion.cursor()
            query = "SHOW TABLES;"        
            cursor.execute(query)
            resultados = cursor.fetchall()
            if resultados:
                for registro in resultados:
                    print(registro)
            else:
                print("Su búsqueda no arrojó resultados.")
        else:
            print("No se pudo establecer la conexión a la base de datos.")

    except Error as error: 
        print(f"Error al ejecutar la consulta: {error}")
    
    finally:
        if conexion and conexion.is_connected():
            cursor.close()
            conexion.close()


ejecutar_consulta()



