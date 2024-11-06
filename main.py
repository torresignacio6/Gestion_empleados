from mysql.connector import (connection)
import submenu as pn

def menu(con):
    while True:
        print("\n^^^ Menú Principal ^^^")
        print("1. Menú de Empleados")
        print("2. Salir")
        
        opcion = input("Laburá loco:  ")
        
        if opcion == "1":
            pn.submenu(con)
        elif opcion == "2":
            break
        else:
            print("Como tan weon.")

def main():
    cnx = connection.MySQLConnection(
        user='root', 
        password='', 
        host='127.0.0.1', 
        database='nachodb',
        port = 3306
        )
    cursor = cnx.cursor()
    cursor.execute(menu(cnx))
    cnx.close()

if __name__ == "__main__":
    main()