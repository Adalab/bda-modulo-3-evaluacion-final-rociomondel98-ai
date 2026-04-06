#importamos librerías 

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

def outliers_iqr(df, columnas):
    """
    Calcula el número de outliers, el porcentaje y la media, 
    separando los resultados visualmente.
    """
    if isinstance(columnas, str):
        columnas = [columnas]
        
    resultados = {}

    for col in columnas:
        if col in df.columns:
            # Imprimimos separador visual en la consola
            print(f"\n" + "*"*50)
            print(f" ANALIZANDO COLUMNA: {col.upper()} ".center(50, "*"))
            print("*"*50)

            # 1. Cálculo de IQR
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1

            # 2. Límites
            limite_inf = Q1 - 1.5 * IQR
            limite_sup = Q3 + 1.5 * IQR

            # 3. Identificación de outliers
            df_outliers = df[(df[col] < limite_inf) | (df[col] > limite_sup)]
            conteo = df_outliers.shape[0]
            porcentaje = (conteo / df.shape[0]) * 100
            media_outliers = df_outliers[col].mean() if conteo > 0 else 0

            # 4. Prints informativos con "rayitas"
            print(f"  > Límites teóricos: [{round(limite_inf, 2)} a {round(limite_sup, 2)}]")
            print(f"  > Total de outliers: {conteo}")
            print(f"  > Porcentaje sobre el total: {round(porcentaje, 2)}%")
            print("-" * 50)

        else:
            print(f"\n[!] La columna '{col}' no existe en el DataFrame.")

    return resultados

def matriz_correlacion(df, columnas):
    """
    Calcula la matriz de correlación para las columnas seleccionadas.
    """
    # Filtramos solo las columnas que existen en el df
    cols_validas = [col for col in columnas if col in df.columns]
    
    # Calculamos la correlación (por defecto es Pearson)
    matriz = df[cols_validas].corr()
    
    return matriz


def distribucion_categoricas(df, columnas):
    """
    Calcula la frecuencia absoluta y relativa de las columnas categóricas.
    """
    for col in columnas:
        if col in df.columns:
            print(f"\n" + "="*50)
            print(f" DISTRIBUCIÓN DE: {col.upper()} ".center(50, "="))
            print("="*50)
            
            # Frecuencia absoluta
            abs_freq = df[col].value_counts()
            # Frecuencia relativa (porcentaje)
            rel_freq = df[col].value_counts(normalize=True) * 100
            
            # Combinamos ambos en un DataFrame para mostrar
            df_dist = pd.DataFrame({
                'Recuento': abs_freq,
                'Porcentaje (%)': rel_freq.round(2)
            })
            
            print(df_dist)
            print("-" * 50)
        else:
            print(f"La columna {col} no existe.")