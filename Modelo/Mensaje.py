class Mensaje:
    def __init__(self, texto):
        self.texto= texto
        self.remitente= None
    
    def getTexto(self):
        return self.texto
    
    def setRemitente(self, remite):
        self.remitente= remite