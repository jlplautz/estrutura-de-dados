import unittest


def merge(left, right):
    resultado = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1
    resultado += left[i:]
    resultado += right[j:]
    return resultado


def ordenar(seq: list) -> list:  # seq = [1,2,3,4] d[1,2,3,4,5,6,7,8]
    if len(seq) <= 1:
        return seq
    meio = len(seq) // 2
    left = ordenar(seq[:meio])
    right = ordenar(seq[meio:])
    return merge(left, right)


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], ordenar([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], ordenar([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], ordenar([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ordenar([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))

    def teste_lista_reversa(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ordenar([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

if __name__ == '__main__':
    unittest.main()
