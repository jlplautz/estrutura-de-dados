from collections import deque


class PilhaVaziaExcecao(Exception):
    pass


class Pilha:
    # inserido atributo nome para identificar a pilhar
    def __init__(self, name):
        self._deque = deque()
        self.name = name

    @property
    def esta_vazia(self):
        return len(self._deque) == 0

    def topo(self):
        try:
            return self._deque[-1]
        except IndexError as e:
            raise PilhaVaziaExcecao('Pilha Vazia') from e

    def empilhar(self, obj):
        self._deque.append(obj)
        pass

    def desempilhar(self):
        try:
            return self._deque.pop()
        except IndexError as e:
            raise PilhaVaziaExcecao('Pilha vazia') from e
