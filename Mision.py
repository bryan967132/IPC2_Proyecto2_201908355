from Constructores import ValorVctr
from Lista import LstVctr,LstMtrz
from Celda import Celda
from FncP import FuncionesP
from FncS import FuncionesS
class Mision:
    def __init__(self,filas,columnas,mapa,militares):
        self.fncP = FuncionesP()
        self.fncS = FuncionesS()
        self.filas = filas
        self.columnas = columnas
        self.mapa = self.fncP.clonarVctr(mapa)
        self.militares = militares
    
    def generarPlanoRescate(self):
        self.transitables = LstVctr()
        self.transitables.insert(ValorVctr(0,' '))
        self.transitables.insert(ValorVctr(1,'E'))
        self.transitables.insert(ValorVctr(2,'C'))
        self.mapa = self.fncS.lstMtrzToVctr(
            self.fncP.ubicarM(
                self.fncS.lstVctrToMtrz(
                    self.filas,
                    self.columnas,
                    self.mapa
                ),
                self.militares
            )
        )
        self.ciudad = self.getciudad(self.filas,self.columnas)
        self.fncP.printCiudad(self.ciudad)
        self.fncP.printPuntos('Entradas',self.entradas)
        self.fncP.printPuntos('Unidades Civiles',self.civiles)
        self.fncP.printPuntos('Recursos',self.recursos)

    def getciudad(self,filas,columnas):
        self.entradas = LstVctr()
        self.civiles = LstVctr()
        self.recursos = LstVctr()
        ciudad = LstMtrz(filas,columnas)
        c = 0
        entradas = 0;civiles = 0;recursos = 0
        for i in range(filas):
            for j in range(columnas):
                u = True;r = True;d = True;l = True
                if self.esTransitable(self.mapa.get(c).valor):
                    if i == 0:
                        if j == 0:
                            if not self.esTransitable(self.mapa.get(c + columnas).valor): d = False
                            if not self.esTransitable(self.mapa.get(c + 1).valor): r = False
                        elif j == columnas - 1:
                            if not self.esTransitable(self.mapa.get(c + columnas)): d = False
                            if not self.esTransitable(self.mapa.get(c - 1)): l = False
                        else:
                            if not self.esTransitable(self.mapa.get(c + columnas).valor): d = False
                            if not self.esTransitable(self.mapa.get(c + 1).valor): r = False
                            if not self.esTransitable(self.mapa.get(c - 1).valor): l = False
                    elif i == filas - 1:
                        if j == 0:
                            if not self.esTransitable(self.mapa.get(c - columnas).valor): u = False
                            if not self.esTransitable(self.mapa.get(c + 1).valor): r = False
                        elif j == columnas - 1:
                            if not self.esTransitable(self.mapa.get(c - columnas).valor): u = False
                            if not self.esTransitable(self.mapa.get(c - 1).valor): l = False
                        else:
                            if not self.esTransitable(self.mapa.get(c - columnas).valor): u = False
                            if not self.esTransitable(self.mapa.get(c + 1).valor): r = False
                            if not self.esTransitable(self.mapa.get(c - 1).valor): l = False
                    else:
                        if j == 0:
                            if not self.esTransitable(self.mapa.get(c + columnas).valor): d = False
                            if not self.esTransitable(self.mapa.get(c - columnas).valor): u = False
                            if not self.esTransitable(self.mapa.get(c + 1).valor): r = False
                        elif j == columnas - 1:
                            if not self.esTransitable(self.mapa.get(c + columnas).valor): d = False
                            if not self.esTransitable(self.mapa.get(c - columnas).valor): u = False
                            if not self.esTransitable(self.mapa.get(c - 1).valor): l = False
                        else:
                            if not self.esTransitable(self.mapa.get(c + columnas).valor): d = False
                            if not self.esTransitable(self.mapa.get(c - columnas).valor): u = False
                            if not self.esTransitable(self.mapa.get(c + 1).valor): r = False
                            if not self.esTransitable(self.mapa.get(c - 1).valor): l = False
                paso = LstVctr()
                paso.insert(ValorVctr(0,u))
                paso.insert(ValorVctr(1,r))
                paso.insert(ValorVctr(2,d))
                paso.insert(ValorVctr(3,l))
                if self.mapa.get(c).valor == 'E':
                    self.entradas.insert(ValorVctr(entradas,Celda('E',i,j,paso,False)))
                    entradas += 1
                elif self.mapa.get(c).valor == 'C':
                    self.civiles.insert(ValorVctr(civiles,Celda('C',i,j,paso,False)))
                    civiles += 1
                elif self.mapa.get(c).valor == 'R':
                    self.recursos.insert(ValorVctr(recursos,Celda('R',i,j,paso,False)))
                    recursos += 1
                ciudad.insert(Celda(self.mapa.get(c).valor,i,j,paso,False))
                c += 1
        return ciudad
    
    def esTransitable(self,celda):
        for i in range(self.transitables.getSize()):
            if self.transitables.get(i).valor == celda:
                return True
        return False