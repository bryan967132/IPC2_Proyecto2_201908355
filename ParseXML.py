from xml.dom import minidom
from Constructores import NCiudad,ValorVctr,UMilitar,Robot
from Lista import LstVctr
class ParseXML:
    def __init__(self):
        self.listaCiudades = LstVctr()
        self.listaRobotsR = LstVctr()
        self.listaRobotsF = LstVctr()
        self.contadorP = 0
        self.contadorR = 0
        self.contadorF = 0

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
                vida = unidadM.firstChild.data.strip()
                posX = int(unidadM.attributes['columna'].value) - 1
                posY = int(unidadM.attributes['fila'].value) - 1
                listaMilitares.insert(UMilitar(contador1,posY,posX,vida))
                contador1 += 1
            indice = self.listaCiudades.search(nombre)
            if indice != - 1:
                self.listaCiudades.replace(NCiudad(indice,filas,columnas,nombre,listaCaracteres,listaMilitares))
            else:
                self.listaCiudades.insert(NCiudad(self.contadorP,filas,columnas,nombre,listaCaracteres,listaMilitares))
                self.contadorP += 1
        return self.listaCiudades

    def getChapinRescue(self,ruta):
        myDoc = minidom.parse(ruta)
        robots = myDoc.getElementsByTagName('robot')
        for robot in robots:
            nomR = robot.getElementsByTagName('nombre')
            for elemento in nomR:
                nombre = elemento.firstChild.data.strip()
                tipo = elemento.attributes['tipo'].value
                if tipo == 'ChapinRescue':
                    indice = self.listaRobotsR.search(nombre)
                    if indice != -1:
                        self.listaRobotsR.replace(Robot(indice,nombre,tipo))
                    else:
                        self.listaRobotsR.insert(Robot(self.contadorR,nombre,tipo))
                        self.contadorR += 1
        return self.listaRobotsR

    def getChapinFighter(self,ruta):
        myDoc = minidom.parse(ruta)
        robots = myDoc.getElementsByTagName('robot')
        for robot in robots:
            nomR = robot.getElementsByTagName('nombre')
            for elemento in nomR:
                nombre = elemento.firstChild.data.strip()
                tipo = elemento.attributes['tipo'].value
                if tipo == 'ChapinFighter':
                    capacidad = int(elemento.attributes['capacidad'].value)
                    indice = self.listaRobotsF.search(nombre)
                    if indice != -1:
                        self.listaRobotsF.replace(Robot(indice,nombre,tipo,capacidad))
                    else:
                        self.listaRobotsF.insert(Robot(self.contadorF,nombre,tipo,capacidad))
                        self.contadorF += 1
        return self.listaRobotsF