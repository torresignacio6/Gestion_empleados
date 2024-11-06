from funciones import agregar_empleado, ver_empleados, eliminar_empleado  # Asegúrate de que estas funciones estén bien importadas

def submenu():
    while True:
        # Mostramos el menú de opciones
        print("\nMenu Empleados")
        print("1. Agregar empleados")
        print("2. Ver empleados")
        print("3. Eliminar empleados")
        print("4. Salir")

        # Leemos la opción del usuario
        opcion = input("Seleccione una opción (1-4): ")

        # Llamamos a la acción correspondiente según la opción seleccionada
        if opcion == "1":
            # Agregar empleados
            agregar_empleado()
        elif opcion == "2":
            # Ver empleados
            ver_empleados()
        elif opcion == "3":
            # Eliminar empleados
            eliminar_empleado()
        elif opcion == "4":
            print("Saliendo del programa.")
            break  # Sale del bucle y termina el programa
        else:
            # Si la opción es inválida
            print("Opción inválida. Por favor, selecciona una opción entre 1 y 4.")

# Inicia el menú si este archivo es ejecutado directamente
if __name__ == "__main__":
    submenu()


