from tabulate import tabulate

def agregarEmpleado(con):
    id_empleado = int(input("Identificador de Empleado: "))
    nombre = input("Nombre y Apellido: ")
    direccion = input("Direccion del sujeto: ")
    telefono = int(input("Numero telefonico: "))
    email = input("Correo electronico: ")
    fecha_inicio = input("Fecha contrato (dd/mm/YYYY): ")
    salario = int(input("Salario del sujeto: "))
    cursor = con.cursor()
    cursor.execute("INSERT INTO empleados (id_empleado, nombre, direccion, telefono, email, fecha_inicio, salario) VALUES (%s,%s,%s,%s,%s,%s,%s)", (id_empleado, nombre, direccion, telefono, email, fecha_inicio, salario))
    con.commit()
    empleados = cursor.fetchall()
    headers = ["ID","Nombre","Direccion","Telefono","Email","Fecha Inicio","Salario"]
    print(tabulate(empleados, headers=headers, tablefmt="double_outline"))
    print("Colaborador agregado.")

def eliminarEmpleado(con):
    id_empleado = int(input("Identificador del sujeto: "))
    cursor = con.cursor()
    cursor.execute("DELETE FROM empleado WHERE id_empleado = %s", (id_empleado,))
    con.commit()
    print("Sujeto eliminado.")

def verEmpleado(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()
    headers = ["ID","Nombre","Direccion","Telefono","Email","Fecha Inicio","Salario"]
    print(tabulate(empleados, headers=headers, tablefmt="rounded_outline"))