from ParseXML import ParseXML
from FncS import FuncionesS
from FncP import FuncionesP
from Mision import Mision

funP = FuncionesP()
funS = FuncionesS()
pXML = ParseXML()
archivo = 'entrada.xml'
listaCiudades = pXML.getCiudades(archivo)
listaRobots = pXML.getChapinRobots(archivo)

print(funS.contarRescues(listaRobots,'ChapinRescue'))

#for i in range(listaCiudades.getSize()):
#    ciudad = listaCiudades.get(i)
#    fncS.printCiudad(ciudad)
#    print('Unidades Militares')
#    militares = ciudad.uMilitar
#    for x in range(militares.getSize()):
#        militar = militares.get(x)
#        print("Capacidad: {:<4} Posicion: ({},{})".format(militar.capacidad,militar.fila,militar.columna))
#print('\nRobots')
#for i in range(listaRobots.getSize()):
#    robot = listaRobots.get(i)
#    print("Nombre: {:<15} Tipo: {:<15} Capacidad: {}".format(robot.nombre,robot.tipo,robot.capacidad))

#if fncS.hayObjetivos(listaCiudades,'C'):
#    fncS.ciudadesObjetivos(listaCiudades,'C')
#    ciudad = listaCiudades.get(listaCiudades.search('CiudadGuate'))
#    fncS.printCiudad(ciudad)
#    mision = Mision(ciudad.filas,ciudad.columnas,ciudad.mapa,ciudad.uMilitar)
#    mision.generarPlanoRescate()
#    uCiviles = fncS.contarObjetivos(ciudad.mapa,'C')
#    if uCiviles > 1:
#        pares = fncS.verObjetivos(ciudad.filas,ciudad.columnas,ciudad.mapa,'C',uCiviles)
#        mision.iniciarRescate(pares.get(1,0).valor,pares.get(1,1).valor)
#    else:
#        par = fncS.unicoObjetivo(ciudad.filas,ciudad.columnas,ciudad.mapa,'C')
#        mision.iniciarRescate(par.get(0).valor,par.get(1).valor)

#fncS.verRescues(listaRobots,'ChapinRescue')
#fncS.verRescues(listaRobots,'ChapinFighter')