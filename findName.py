from array import array
from statistics import median
import pandas as pd

namesMas = pd.read_csv('./ibge-mas-10000.csv', delimiter=',')
namesFem = pd.read_csv('./ibge-fem-10000.csv', delimiter=',')

frames = [namesFem,namesMas]

lists = pd.concat(frames)

just_list = lists.sort_values("nome").loc[:,"nome"].values.tolist()

def binary_search(just_list, nome):
    #define tamanho para lista e os lados para quais haverao a divisao 
    lenght = len(just_list)
    #define qual lado vai começar valendo
    left = 0
    right = lenght -1

    while (left <= right):
        middle = int ((left + right)/2)
        if just_list[middle] == nome:
                print(middle)
                break
        if nome < just_list[middle]:
                right = middle -1
        if nome > just_list[middle]:
                left = middle + 1
        else:
                print("name not found")

nome=input("insert a name here:  ")
print(binary_search(just_list, nome))
