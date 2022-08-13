from statistics import median
import pandas as pd

df = pd.read_csv('nomes-brasileiros-ibge/ibge-fem-10000.csv', delimiter=',')
df2 = pd.read_csv('nomes-brasileiros-ibge/ibge-mas-10000.csv', delimiter=',')

frames = [df,df2]

df3 = pd.concat(frames)

dicionario = df3.sort_values("nome").reset_index().loc[:,"nome"].to_dict()

dicio_invertido = dict(map(reversed, dicionario.items()))

nome=input("insira um nome (full caps): ")

print(dicio_invertido.get(nome))
