from ParseXML import ParseXML
from FncS import FuncionesS
from FncP import FuncionesP

fncS = FuncionesS()
fncP = FuncionesP()
pXML = ParseXML()
archivo = 'ciudades.xml'
listaCiudades = pXML.getCiudades(archivo)
listaRobotsR = pXML.getChapinRescue(archivo)
listaRobotsF = pXML.getChapinFighter(archivo)

for i in range(listaCiudades.getL()):
    ciudad = listaCiudades.get(i)
    mapa = fncP.clonarVctr(ciudad.mapa)
    fncS.printVctr(ciudad)
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