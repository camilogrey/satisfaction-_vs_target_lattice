import seaborn as sns
import pandas as pd
pd.set_option('display.max_columns', None)
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t
from scipy.stats import zscore


df = pd.read_excel("Route")
print(df.columns)

adultos=df.loc[df["Segmentación"]=="Adultos"]
adultos_may=df.loc[df["Segmentación"]=="Adultos mayores"]
Jovenes=df.loc[df["Segmentación"]=="Jóvenes"]

#1. Lattice Plot in multiple groups
sns.lmplot(x="Satisfacción", y="Gasto Promedio", col="Segmentación", data=df, height=5)
plt.show()


#2. Lattice Plot joined together
sns.lmplot(x="Satisfacción", y="Gasto Promedio", hue="Segmentación", data=df, height=5)
plt.show()



# 3. Pair plot general para ver (relaciones, tendencias o patrones posibles entre variables, las distribuciones de los datos)
#Detectar tendencias lineales o no lineales o correlaciones 
sns.pairplot(df)
plt.show()

# Calcular coeficientes de correlación
correlation_matrix = df.corr()
print("Matriz de correlación:")
print(correlation_matrix)


# Crear pair plot
sns.pairplot(adultos)
plt.show()

# Crear pair plot
sns.pairplot(adultos_may)
plt.show()


# Crear pair plot
sns.pairplot(Jovenes)
plt.show()

