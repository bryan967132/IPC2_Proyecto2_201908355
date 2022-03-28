from xml.dom import minidom
from Constructores import NCiudad,ValorVctr,UMilitar,Robot
from Lista import LstVctr
class ParseXML:
    def __init__(self):
        self.listaCiudades = LstVctr()
        self.listaRobots = LstVctr()
        self.contadorP = 0
        self.contadorR = 0

    def getCiudades(self,ruta):
        myDoc = minidom.parse(ruta)
        ciudades = myDoc.getElementsByTagName('ciudad')
        for ciudad in ciudades:
            etiqNom = ciudad.getElementsByTagName('nombre')
            for elemento in etiqNom:
                nombre = elemento.firstChild.data.strip()
                filas = int(elemento.attributes['filas'].value)
                columnas = int(elemento.attributes['columnas'].value)
            listaCaracteres = LstVctr()
            contador1 = 0
            for fila in ciudad.getElementsByTagName('fila'):
                for columna in fila.firstChild.data.replace('"',''):
                    listaCaracteres.insert(ValorVctr(contador1,columna))
                    contador1 += 1
            listaMilitares = LstVctr()
            contador1 = 0
            for unidadM in ciudad.getElementsByTagName('unidadMilitar'):
                capacidad = int(unidadM.firstChild.data)
                posX = int(unidadM.attributes['columna'].value) - 1
                posY = int(unidadM.attributes['fila'].value) - 1
                listaMilitares.insert(UMilitar(contador1,posY,posX,capacidad))
                contador1 += 1
            indice = self.listaCiudades.search(nombre)
            if indice != - 1:
                self.listaCiudades.replace(NCiudad(indice,filas,columnas,nombre,listaCaracteres,listaMilitares))
            else:
                self.listaCiudades.insert(NCiudad(self.contadorP,filas,columnas,nombre,listaCaracteres,listaMilitares))
                self.contadorP += 1
        return self.listaCiudades

    def getChapinRobots(self,ruta):
        myDoc = minidom.parse(ruta)
        robots = myDoc.getElementsByTagName('robot')
        for robot in robots:
            nomR = robot.getElementsByTagName('nombre')
            for elemento in nomR:
                nombre = elemento.firstChild.data.strip()
                tipo = elemento.attributes['tipo'].value
                indice = self.listaRobots.search(nombre)
                capacidad = 0
                if tipo == 'ChapinFighter':
                    capacidad = int(elemento.attributes['capacidad'].value)
                if indice != -1:
                    self.listaRobots.replace(Robot(indice,nombre,tipo,capacidad))
                else:
                    self.listaRobots.insert(Robot(self.contadorR,nombre,tipo,capacidad))
                    self.contadorR += 1
        return self.listaRobots