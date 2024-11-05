from bd import bd
class Empleado:
    def __init__(self, nombre, direccion, telefono, email, fecha_inicio, salario):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.fecha_inicio = fecha_inicio
        self.salario = salario
    
    @staticmethod
    def crear_empleado(empleado):
        conexion = bd()
        cursor = conexion.cursor()
        query = """
            INSERT INTO Empleados (nombre, direccion, telefono, email, fecha_inicio, salario) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (empleado.nombre, empleado.direccion, empleado.telefono, empleado.email, empleado.fecha_inicio, empleado.salario))
        conexion.commit()
        conexion.close()

    @staticmethod
    def  leer_empleados():
        conexion = bd()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Empleados")
        empleados = cursor.fetchall()
        conexion.close()
        return empleados
    
    @staticmethod
    def actualizar_empleado(empleado_id, nuevo_salario):
        conexion = bd()
        cursor = conexion.cursor()
        query = "UPDATE Empleados SET salario = %s WHERE id = %s"
        cursor.execute(query, (nuevo_salario, empleado_id))
        conexion.commit()
        conexion.close()
    
    @staticmethod
    def eliminar_empleado(empleado_id):
        conexion = bd()
        cursor = conexion.cursor()
        query = "DELETE FROM Empleados WHERE id = %s"
        cursor.execute(query, (empleado_id,))
        conexion.commit()
        conexion.close()
