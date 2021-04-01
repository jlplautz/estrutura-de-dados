from math import inf

def for_loop_minmax(lista: list) -> tuple:
    """
    Implementação ierativa comparando todos os elementos da lista com os valores
    de maoir e menor armazenadaos anteriormente

    Doctests:
    >>> for_loop_minmax([0,1,2,3])
    (0, 3)

    >>> for_loop_minmax([1])
    (1, 1)

    >>> for_loop_minmax([])
    raise ValueError('Valor de lista vazia')

    Complexidade em tempo de Execução:
    4 atrubuição  --> f(n) = c -> 1
    2 comparaçoes --> f(n) = c -> 1
    1 decisão     --> f(n) = c -> 1
    1 laço        --> f(n) = n -> n
    Total: f(n) = 3 + n -> O(n) -> linear

    Complexidade em Espaço de Memoria:
    3 variaveis (int) -> f(n) = c -> 1
    Total: f(n) = 3 -> O(1)  -> constante

    :param lista:
    :return:
    """
    menor = inf
    maior = -inf

    if not lista:
        raise ValueError('Valor de lista vazia')

    for item in lista:
        if item < menor:
            menor = item

        if item > maior:
            maior = item
    return (menor, maior)


def recursivo_minmax(lista: list) -> tuple:
    """
    Implementacão recursiva deixando todas as comparaçoes na pilha de chamadas
    até alcançar a minima lista para resolver a comparação dos elementos

    Doctests:
    >>> recursivo_minmax([0,1,2,3])
    (0, 3)

    >>> recursivo_minmax([0])
    (0, 0)

    Complexidade em tempo de Execução:
    2n atrubuição   --> f(n) = 2n -> n
    2n slicing      --> f(n) = 2n -> n
    2n+2 atribuição --> f(n) = 2n +2  -> n
    n*2 call stack  --> f(n) = n*2 -> n*2
    Total: f(n) = 4n -> O(n^2)  -> Quandratica

    Complexidade em Espaço de Memoria:
    2 funçoes         -> f(n) = c -> 1
    2n variaveis (list) -> f(n) = 2n -> n
    n^2 call stack    -> f(n) = n^2 -> n^2
    Total: f(n) = 1 + n * n^2 -> O(n^2) -> Quadratica

    :param lista:
    :return:
    """

    def recursivo_menor(lista: list) -> int:
        primeiro = lista[0]

        if len(lista) == 1:
            return primeiro
        else:
            menor = recursivo_menor(lista[1:])
            return menor if menor < primeiro else primeiro

    def recursivo_maior(lista: list) -> int:
        primeiro = lista[0]

        if len(lista) == 1:
            return primeiro
        else:
            maior = recursivo_maior(lista[1:])
            return maior if maior > primeiro else primeiro

    if not lista:
        raise ValueError('Valor de lista vazia')

    _menor = recursivo_menor(lista)
    _maior = recursivo_maior(lista)

    return (_menor,_maior)


def tail_recursivo_minmax(lista: list) -> tuple:
     """
    Implementação recursiva com otimização de calda passando o maior ou menor
    valor encontrado até o momento como parametro para a proxima chamada

    Doctests:
    >>> tail_recursivo_minmax([0,1,2,3])
    (0, 3)
    >>> tail_recursivo_minmax([0])
    (0, 0)

    Complexidade em tempo de Execução:
    2n slicing      --> f(n) = 2n² -> n²
    2n comparaçoes  --> f(n) = 2n -> n
    2n+2 atribuição --> f(n) = 2n + 2 -> n
    2n+1 decisao    --> f(n) = 2n + 1 -> N
    Total: f(n) = 4n + 2n² -> O(n²)  -> Quandratica

    Complexidade em Espaço de Memoria:
    2 funçoes          -> f(n) = c -> 1
    2 variaveis (list) -> f(n) = 2n -> n
    1 varialvel (list) -> f(n) = n -1  -> n
    Total: f(n) = 2 + n -> O(n) -> linear

    :param lista:
    :return:
    """

    def tail_recursivo_menor(lista: int, tail=inf) -> int:
        primeiro = lista[0]
        
        if primeiro < tail:
            tail = primeiro
            
        if len(lista) == 1:
            return tail
        
        return tail_recursivo_menor(lista[1:], tail)


    def tail_recursivo_maior(lista: int, tail=-inf) -> int:
        primeiro = lista[0]

        if primeiro > tail:
            tail = primeiro

        if len(lista) == 1:
            return tail

        return tail_recursivo_maior(lista[1:], tail)

    if not lista:
        raise ValueError

    _menor = tail_recursivo_menor(lista)
    _maior = tail_recursivo_maior(lista)

    return (_menor, _maior)


if __name__ == '__main__':
    for_loop_minmax([0, 1, 2, 3])
    recursivo_minmax([0, 1, 2, 3])
    tail_recursivo_minmax([0, 1, 2, 3])
