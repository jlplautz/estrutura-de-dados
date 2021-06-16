import unittest


def ordenar(seq: list) -> list:

    # Bubble com dois laços for onde a a comparação ocorreu n-1 vezes
    for i in range(len(seq)):
        sentinela = True

        for j in range(i+1, len(seq)):
            if seq[j] < seq[i]:
                seq[j], seq[i] = seq[i], seq[j]
                sentinela = False

            if sentinela:
                return seq

    return seq


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
