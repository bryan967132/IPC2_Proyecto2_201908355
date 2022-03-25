class Valor:
    def __init__(self,i,valor):
        self.i = i
        self.valor = valor

class Robot:
    def __init__(self,i,nombre,tipo,capacidad = 0):
        self.i = i
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad

class UMilitar:
    def __init__(self,i,fila,columna,capacidad):
        self.i = i
        self.fila = fila
        self.columna = columna
        self.capacidad = capacidad

class NCiudad:
    def __init__(self,i,filas,columnas,nombre,mapa,uMilitar):
        self.i = i
        self.filas = filas
        self.columnas = columnas
        self.nombre = nombre
        self.mapa = mapa
        self.uMilitar = uMilitar

class Celda:
    def __init__(self,i,j,caracter,paso,fin):
        self.setI(i)
        self.setJ(j)
        self.setCaracter(caracter)
        self.setPaso(paso)
        self.setFin(fin)
        self.setVisitado(False)

    def getCaracter(self):
        return self.caracter

    def setCaracter(self,caracter):
        self.caracter = caracter
    
    def getI(self):
        return self.i
    
    def setI(self,i):
        self.i = i

    def getJ(self):
        return self.posY
    
    def setJ(self,posY):
        self.posY = posY
    
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