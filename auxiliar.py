from ParseXML import ParseXML
from FncS import FuncionesS
from FncP import FuncionesP
from Mision import Mision

funP = FuncionesP()
funS = FuncionesS()
pXML = ParseXML()
archivo = 'ciudades.xml'
listaCiudades = pXML.getCiudades(archivo)
listaRobots = pXML.getChapinRobots(archivo)

#print(funS.contarRobots(listaRobots,'ChapinRescue'))
#print(funS.contarRobots(listaRobots,'ChapinFighter'))

#for i in range(listaCiudades.getSize()):
#    ciudad = listaCiudades.get(i)
#    funS.printCiudad(ciudad)
#    print('Unidades Militares')
#    militares = ciudad.uMilitar
#    for x in range(militares.getSize()):
#        militar = militares.get(x)
#        print("Capacidad: {:<4} Posicion: ({},{})".format(militar.capacidad,militar.fila,militar.columna))
#print('\nRobots')
#for i in range(listaRobots.getSize()):
#    robot = listaRobots.get(i)
#    print("Nombre: {:<15} Tipo: {:<15} Capacidad: {}".format(robot.nombre,robot.tipo,robot.capacidad))

funS.verRobots(listaRobots,'ChapinRescue')
funS.verRobots(listaRobots,'ChapinFighter')

ciudad = listaCiudades.get(listaCiudades.search('CiudadGotica'))
rescue = listaRobots.get(listaRobots.search('Ironman'))
rescate1 = Mision(ciudad.filas,ciudad.columnas,ciudad.mapa,ciudad.uMilitar,rescue)
rescate1.generarPlanoRescate()
rescate1.iniciarRescate(13,18)

rescate2 = Mision(ciudad.filas,ciudad.columnas,ciudad.mapa,ciudad.uMilitar,rescue)
rescate2.generarPlanoRescate()
rescate2.iniciarRescate(2,15)

ciudad = listaCiudades.get(listaCiudades.search('CiudadGotica'))
fight = listaRobots.get(listaRobots.search('Robocop'))
extraccion1 = Mision(ciudad.filas,ciudad.columnas,ciudad.mapa,ciudad.uMilitar,fight)
extraccion1.generarPlanoExtraccion()
extraccion1.iniciarExtraccion(6,18)

extraccion2 = Mision(ciudad.filas,ciudad.columnas,ciudad.mapa,ciudad.uMilitar,fight)
extraccion2.generarPlanoExtraccion()
extraccion2.iniciarExtraccion(3,19)