import unittest


# # Explicação do Renzo
# def selection_sort(seq):
#     ordenada = []
#     for _ in list(seq):
#         valor_minimo = min(seq)
#         ordenada.append(valor_minimo)
#         seq.remove(valor_minimo)
#     return ordenada

def selection_sort(seq):
    # fazer um enumerate na seq com _ não será utilizado o valor
    for indice_atual, _ in enumerate(seq):
        indice_do_valor_minimo = min(
            # verifica o valor minimo e o indice pois queremos saber oice do valor minimo
            (valor, indice) for indice, valor in
            enumerate(gerar_slice_sem_gastar_memoria(indice_atual, seq), start=indice_atual)
            # pegar o segundo valor da tupla que é o indice  do valor minimo
        )[1]
        # faz o swap dos valor dentro da seq
        seq[indice_atual], seq[indice_do_valor_minimo] = seq[indice_do_valor_minimo], seq[indice_atual]
    return seq


# expŕessão geradora -> para gerar slice sem gastar memoria
def gerar_slice_sem_gastar_memoria(indice_atual, seq):
    for indice in range(indice_atual, len(seq)):
        yield seq[indice]


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], selection_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], selection_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], selection_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], selection_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()


"""

Enumerator é lazy -> Generator
list(enumerate('Plautz'))
Out[3]: [(0, 'P'), (1, 'l'), (2, 'a'), (3, 'u'), (4, 't'), (5, 'z')]

for indice, letra in enumerate('Linda'):
    print(indice, letra)
    
0 L
1 i
2 n
3 d
4 a

"""