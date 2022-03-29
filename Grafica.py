import webbrowser
import os
class Grafica:
    def exportR(self,x,y,robot,ciudad):
        reporte = self.getHead()
        reporte += self.getMapa(ciudad)
        reporte += self.getTiposC()
        reporte += self.getResumenR(x,y,robot)
        reporte += self.getConeccionCT()
        reporte += self.getConeccionTR()
        reporte += self.getClose()
        with open('ArchivoMision/Rescate.txt','w') as rescate:
            rescate.write(reporte)
        os.system('dot -Tpdf ArchivoMision/Rescate.txt -o Rescate.pdf')
        print('Reporte de Misión Generado')
        webbrowser.open('Rescate.pdf')

    def exportE(self,x,y,robot,capIni,capFin,ciudad):
        reporte = self.getHead()
        reporte += self.getMapa(ciudad)
        reporte += self.getTiposC()
        reporte += self.getResumenE(x,y,robot,capIni,capFin)
        reporte += self.getConeccionCT()
        reporte += self.getConeccionTR()
        reporte += self.getClose()
        with open('ArchivoMision/Extraccion.txt','w') as extraccion:
            extraccion.write(reporte)
        os.system('dot -Tpdf ArchivoMision/Extraccion.txt -o Extraccion.pdf')
        print('Reporte de Misión Generado')
        webbrowser.open('Extraccion.pdf')

    def exportRF(self,x,y,robot,ciudad):
        reporte = self.getHead()
        reporte += self.getMapa(ciudad)
        reporte += self.getTiposC()
        reporte += self.getResumenRF(x,y,robot)
        reporte += self.getConeccionCT()
        reporte += self.getConeccionTR()
        reporte += self.getClose()
        with open('ArchivoMision/Imposible.txt','w') as rescate:
            rescate.write(reporte)
        os.system('dot -Tpdf ArchivoMision/Imposible.txt -o Imposible.pdf')
        print('Reporte de Misión Generado')
        webbrowser.open('Imposible.pdf')

    def exportEF(self,x,y,robot,ciudad):
        reporte = self.getHead()
        reporte += self.getMapa(ciudad)
        reporte += self.getTiposC()
        reporte += self.getResumenEF(x,y,robot)
        reporte += self.getConeccionCT()
        reporte += self.getConeccionTR()
        reporte += self.getClose()
        with open('ArchivoMision/Imposible.txt','w') as rescate:
            rescate.write(reporte)
        os.system('dot -Tpdf ArchivoMision/Imposible.txt -o Imposible.pdf')
        print('Reporte de Misión Generado')
        webbrowser.open('Imposible.pdf')

    def getHead(self):
        return """digraph {
    node [shape = none fontcolor="#000000" fontsize="35" fontname="Calibri"]"""

    def getClose(self):
        return '\n}'

    def getMapa(self,ciudad):
        ciudadS = """
    ciudad[
        label=<
            <table border="0" cellborder="1" cellspacing="0" cellpadding="0">"""
        ciudadS += """
                <tr>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75"></td>"""
        for j in range(ciudad.getC()):
            ciudadS += """
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75">""" + str(j + 1) + """</td>"""
        ciudadS += """
                </tr>"""
        for i in range(ciudad.getF()):
            ciudadS += """
                <tr>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75">""" + str(i + 1) + """</td>"""
            for j in range(ciudad.getC()):
                celda = ciudad.get(i,j)
                if celda.getCaracter() == '*':
                    ciudadS += """
                    <td color="#F2F2F2" bgcolor = "#000000" height = "64" width = "75"></td>"""
                elif celda.getCaracter() == ' ':
                    ciudadS += """
                    <td color="#F2F2F2" bgcolor = "#FFFFFF" height = "64" width = "75"></td>"""
                elif celda.getCaracter() == 'E':
                    ciudadS += """
                    <td color="#F2F2F2" bgcolor = "#70AD47" height = "64" width = "75"></td>"""
                elif celda.getCaracter() == 'C':
                    ciudadS += """
                    <td color="#F2F2F2" bgcolor = "#2F75B5" height = "64" width = "75"></td>"""
                elif celda.getCaracter() == 'R':
                    ciudadS += """
                    <td color="#F2F2F2" bgcolor = "#7B7B7B" height = "64" width = "75"></td>"""
                elif celda.getCaracter() == 'M':
                    if celda.isVisitado():
                        ciudadS += """
                    <td color="#FFC000" bgcolor = "#C00000" height = "64" width = "75"></td>"""
                    else:
                        ciudadS += """
                    <td color="#F2F2F2" bgcolor = "#C00000" height = "64" width = "75"></td>"""
                if celda.getCaracter() == 'P':
                    ciudadS += """
                    <td color="#F2F2F2" bgcolor = "#FFE699" height = "64" width = "75"></td>"""
            ciudadS += """
                </tr>"""
        ciudadS += """
            </table>
        >
    ];"""
        return ciudadS

    def getTiposC(self):
        return """
    tiposC[
        label=<
            <table border="0" cellborder="1" cellspacing="0" cellpadding="0">
                <tr>
                    <td color="#F2F2F2" bgcolor = "#000000" height = "64" width = "75"></td>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" width = "10"></td>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75" align="left">Intransitable</td>
                </tr>
                <tr>
                    <td color="#F2F2F2" bgcolor = "#70AD47" height = "64" width = "75"></td>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" width = "10"></td>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75" align="left">Punto de Entrada</td>
                </tr>
                <tr>
                    <td color="#F2F2F2" bgcolor = "#FFFFFF" height = "64" width = "75"></td>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" width = "10"></td>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75" align="left">Camino</td>
                </tr>
                <tr>
                    <td color="#F2F2F2" bgcolor = "#C00000" height = "64" width = "75"></td>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" width = "10"></td>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75" align="left">Unidad Militar</td>
                </tr>
                <tr>
                    <td color="#F2F2F2" bgcolor = "#2F75B5" height = "64" width = "75"></td>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" width = "10"></td>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75" align="left">Unidad Civil</td>
                </tr>
                <tr>
                    <td color="#F2F2F2" bgcolor = "#7B7B7B" height = "64" width = "75"></td>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" width = "10"></td>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75" align="left">Recurso</td>
                </tr>
            </table>
        >
    ]"""

    def getResumenR(self,x,y,robot):
        return """
    resumen[
        label=<
            <table border="0" cellborder="1" cellspacing="0" cellpadding="0">
                <tr>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75">Tipo de Mision: Rescate</td>
                </tr>
                <tr>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75">Unidad Civil Rescatada: """ + str(x) + """,""" + str(y) + """</td>
                </tr>
                <tr>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75">Robot Utilizado: """ + robot + """ (ChapinRescue)</td>
                </tr>
            </table>
        >
    ];"""

    def getResumenRF(self,x,y,robot):
        return """
    resumen[
        label=<
            <table border="0" cellborder="1" cellspacing="0" cellpadding="0">
                <tr>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75">Tipo de Mision: Rescate</td>
                </tr>
                <tr>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75">Unidad Civil Objetivo: """ + str(x) + """,""" + str(y) + """</td>
                </tr>
                <tr>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75">Robot Utilizado: """ + robot + """ (ChapinRescue)</td>
                </tr>
                <tr>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75">MISION IMPOSIBLE</td>
                </tr>
            </table>
        >
    ];"""

    def getResumenE(self,x,y,robot,capIni,capFin):
        return """
    resumen[
        label=<
            <table border="0" cellborder="1" cellspacing="0" cellpadding="0">
                <tr>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75">Tipo de Mision: Extraccion de Recursos</td>
                </tr>
                <tr>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75">Recurso Extraido: """ + str(x) + """,""" + str(y) + """</td>
                </tr>
                <tr>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75">Robot Utilizado: """ + robot + """ (ChapinFighter)</td>
                </tr>
                <tr>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75">Capacidad de Combate Inicial: """ + str(capIni) + """</td>
                </tr>
                <tr>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75">Capacidad de Combate Final: """ + str(capFin) + """</td>
                </tr>
            </table>
        >
    ];"""

    def getResumenEF(self,x,y,robot):
        return """
    resumen[
        label=<
            <table border="0" cellborder="1" cellspacing="0" cellpadding="0">
                <tr>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75">Tipo de Mision: Extraccion de Recursos</td>
                </tr>
                <tr>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75">Recurso Objetivo: """ + str(x) + """,""" + str(y) + """</td>
                </tr>
                <tr>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75">Robot Utilizado: """ + robot + """ (ChapinFighter)</td>
                </tr>
                <tr>
                    <td color="#FFFFFF" bgcolor = "#FFFFFF" height = "64" width = "75">MISION IMPOSIBLE</td>
                </tr>
            </table>
        >
    ];"""

    def getConeccionCT(self):
        return """
    ciudad -> tiposC [color="white"]"""

    def getConeccionTR(self):
        return """
    tiposC -> resumen [color="white"]"""