from Constructores import ValorVctr
from Lista import LstVctr,LstMtrz
class Mision:
    def __init__(self,filas,columnas,mapa,militares):
        self.filas = filas
        self.columnas = columnas
        self.mapa = mapa
        self.militares = militares
    
    def generarPlanoRescate(self):
        self.transitables = LstVctr()
        self.transitables.insert(ValorVctr(0,' '))
        self.transitables.insert(ValorVctr(1,'E'))
        self.transitables.insert(ValorVctr(2,'C'))
        