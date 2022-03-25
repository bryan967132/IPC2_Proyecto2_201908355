class ValorVctr:
    def __init__(self,i,valor):
        self.i = i
        self.valor = valor

class ValorMtrz:
    def __init__(self,i,j,valor):
        self.i = i
        self.j = j
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