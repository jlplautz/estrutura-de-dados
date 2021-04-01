import unittest

from aula_04.balanceamento.pilha import Pilha

# Código para adicionar path do projeto
import sys
from os import path

file_path = path.abspath(__file__)
projeto_path = path.join(file_path, '..', '..')
projeto_path = path.abspath(projeto_path)
sys.path.append(projeto_path)

# Fim


def esta_balanceada(expressao):
    """
    Função que calcula se expressão possui parenteses, colchetes e chaves balanceados
    O Aluno deverá informar a complexidade de tempo e espaço da função
    Deverá ser usada como estrutura de dados apenas a pilha feita na aula anterior
    :param expressao: string com expressao a ser balanceada
    :return: boleano verdadeiro se expressao está balanceada e falso caso contrário

    Complexidade de Tempo:   O(1)  -> Constante
    Complexidade de Espaço:  O(1)  -> Constante

    """
    colchete = 0
    parentese = 0
    chave = 0
    pilha = Pilha()

    for exp in expressao:
        # teste inicial:
        # se a pilha esta vazia retornar false para os caracteres ')', ']', '}'
        if (exp == ')' or exp == ']' or exp == '}') and pilha.esta_vazia:
            return False
        # empilhar e contar o caractere '['
        if exp == '[':
            colchete += 1
            pilha.empilhar(exp)
        # empilhar e contar o caractere '('
        elif exp == '(':
            parentese += 1
            pilha.empilhar(exp)
        # empilhar e contar o caractere '{'
        elif exp == '{':
            chave += 1
            pilha.empilhar(exp)
        # empilhar o caractere ')', ']' and '}'
        elif exp == ')' or exp == ']' or exp == '}':
            pilha.empilhar(exp)

    # enquanto o flag pilha.esta_vazia for diferente de TRUE
    # desempilhe os caracteres da pilha
    while pilha.esta_vazia is not True:
        expr = pilha.desempilhar()
        if expr == ')':
            parentese -= 1
        elif expr == ']':
            colchete -= 1
        elif expr == '}':
            chave -= 1
        elif expr == '(' or expr == '[' or expr == '{':
            pass

    if colchete == 0 and parentese == 0 and chave == 0:
        return True
    else:
        return False


class BalancearTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertTrue(esta_balanceada(''))

    def test_parenteses(self):
        self.assertTrue(esta_balanceada('()'))

    def test_chaves(self):
        self.assertTrue(esta_balanceada('{}'))

    def test_colchetes(self):
        self.assertTrue(esta_balanceada('[]'))

    def test_todos_caracteres(self):
        self.assertTrue(esta_balanceada('({[]})'))
        self.assertTrue(esta_balanceada('[({})]'))
        self.assertTrue(esta_balanceada('{[()]}'))

    def test_chave_nao_fechada(self):
        self.assertFalse(esta_balanceada('{'))

    def test_colchete_nao_fechado(self):
        self.assertFalse(esta_balanceada('['))

    def test_parentese_nao_fechado(self):
        self.assertFalse(esta_balanceada('('))

    def test_chave_nao_aberta(self):
        self.assertFalse(esta_balanceada('}{'))

    def test_colchete_nao_aberto(self):
        self.assertFalse(esta_balanceada(']['))

    def test_parentese_nao_aberto(self):
        self.assertFalse(esta_balanceada(')('))

    def test_falta_de_caracter_de_fechamento(self):
        self.assertFalse(esta_balanceada('({[]}'))

    def test_falta_de_caracter_de_abertura(self):
        self.assertFalse(esta_balanceada('({]})'))

    def test_expressao_matematica_valida(self):
        self.assertTrue(esta_balanceada('({[1+3]*5}/7)+9'))

    def test_char_errado_fechando(self):
        self.assertFalse(esta_balanceada('[)'))
