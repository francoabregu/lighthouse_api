from AdministradorCSV import AdministradorCSV
import os

class Reporte:
    def __init__(self,path_origen,path_resultado,carpeta):
        self.carpeta = carpeta
        self.path_resultado = path_resultado
        self.path_origen = path_origen
        self.administradorCSV = AdministradorCSV()

    def agregarCorrida(self,url,current_path):
        df_lighthouse = self.administradorCSV.abrirCsvLighthouse()
        if(os.path.exists(self.path_resultado)):
            df_corridas = self.administradorCSV.abrirCsv(self.path_resultado)
            index = self.administradorCSV.obtenerPróximoIndiceEscritura(df_corridas)
        else:
            df_corridas = self.administradorCSV.crearCsvCorridas()
            index = 0    
        self.administradorCSV.agregarFilaCSVCorridas(df_corridas,df_lighthouse,index,url)
        return