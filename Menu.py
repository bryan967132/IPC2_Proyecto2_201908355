from Limpiar import Limpiar
from ParseXML import ParseXML
from FncP import FuncionesP
from FncS import FuncionesS
from Mision import Mision
class Menu:
    def principal(self):
        pXML = ParseXML()
        limpiar = Limpiar()
        limpiar.limpiarConsola()
        funP = FuncionesP()
        funS = FuncionesS()
        listaCiudades = None
        listaRobots = None
        opcion = 0
        while opcion != 5:
            #try:
                self.opciones()
                opcion = int(input('Opción: '))
                if opcion == 1:
                    try:
                        archivo = input('\nIngrese la ruta del archivo: ')
                        listaCiudades = pXML.getCiudades(archivo)
                        listaRobots = pXML.getChapinRobots(archivo)
                        limpiar.limpiarConsola()
                        print('\nConfiguraciones cargadas')
                    except:
                        limpiar.limpiarConsola()
                        print('\nHa ocurrido un error al cargar el archivo')
                elif opcion == 2:
                    limpiar.limpiarConsola()
                    if listaCiudades and listaRobots:
                        if listaRobots.getSize() > 0:
                            if funS.hayObjetivos(listaCiudades,'C'):
                                funS.ciudadesObjetivos(listaCiudades,'C')
                                while True:
                                    indice = listaCiudades.search(input('\nIngrese el Nombre de la Ciudad: '))
                                    if indice != - 1:
                                        break
                                ciudad = listaCiudades.get(indice)
                                mision = Mision(ciudad.filas,ciudad.columnas,ciudad.mapa,ciudad.uMilitar)
                                mision.generarPlanoRescate()
                                uCiviles = funS.contarObjetivos(ciudad.mapa,'C')
                                if uCiviles > 1:
                                    pares = funS.verObjetivos(ciudad.filas,ciudad.columnas,ciudad.mapa,'C',uCiviles)
                                    while True:
                                        try:
                                            parC = int(input('\nIngrese el número del objetivo: '))
                                            if parC >= 1 and parC <= pares.getF():
                                                mision.iniciarRescate(pares.get(parC - 1,0).valor,pares.get(parC - 1,1).valor)
                                                break
                                        except:
                                            pass
                                else:
                                    par = funS.unicoObjetivo(ciudad.filas,ciudad.columnas,ciudad.mapa,'C')
                                    mision.iniciarRescate(par.get(0).valor,par.get(1).valor)
                            else:
                                print('\nTodas las ciudades están despejadas de civiles')
                        else:
                            print('\nNo hay robots ChapinRescue disponibles')
                    else:
                        print('\nNo se han cargado configuraciones')
                elif opcion == 3:
                    limpiar.limpiarConsola()
                    if listaCiudades and listaRobots:
                        pass
                    else:
                        print('\nNo se han cargado configuraciones')
                elif opcion == 4:
                    if listaCiudades and listaRobots:
                        indice = listaCiudades.search(input('\nIngrese el Nombre de la Ciudad: '))
                        limpiar.limpiarConsola()
                        if indice != - 1:
                            ciudad = listaCiudades.get(indice)
                            funS.printCiudad(ciudad)
                        else:
                            print('\nLa ciudad no se encuentra registrada')
                    else:
                        print('\nNo se han cargado configuraciones')
                elif opcion == 5:
                    print('\n¡Finalizado!')
                else:
                    limpiar.limpiarConsola()
                    print('\nSolo números entre 1 y 4')
            #except:
            #    limpiar.limpiarConsola()
            #    print('\nOpción Inválida')

    def opciones(self):
        print("""
╔══════════════════════════════════════════════════════╗
║                                                      ║
║                    Menú Principal                    ║
║                                                      ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║           1. Cargar Configuraciones                  ║
║           2. Realizar Misión de Rescate              ║
║           3. Realizar Misión de Extracción           ║
║           4. Ver Ciudad                              ║
║           5. Salir                                   ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
""")