from Lista import LstVctr
class Ciudad:
    def __init__(self,ciudad):
        self.ciudad = ciudad
        self.caminos = LstVctr()
    
    def arribaDisponible(self,celdaActual,celdaDestino):
        if celdaActual and not celdaDestino.isVisitado():
            return celdaActual.arribaDisponible()
        return False
    
    def derechaDisponible(self,celdaActual,celdaDestino):
        if celdaActual and not celdaDestino.isVisitado():
            return celdaActual.derechaDisponible()
        return False
    
    def abajoDisponible(self,celdaActual,celdaDestino):
        if celdaActual and not celdaDestino.isVisitado():
            return celdaActual.abajoDisponible()
        return False
    
    def izquierdaDisponible(self,celdaActual,celdaDestino):
        if celdaActual and not celdaDestino.isVisitado():
            return celdaActual.izquierdaDisponible()
        return False
    
    def getCeldaAt(self,x,y):
        if self.dentroDelLimite(x,y):
            return self.ciudad.get(x,y)
        return None
    
    def dentroDelLimite(self,x,y):
        return x >= 0 and x < self.ciudad.getF() and y >= 0 and y < self.ciudad.getC()
    
    def agregarCamion(self,camino):
        if camino:
            self.caminos.insert(camino)
    
    def getCamino(self):
        for i in range(self.caminos.getSize()):
            for j in range(self.caminos.getSize()):
                pass#if self.caminos.get(j)