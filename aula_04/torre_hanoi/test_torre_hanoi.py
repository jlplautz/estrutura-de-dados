import unittest

from aula_04.torre_hanoi.pilha import Pilha, PilhaVaziaExcecao


class TestTorreHanoi(unittest.TestCase):
    def test_criacao(self):
        origem = Pilha('A')
        destino = Pilha('B')
        auxiliar = Pilha('C')

    def test_topo_com_pilha_vazia(self):
        origem = Pilha('A')
        destino = Pilha('B')
        auxiliar = Pilha('C')

        with self.assertRaises(PilhaVaziaExcecao):
            origem.topo()
        with self.assertRaises(PilhaVaziaExcecao):
            destino.topo()
        with self.assertRaises(PilhaVaziaExcecao):
            auxiliar.topo()

    def test_esta_vazia_com_pilha_vazia(self):
        origem = Pilha('A')
        destino = Pilha('B')
        auxiliar = Pilha('C')
        self.assertTrue(origem.esta_vazia)
        self.assertTrue(destino.esta_vazia)
        self.assertTrue(auxiliar.esta_vazia)

    def teste_topo_com_pilha_nao_vazia(self):
        origem = Pilha('A')
        origem.empilhar(1)
        self.assertEqual(1, origem.topo())

    def test_move_one_disc(self):
        origem = Pilha('A')
        destino = Pilha('B')
        origem.empilhar(1)
        destino.empilhar(origem.desempilhar())
        self.assertEqual(1, destino.topo())

    def test_move_two_disc(self):
        origem = Pilha('A')
        destino = Pilha('B')
        auxiliar = Pilha('C')
        origem.empilhar(2)
        origem.empilhar(1)
        destino.empilhar(origem.desempilhar())
        auxiliar.empilhar(origem.desempilhar())
        auxiliar.empilhar(destino.desempilhar())
        self.assertEqual(1, auxiliar.topo())
        self.assertTrue(origem.esta_vazia)
        self.assertTrue(destino.esta_vazia)

    def teste_move_three_disc(self):
        origem = Pilha('A')
        destino = Pilha('B')
        auxiliar = Pilha('C')
        origem.empilhar(3)
        origem.empilhar(2)
        origem.empilhar(1)
        destino.empilhar(origem.desempilhar())     # disc_1
        auxiliar.empilhar(origem.desempilhar())    # disc_2
        auxiliar.empilhar(destino.desempilhar())   # disc_1
        destino.empilhar(origem.desempilhar())     # disc-3
        origem.empilhar(auxiliar.desempilhar())    # disc-1
        destino.empilhar(auxiliar.desempilhar())   # disc_2
        destino.empilhar(origem.desempilhar())     # disc-1
        self.assertEqual(1, destino.topo())
        self.assertTrue(origem.esta_vazia)
        self.assertTrue(auxiliar.esta_vazia)
