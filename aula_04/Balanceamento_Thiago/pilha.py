
from collections import deque


class PilhaVaziaErro(Exception):
    pass


class Pilha:

    def __init__(self):
        self._deque = deque()

    @property
    def esta_vazia(self):
        return len(self._deque) == 0

    def topo(self):
        try:
            return self._deque[-1]
        except IndexError as e:
            raise PilhaVaziaErro('Pilha Vazia') from e

    def empilhar(self, obj):
        self._deque.append(obj)
        pass

    def desempilhar(self):
        try:
            return self._deque.pop()
        except IndexError as e:
            raise PilhaVaziaErro('Pilha vazia') from e
