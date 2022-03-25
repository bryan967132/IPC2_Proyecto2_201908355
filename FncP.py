from Lista import LstVctr,LstMtrz
from Constructores import ValorVctr
class FuncionesP:
    def ubicarM(self,matriz,militares):
        for i in range(militares.getL()):
            militar = militares.get(i)
            matriz.get(militar.fila,militar.columna).setCaracter('M')
        return matriz

    def clonarMtrz(self,matriz):
        clon = LstMtrz(matriz.getF(),matriz.getC())
        for i in range(matriz.getF()):
            for j in range(matriz.getC()):
                clon.insert(matriz.get(i,j))
        return clon
    
    def clonarVctr(self,vector):
        clon = LstVctr()
        for i in range(vector.getL()):
            clon.insert(vector.get(i))
        return clon

    def mapaN(self,matriz):
        mapa = LstVctr()
        c = 0
        for i in range(matriz.getF()):
            for j in range(matriz.getC()):
                mapa.insert(ValorVctr(c,matriz.get(i,j).getCaracter()))
                c += 1
        return mapa
    
    def ciudad(self,ciudad):
        ciudad = LstMtrz()
        mapa = self.clonarVctr(ciudad.mapa)
        c = 0
        for x in range(ciudad.filas):
            for y in range(ciudad.columnas):
                
                c += 1
        return ciudad