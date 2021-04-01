import unittest

from aula_03.dequelist.dequelist import DequeList
from aula_03.dequelist.node import Node
from aula_03.dequelist.dequelist import ListaVaziaErro


class NodeTestes(unittest.TestCase):
    def test_init_with_standard_value(self):
        node = Node(4)
        self.assertEqual(4, node.valor)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def test_init_with_node_left(self):
        left = Node(1)
        node = Node(2, left)
        self.assertEqual(left, node.left)
        self.assertIsNone(node.right)
        node3 = Node(3, left=left)
        self.assertEqual(left, node3.left)
        self.assertIsNone(node3.right)

    def test_init_with_node_right(self):
        right = Node(1)
        node = Node(2, right=right)
        self.assertEqual(right, node.right)
        self.assertIsNone(node.left)

    def test_init_with_node_left_and_right(self):
        left = Node(1)
        right = Node(2)
        node = Node(3, left, right)
        self.assertEqual(left, node.left)
        self.assertEqual(right, node.right)


class ListTests(unittest.TestCase):
    def test_init(self):
        lista = DequeList()
        self.assertEqual(0, lista.tam)
        self.assertIsNone(lista.first)
        self.assertIsNone(lista.last)

    def test_add_first(self):
        lista = DequeList()
        lista.add(0)
        self.assertEqual(1, lista.tam)
        first = lista.first
        self.assertEqual(0, first.valor)
        self.assertEqual(first, lista.last)
        self.assertIsNone(first.left)
        self.assertIsNone(first.right)

    def test_add_second(self):
        lista = DequeList()
        lista.add(0)
        lista.add(1)
        self.assertEqual(2, lista.tam)
        first = lista.first
        self.assertEqual(0, first.valor)
        last = lista.last
        self.assertEqual(1, last.valor)
        self.assertEqual(first, last.left)
        self.assertEqual(last, first.right)
        self.assertIsNone(first.left)
        self.assertIsNone(last.right)

    def test_add_third(self):
        lista = DequeList()
        lista.add(0)
        lista.add(1)
        lista.add(2)
        self.assertEqual(3, lista.tam)
        first = lista.first
        self.assertEqual(0, first.valor)
        last = lista.last
        second = first.right
        self.assertEqual(1, second.valor)
        self.assertEqual(2, last.valor)

        self.assertEqual(first, second.left)

        self.assertEqual(second, last.left)
        self.assertEqual(last, second.right)

        self.assertIsNone(first.left)
        self.assertIsNone(last.right)

    def test_add_first_left(self):
        lista = DequeList()
        lista.add_left(0)
        self.assertEqual(1, lista.tam)
        first = lista.first
        self.assertEqual(0, first.valor)
        self.assertEqual(first, lista.last)
        self.assertIsNone(first.left)
        self.assertIsNone(first.right)

    def test_add_second_left(self):
        lista = DequeList()
        lista.add_left(0)
        lista.add_left(1)
        self.assertEqual(2, lista.tam)
        first = lista.first
        self.assertEqual(1, first.valor)
        last = lista.last
        self.assertEqual(0, last.valor)
        self.assertEqual(first, last.left)
        self.assertEqual(last, first.right)
        self.assertIsNone(first.left)
        self.assertIsNone(last.right)

    def test_add_third_left(self):
        lista = DequeList()
        lista.add_left(0)
        lista.add_left(1)
        lista.add_left(2)
        self.assertEqual(3, lista.tam)
        first = lista.first
        self.assertEqual(2, first.valor)
        last = lista.last
        second = first.right
        self.assertEqual(1, second.valor)
        self.assertEqual(0, last.valor)

        self.assertEqual(first, second.left)

        self.assertEqual(second, last.left)
        self.assertEqual(last, second.right)

        self.assertIsNone(first.left)
        self.assertIsNone(last.right)

    def test_remove_empty_list(self):
        lista = DequeList()
        self.assertRaises(ListaVaziaErro, lista.remove)

    def test_remove_lista_1_element(self):
        lista = DequeList()
        lista.add(0)
        self.assertEqual(0, lista.remove())
        self.assertEqual(0, lista.tam)
        self.assertIsNone(lista.first)
        self.assertIsNone(lista.last)

    def test_remove_lista_2_elements(self):
        lista = DequeList()
        lista.add(0)
        lista.add(1)
        self.assertEqual(1, lista.remove())
        self.assertEqual(1, lista.tam)
        first = lista.first
        self.assertEqual(first, lista.last)
        self.assertEqual(0, first.valor)
        self.assertIsNone(first.right)
        self.assertIsNone(first.left)

    def test_remove_lista_3_elements(self):
        lista = DequeList()
        lista.add(0)
        lista.add(1)
        lista.add(2)
        self.assertEqual(2, lista.remove())
        self.assertEqual(2, lista.tam)
        first = lista.first
        last = lista.last
        self.assertEqual(last, first.right)
        self.assertEqual(first, last.left)
        self.assertEqual(0, first.valor)
        self.assertEqual(1, last.valor)
        self.assertIsNone(first.left)
        self.assertIsNone(last.right)

    def test_remove_left_empty_lista(self):
        lista = DequeList()
        self.assertRaises(ListaVaziaErro, lista.remove_left)

    def test_remove_left_element_1(self):
        lista = DequeList()
        lista.add(0)
        self.assertEqual(0, lista.remove_left())
        self.assertEqual(0, lista.tam)
        self.assertIsNone(lista.first)
        self.assertIsNone(lista.last)

    def test_remove_left_element_2(self):
        lista = DequeList()
        lista.add(0)
        lista.add(1)
        self.assertEqual(0, lista.remove_left())
        self.assertEqual(1, lista.tam)
        first = lista.first
        self.assertEqual(first, lista.last)
        self.assertEqual(1, first.valor)
        self.assertIsNone(first.right)
        self.assertIsNone(first.left)

    def test_remove_left_element_3(self):
        lista = DequeList()
        lista.add(0)
        lista.add(1)
        lista.add(2)
        self.assertEqual(0, lista.remove_left())
        self.assertEqual(2, lista.tam)
        first = lista.first
        last = lista.last
        self.assertEqual(last, first.right)
        self.assertEqual(first, last.left)
        self.assertEqual(1, first.valor)
        self.assertEqual(2, last.valor)
        self.assertIsNone(first.left)
        self.assertIsNone(last.right)

    def test_iter_empty_lista(self):
        lista = DequeList()
        for i in lista:
            self.fail('Não deveria executar nada')

    def test_iter_not_empty_lista(self):
        lista = DequeList()
        numbers = list(range(3))
        for n in numbers:
            lista.add(n)

        for i, elemento_da_lista in zip(range(3), lista):
            self.assertEqual(i, elemento_da_lista)

    def test_iter_reversed_empty_lista(self):
        lista = DequeList()
        for i in reversed(lista):
            self.fail('Não deveria executar nada')

    def test_iter_lista_reversed_not_empty(self):
        lista = DequeList()
        numbers = list(range(3))
        for n in numbers:
            lista.add(n)

        for i, element_in_lista in zip(reversed(range(3)), reversed(lista)):
            self.assertEqual(i, element_in_lista)

    def test_len(self):
        lista = DequeList()
        self.assertEqual(0, len(lista))
        lista.add_left(0)
        lista.add_left(1)
        lista.add_left(2)
        self.assertEqual(3, len(lista))


if __name__ == '__main__':
    unittest.main()
