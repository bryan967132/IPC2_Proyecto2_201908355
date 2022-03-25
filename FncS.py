from Lista import LstMtrz
from FncP import FuncionesP
from Constructores import ValorMtrz
class FuncionesS:
    def lstVctrToMtrz(self,filas,columnas,vector):
        matriz = LstMtrz(filas,columnas)
        c = 0
        for i in range(matriz.getF()):
            for j in range(matriz.getC()):
                matriz.insert(ValorMtrz(i,j,vector.get(c).valor))
                c += 1
        return matriz
    
    def ubicarM(self,matriz,militares):
        for i in range(militares.getL()):
            militar = militares.get(i)
            matriz.get(militar.fila,militar.columna).valor = 'M'
        return matriz

    def printCiudad(self,ciudad):
        fncP = FuncionesP()
        mapa = self.ubicarM(self.lstVctrToMtrz(ciudad.filas,ciudad.columnas,fncP.clonarVctr(ciudad.mapa)),ciudad.uMilitar)
        print("\n{}".format(ciudad.nombre))
        self.printMtrz(mapa)
    
    def printMtrz(self,matriz):
        cadenaM = ''
        for x in range(matriz.getF()):
            for y in range(matriz.getC()):
                celda = matriz.get(x,y).valor
                if celda == ' ':
                    cadenaM += ' · '
                elif celda == '*':
                    cadenaM += '▒▒▒'
                elif celda == 'E':
                    cadenaM += ' E '
                elif celda == 'R':
                    cadenaM += ' R '
                elif celda == 'C':
                    cadenaM += ' C '
                elif celda == 'M':
                    cadenaM += ' M '
                elif celda == 'P':
                    cadenaM += ' P '
            if x < matriz.getF() - 1:
                cadenaM += '\n'
        print(cadenaM)