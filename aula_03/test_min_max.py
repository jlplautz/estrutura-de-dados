import unittest

from aula_02.minmax import minmax

class TestMinMax(unittest.TestCase):

    def test_min_max(self):
        self.assertEqual(1, 1)

    def test_min_max_lista_com_um_elem(self):
        resultado = minmax([1])
        self.assertEqual((1, 1), resultado)

    def test_min_max_lista_com_dois_elem(self):
        resultado = minmax([1, 2])
        self.assertEqual((1, 2), resultado)

    def test_min_max_lista_vazia(self):
        with self.assertRaises(ValueError):
            minmax([])
        # try:
        #     resultado = minmax([])
        # except ValueError:
        #     pass
        # else:
        #     raise AssertionError()

