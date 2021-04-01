
class PilhaVaziaExcecao(Exception):
    pass


class Pilha:

    def __init__(self):
        """
        Complexidade de Tempo:  f(n) = 1 -> O(1)
        Complexidade de Espaço: f(n) = 1 -> O(1)
        """
        self._list = list()

    @property
    def esta_vazia(self):
        """
        Complexidade de Tempo:  f(n) = 1 -> O(1)
        Complexidade de Espaço: f(n) = 1 -> O(1)
        :return:
        """
        return len(self._list) == 0

    def topo(self):
        """
        Complexidade de Tempo:  f(n) = 3 -> O(1)
        Complexidade de Espaço: f(n) = 1 -> O(1)
        :return:
        """
        try:
            return self._list[-1]
        except IndexError as e:
            raise PilhaVaziaExcecao('Pilha Vazia') from e

    def empilhar(self, obj):
        """
        Complexidade de Tempo:  f(n) = 1 -> O(1)
        Complexidade de Espaço: f(n) = 1 -> O(1)
        :param obj:
        :return:
        """
        self._list.append(obj)

    def desempilhar(self):
        """
        Complexidade de Tempo:  f(n) = 3 -> O(1)
        Complexidade de Espaço: f(n) = 1 -> O(1)
        :return:
        """
        try:
            return self._list.pop()
        except IndexError as e:
            raise PilhaVaziaExcecao('Pilha vazia') from e
