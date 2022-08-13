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

def func1(nome):

def func2(nome):


if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()

def verificaHomemMulher(nome):
    if func1(nome)==func2(nome):
        return "é nome de homi e muie"
    else
        return
    
