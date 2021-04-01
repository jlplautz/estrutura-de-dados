from .node import Node


class ListaVaziaErro(Exception):
    pass


class DequeList:

    def __init__(self, tam=None, first=None, last=None):
        """
        :param tam:
        :param first:
        :param last:
        """
        self.tam = 0
        self.first = first
        self.last = last

    def __iter__(self):
        """
        Complexidade de Tempo:  f(n) = 3n + 1 -> O(n)
        Complexidade de Espaço: f(n) = 1 -> O(1)
        """
        node = self.first
        while node is not None:
            yield node.valor
            node = node.right

    def add(self, value):
        """
        :param value:
        :return:
        """
        self.tam += 1
        node = Node(value)
        if self.first is None:
            self.first = node
            self.last = node
        else:
            node.left = self.last
            self.last.right = node
            self.last = node

    def add_left(self, value):
        """
          :param value:
        :return:
        """
        self.tam += 1
        node = Node(value)
        if self.first is None:
            self.first = node
            self.last = node
        else:
            node.right = self.first
            self.first.left = node
            self.first = node

    def remove(self):
        """
        Complexidade de Tempo:  f(n) = 8 -> O(1)
        Complexidade de Espaço: f(n) = 1 -> O(1)

        :return:
        """

        if self.first is None:
            raise ListaVaziaErro('Não existem elementos na lista')
        elif self.last is self.first:
            node = self.first
            self.first = None
            self.last = None
        else:
            node = self.last
            self.last = node.left
            self.last.right = None
        self.tam -= 1
        return node.valor

    def remove_left(self):
        """
        Complexidade de Tempo:  f(n) = 8 -> O(1)
        Complexidade de Espaço: f(n) = 1 -> O(1)

        :return:
        """
        if self.first is None:
            raise ListaVaziaErro('Não existem elementos na lista')
        elif self.last is self.first:
            node = self.first
            self.first = None
            self.last = None
        else:
            node = self.first
            self.first = node.right
            self.first.left = None
        self.tam -= 1
        return node.valor

    def __len__(self):
        """
        Complexidade de Tempo:  f(n) = 1 -> O(1)
        Complexidade de Espaço: f(n) = 1 -> O(1)
        """
        return self.tam

    def __reversed__(self):
        """
        Complexidade de Tempo:  f(n) = 3n + 1 -> O(n)
        Complexidade de Espaço: f(n) = 1 -> O(1)
        """
        node = self.last
        while node is not None:
            yield node.valor
            node = node.left


