#importa as bibliotecas
from array import array
from statistics import median
import pandas as pd

#capta as listas como variaval 
namesMas = pd.read_csv('./ibge-mas-10000.csv', delimiter=',')
namesFem = pd.read_csv('./ibge-fem-10000.csv', delimiter=',')

#define frame == frames em python sao onde guardamos um um conjunto de informações
frames = [namesFem,namesMas]
#bliblioteca do panda para concatenar as informações
lists = pd.concat(frames)

#vai pegar a lista e ordenar os valores para variavel nome
just_list = lists.sort_values("nome").loc[:,"nome"].values.tolist()

def binary_search(just_list, nome):
    #define tamanho para lista e os lados para quais haverao a divisao 
    lenght = len(just_list)
    left = 0
    right = lenght -1

    while (left <= right):
        middle = int ((left + right)/2)
        if just_list[middle] == nome:
                return True
        if nome < just_list[middle]:
                right = middle -1
        if nome > just_list[middle]:
                left = middle + 1
        else:
                return False
            
nome=input("insert a name here: ")
namesMas = binary_search(namesMas, nome)
namesFem = binary_search(namesFem, nome)

if(listaM == False or listaF == False):
    print("name not found on the lists")
else:
    print("the name is on the both lists")

