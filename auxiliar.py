from ParseXML import ParseXML
from FncS import FuncionesS
from FncP import FuncionesP
from Mision import Mision

fncP = FuncionesP()
fncS = FuncionesS()
pXML = ParseXML()
archivo = 'ciudades.xml'
listaCiudades = pXML.getCiudades(archivo)
listaRobotsR = pXML.getChapinRescue(archivo)
listaRobotsF = pXML.getChapinFighter(archivo)

ciudad = listaCiudades.get(listaCiudades.search('CiudadGotica'))
print(ciudad.nombre,'->',ciudad.filas,'x',ciudad.columnas)
mision = Mision(ciudad.filas,ciudad.columnas,ciudad.mapa,ciudad.uMilitar)
mision.generarPlanoRescate()
mision.iniciarRescate(13,18)

#for i in range(listaCiudades.getSize()):
#    ciudad = listaCiudades.get(i)
#    fncS.printCiudad(ciudad)
#    print('Unidades Militares')
#    militares = ciudad.uMilitar
#    for x in range(militares.getSize()):
#        militar = militares.get(x)
#        print("Capacidad: {:<4} Posicion: ({},{})".format(militar.capacidad,militar.fila,militar.columna))
#print('\nChapinRescue')
#for i in range(listaRobotsR.getSize()):
#    robot = listaRobotsR.get(i)
#    print("Nombre: {}".format(robot.nombre))
#print('\nChapinFighter')
#for i in range(listaRobotsF.getSize()):
#    robot = listaRobotsF.get(i)
#    print("Nombre: {:<15} Capacidad: {:<5}".format(robot.nombre,robot.capacidad))
#print()