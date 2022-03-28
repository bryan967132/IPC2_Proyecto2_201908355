from Constructores import ValorVctr,ValorMtrz
from Limpiar import Limpiar
from Lista import LstVctr,LstMtrz
from Ciudad import Ciudad
from Celda import Celda
from FncP import FuncionesP
from FncS import FuncionesS
import sys
class Mision:
    def __init__(self,filas,columnas,mapa,militares,robot):
        self.fncP = FuncionesP()
        self.fncS = FuncionesS()
        self.caminosT = 0
        self.filas = filas
        self.columnas = columnas
        self.mapa = self.fncP.clonarVctr(mapa)
        self.militares = militares
        self.robot = robot
    
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
    
    def generarPlanoExtraccion(self):
        self.transitables = LstVctr()
        self.transitables.insert(ValorVctr(0,' '))
        self.transitables.insert(ValorVctr(1,'E'))
        self.transitables.insert(ValorVctr(2,'C'))
        self.transitables.insert(ValorVctr(3,'M'))
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
        sys.setrecursionlimit(20000)
        self.ordenarEntradas(x1,y1)
        for i in range(self.entradas.getSize()):
            try:
                camino = LstVctr()
                clonCiudad = self.fncP.clonarMtrz(self.ciudad)
                tmpCiudad = Ciudad(self.marcarDestino(clonCiudad,x1,y1,'Rescate'))
                camino.insert(ValorVctr(0,clonCiudad.get(self.entradas.get(i).valor.getI(),self.entradas.get(i).valor.getJ())))
                self.encontrarCaminosR(tmpCiudad,clonCiudad.get(self.entradas.get(i).valor.getI(),self.entradas.get(i).valor.getJ()),camino,1)
                camino = tmpCiudad.getCamino()
                clonCiudad = self.getMision(clonCiudad,camino,'P','Rescate')
                Limpiar().limpiarConsola()
                print('\nÚltima Misión: Misión Completada')
                print('Tipo de Misión: Rescate')
                print('Unidad Civil Rescatada: {},{}'.format(x1 + 1,y1 + 1))
                print('Robot Utilizado: {} (ChapinRescue)'.format(self.robot.nombre))
                self.fncP.printCiudad(clonCiudad)
                return
            except:
                pass
        Limpiar().limpiarConsola()
        print('\nÚltima Misión De Rescate\nMisión Imposible')
    
    def iniciarExtraccion(self,x1,y1):
        sys.setrecursionlimit(20000)
        self.ordenarEntradas(x1,y1)
        capIni = self.robot.capacidad
        self.capFin = capIni
        for i in range(self.entradas.getSize()):
            try:
                camino = LstVctr()
                clonCiudad = self.fncP.clonarMtrz(self.ciudad)
                tmpCiudad = Ciudad(self.marcarDestino(clonCiudad,x1,y1,'Extraccion'))
                camino.insert(ValorVctr(0,clonCiudad.get(self.entradas.get(i).valor.getI(),self.entradas.get(i).valor.getJ())))
                self.encontrarCaminosE(tmpCiudad,clonCiudad.get(self.entradas.get(i).valor.getI(),self.entradas.get(i).valor.getJ()),camino,capIni,1)
                camino = tmpCiudad.getCamino()
                clonCiudad = self.getMision(clonCiudad,camino,'P','Extraccion')
                Limpiar().limpiarConsola()
                print('\nÚltima Misión: Misión Completada')
                print('Tipo de Misión: Extracción de Recursos')
                print('Unidad Civil Rescatada: {},{}'.format(x1 + 1,y1 + 1))
                print('Robot Utilizado: {} (ChapinFighter)'.format(self.robot.nombre))
                print('\tCapacidad de Combate Inicial:',capIni)
                print('\tCapacidad de Combate Final:',self.capFin)
                self.fncP.printCiudad(clonCiudad)
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
                else:
                    u = False;r = False;d = False;l = False
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
    
    def ordenarEntradas(self,x1,y1):
        for i in range(self.entradas.getSize() - 1):
            for x in range(self.entradas.getSize() - i - 1):
                actual = self.entradas.get(x).valor
                actual = abs(x1 - actual.getI()) + abs(y1 - actual.getJ())
                siguiente = self.entradas.get(x + 1).valor
                siguiente = abs(x1 - siguiente.getI()) + abs(y1 - siguiente.getJ())
                if actual > siguiente:
                    self.entradas.change(x,x + 1)
    
    def marcarDestino(self,ciudad,x,y,mision):
        ciudad.get(x,y).setFin(True)
        if mision == 'Extraccion':
            if self.dentroDelLimite(ciudad,x - 1,y):
                if self.esTransitable(ciudad.get(x - 1,y).getCaracter()):
                    ciudad.get(x,y).paso.get(0).valor = True
                    ciudad.get(x - 1,y).paso.get(2).valor = True
            if self.dentroDelLimite(ciudad,x + 1,y):
                if self.esTransitable(ciudad.get(x + 1,y).getCaracter()):
                    ciudad.get(x,y).paso.get(2).valor = True
                    ciudad.get(x + 1,y).paso.get(0).valor = True
            if self.dentroDelLimite(ciudad,x,y - 1):
                if self.esTransitable(ciudad.get(x,y - 1).getCaracter()):
                    ciudad.get(x,y).paso.get(3).valor = True
                    ciudad.get(x,y - 1).paso.get(1).valor = True
            if self.dentroDelLimite(ciudad,x,y + 1):
                if self.esTransitable(ciudad.get(x,y + 1).getCaracter()):
                    ciudad.get(x,y).paso.get(1).valor = True
                    ciudad.get(x,y + 1).paso.get(3).valor = True
        return ciudad
    
    def esTransitable(self,celda):
        for i in range(self.transitables.getSize()):
            if self.transitables.get(i).valor == celda:
                return True
        return False
    
    def dentroDelLimite(self,ciudad,x,y):
        return x >= 0 and x < ciudad.getF() and y >= 0 and y < ciudad.getC()
    
    def encontrarCaminosR(self,ciudad,celdaActual,camino,n):
        if self.caminosT > 250: return
        if celdaActual.isFin():
            ciudad.agregarCamino(self.fncP.clonarVctr(camino))
            self.caminosT += 1
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
                        self.encontrarCaminosR(ciudad,celdaDestino,camino,n + 1)
                        celdaActual.setVisitado(False)
                        camino.remove(n)
                elif i == 1:
                    if ciudad.derechaDisponible(celdaActual,celdaDestino):
                        camino.insert(ValorVctr(n,celdaDestino))
                        celdaActual.setVisitado(True)
                        self.encontrarCaminosR(ciudad,celdaDestino,camino,n + 1)
                        celdaActual.setVisitado(False)
                        camino.remove(n)
                elif i == 2:
                    if ciudad.abajoDisponible(celdaActual,celdaDestino):
                        camino.insert(ValorVctr(n,celdaDestino))
                        celdaActual.setVisitado(True)
                        self.encontrarCaminosR(ciudad,celdaDestino,camino,n + 1)
                        celdaActual.setVisitado(False)
                        camino.remove(n)
                elif i == 3:
                    if ciudad.izquierdaDisponible(celdaActual,celdaDestino):
                        camino.insert(ValorVctr(n,celdaDestino))
                        celdaActual.setVisitado(True)
                        self.encontrarCaminosR(ciudad,celdaDestino,camino,n + 1)
                        celdaActual.setVisitado(False)
                        camino.remove(n)
    
    def encontrarCaminosE(self,ciudad,celdaActual,camino,capacidad,n):
        if self.caminosT > 250: return
        if celdaActual.isFin() and capacidad > 0:
            ciudad.agregarCamino(self.fncP.clonarVctr(camino))
            self.caminosT += 1
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
                    if ciudad.arribaDisponible(celdaActual,celdaDestino) and capacidad > 0:
                        camino.insert(ValorVctr(n,celdaDestino))
                        celdaActual.setVisitado(True)
                        if celdaDestino.getCaracter() == 'M':
                            self.encontrarCaminosE(ciudad,celdaDestino,camino,capacidad - self.getCapacidadMilitar(celdaDestino.getI(),celdaDestino.getJ()),n + 1)
                        else:
                            self.encontrarCaminosE(ciudad,celdaDestino,camino,capacidad,n + 1)
                        celdaActual.setVisitado(False)
                        camino.remove(n)
                elif i == 1:
                    if ciudad.derechaDisponible(celdaActual,celdaDestino) and capacidad > 0:
                        camino.insert(ValorVctr(n,celdaDestino))
                        celdaActual.setVisitado(True)
                        if celdaDestino.getCaracter() == 'M':
                            self.encontrarCaminosE(ciudad,celdaDestino,camino,capacidad - self.getCapacidadMilitar(celdaDestino.getI(),celdaDestino.getJ()),n + 1)
                        else:
                            self.encontrarCaminosE(ciudad,celdaDestino,camino,capacidad,n + 1)
                        celdaActual.setVisitado(False)
                        camino.remove(n)
                elif i == 2:
                    if ciudad.abajoDisponible(celdaActual,celdaDestino) and capacidad > 0:
                        camino.insert(ValorVctr(n,celdaDestino))
                        celdaActual.setVisitado(True)
                        if celdaDestino.getCaracter() == 'M':
                            self.encontrarCaminosE(ciudad,celdaDestino,camino,capacidad - self.getCapacidadMilitar(celdaDestino.getI(),celdaDestino.getJ()),n + 1)
                        else:
                            self.encontrarCaminosE(ciudad,celdaDestino,camino,capacidad,n + 1)
                        celdaActual.setVisitado(False)
                        camino.remove(n)
                elif i == 3:
                    if ciudad.izquierdaDisponible(celdaActual,celdaDestino) and capacidad > 0:
                        camino.insert(ValorVctr(n,celdaDestino))
                        celdaActual.setVisitado(True)
                        if celdaDestino.getCaracter() == 'M':
                            self.encontrarCaminosE(ciudad,celdaDestino,camino,capacidad - self.getCapacidadMilitar(celdaDestino.getI(),celdaDestino.getJ()),n + 1)
                        else:
                            self.encontrarCaminosE(ciudad,celdaDestino,camino,capacidad,n + 1)
                        celdaActual.setVisitado(False)
                        camino.remove(n)
    
    def getMision(self,ciudad,camino,caracter,mision):
        for i in range(camino.getSize()):
            cmn = camino.get(i).valor
            celda = ciudad.get(cmn.getI(),cmn.getJ())
            if celda.getCaracter() == ' ':
                celda.setCaracter(caracter)
                celda.setVisitado(True)
            if mision == 'Extraccion':
                if celda.getCaracter() == 'M':
                    self.capFin -= self.getCapacidadMilitar(celda.getI(),celda.getJ())
                    celda.setVisitado(True)
        return ciudad
    
    def getCapacidadMilitar(self,x,y):
        for i in range(self.militares.getSize()):
            militar = self.militares.get(i)
            if militar.fila == x and militar.columna == y:
                return militar.capacidad
        return 0