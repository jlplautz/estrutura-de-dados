from aula_04.torre_hanoi.pilha import Pilha


def _torre_de_hanoi_recursivo(numero_de_discos, origem, destino, auxiliar):
    """
    chamado do print tem tempo constante ->  1
    f(n) = 1 + 2 * f(n-1)
    f(n) = 1 + 2 * (1 + 2 * f(n-2))      -> 1 + 2 + 4*f(n-2)
    f(n) = 1 + 2 + 4 * ( 1 + 2 * f(n-3)) -> 1 + 2 + 4 + 8* f(n-3)
    f(n) = 1 + 2 + 4 ... 2**(n-1)        -> somatorio da progressao geometrica   (I) expressao
    2 * f(n) = 2+ 4 + 8 ... 2 ** n          (II) expressao
    f(n) = 2**n - 1                          II - I expressao

    O(2**n) para tempo de execução  -> exponencial
    #### Hanoi para 1 discos com Pilha ***1 chamadas
    #### Hanoi para 2 discos com Pilha ***3 chamadas
    #### Hanoi para 3 discos com Pilha ***7 chamadas
    #### Hanoi para 4 discos com Pilha ***15 chamadas
    #### Hanoi para 5 discos com Pilha ***31 chamadas
    #### Hanoi para 6 discos com Pilha ***63 chamadas

    O(n) para memória               -> linear

    :param numero_de_discos:
    :param origem:   A
    :param destino:  B
    :param auxiliar: C
    :return:
    """

    global contagem_de_chamadas_recursivas
    contagem_de_chamadas_recursivas += 1

    if numero_de_discos == 1:
        origem.empilhar(1)
        destino.empilhar(origem.desempilhar())
        print(f'{origem.name} -> {destino.name} : {numero_de_discos}')
        return

    _torre_de_hanoi_recursivo(numero_de_discos - 1, origem, auxiliar, destino)
    print(f'{origem.name} -> {destino.name} : {numero_de_discos}')
    _torre_de_hanoi_recursivo(numero_de_discos - 1, auxiliar, destino, origem)


def torre_de_hanoi(numero_de_discos: int):
    global contagem_de_chamadas_recursivas
    contagem_de_chamadas_recursivas = 0

    origem = Pilha('A')
    destino = Pilha('B')
    auxiliar = Pilha('C')

    _torre_de_hanoi_recursivo(numero_de_discos, origem, destino, auxiliar)


if __name__ == '__main__':
    for i in range(6, 7):
        print(f'#### Hanoi para {i} discos com Pilha')
        torre_de_hanoi(i)
        print(f'***{contagem_de_chamadas_recursivas}', 'chamadas')
