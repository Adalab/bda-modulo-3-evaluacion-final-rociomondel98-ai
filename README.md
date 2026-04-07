# Análisis de Fidelización de Clientes: Aerolínea ✈️
Este proyecto consiste en un análisis integral de datos de una aerolínea para entender el comportamiento de sus clientes en relación con su programa de lealtad, salarios y hábitos de vuelo. El objetivo es identificar patrones que permitan mejorar las estrategias de marketing y retención.

# 📋 Estructura del Proyecto
El análisis se divide en tres fases críticas que cubren desde el procesamiento de datos brutos hasta la validación estadística y la comunicación visual.

# 🛠️ Fase 1: Exploración y Limpieza de Datos
En esta etapa, nos familiarizamos con los datos de los CSVs iniciales, unificamos dos fuentes de datos y corregimos inconsistencias para garantizar un análisis fiable.

Hitos clave: 
  - Imputación de nulos en la columna salary utilizando la media segmentada por nivel educativo.
  - Eliminación de la columna Country al no aportar datos relevantes.
  - Unión de los dos CSVs.

Ejemplo de código de la fase 1:

**Gráfica para detectar los outliers negativos en la columna Salario**
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 5))

sns.boxplot(x=df_2['Salary'], color="#FFDAC1", fliersize=8)

plt.title('Detección de Outliers en Salary', fontsize=14, fontweight='bold')
plt.xlabel('Salario Anual', fontsize=12)

plt.show()

OUTPUT: 

<img width="992" height="597" alt="image" src="https://github.com/user-attachments/assets/1b160969-504e-41b8-b426-419753997b0a" />

**Código de unión de los dos CSVs con merge**
df_unido = pd.merge(df_1, df_2, on='Loyalty Number', how='left')

print(f"Filas originales vuelos: {df_1.shape[0]}")
print(f"Filas tras el merge: {df_unido.shape[0]}")

OUTPUT: 

<img width="321" height="65" alt="image" src="https://github.com/user-attachments/assets/d3ff1810-9f6e-4c1d-999f-4da51e7d759e" />


# 📊 Fase 2: Análisis Estadístico
Realizamos un análisis descriptivo a través del análisis más en profundidad de las columnas tanto numéricas como categóricas. 
A partir de esta fase ya se trabaja con el CSV unido con los datos de los dos CSVs iniciales. 

Hitos clave: 
  - Uso de estadísticas descriptivas para conseguir insights de las columnas numéricas.
  - Uso de funciones para obtener outliers en las columnas numéricas y la distribución de frecuencia en las categóricas.   

Ejemplos de código Fase 2:

**Estadísticas descriptivas de las columnas numéricas** 

cols_relevantes = [
    'flights_booked', 'total_flights', 'distance',
    'points_accumulated', 'dollar_cost_points_redeemed',
    'salary', 'clv'
]

estadisticas = df_unido_limpio[cols_relevantes].agg(['mean', 'median', 'std', 'min', 'max'])

estadisticas.loc['mode'] = df_unido_limpio[cols_relevantes].mode().iloc[0]

estadisticas

OUTPUT: 

<img width="1165" height="241" alt="image" src="https://github.com/user-attachments/assets/bc6563dd-9982-44fc-abab-ddc80f11e417" />

**Función para obtener la distribución de frecuencia en las variables categóricas**

cols_categoricas = ['province', 'city', 'postal_code', 'gender', 'education',
       'marital_status', 'loyalty_card', 'enrollment_type'
]

sp_analisis.distribucion_categoricas(df_unido_limpio, cols_categoricas)

PARTE DEL OUTPUT:

<img width="510" height="711" alt="image" src="https://github.com/user-attachments/assets/395423a5-51cc-41d1-ad73-927f0465e587" />

# 📈 Fase 3: Visualización de Datos
Se realizan visualizaciones para tener más insights de las relaciones entre los distintos datos del CSV. 
A destacar: se ha mantenido la misma gama de colores en las visualizaciones para hacerlo de forma más profesional y homogénea. 

Hitos clave: 
  - Se confirma la relación de la cantidad de vuelos con los periodos vacacionales.
  - También se confirma la relación positiva fuerte entre la distancia y los puntos acumulados por clientes. 

Ejemplo de código:

**Visualización de la proporción de clientes con las tarjetas de fidelidad**

plt.figure(figsize=(8, 8))

data_tarjetas = df['loyalty_card'].value_counts()

colores = sns.color_palette('pastel')[0:3]

plt.pie(data_tarjetas, 
        labels = data_tarjetas.index, 
        autopct='%1.1f%%', # Esto pone el porcentaje con un decimal
        startangle=140,    # Gira el gráfico para que se vea mejor
        colors=colores) # Saca un poco la porción más grande para resaltarla
        
centro_circulo = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centro_circulo)

plt.title('Proporción de Clientes por Tipo de Tarjeta', fontsize=15)
plt.axis('equal') # Para que el círculo no salga ovalado

plt.show()

VISUALIZACIÓN:

<img width="843" height="801" alt="image" src="https://github.com/user-attachments/assets/7ad575a9-1e27-4f8c-8d39-a0948f7fb685" />

**Visualización de la distribución de clientes por estado civil y género**

plt.figure(figsize=(12, 6))

sns.countplot(data=df, x='marital_status', hue='gender', palette='pastel')

plt.title('Distribución de Clientes por Estado Civil y Género', fontsize=15)
plt.xlabel('Estado Civil', fontsize=12)
plt.ylabel('Número de Clientes', fontsize=12)
plt.legend(title='Género')

plt.show()

VISUALIZACIÓN:

<img width="1287" height="702" alt="image" src="https://github.com/user-attachments/assets/abc8b3ea-a9dc-4ed6-9cb0-440e118a69eb" />

⚙️ Tecnologías Utilizadas
Python 3.10+

Pandas / Numpy (Procesamiento de datos)

Matplotlib / Seaborn (Visualización)

🚀 Cómo ejecutar el proyecto
Clona el repositorio.

Ejecuta los notebooks en orden: Fase 1 -> Fase 2 -> Fase 3.

WARNING: las funciones están en la carpeta src y los CSVs en la carpeta files 
