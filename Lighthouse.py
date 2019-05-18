import os
import sys
from Reporte import Reporte

class Lighthouse:
    def __init__(self, url, cantidadCorridas,carpetaCorridas,archivoResultado):
        self.url = url
        self.current_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.cantidadCorridas = cantidadCorridas
        return

    def crearReporte(self,carpeta):
        print("Ejecutando " + str(self.cantidadCorridas) + " corridas en " + self.url)
        os.system('mkdir ' + carpeta)
        path_reporte = self.current_path + '/' + carpeta + '/' + self.archivoResultado
        path_corridas = self.current_path + '/' + carpeta + '/Corridas.csv'
        self.reporte = Reporte(path_reporte,path_corridas,carpeta)
        for i in range(self.cantidadCorridas):
            os.system("node " + self.current_path + "/lighthouseAPI.js " + self.url)
            self.reporte.agregarCorrida(self.url,self.current_path)
        return
    
    def setCantidadCorridas(self,cantidad):
        self.cantidadCorridas = cantidad
        return
    
    def setArchivoResultado(self,nombre):
        self.archivoResultado = nombre
        return

    def setCarpetaCorridas(self,nombre):
        self.carpetaCorridas = nombre
        return

    def setUrl(self,url):
        self.url = url
        return