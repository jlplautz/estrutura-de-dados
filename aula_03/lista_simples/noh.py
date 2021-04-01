# para refactorar (mover) a classe basta precionar F6
class Noh:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo

    def __iter__(self):
        noh_atual = self
        while noh_atual != None:
            yield noh_atual
            noh_atual = noh_atual.proximo