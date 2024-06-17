from Modelo.Usuario import Usuario
from Utilidades.Utilidades import Utilidades


class Red:
    def __init__(self):
        self.usuarios=[]

    def altaUsuario(self):
        nombre= Utilidades.leerString("Introduce nombre de usuario:")
        apellido= Utilidades.leerString("Introduce apellido de usuario:")
        password= Utilidades.leerString("Introduce contraseña de usuario:")
        id= Utilidades.leerInteger("Introduce id de usuario:")

        usuario= Usuario(nombre,apellido,password,id)
        if any(user.getId()==usuario.getId() for user in self.usuarios):
            print("El usuario no se puede dar de alta, porque ya existe")
        else:
            usuario.setRed(self)
            self.usuarios.append(usuario)
            print("Usuario dado de alta")
    
    def bajaUsuario(self):
        id= Utilidades.leerInteger("Introduce el id del usuario que vas a dar de baja:")

        for usuario in self.usuarios:
            if usuario.getId()==id:
                password= Utilidades.leerString("Introduce contraseña de usuario que vas a dar de baja:")
                if(usuario.getPassword()== password):
                    self.usuarios.remove(usuario)
                    print(f"Usuario con Nombre: {usuario.getNombre()} y ID: {usuario.getId()} ha sido dado de baja")
                else:
                    print("Lo siento la contraseña es incorrecta")
            else:
                print(f"El usuario con ID: {id} no esta registrado")
    
    def login(self):
        id= Utilidades.leerInteger("Introduce el id del usuario:")
        password= Utilidades.leerString("Introduce contraseña de usuario:")

        for usuario in self.usuarios:
            if usuario.getId()==id and usuario.getPassword()==password:
                usuario.menu()
            else:
                print("Error: id o contraseña incorrecta")
    
    def getUsuarios(self):
        return self.usuarios