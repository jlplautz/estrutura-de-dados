import unittest

from aula_04.pilha_com_lista.pilha import Pilha, PilhaVaziaExcecao


class PilhaTestes(unittest.TestCase):

    def teste_criacao(self):
        Pilha()

    def teste_topo_com_pilha_vazia(self):
        pilha = Pilha()
        with self.assertRaises(PilhaVaziaExcecao):
            pilha.topo()

    def teste_esta_vazia_com_pilha_vazia(self):
        pilha = Pilha()
        self.assertTrue(pilha.esta_vazia)

    def teste_esta_vazia_com_pilha_nao_vazia(self):
        pilha = Pilha()
        pilha.empilhar('A')
        self.assertFalse(pilha.esta_vazia)

    def teste_topo_com_pilha_nao_vazia(self):
        pilha = Pilha()
        pilha.empilhar('A')
        self.assertEqual('A', pilha.topo())

    def teste_topo_nao_remove_elemento(self):
        pilha = Pilha()
        pilha.empilhar('A')
        pilha.topo()
        self.assertFalse(pilha.esta_vazia)

    def teste_desempilhar_remove_elemento(self):
        pilha = Pilha()
        pilha.empilhar('A')
        pilha.desempilhar()
        self.assertTrue(pilha.esta_vazia)

    def teste_desempilhar_retorna_ultimo_elemento(self):
        pilha = Pilha()
        pilha.empilhar('A')
        self.assertEqual('A', pilha.desempilhar())

    def teste_desempilhar_pilha_vazia_excecao(self):
        pilha = Pilha()
        with self.assertRaises(PilhaVaziaExcecao):
            pilha.desempilhar()

    def testo_primeiro_a_entrar_ultimo_a_sair(self):
        pilha = Pilha()
        letras = 'ABCD'
        for letra in letras:
            pilha.empilhar(letra)

        for letra in reversed(letras):
            with self.subTest(letra):
                self.assertEqual(letra, pilha.desempilhar())
