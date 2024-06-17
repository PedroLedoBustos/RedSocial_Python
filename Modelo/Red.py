from Modelo.Usuario import Usuario
from Utilidades.Utilidades import Utilidades


class Red:
    usuarios=[]

    def altaUsuario():
        nombre= Utilidades.leerString("Introduce nombre de usuario:")
        apellido= Utilidades.leerString("Introduce apellido de usuario:")
        password= Utilidades.leerString("Introduce contraseña de usuario:")
        id= Utilidades.leerInteger("Introduce id de usuario:")

        usuario= Usuario(nombre,apellido,password,id)
        if any(user.getId()==usuario.getId() for user in Red.usuarios):
            print("El usuario no se puede dar de alta, porque ya existe")
        else:
            Red.usuarios.append(usuario)
            print("Usuario dado de alta")
    
    def bajaUsuario():
        id= Utilidades.leerInteger("Introduce el id del usuario que vas a dar de baja:")

        for usuario in Red.usuarios:
            if usuario.getId()==id:
                password= Utilidades.leerString("Introduce contraseña de usuario que vas a dar de baja:")
                if(usuario.getPassword()== password):
                    Red.usuarios.remove(usuario)
                    print(f"Usuario con Nombre: {usuario.getNombre()} y ID: {usuario.getId()} ha sido dado de baja")
                else:
                    print("Lo siento la contraseña es incorrecta")
            else:
                print(f"El usuario con ID: {id} no esta registrado")
    
    def login():
        id= Utilidades.leerInteger("Introduce el id del usuario:")
        password= Utilidades.leerString("Introduce contraseña de usuario:")

        for usuario in Red.usuarios:
            if usuario.getId()==id and usuario.getPassword()==password:
                usuario.menu()
            else:
                print("Error: id o contraseña incorrecta")