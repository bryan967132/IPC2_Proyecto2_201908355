from Limpiar import Limpiar
from ParseXML import ParseXML
from FuncionesS import FuncionesS
class Menu:
    def principal(self):
        pXML = ParseXML()
        limpiar = Limpiar()
        limpiar.limpiarConsola()
        funS = FuncionesS()
        listaCiudades = None
        listaRobotsR = None
        listaRobotsF = None
        opcion = 0
        while opcion != 5:
            try:
                self.opciones()
                opcion = int(input('Opción: '))
                if opcion == 1:
                    try:
                        archivo = input('\nIngrese la ruta del archivo: ')
                        listaCiudades = pXML.getCiudades(archivo)
                        listaRobotsR = pXML.getChapinRescue(archivo)
                        listaRobotsF = pXML.getChapinFighter(archivo)
                        limpiar.limpiarConsola()
                        print('\nConfiguraciones cargadas')
                    except:
                        limpiar.limpiarConsola()
                        print('\nHa ocurrido un error al cargar el archivo')
                elif opcion == 2:
                    limpiar.limpiarConsola()
                    if listaCiudades and listaRobotsR and listaRobotsF:
                        pass
                    else:
                        print('\nNo se han cargado configuraciones')
                elif opcion == 3:
                    limpiar.limpiarConsola()
                    if listaCiudades and listaRobotsR and listaRobotsF:
                        pass
                    else:
                        print('\nNo se han cargado configuraciones')
                elif opcion == 4:
                    if listaCiudades and listaRobotsR and listaRobotsF:
                        indice = listaCiudades.search(input('\nIngrese el Nombre de la Ciudad: '))
                        limpiar.limpiarConsola()
                        if indice != - 1:
                            ciudad = listaCiudades.get(indice)
                            funS.printVctr(ciudad)
                        else:
                            print('\nLa ciudad no se encuentra registrada')
                    else:
                        print('\nNo se han cargado configuraciones')
                elif opcion == 5:
                    print('\n¡Finalizado!')
                else:
                    limpiar.limpiarConsola()
                    print('\nSolo números entre 1 y 4')
            except:
                limpiar.limpiarConsola()
                print('\nOpción Inválida')

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