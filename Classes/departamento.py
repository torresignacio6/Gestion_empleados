from bd import bd

class Departamento:
    def __init__(self, nombre, id_gerente):
        self.nombre = nombre
        self.id_gerente = id_gerente
    
    @staticmethod
    def crear_departamento(departamento):
        conexion = bd()
        if conexion:
            cursor = conexion.cursor()
            query = "INSERT INTO Departamentos (nombre, id_gerente) VALUES (%s, %s)"
            cursor.execute(query, (departamento.nombre, departamento.id_gerente))
            conexion.commit()
            conexion.close()
        else:
            print("No se pudo establecer la conexión para crear el departamento.")
    
    @staticmethod
    def leer_departamentos():
        conexion = bd()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Departamentos")
            departamentos = cursor.fetchall()
            conexion.close()
            
            for departamento in departamentos:
                print(departamento)  # Imprimir cada registro encontrado
            
            return departamentos
        else:
            print("No se pudo establecer la conexión para leer los departamentos.")

if __name__ == "__main__":
    print("Departamentos en la base de datos:")
    Departamento.leer_departamentos()
