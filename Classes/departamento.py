from bd import bd
class Departamento:
    def __init__(self, nombre, id_gerente):
        self.nombre = nombre
        self.id_gerente = id_gerente
    
    @staticmethod
    def crear_departamento(departamento):
        conexion = bd()
        cursor = conexion.cursor()
        query = "INSERT INTO Departamentos (nombre, id_gerente) VALUES (%s, %s)"
        cursor.execute(query, (departamento.nombre, departamento.id_gerente))
        conexion.commit()
        conexion.close()
    
    @staticmethod
    def leer_departamentos():
        conexion = bd()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Departamentos")
        departamentos = cursor.fetchall()
        conexion.close()
        return   departamentos
