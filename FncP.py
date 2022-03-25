from Lista import LstVctr,LstMtrz
from Constructores import Valor
class FuncionesP:
    def clonar(self,matriz):
        clon = LstMtrz(matriz.getF(),matriz.getC())
        for i in range(matriz.getF()):
            for j in range(matriz.getC()):
                clon.insert(matriz.get(i,j)) 

    def mapaN(self,matriz):
        mapa = LstVctr()
        c = 0
        for i in range(matriz.getF()):
            for j in range(matriz.getC()):
                mapa.insert(Valor(c,matriz.get(i,j)))
                c += 1
        return mapa