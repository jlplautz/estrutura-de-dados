import unittest


def selection_sort(seq):
    """
    complexidade de tempo: O(n**2 + n/2)
    Complexidade de espaço : Constante
    :param seq:
    :return:
    """
    for i in range(len(seq)):
        menor = i

        for j in range(i + 1, len(seq)) :
            if seq[j] < seq[menor]:
                menor = j
        # swap o valor min da seq será inserido no indice 0
        seq[i], seq[menor] = seq[menor], seq[i]

    return seq



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
