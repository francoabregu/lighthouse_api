from Lighthouse import Lighthouse
import os
import sys

current_path = os.path.dirname(os.path.realpath(sys.argv[0]))
url = sys.argv[1] 
carpeta = sys.argv[2] 

cantidadCorridas = 10

lighthouse = Lighthouse(url)
lighthouse.crearReporte(carpeta,cantidadCorridas)