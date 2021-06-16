import unittest


def ordenar(seq: list) -> list:
    """
    Iniciamos comparação no segundo elemento da lista pois lista com somente um elemento
    sempre esta ordenada.
    :param seq:
    :return:
    """

    # laço verificando a partir do segundo elemento ate tamanho da lista

    for index in range(1, len(seq)):

        curElem = seq[index]
        # se o elemento do apontado pelo índice for maior que o seu anterior
        # e o índice for maior que zero -> execute
        # faça o swap dos elementos
        for j in range(index-1, 0, -1):
            if seq[j] > curElem:
                seq[j+1] = seq[j]
            else:
                seq[j+1] = curElem
                break
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