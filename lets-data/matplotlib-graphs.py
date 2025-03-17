# %%
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# %% #uma figure eh como se fosse uma janela
janela = plt.figure()
# %%
#* os parametros sao: comeca no 0 no x e no y e o frafico tem largura 1 e altura 1
grafico = janela.add_axes([0, 0, 1, 1])
janela
# %%
x = np.linspace(0, 100, 10)
y = x**3
# %%

grafico.plot(x, y, 'red')
janela

# %%
df_bitcoin = pd.read_csv('../data/bitcoin_data.csv')
df_bitcoin.head()
# %%

df_bitcoin['Price'].tail(20)
# %%
janela = plt.figure(figsize=(10,5)) 
grafico = janela.add_axes([0, 0, 1, 1])
grafico.plot(df_bitcoin['Date'], df_bitcoin['Price'])
plt.xticks(rotation=45)

# %%
#%%
df_titanic = pd.read_csv('../data/train.csv')
df_titanic.head()

# %%
#* Grafico de barras
df_por_sexo = df_titanic.groupby('Sex')['Survived'].sum().reset_index()
df_por_sexo
# %%
janela_vivos = plt.figure(figsize=(10,5))
grafico_vivos = janela_vivos.add_axes([0,0,1,1])
grafico_vivos.bar(df_por_sexo['Sex'], df_por_sexo['Survived'])
grafico_vivos

# %%
#* Histograma (Contagem de uma variavel so)
janela = plt.figure(figsize=(10,5))
grafico = janela.add_axes([0,0,1,1])
grafico.hist(df_titanic['Age'])

# %%
#* Boxplot ()
df_titanic.dtypes

# %%
df_titanic.isnull().sum()

# %%

df_titanic = df_titanic.dropna()
# %%
df_titanic.isnull().sum()

# %%

janela = plt.figure(figsize=(10,5))
grafico = janela.add_axes([0,0,1,1])
grafico.boxplot(df_titanic['Age'])
# %%

idades_com_outlier = list(df_titanic['Age'])
idades_com_outlier.append(120)
# %%

janela = plt.figure(figsize=(10,5))
grafico = janela.add_axes([0,0,1,1])
grafico.boxplot(idades_com_outlier)

# %%
df_titanic.describe()

# %%
#* Criando varios graficos em grade
janela, grafico = plt.subplots(nrows=1, ncols=1)
# %%
# * removendo o grafico da janela
grafico.remove()
janela
# %%
janela, grafico = plt.subplots(nrows=1, ncols=1)

# %%
janela, grafico = plt.subplots(nrows=1, ncols=1, figsize=(5,5))

# %%
janela, grafico = plt.subplots(nrows=1, ncols=1, figsize=(5,10))
# %%
janela, grafico = plt.subplots(nrows=1, ncols=1, figsize=(10,5))
# %%
janela, grafico = plt.subplots(nrows=2, ncols=2)
plt.tight_layout()
# %%
janela, graficos = plt.subplots(nrows=2, ncols=2, figsize=(20,10))

# %%
type(graficos)
# %%
graficos
# %%
# * a partir disso, eh possivel acessar cada grafico e plotar algo diferente em cada
graficos[0][1]
# %%
graficos[0][0].plot(df_bitcoin['Date'], df_bitcoin['Price'])
graficos[0][1].bar(df_por_sexo['Sex'], df_por_sexo['Survived'])
graficos[1][0].hist(df_titanic['Age'])
graficos[1][1].boxplot(df_titanic['Age'])
# %%
# %%
janela

# %%
