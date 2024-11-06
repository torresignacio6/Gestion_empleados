from bd import ejecutar_consulta

def agregar_empleado():
    # Aquí pedimos los datos al usuario para agregar un empleado
    nombre = input("Ingrese el nombre del empleado: ")
    direccion = input("Ingrese la dirección del empleado: ")
    telefono = input("Ingrese el teléfono del empleado: ")
    email = input("Ingrese el correo electrónico del empleado: ")
    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    salario = float(input("Ingrese el salario del empleado: "))

    
    query = f"""
        INSERT INTO Empleados (nombre, direccion, telefono, email, fecha_inicio, salario)
        VALUES ('{nombre}', '{direccion}', '{telefono}', '{email}', '{fecha_inicio}', {salario});
    """

    
    ejecutar_consulta(query)
    print("Empleado agregado exitosamente.")

def ver_empleados():
    
    query = "SELECT id, nombre, direccion, telefono, email, fecha_inicio, salario FROM Empleados;"
    
   
    resultados = ejecutar_consulta(query)
    
    if resultados:
        print("\nListado de empleados:")
        for empleado in resultados:
            
            id_empleado, nombre, direccion, telefono, email, fecha_inicio, salario = empleado

           
            fecha_inicio_formateada = fecha_inicio.strftime('%d-%m-%Y') if isinstance(fecha_inicio, datetime.date) else fecha_inicio
            salario_formateado = f"{salario:.2f}" if isinstance(salario, Decimal) else salario

            
            print(f"ID: {id_empleado}, Nombre: {nombre}, Dirección: {direccion}, Teléfono: {telefono}, "
                  f"Email: {email}, Fecha de Inicio: {fecha_inicio_formateada}, Salario: {salario_formateado}")
    else:
        print("No hay empleados registrados.")

def eliminar_empleado():
    
    id_empleado = input("Ingrese el ID del empleado que desea eliminar: ")
    
    
    query = f"DELETE FROM Empleados WHERE id = {id_empleado};"
    
    
    ejecutar_consulta(query)
    print(f"Empleado con ID {id_empleado} eliminado exitosamente.")
