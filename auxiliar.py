from ParseXML import ParseXML
from FncS import FuncionesS

fncS = FuncionesS()
pXML = ParseXML()
archivo = 'ciudades.xml'
listaCiudades = pXML.getCiudades(archivo)
listaRobotsR = pXML.getChapinRescue(archivo)
listaRobotsF = pXML.getChapinFighter(archivo)

for i in range(listaCiudades.getSize()):
    ciudad = listaCiudades.get(i)
    fncS.printCiudad(ciudad)
    print('Unidades Militares')
    militares = ciudad.uMilitar
    for x in range(militares.getSize()):
        militar = militares.get(x)
        print("Capacidad: {:<4} Posicion: ({},{})".format(militar.capacidad,militar.fila,militar.columna))
for i in range(listaRobotsR.getSize()):
    robot = listaRobotsR.get(i)
    print("Nombre: {}".format(robot.nombre))
for i in range(listaRobotsF.getSize()):
    robot = listaRobotsF.get(i)
    print("Nombre: {:<15} Capacidad: {:<5}".format(robot.nombre,robot.capacidad))