from statistics import median
import pandas as pd

df = pd.read_csv('nomes-brasileiros-ibge/ibge-fem-10000.csv', delimiter=',')
df2 = pd.read_csv('nomes-brasileiros-ibge/ibge-mas-10000.csv', delimiter=',')

frames = [df,df2]

df3 = pd.concat(frames)

lista = df3.sort_values("nome").loc[:,"nome"].values.tolist()

nome=input("insira um nome (full caps): ")

def busca_binaria(lista,nome):
    min=0
    mid=0
    max=len(lista)

    while min<=max:
        mid=(min+max)//2

        if(lista[mid]<nome):
            min=mid+1
        elif(lista[mid]>nome):
            max=mid-1
        else:
            return mid
    return "não tá na lista"

print(busca_binaria(lista,nome))