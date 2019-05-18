import pandas as pd

class AdministradorCSV:
    def __init__(self):
        return
    
    def abrirCsvLighthouse(self,path):
        df = pd.read_csv(filepath_or_buffer=path)
        df = df.loc[df['score'] != -1]
        return df

    def abrirCsv(self,path):
        return pd.read_csv(filepath_or_buffer=path)

    def obtenerPróximoIndiceEscritura(self,df):
        return df.tail(1).index[0] + 1
    
    def obtenerPromedioNumerico(self,df,category):
        df_performance = df.loc[df['category'] == category]
        df_performance = df_performance.loc[df_performance['type'] == 'numeric']
        return float("{0:.2f}".format(df_performance['score'].sum() /  df_performance.category.count()))
    
    def obtenerPromedioBinario(self,df,category):
        df_categoria = df.loc[df['category'] == category]
        return float("{0:.2f}".format(df_categoria.loc[df_categoria['score'] == 1]['score'].sum() /  df_categoria.category.count()))
    
    def crearCsvCorridas(self):
        return pd.DataFrame(index=[], columns=['Corrida','URL','Performance','Accessibility','SEO','Best Practices','First Contentful Paint',   'First Meaningful Paint'])
    
    def agregarFilaCSVCorridas(self,dfResultado,dfEntrada,index,url):
        dfResultado.loc[index,'Corrida'] = int(index) + 1
        dfResultado.loc[index,'URL'] = url
        dfResultado.loc[index,'Performance'] = self.obtenerPromedioNumerico(dfEntrada,'Performance')
        dfResultado.loc[index,'Accessibility'] = self.obtenerPromedioBinario(dfEntrada,'Accessibility')
        dfResultado.loc[index,'SEO'] = self.obtenerPromedioBinario(dfEntrada,'SEO')
        dfResultado.loc[index,'Best Practices'] = self.obtenerPromedioBinario(dfEntrada,'Best Practices')
        dfResultado.loc[index,'First Contentful Paint'] = dfEntrada.loc[dfEntrada['name'] == 'first-contentful-paint']['score'].values[0]
        dfResultado.loc[index,'First Meaningful Paint'] = dfEntrada.loc[dfEntrada['name'] == 'first-meaningful-paint']['score'].values[0] 
        return dfResultado
    
    def guardarCSV(self,df,path):
        df.to_csv(path_or_buf=path,index=False)
        return