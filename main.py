from Modelo.Red import Red
from Utilidades.Utilidades import Utilidades

red= Red

def menu():
    salir= False
    print("#########################################")
    print("############ MENU PRINCIPAL #############")
    print("#########################################")
    print("1 Alta Usuario")
    print("2 Baja Usuario")
    print("3 Login")
    print("9 Salir")

    opcion= Utilidades.leerString("Elige una opción: ")

    if opcion == "1":
        red.altaUsuario()
    elif opcion == "2":
        red.bajaUsuario()
    elif opcion == "3":
        red.login()
    elif opcion == "9":
        print("Saliendo...")
        salir= True
    else:
        print("Escoge una opción válida")
    
    return salir

def aplicacion():
    salir=False
    while salir==False:
        salir=menu()

aplicacion()
