import pandas as pd
import os
import sys

current_path = os.path.dirname(os.path.realpath(sys.argv[0]))
url = sys.argv[1] 
carpeta = sys.argv[2] 

cantidadCorridas = 10


print("Ejecutando " + str(cantidadCorridas) + " corridas en " + url)


def promedio_binario(categoria):
    df_categoria = df.loc[df['category'] == categoria]
    return float("{0:.2f}".format(df_categoria.loc[df_categoria['score'] == 1]['score'].sum() /  df_categoria.category.count()))

path_resultado = current_path + '/' + carpeta + '/Corridas.csv'


for i in range(cantidadCorridas):
    os.system("node " + current_path + "/lighthouseAPI.js " + url)
    df = pd.read_csv(filepath_or_buffer=current_path + "/report.csv")
    df = df.loc[df['score'] != -1]
    df_performance = df.loc[df['category'] == 'Performance']
    df_performance = df_performance.loc[df_performance['type'] == 'numeric']
    performance_average = float("{0:.2f}".format(df_performance['score'].sum() /  df_performance.category.count()))
    if(os.path.exists(path_resultado)):
        df_promedios = pd.read_csv(filepath_or_buffer=path_resultado)
        index = df_promedios.tail(1).index[0] + 1
    else:
        os.system('mkdir ' + carpeta)
        df_promedios = pd.DataFrame(index=[], columns=['Corrida','URL','Performance','Accessibility','SEO','Best Practices','First Contentful Paint',   'First Meaningful Paint'])
        index = 0    

    df_promedios.loc[index,'Corrida'] = int(index) + 1
    df_promedios.loc[index,'URL'] = url
    df_promedios.loc[index,'Performance'] = performance_average
    df_promedios.loc[index,'Accessibility'] = promedio_binario('Accessibility')
    df_promedios.loc[index,'SEO'] = promedio_binario('SEO')
    df_promedios.loc[index,'Best Practices'] = promedio_binario('Best Practices')
    df_promedios.loc[index,'First Contentful Paint'] = df.loc[df['name'] == 'first-contentful-paint']['score'].values[0]
    df_promedios.loc[index,'First Meaningful Paint'] = df.loc[df['name'] == 'first-meaningful-paint']['score'].values[0] 
    df_promedios.to_csv(path_or_buf=path_resultado,index=False)