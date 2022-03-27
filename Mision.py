from Constructores import ValorVctr,ValorMtrz
from Limpiar import Limpiar
from Lista import LstVctr,LstMtrz
from Ciudad import Ciudad
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
    
    def iniciarRescate(self,x1,y1):
        self.ordenarEntradas(x1,y1)
        for i in range(self.entradas.getSize()):
            try:
                camino = LstVctr()
                clonCiudad = self.fncP.clonarMtrz(self.ciudad)
                tmpCiudad = Ciudad(self.marcarDestino(clonCiudad,x1,y1))
                camino.insert(ValorVctr(0,clonCiudad.get(self.entradas.get(i).valor.getI(),self.entradas.get(i).valor.getJ())))
                self.encontrarCaminos(tmpCiudad,clonCiudad.get(self.entradas.get(i).valor.getI(),self.entradas.get(i).valor.getJ()),camino,1)
                camino = tmpCiudad.getCamino()
                clonCiudad = self.getMision(clonCiudad,camino,'P')
                Limpiar().limpiarConsola()
                print('\nÚltima Misión De Rescate\nMisión Completada')
                return
            except:
                pass
        Limpiar().limpiarConsola()
        print('\nÚltima Misión De Rescate\nMisión Imposible')

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
    
    def ordenarEntradas(self,x1,y1):
        for i in range(self.entradas.getSize() - 1):
            for x in range(self.entradas.getSize() - i - 1):
                actual = self.entradas.get(x).valor
                actual = abs(x1 - actual.getI()) + abs(y1 - actual.getJ())
                siguiente = self.entradas.get(x + 1).valor
                siguiente = abs(x1 - siguiente.getI()) + abs(y1 - siguiente.getJ())
                if actual > siguiente:
                    self.entradas.change(x,x + 1)
    
    def marcarDestino(self,ciudad,x,y):
        ciudad.get(x,y).setFin(True)
        return ciudad
    
    def encontrarCaminos(self,ciudad,celdaActual,camino,n):
        if celdaActual.isFin():
            ciudad.agregarCamino(self.fncP.clonarVctr(camino))
        else:
            movimientos = LstMtrz(4,2)
            movimientos.insert(ValorMtrz(0,0,-1));movimientos.insert(ValorMtrz(0,1,0))
            movimientos.insert(ValorMtrz(1,0,0));movimientos.insert(ValorMtrz(1,1,1))
            movimientos.insert(ValorMtrz(2,0,1));movimientos.insert(ValorMtrz(2,1,0))
            movimientos.insert(ValorMtrz(3,0,0));movimientos.insert(ValorMtrz(3,1,-1))
            for i in range(movimientos.getF()):
                posI = celdaActual.getI() + movimientos.get(i,0).valor
                posJ = celdaActual.getJ() + movimientos.get(i,1).valor
                celdaDestino = ciudad.getCeldaDestino(posI,posJ)
                if i == 0:
                    if ciudad.arribaDisponible(celdaActual,celdaDestino):
                        camino.insert(ValorVctr(n,celdaDestino))
                        celdaActual.setVisitado(True)
                        self.encontrarCaminos(ciudad,celdaDestino,camino,n + 1)
                        celdaActual.setVisitado(False)
                        camino.remove(n)
                elif i == 1:
                    if ciudad.derechaDisponible(celdaActual,celdaDestino):
                        camino.insert(ValorVctr(n,celdaDestino))
                        celdaActual.setVisitado(True)
                        self.encontrarCaminos(ciudad,celdaDestino,camino,n + 1)
                        celdaActual.setVisitado(False)
                        camino.remove(n)
                elif i == 2:
                    if ciudad.abajoDisponible(celdaActual,celdaDestino):
                        camino.insert(ValorVctr(n,celdaDestino))
                        celdaActual.setVisitado(True)
                        self.encontrarCaminos(ciudad,celdaDestino,camino,n + 1)
                        celdaActual.setVisitado(False)
                        camino.remove(n)
                elif i == 3:
                    if ciudad.izquierdaDisponible(celdaActual,celdaDestino):
                        camino.insert(ValorVctr(n,celdaDestino))
                        celdaActual.setVisitado(True)
                        self.encontrarCaminos(ciudad,celdaDestino,camino,n + 1)
                        celdaActual.setVisitado(False)
                        camino.remove(n)
    
    def getMision(self,ciudad,camino,caracter):
        for i in range(camino.getSize()):
            cmn = camino.get(i).valor
            celda = ciudad.get(cmn.getI(),cmn.getJ())
            if celda.getCaracter() == ' ':
                celda.setCaracter(caracter)
                celda.setVisitado(True)
        return ciudad