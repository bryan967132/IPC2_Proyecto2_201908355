from Constructores import ValorVctr
from Lista import LstVctr
import sys
class Ciudad:
    def __init__(self,ciudad):
        self.ciudad = ciudad
        self.caminos = LstVctr()
        self.nCmn = 0
        self.transitables = 0
    
    def arribaDisponible(self,celdaActual,celdaDestino):
        if celdaDestino and not celdaDestino.isVisitado():
            return celdaActual.arribaDisponible()
        return False
    
    def derechaDisponible(self,celdaActual,celdaDestino):
        if celdaDestino and not celdaDestino.isVisitado():
            return celdaActual.derechaDisponible()
        return False
    
    def abajoDisponible(self,celdaActual,celdaDestino):
        if celdaDestino and not celdaDestino.isVisitado():
            return celdaActual.abajoDisponible()
        return False
    
    def izquierdaDisponible(self,celdaActual,celdaDestino):
        if celdaDestino and not celdaDestino.isVisitado():
            return celdaActual.izquierdaDisponible()
        return False
    
    def getCeldaDestino(self,x,y):
        if self.dentroDelLimite(x,y):
            return self.ciudad.get(x,y)
        return None
    
    def dentroDelLimite(self,x,y):
        return x >= 0 and x < self.ciudad.getF() and y >= 0 and y < self.ciudad.getC()
    
    def agregarCamino(self,camino):
        if camino:
            self.caminos.insert(ValorVctr(self.nCmn,camino))
            self.nCmn += 1
    
    def getCamino(self):
        for j in range(self.caminos.getSize() - 1):
            for i in range(self.caminos.getSize() - j - 1):
                if self.caminos.get(i).valor.getSize() > self.caminos.get(i + 1).valor.getSize():
                    self.caminos.change(i,i + 1)
        return self.caminos.get(0).valor