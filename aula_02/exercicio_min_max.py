"""
Criar função que retorne min e max de uma sequência numérica aleatória
Só pode usar if, comparações, recursão e funções ou laço que sejam de sua autoria
(quem fizer recursivo e iterativo, será escolhido)
Deve informar via docstring qual é a complexidade de tempo e espaço *
"""
import random
from random import shuffle


min_valor = 0
max_valor = 0

def min_max_function():
    lista = list(range(100))
    random.shuffle(lista)
    print(lista)
    global min_valor, max_valor

    for elemento in lista:
        if elemento < min_valor:
            min_valor = elemento
        elif elemento > max_valor:
            max_valor = elemento

    return min_valor, max_valor


if __name__ == '__main__':
    print(min_max_function())


