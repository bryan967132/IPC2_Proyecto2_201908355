from Lista import LstMtrz,LstVctr
from FncP import FuncionesP
from Constructores import ValorMtrz,ValorVctr
class FuncionesS:
    def lstVctrToMtrz(self,filas,columnas,vector):
        matriz = LstMtrz(filas,columnas)
        c = 0
        for i in range(matriz.getF()):
            for j in range(matriz.getC()):
                matriz.insert(ValorMtrz(i,j,vector.get(c).valor))
                c += 1
        return matriz
    
    def lstMtrzToVctr(self,matriz):
        vector = LstVctr()
        c = 0
        for i in range(matriz.getF()):
            for j in range(matriz.getC()):
                vector.insert(ValorVctr(c,matriz.get(i,j).valor))
                c += 1
        return vector

    def printCiudad(self,ciudad):
        fncP = FuncionesP()
        mapa = fncP.ubicarM(self.lstVctrToMtrz(ciudad.filas,ciudad.columnas,fncP.clonarVctr(ciudad.mapa)),ciudad.uMilitar)
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
    
    def printVisitados(self,matriz):
        cadenaM = ''
        for i in range(matriz.getF()):
            for j in range(matriz.getC()):
                if matriz.get(i,j).isVisitado():
                    cadenaM += 'true  '
                else:
                    cadenaM += 'false '
            if i < matriz.getF() - 1:
                cadenaM += '\n'
        print(cadenaM)
    
    def printPuntos(self,titulo,lista):
        print(titulo)
        for i in range(lista.getSize()):
            punto = lista.get(i).valor
            print(punto.getI(),',',punto.getJ())

    def printPuntosM(self,lista):
        print('Militares')
        for i in range(lista.getSize()):
            punto = lista.get(i)
            print(punto.fila,',',punto.columna,'Capacidad:',punto.capacidad)
    
    def verRobots(self,listaRobots,tipo):
        print('\n{} Disponibles'.format(tipo))
        for i in range(listaRobots.getSize()):
            robot = listaRobots.get(i)
            if robot.tipo == tipo:
                nrob = '- Nombre: {:<15}'.format(robot.nombre)
                if robot.capacidad > 0:
                    nrob += ' Capacidad: {}'.format(robot.capacidad)
                print(nrob)
        print()
    
    def contarRobots(self,listaRobots,tipo):
        contador = 0
        for i in range(listaRobots.getSize()):
            if listaRobots.get(i).tipo == tipo:
                contador += 1
        return contador
    
    def unicoRobot(self,listaRobots,tipo):
        for i in range(listaRobots.getSize()):
            if listaRobots.get(i).tipo == tipo:
                return listaRobots.get(i)

    def hayObjetivos(self,listaCiudades,objetivo):
        for i in range(listaCiudades.getSize()):
            ciudad = listaCiudades.get(i).mapa
            for x in range(ciudad.getSize()):
                if ciudad.get(x).valor == objetivo:
                    return True
        return False
    
    def ciudadesObjetivos(self,listaCiudades,objetivo):
        print()
        if objetivo == 'C':
            print('Ciudades con Civiles')
        elif objetivo == 'R':
            print('Ciudades con Recursos')
        for i in range(listaCiudades.getSize()):
            ciudad = listaCiudades.get(i)
            for x in range(ciudad.mapa.getSize()):
                if ciudad.mapa.get(x).valor == objetivo:
                    print(' -',ciudad.nombre)
                    break
        print()

    def contarObjetivos(self,mapa,objetivo):
        contador = 0
        for i in range(mapa.getSize()):
            if mapa.get(i).valor == objetivo:
                contador += 1
        return contador
    
    def verObjetivos(self,filas,columnas,mapa,objetivo,cantidad):
        pares = LstMtrz(cantidad,2)
        c = 0
        par = 0
        if objetivo == 'C':
            print('\nPosibles Objetivos Civiles')
        elif objetivo == 'R':
            print('\nPosibles Recursos Extraibles')
        for i in range(filas):
            for j in range(columnas):
                if mapa.get(c).valor == objetivo:
                    print('{:<4} Fila: {:<4} Columna: {:<4}'.format(str(par + 1) + ')',i + 1,j + 1))
                    pares.insert(ValorMtrz(par,0,i))
                    pares.insert(ValorMtrz(par,1,j))
                    par += 1
                c += 1
        print()
        return pares
    
    def unicoObjetivo(self,filas,columnas,mapa,objetivo):
        parCoord = LstVctr()
        c = 0
        for i in range(filas):
            for j in range(columnas):
                if mapa.get(c).valor == objetivo:
                    parCoord.insert(ValorVctr(0,i))
                    parCoord.insert(ValorVctr(1,j))
                    return parCoord
                c += 1