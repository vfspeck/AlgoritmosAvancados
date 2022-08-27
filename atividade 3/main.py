from statistics import median
from threading import Thread
import pandas as pd

df = pd.read_csv('nomes-brasileiros-ibge/ibge-fem-10000.csv', delimiter=',')
df2 = pd.read_csv('nomes-brasileiros-ibge/ibge-mas-10000.csv', delimiter=',')

dicionario_fem = df.sort_values("nome").reset_index().loc[:,"nome"].to_dict()

dicionario_mas = df2.sort_values("nome").reset_index().loc[:,"nome"].to_dict()

# classe thread - start - join 

dicio_inv_fem = dict(map(reversed, dicionario_fem.items()))

dicio_inv_mas = dict(map(reversed, dicionario_mas.items()))

nome=input("insira um nome (full caps): ")

def func(dicio,nome):
    dicio.get(nome)

if __name__ == '__main__':
    Thread(target = func).start()
    Thread(target = func).start()

def verificaHomemMulher(dicio1, dicio2, nome):
    if __name__ == '__main__':
        Thread(target = func(dicio1, nome)).start()
        Thread(target = func(dicio2, nome)).start()
    if func(dicio1, nome)==func(dicio2, nome):
        return "é nome de homi e muie"
    else:
        return "nao é"

print(func(dicio_inv_fem,nome))
