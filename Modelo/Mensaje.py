class Mensaje:
    def __init__(self, texto):
        self.texto= texto
        self.remitente= None
    
    def getTexto(self):
        return self.texto
    
    def getRemitente(self):
        return self.remitente
    
    def setRemitente(self, remite):
        self.remitente= remite