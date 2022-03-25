class FuncionesS:
    def printVctr(self,ciudad):
        mapa = ciudad.mapa
        cadenaM = ''
        c = 0
        print("\n{}".format(ciudad.nombre))
        for x in range(ciudad.filas):
            for y in range(ciudad.columnas):
                celda = mapa.get(c).valor
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
                c += 1
            if x < ciudad.filas - 1:
                cadenaM += '\n'
        print(cadenaM)