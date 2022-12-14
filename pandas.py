# -*- coding: utf-8 -*-
"""Pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b1zBOwu2yo0sRbHsH8QFZhf2I6Y_ljs6

#Python para análise de dados(Pandas)- Everton Cardoso
"""

#importando a biblioteca pandas, dando o apelido de df
import pandas as pd

#fazendo a leitura do arquivo vcs e ignorando linhas com erro. sep, separa as linhas.
df = pd.read_csv("/content/drive/MyDrive/Curso_Pandas/Gapminder.csv", error_bad_lines=False, sep=";")

#Visualizando as 5 primeiras linhas
df.head()

#Mudando o nome das coluna
df = df.rename(columns={"country":"Pais", "continent":"Continente", "year":"Ano", "lifeExp":"Expec de vida", "pop": "Pop Total", "gdpPercap":"PIB"})

#Comando para saber a quantidade de linhas e colunas e atribuindo os nomes renomeados para df
df.shape

#Comando para verificar nome das colunas
df.columns

#Comando para saber os tipos de cada coluna
df.dtypes

#Comando para mostrar as ultimas linhas do arquivo
df.tail()

df.describe()

#Comando para fazer filtro
df["Continente"].unique()

Oceania = df.loc[df["Continente"] == "Oceania"]
Oceania.head()

from google.colab import drive
drive.mount('/content/drive')

