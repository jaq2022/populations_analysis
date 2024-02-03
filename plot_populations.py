# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 18:13:55 2024

@author: Javier
"""

# Se importan las librerias.
import pandas as pd
import matplotlib.pyplot as plt

# Se carga el dataset en python.
data = pd.read_csv("populations.csv", delimiter = ",")

# Se seleccionan los datos de Cantabria.
data_cantabria = data[data["Provincia"] == "Cantabria"]
# Se agrupa la poblacion por municipio y se suma.
pob_by_mun = data_cantabria.groupby("Municipio")["Poblacion"].sum()

# Se realiza un grafico de barras con la poblacion por municipio.
pob_by_mun.plot.bar(x = "Municipio", y = "Poblacion", rot = 90)
plt.title("Población de municipios en Cantabria")
plt.savefig("barplot_poblacion")