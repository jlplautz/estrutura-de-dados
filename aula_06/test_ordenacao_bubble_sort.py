import unittest


def ordenar(seq: list) -> list:

    # [5, 1, 3, 2] original
    # [1, 3, 2, 5] passada 1
    # [1, 2, 3, 5] passada2

    # [5, 4, 3, 2] original
    # [4, 3, 2, 5] original
    # [3, 2, 4, 5] original
    # [2, 3, 4, 5] original  O (n ** 2)

    # Bubble com dois laços for onde a a comparação ocorreu n-1 vezes
    for i in range(1, len(seq)):
        for j in range(1, len(seq)):
            if seq[j] < seq[j-1]:
                seq[j], seq[j-1] = seq[j-1], seq[j]
                j += 1
    return seq



    # index = len(seq) - 1
    # ordenado = False
    # while not ordenado:
    #     ordenado = True
    #     for i in range(0, index):
    #
    #         if seq[i] > seq[i+1]:
    #             ordenado = False
    #             seq[i], seq[i+1] = seq[i+1],  seq[i]
    # return seq


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], ordenar([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], ordenar([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], ordenar([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ordenar([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
