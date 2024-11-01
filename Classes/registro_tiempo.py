from bd import obtener_conexion
class RegistroTiempo:
    def __init__(self, id_empleado, id_proyecto, fecha, horas_trabajadas, descripcion):
        self.id_empleado = id_empleado
        self.id_proyecto = id_proyecto
        self.fecha = fecha
        self.horas_trabajadas = horas_trabajadas
        self.descripcion = descripcion
    
    @staticmethod
    def crear_registro_tiempo(registro):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = """
            INSERT INTO Registro_Tiempo (id_empleado, id_proyecto, fecha, horas_trabajadas, descripcion)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (registro.id_empleado, registro.id_proyecto, registro.fecha, registro.horas_trabajadas, registro.descripcion))
        conexion.commit()
        conexion.close()
    
    @staticmethod
    def leer_registros_tiempo():
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Registro_Tiempo")
        registros = cursor.fetchall()
        conexion.close()
        return registros
