# -*- coding: utf-8 -*-
"""Aula_06-Analise_exploratoria.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18HVLfyJmt49lOsDCyjfU1fcGj4RNprYj
"""

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

#comando para uploade do arquivo
from google.colab import files
arq = files.upload()

#comando para criar nosso DataFrame
df = pd.read_excel("AdventureWorks.xlsx")

#comando para visualizar as 5 primeira linhas
df.head()

#comando para ver quantidade de linhas e colunas
df.shape

#comando para verificar os tipos de dados
df.dtypes

#comando para verificar qual a receita total
df["Valor Venda"].sum()

#comando para verificar o custo total
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"]) # Criando a coluna de custo

df.head(1)

#comando para achar qual o custo total
round(df["custo"].sum(), 2)

#Agora que sabemos a receita e custo total, podemos achar o Lucro total 
#Criar uma coluna de lucro que será Receita - Custo
df["lucro"] = df["Valor Venda"] - df["custo"]

df.head(1)

#Comando para visualizar o total lucro
round(df["lucro"].sum(), 2)

#criando uma coluna com total de dias para enviar o produto
df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]

df.head(1)

"""####Tempo de envio de cada maraca, com isso deve-se transformar a coluna Tempo_envio em numerica"""

#extrair apenas os dias
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

df.head(1)

#verificando o tipo da coluna Tempo_envio
df["Tempo_envio"].dtype

#Média do tempo de envio por Marca
df.groupby("Marca")["Tempo_envio"].mean()

"""####Missing Values"""

#Verificando se temos dados faltantes
df.isnull().sum()

"""####Descobrindo o Lucro por ano e Marca"""

#Agrupar por ano e marca
df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum()

pd.options.display.float_format = '{:20,.2f}'.format

#Resetando o index
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()
lucro_ano

#Qual o total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

#Gráfico total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto");

df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("Receita");

df.groupby(df["Data Venda"].dt.year)["lucro"].sum()

#Selecionando apenas as vendas de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]
df_2009.head()

df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro x Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro");

df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="Lucro x Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');

df_2009.groupby("Classe")["lucro"].sum().plot.bar(title="Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');

df["Tempo_envio"].describe()

#Gráfico de Boxplot
plt.boxplot(df["Tempo_envio"]);

#Histograma
plt.hist(df["Tempo_envio"]);

#Tempo mínimo de envio
df["Tempo_envio"].min()

#Tempo maximo de envio
df["Tempo_envio"].max()

#Identificando o Outlier
df[df["Tempo_envio"] == 20]

