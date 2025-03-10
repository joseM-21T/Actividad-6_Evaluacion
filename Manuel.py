def cargar_dataset(archivo):
    import pandas as pd
    import os
    #Si se desea agregar un input se coloca:
    #archivo = input("Por favor, ingresa el nombre del archivo: ")
    extension = os.path.splitext(archivo)[1].lower()
    #Cargar el carchivo según su extención
    if extension == '.csv':
        df = pd.read_csv(archivo)
        return (df)
    elif extension == '.xlsx':
        df = pd.read_excel(archivo)
        return(df)
    else:
        raise ValueError(f"Este Formato no esta soportado para esta función: {extension}")

def cuenta_valores_nulos(dataframe):
    #Valores nulos por columna
    valores_nulos_cols = dataframe.isnull().sum()
    #Valores nulos por dataframe
    valores_nulos_df = dataframe.isnull().sum().sum()

    return("Valores nulos por columna", valores_nulos_cols,
           "Valores nulos por dataframe", valores_nulos_df)

def sustitucion_promedio(dataframe):
    import pandas as pd
    #Separo colunas cuantitativas del dataframe
    cuantitativas_con_nulos = dataframe.select_dtypes(include=['float64', 'int64', 'float', 'int'])
    #Separo columnas cualitativas del dataframe
    cualitativas = dataframe.select_dtypes(include=['object', 'datetime', 'category'])
    #Sustituir valores nulos con promedio o media
    cuantitativas = cuantitativas_con_nulos.fillna(round(cuantitativas_con_nulos.mean(), 1))
    #Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)

    return(Datos_sin_nulos)


def sustitucion_mediana(dataframe):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe
    cuantitativas_con_nulos = dataframe.select_dtypes(include=['float64', 'int64', 'float', 'int'])
    #Separo columnas cualitativas del dataframe
    cualitativas = dataframe.select_dtypes(include=['object', 'datetime', 'category'])

    #Sustituir valores nulos con promedio o media
    cuantitativas = cuantitativas_con_nulos.fillna(round(cuantitativas_con_nulos.median(), 1))
    #Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)

    return(Datos_sin_nulos)


def sustitucion_ffill(dataframe):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe
    cuantitativas_con_nulos = dataframe.select_dtypes(include=['float64', 'int64', 'float', 'int'])
    #Separo columnas cualitativas del dataframe
    cualitativas_con_nulos = dataframe.select_dtypes(include=['object', 'datetime', 'category'])

    #sustitur valores nulos con fill
    cualitativas = cualitativas_con_nulos.fillna(method="ffill")
     #Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cualitativas, cuantitativas_con_nulos], axis=1)

    return(Datos_sin_nulos)


def sustitucion_bfill(dataframe):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe 
    cuantitativas_con_nulos = dataframe.select_dtypes(include=['float64', 'int64', 'float', 'int'])
    #Separo columnas cualitativas del dataframe
    cualitativas_con_nulos = dataframe.select_dtypes(include=['object','datetime','category'])
    
    #sustitur valores nulos con bfill
    cualitativas = cualitativas_con_nulos.fillna(method="bfill")
    #Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cualitativas,cuantitativas_con_nulos], axis=1)

    return(Datos_sin_nulos)


def sustitucion_stringConcreto(dataframe):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe 
    cuantitativas_con_nulos = dataframe.select_dtypes(include=['float64', 'int64', 'float', 'int'])
    #Separo columnas cualitativas del dataframe
    cualitativas_con_nulos = dataframe.select_dtypes(include=['object','datetime','category'])
    
    #sustitur valores nulos con string concreto
    cualitativas = cualitativas_con_nulos.fillna("calendar_date")
    #Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cualitativas,cuantitativas_con_nulos], axis=1)

    return(Datos_sin_nulos)


def sustitucion_constante(dataframe):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe
    cuantitativas_con_nulos = dataframe.select_dtypes(include=['float64', 'int64', 'float', 'int'])
    #Separo columnas cualitativas del dataframe
    cualitativas_con_nulos = dataframe.select_dtypes(include=['object','datetime','category'])
    
    #sustitur valores nulos con el constante
    cualitativas = cualitativas_con_nulos.fillna("f")
    #Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cualitativas,cuantitativas_con_nulos], axis=1)

    return(Datos_sin_nulos)

