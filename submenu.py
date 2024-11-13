import funciones as fn

def submenu(con):
    while True:
        print("\nMenu Empleados")
        print("1. Agregar empleados")
        print("2. Eliminar empleados")
        print("3. Ver empleados")

        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            fn.agregarEmpleado(con)
        elif opcion == "2":
            fn.eliminarEmpleado(con)
        elif opcion == "3":
            fn.verEmpleado(con)
        elif opcion == "4":
            print("Cerrando...")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción entre 1 y 4.")

if __name__ == "__main__":
    submenu()


