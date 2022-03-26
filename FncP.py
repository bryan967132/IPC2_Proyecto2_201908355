from Lista import LstVctr,LstMtrz
class FuncionesP:
    def clonarMtrz(self,matriz):
        clon = LstMtrz(matriz.getF(),matriz.getC())
        for i in range(matriz.getF()):
            for j in range(matriz.getC()):
                clon.insert(matriz.get(i,j))
        return clon
    
    def clonarVctr(self,vector):
        clon = LstVctr()
        for i in range(vector.getSize()):
            clon.insert(vector.get(i))
        return clon
    
    def ubicarM(self,matriz,militares):
        for i in range(militares.getSize()):
            militar = militares.get(i)
            matriz.get(militar.fila,militar.columna).valor = 'M'
        return matriz
    
    def printCiudad(self,ciudad):
        cadena = ''
        for i in range(ciudad.getF()):
            for j in range(ciudad.getC()):
                celda = ciudad.get(i,j).getCaracter()
                if celda == ' ':
                    cadena += ' · '
                elif celda == '*':
                    cadena += '▒▒▒'
                elif celda == 'E':
                    cadena += ' E '
                elif celda == 'R':
                    cadena += ' R '
                elif celda == 'C':
                    cadena += ' C '
                elif celda == 'M':
                    cadena += ' M '
                elif celda == 'P':
                    cadena += ' P '
            if i < ciudad.getF() - 1:
                cadena += '\n'
        print(cadena)
    
    def printTablero(self,tablero):
        cadena = ''
        for i in range(tablero.getF()):
            for j in range(tablero.getC()):
                if not tablero.get(i,j).arribaDisponible():
                    cadena += ' ═════ '
                else:
                    cadena += '       '
            cadena += '\n'
            for j in range(tablero.getC()):
                if not tablero.get(i,j).izquierdaDisponible():
                    cadena += '║'
                else:
                    cadena += ' '
                cadena += '  ' + tablero.get(i,j).getCaracter() + '  '
                if not tablero.get(i,j).derechaDisponible():
                    cadena += '║'
                else:
                    cadena += ' '
            cadena += '\n'
            for j in range(tablero.getC()):
                if not tablero.get(i,j).abajoDisponible():
                    cadena += ' ═════ '
                else:
                    cadena += '       '
            cadena += '\n'
        print(cadena)

    def printPuntos(self,titulo,lista):
        print(titulo)
        for i in range(lista.getSize()):
            punto = lista.get(i).valor
            print(punto.i,',',punto.j)