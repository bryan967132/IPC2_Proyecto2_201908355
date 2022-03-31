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
        funS = FuncionesS()
        listaCiudades = None
        listaRobots = None
        opcion = 0
        while opcion != 5:
            try:
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
                        cantRobots = funS.contarRobots(listaRobots,'ChapinRescue')
                        if cantRobots > 0:
                            if funS.hayObjetivos(listaCiudades,'C'):
                                if cantRobots > 1:
                                    funS.verRobots(listaRobots,'ChapinRescue')
                                    while True:
                                        indice = listaRobots.search(input('Ingrese el Nombre del ChapinRescue: '))
                                        if indice != - 1:
                                            rescue = listaRobots.get(indice)
                                            if rescue.tipo == 'ChapinRescue':
                                                break
                                else:
                                    rescue = funS.unicoRobot(listaRobots,'ChapinRescue')
                                limpiar.limpiarConsola()
                                print('\nChapinRescue Enviado: {}'.format(rescue.nombre))
                                funS.ciudadesObjetivos(listaCiudades,'C')
                                while True:
                                    indice = listaCiudades.search(input('Ingrese el Nombre de la Ciudad: '))
                                    if indice != - 1:
                                        ciudad = listaCiudades.get(indice)
                                        if funS.contarObjetivos(ciudad.mapa,'C') > 0:
                                            break
                                mision = Mision(ciudad.filas,ciudad.columnas,ciudad.mapa,ciudad.uMilitar,rescue)
                                mision.generarPlanoRescate()
                                uCiviles = funS.contarObjetivos(ciudad.mapa,'C')
                                limpiar.limpiarConsola()
                                if uCiviles > 1:
                                    funS.printCiudad(ciudad)
                                    pares = funS.verObjetivos(ciudad.filas,ciudad.columnas,ciudad.mapa,'C',uCiviles)
                                    while True:
                                        try:
                                            parC = int(input('Ingrese el número del objetivo: '))
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
                        cantRobots = funS.contarRobots(listaRobots,'ChapinFighter')
                        if cantRobots > 0:
                            if funS.hayObjetivos(listaCiudades,'R'):
                                if cantRobots > 1:
                                    funS.verRobots(listaRobots,'ChapinFighter')
                                    while True:
                                        indice = listaRobots.search(input('Ingrese el Nombre del ChapinFighter: '))
                                        if indice != - 1:
                                            fighter = listaRobots.get(indice)
                                            if fighter.tipo == 'ChapinFighter':
                                                break
                                else:
                                    fighter = funS.unicoRobot(listaRobots,'ChapinRescue')
                                limpiar.limpiarConsola()
                                print('\nChapinFighter Enviado: {}'.format(fighter.nombre))
                                funS.ciudadesObjetivos(listaCiudades,'R')
                                while True:
                                    indice = listaCiudades.search(input('Ingrese el Nombre de la Ciudad: '))
                                    if indice != - 1:
                                        ciudad = listaCiudades.get(indice)
                                        if funS.contarObjetivos(ciudad.mapa,'R') > 0:
                                            break
                                mision = Mision(ciudad.filas,ciudad.columnas,ciudad.mapa,ciudad.uMilitar,fighter)
                                mision.generarPlanoExtraccion()
                                uRecursos = funS.contarObjetivos(ciudad.mapa,'R')
                                limpiar.limpiarConsola()
                                if uRecursos > 1:
                                    funS.printCiudad(ciudad)
                                    pares = funS.verObjetivos(ciudad.filas,ciudad.columnas,ciudad.mapa,'R',uRecursos)
                                    while True:
                                        try:
                                            parR = int(input('Ingrese el número del objetivo: '))
                                            if parR >= 1 and parR <= pares.getF():
                                                mision.iniciarExtraccion(pares.get(parR - 1,0).valor,pares.get(parR - 1,1).valor)
                                                break
                                        except:
                                            pass
                                else:
                                    par = funS.unicoObjetivo(ciudad.filas,ciudad.columnas,ciudad.mapa,'R')
                                    mision.iniciarExtraccion(par.get(0).valor,par.get(1).valor)
                            else:
                                print('\nTodas las ciudades están despejadas de recursos')
                        else:
                            print('\nNo hay robots ChapinFighter disponibles')
                    else:
                        print('\nNo se han cargado configuraciones')
                elif opcion == 4:
                    if listaCiudades and listaRobots:
                        indice = listaCiudades.search(input('\nIngrese el Nombre de la Ciudad: '))
                        if indice != - 1:
                            ciudad = listaCiudades.get(indice)
                            limpiar.limpiarConsola()
                            funS.exportCiudad(ciudad)
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