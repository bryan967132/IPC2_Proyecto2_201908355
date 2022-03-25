class Nodo:
    def __init__(self,objeto = None,siguiente = None):
        self.objeto = objeto
        self.siguiente = siguiente

class LstMtrz:
    def __init__(self,filas,columnas):
        self.primero = None
        self.filas = filas
        self.columnas = columnas
    
    def getF(self):
        return self.filas
    
    def getC(self):
        return self.columnas
    
    def insert(self,nuevo):
        if self.primero is None:
            self.primero = Nodo(objeto = nuevo)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(objeto = nuevo)
    
    def get(self,i,j):
        actual = self.primero
        while actual:
            if actual.objeto.i == i and actual.objeto.j == j:
                return actual.objeto
            actual = actual.siguiente

class LstVctr:
    def __init__(self):
        self.primero = None
        self.longitud = 0
    
    def getL(self):
        return self.longitud

    def insert(self,nuevo):
        if self.primero is None:
            self.primero = Nodo(objeto = nuevo)
            self.longitud += 1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(objeto = nuevo)
        self.longitud += 1
    
    def replaceCiudad(self,nuevo):
        actual = self.primero
        while actual:
            if actual.objeto.nombre == nuevo.nombre:
                actual.objeto.filas = nuevo.filas
                actual.objeto.columnas = nuevo.columnas
                actual.objeto.mapa = nuevo.mapa
                actual.objeto.uMilitar = nuevo.uMilitar
                return
            actual = actual.siguiente
    
    def replaceRobot(self,nuevo):
        actual = self.primero
        while actual:
            if actual.objeto.nombre == nuevo.nombre:
                actual.objeto.tipo = nuevo.tipo
                actual.objeto.capacidad = nuevo.capacidad
                return
            actual = actual.siguiente

    def search(self,nombre):
        if self.primero is None:
            return - 1
        actual = self.primero
        while actual:
            if actual.objeto.nombre == nombre:
                return actual.objeto.i
            actual = actual.siguiente
        return - 1
    
    def get(self,i):
        actual = self.primero
        while actual:
            if actual.objeto.i == i:
                return actual.objeto
            actual = actual.siguiente