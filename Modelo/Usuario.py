from Utilidades.Utilidades import Utilidades


class Usuario:

    def __init__(self, nombre, apellido, password, id):
        self.nombre= nombre
        self.apellido= apellido
        self.password= password
        self.id=id
        self.mensajes=[]
        self.amigos=[]
    
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getPassword(self):
        return self.password
    
    def getId(self):
        return self.id
    
    def menu(self):
        salir=False
        while salir==False:
            print("##################################")
            print(f"##### Menu de {self.nombre}######")
            print("##################################")
            print("1 Alta amigo")
            print("2 Baja amigo")
            print("3 Lista de amigos")
            print("4 Enviar mensaje")
            print("5 Leer mensajes")
            print("9 Salir")

            opcion= Utilidades.leerString("Escoge una opción: ")
            if opcion=="1":
                altaAmigo()
            elif opcion=="2":
                bajaAmigo()
            elif opcion=="3":
                listaAmigos()
            elif opcion=="4":
                enviarMensaje()
            elif opcion=="5":
                leerMensaje()
            elif opcion=="9":
                print("Saliendo...")
                salir=True
            else:
                print("Escoge una opción válida")

      