# *************************************************************************
# Função potencia iterativa
# *************************************************************************

def potencia_iterativa(base: int, expoente: int):
    """
    O(n) para tempo de execução
    O(1) em memoria

    :param base:
    :param expoente:
    :return:
    """
    resultado = 1
    for _ in range(expoente):
        resultado *= base

    return resultado

# *************************************************************************
# Função recursiva linear
# *************************************************************************

def _potencia_recursiva_linear(base, expoente, resultado=1):
    if expoente == 0:
        return resultado
    return _potencia_recursiva_linear(base, expoente - 1, resultado * base)


def potencia_recursiva_linear(base: int, expoente: int):
    """
    f(n) = 4 + f(n-1)
    f(n) = 4 + 4 + f(n-2)
    f(n) = 4 + 4 4 + f(n-3)
    f(n) = 4*n
    O(n) em prelo de execusão
    onde n é o expoente

    O(n) para memoria

    :param base:
    :param expoente:
    :return:
    """
    return _potencia_recursiva_linear(base, expoente - 1, base)

# *************************************************************************
# Função rexursiva algoritmica
# *************************************************************************


def _potencia_recursiva_algoritmica(base: int, expoente: int, resultado=1):
    """
    Na solução algoritma imaginar dividir o problema por 2

    base ** expoente = se expoente é par: base ** (2-n), onde n é expoente // 2
    Simplificado (base * base) ** n
    base ** expoente = se o expoente é impar -> expoente = 2*n + 1  base **(2*n + 1)
    Simplificado base **(2*n + 1) -> base * (base **(2 * n)) = base * [(base*base)**n]

    O(log n) para tempo de execução e tmabem memoria


    :param base:
    :param expoente:
    :return:
    """
    if expoente == 0:
        return resultado

    if expoente % 2 == 0:
        return _potencia_recursiva_algoritmica(base * base, expoente//2, resultado)
    else:
        resultado *= base
        return _potencia_recursiva_algoritmica(base, expoente-1, resultado)


def potencia_recursiva_algoritmica(base: int, expoente: int, resultado=1):
    return _potencia_recursiva_algoritmica(base, expoente)


if __name__ == '__main__':
    print(potencia_iterativa(2, 10))
    print(potencia_recursiva_linear(2, 10))
    print(potencia_recursiva_algoritmica(2, 0))
    print(potencia_recursiva_algoritmica(2, 5))
    print(potencia_recursiva_algoritmica(2, 6))