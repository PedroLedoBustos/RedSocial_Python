class Utilidades:

    def leerString(dato):
        respuesta= input(dato)
        return respuesta
    
    def leerInteger(dato):
        while True:
            try:
                respuesta= int(input(dato))
                return respuesta
            except:
                print("Introduce un valor válido")