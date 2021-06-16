import unittest
from random import randint


def quick_sort(seq):

    return _quick_sort_recursivo(seq, 0, len(seq)-1)


def _quick_sort_recursivo(seq, inicial, final):

    if inicial < final:
        print("Partition  ", seq)
        pivot = partition(seq, inicial, final)
        print("Pivot-1  ", pivot, seq)
        _quick_sort_recursivo(seq, inicial, pivot - 1)
        print("Pivot+1  ", pivot, seq)
        _quick_sort_recursivo(seq, pivot + 1, final)
    return seq


def partition(seq, inicial, final):
    random_pivot_index = randint(inicial, final)
    seq[random_pivot_index], seq[final] = seq[final], seq[random_pivot_index]
    pivot = seq[final]
    pivot_index = inicial

    # a função range inclui o inicio da intervalo e exclui o final do intervalo
    for j in range(inicial, final):
        if seq[j] < pivot:
            seq[j], seq[pivot_index] = seq[pivot_index], seq[j]
            pivot_index = pivot_index + 1
    seq[pivot_index], seq[final] = seq[final], seq[pivot_index]

    return pivot_index


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], quick_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], quick_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], quick_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], quick_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))

    def teste_lista_desordenada2(self):
        self.assertListEqual([0, 1, 2, 3, 4], quick_sort([1, 0, 3, 4, 2]))


if __name__ == '__main__':
    unittest.main()
    # inicial=0 final=9  = pivot
    # [9, 7, 1, 8, 5, 3, 6, 4, 2, 0]
    # Passo 1: trocar indice final com indice do pivo
    # inicio=0 pivot=9 final=8
    # [9, 7, 1, 8, 0, 3, 6, 4, 2, 5]
    # Passo 2 incrementar inicio até encontrar valor que seja maior que o valor do pivot
    # inicio = 1 pivot = 0 final = 8
    # [5, 7, 1, 8, 0, 3, 6, 4, 2, 9]
    # Passo 3: decrementar valor de indice final até encontrar valor menor que o pivot
    # inicio = 1 pivot = 8 final = 7
    # [2, 7, 1, 8, 0, 3, 6, 4, 5, 9]
    # Refazer passo 2
    # inicio = 5 pivot = 5 final = 5
    # [2, 4, 1, 3, 0, 5, 6, 8, 7, 9]
    # repetir inicio = 0  fim = 4 pivot= 2
    # repetir inicio= 6 fim=9