from bd import obtener_conexion
class  Proyecto:
    def __init__(self, nombre, descripcion, fecha_inicio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
    
    @staticmethod
    def  crear_proyecto(proyecto):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "INSERT INTO Proyectos (nombre, descripcion, fecha_inicio) VALUES (%s, %s, %s)"
        cursor.execute(query, (proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio))
        conexion.commit()
        conexion.close()
    
    @staticmethod
    def  leer_proyectos():
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Proyectos")
        proyectos = cursor.fetchall()
        conexion.close()
        return proyectos
