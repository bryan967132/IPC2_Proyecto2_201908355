class Celda:
    def __init__(self,caracter,i,j,paso,fin):
        self.setCaracter(caracter)
        self.i = i
        self.j = j
        self.setPaso(paso)
        self.setFin(fin)
        self.setVisitado(False)

    def getCaracter(self):
        return self.caracter

    def setCaracter(self,caracter):
        self.caracter = caracter
    
    def getI(self):
        return self.i

    def getJ(self):
        return self.j
    
    def arribaDisponible(self):
        return self.paso.get(0)

    def derechaDisponible(self):
        return self.paso.get(1)

    def abajoDisponible(self):
        return self.paso.get(2)

    def izquierdaDisponible(self):
        return self.paso.get(3)

    def setPaso(self,paso):
        self.paso = paso
    
    def isFin(self):
        return self.fin
    
    def setFin(self,fin):
        self.fin = fin
    
    def isVisitado(self):
        return self.visitado
    
    def setVisitado(self,visitado):
        self.visitado = visitado