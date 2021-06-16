import unittest


def ordenar(seq: list) -> list:
    """
    Iniciamos comparação no segundo elemento da lista pois lista com somente um elemento
    sempre esta ordenada.
    :param seq:
    :return:
    O(n^2) para tempo de execução  -> quadratico
    O(1) para memória               -> constante

    """

    # laço verificando a partir do segundo elemento ate tamanho da lista
    swap = 0
    for index in range(1, len(seq)):
        # se o elemento do apontado pelo índice for maior que o seu anterior
        # e o índice for maior que zero -> execute
        # faça o swap dos elementos
        while seq[index] < seq[index-1] and index > 0:
            seq[index], seq[index-1] = seq[index-1], seq[index]
            swap = swap + 2
            index -= 1
    print(swap)
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