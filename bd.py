import mysql.connector
from mysql.connector import errorcode

def bd():
    config = {
        'user': "root",
        'password': "",
        'host': "localhost",
        'database': "gestion_empleados"
    }
    try:
        conexion = mysql.connector.connect(**config)
        return conexion
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Acceso denegado para el usuario o la contraseña")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Su base de datos NO existe")
        else:
            print("Error de conexión:", error)
        return None

def ejecutar_consulta(consulta):
    conexion = bd()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute(consulta)
            resultados = cursor.fetchall()  # Guardamos los resultados
            return resultados  # Los devolvemos a quien llame a esta función
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
            return None  # Si ocurre un error, retornamos None
        finally:
            cursor.close()
            conexion.close()
    else:
        print("No se pudo establecer la conexión a la base de datos.")
        return None  # Si no se pudo conectar, también retornamos None
