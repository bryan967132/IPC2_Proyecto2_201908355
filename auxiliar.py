from ParseXML import ParseXML

pXML = ParseXML()
archivo = 'ciudades.xml'
listaCiudades = pXML.getCiudades(archivo)
listaRobotsR = pXML.getChapinRescue(archivo)
listaRobotsF = pXML.getChapinFighter(archivo)

for i in range(listaCiudades.getL()):
    print()
    ciudad = listaCiudades.get(i)
    print(ciudad.nombre)
    mapa = ciudad.mapa
    cadenaM = ''
    contadorP = 0
    for x in range(ciudad.filas):
        for y in range(ciudad.columnas):
            celda = mapa.get(contadorP).valor
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
            contadorP += 1
        if x < ciudad.filas - 1:
            cadenaM += '\n'
    print(cadenaM)
    print('Unidades Militares')
    militares = ciudad.uMilitar
    for x in range(militares.getL()):
        militar = militares.get(x)
        print("Capacidad: {:<4} Posicion: ({},{})".format(militar.capacidad,militar.fila,militar.columna))
for i in range(listaRobotsR.getL()):
    robot = listaRobotsR.get(i)
    print("Nombre: {}".format(robot.nombre))
for i in range(listaRobotsF.getL()):
    robot = listaRobotsF.get(i)
    print("Nombre: {:<15} Capacidad: {:<5}".format(robot.nombre,robot.capacidad))