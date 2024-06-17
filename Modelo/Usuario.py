from Utilidades.Utilidades import Utilidades


class Usuario:

    def __init__(self, nombre, apellido, password, id):
        self.nombre= nombre
        self.apellido= apellido
        self.password= password
        self.id=id
        self.mensajes=[]
        self.amigos=[]
        self.red=None
    
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getPassword(self):
        return self.password
    
    def getId(self):
        return self.id
    
    def setRed(self,redNueva):
        self.red= redNueva

    def comprobarUsuario(self,id):
        listaRed=self.red.getUsuarios()
        for user in listaRed:
            if user.getId() == id:
                return user
        return None

    def altaAmigo(self):
        id= Utilidades.leerInteger("Introduce el Id de la persona que quieres agregar como amigo:")
        amigo= self.comprobarUsuario(id)
        if amigo==None:
            print("Este usuario no esta registrado en la aplicación")
        else:
            if any(user.getId()==id for user in self.amigos):
                print("Lo siento, este usuario ya es tu amigo")
            else:
                self.amigos.append(amigo)
                print(f"El usuario {amigo.getNombre()} {amigo.getApellido()} ahora esta en tu lista de amigos")
    
    def bajaAmigo(self):
        id= Utilidades.leerInteger("Introduce el Id de la persona que quieres agregar como amigo:")
        amigo= self.comprobarUsuario(id)
        if amigo==None:
            print("Este usuario no esta registrado en la aplicación")
        else:
            if any(user.getId()==id for user in self.amigos):
                self.amigos.remove(amigo)
                print(f"El usuario: {amigo.getNombre()} {amigo.getApellido()} ya no es tu amigo")
            else:
                print(f"Lo siento, el usuario: {amigo.getNombre()} {amigo.getApellido()} no esta en tu lista de amigos")

    def listaAmigos(self):
        print(f"LISTA DE AMIGOS DE: {self.nombre} {self.apellido}")
        for user in self.amigos:
            print(f"Nombre: {user.getNombre()} Apellido: {user.getApellido()} Id: {user.getId()}") 
    
    def menu(self):
        salir=False
        while salir==False:
            print("##################################")
            print(f"##### Menu de {self.nombre} ######")
            print("##################################")
            print("1 Alta amigo")
            print("2 Baja amigo")
            print("3 Lista de amigos")
            print("4 Enviar mensaje")
            print("5 Leer mensajes")
            print("9 Salir")

            opcion= Utilidades.leerString("Escoge una opción: ")
            if opcion=="1":
                self.altaAmigo()
            elif opcion=="2":
                self.bajaAmigo()
            elif opcion=="3":
                self.listaAmigos()
            elif opcion=="4":
                enviarMensaje()
            elif opcion=="5":
                leerMensaje()
            elif opcion=="9":
                print("Saliendo...")
                salir=True
            else:
                print("Escoge una opción válida")

      