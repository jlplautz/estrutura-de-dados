from typing import Iterable, Tuple
from math import inf
from numbers import Number


def _minmax_recursiva(iteravel: Iterable, valor_minimo: Number, valor_maximo: Number) -> Tuple[int, int]:
    try:
        elemento = next(iteravel)
    except StopIteration:
        raise ValueError('não existe')
    else:
        if elemento < valor_minimo:
            valor_minimo = elemento
        if elemento > valor_maximo:
            valor_maximo = elemento
        return valor_minimo, valor_maximo


def minmax(iteravel: Iterable) -> Tuple[int, int]:
    """
    >>> minmax([])
    Traceback (most recent call last):
        ...
    ValueError: não existe minimo e maximo de iteravel sem elemento
    >>> minmax([1])
    (1, 1)

    :param iteravel:
    :return:
    """
    iteravel = iter(iteravel)
    valor_minimo, valor_maximo = _minmax_recursiva(iteravel, inf, -inf)
    if valor_minimo is inf:
        raise ValueError('não existe mínimo e máximo de iterável sem elemento')
    return valor_minimo, valor_maximo
