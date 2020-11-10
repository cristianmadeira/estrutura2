import unittest
from deque_dinamico import DequeDinamico, Node


class DequeTest(unittest.TestCase):

    def setUp(self):
        self.limite = 10
        self.deque = DequeDinamico(self.limite)

    def test_get_tamanho(self):
        expected = 0
        result = self.deque.get_tamanho()
        self.assertEqual(expected, result)

    def test_get_limite(self):
        expected = 10
        self.assertEqual(expected, self.deque.get_limite())

    def test_insere_na_direita(self):
        element1 = 'CEFET/RJ'
        result1 = self.deque.insere_na_direita(element1)
        expected1 = 'CEFET/RJ'
        self.assertEqual(expected1, result1.conteudo)

        element2 = 'Maria da Graça'
        result2 = self.deque.insere_na_direita(element2)
        expected2 = 'Maria da Graça'
        self.assertEqual(expected2, result2.conteudo)

        expected_tamanho = 2
        result_tamanho = self.deque.get_tamanho()

        self.assertEqual(expected_tamanho, result_tamanho)

    def test_get_ultimo_elemento(self):

        elemento1, elemento2 = 'CEFET/RJ', 'Maria da Graça'

        deque = DequeDinamico(3)
        deque.insere_na_direita(elemento1)
        deque.insere_na_direita(elemento2)

        result = deque.get_ultimo_elemento()
        expected = elemento2

        self.assertEqual(expected, result.conteudo)

    def test_insere_na_esquerda(self):
        elemento1, elemento2 = 'CEFET/RJ', 'Maria da Graça'

        deque = DequeDinamico(3)
        deque.insere_na_esquerda(elemento1)
        deque.insere_na_esquerda(elemento2)

        result = deque.get_tamanho()
        expected = 2

        self.assertEqual(expected, result)

    def test_get_primeiro_elemento_inserindo_na_esquerda(self):
        elemento1, elemento2 = 'CEFET/RJ', 'Maria da Graça'

        deque = DequeDinamico(3)
        deque.insere_na_esquerda(elemento1)
        deque.insere_na_esquerda(elemento2)

        result = deque.get_primeiro_elemento()
        expected = elemento2

        self.assertEqual(expected, result.conteudo)

    def test_get_ultimo_elemento_inserindo_na_esquerda(self):
        elemento1, elemento2 = 'CEFET/RJ', 'Maria da Graça'

        deque = DequeDinamico(3)
        deque.insere_na_esquerda(elemento1)
        deque.insere_na_esquerda(elemento2)

        result = deque.get_ultimo_elemento()
        expected = elemento1

        self.assertEqual(expected, result.conteudo)

    def test_get_primeiro_elemento_inserindo_na_direita(self):
        elemento1, elemento2 = 'CEFET/RJ', 'Maria da Graça'

        deque = DequeDinamico(3)
        deque.insere_na_direita(elemento1)
        deque.insere_na_direita(elemento2)

        result = deque.get_primeiro_elemento()
        expected = elemento1

        self.assertEqual(expected, result.conteudo)

    def test_get_ultimo_elemento_inserindo_na_direita(self):
        elemento1, elemento2 = 'CEFET/RJ', 'Maria da Graça'

        deque = DequeDinamico(3)
        deque.insere_na_direita(elemento1)
        deque.insere_na_direita(elemento2)

        result = deque.get_ultimo_elemento()
        expected = elemento2

        self.assertEqual(expected, result.conteudo)

    def test_remove_na_esquerda(self):
        elemento1, elemento2 = 'CEFET/RJ', 'Maria da Graça'

        deque = DequeDinamico(3)
        deque.insere_na_direita(elemento1)
        deque.insere_na_direita(elemento2)

        result = deque.remove_na_esquerda()
        expected = elemento1

        self.assertEqual(expected, result.conteudo)

    def test_remove_na_direita(self):
        elemento1, elemento2 = 'CEFET/RJ', 'Maria da Graça'

        deque = DequeDinamico(3)
        deque.insere_na_direita(elemento1)
        deque.insere_na_direita(elemento2)

        result = deque.remove_na_direita()
        expected = elemento2

        self.assertEqual(expected, result.conteudo)

    def test_ordenar(self):
        test_sorted_list = ['a', 'b', 'c', 'd']

        deque = DequeDinamico(4)
        deque.insere_na_direita('d')
        deque.insere_na_direita('c')
        deque.insere_na_direita('b')
        deque.insere_na_direita('a')

        self.assertEqual(test_sorted_list, deque.ordena())

    def test_pesquisa(self):
        elemento = 'b'

        deque = DequeDinamico(4)
        deque.insere_na_direita('d')
        deque.insere_na_direita('c')
        deque.insere_na_direita('b')
        deque.insere_na_direita('a')

        expected = 'b'
        result = deque.pesquisa(elemento)

        self.assertEqual(expected, result)

    def test_remove_na_esquerda_quando_deque_estiver_vazio(self):
        self.assertRaises(Exception, DequeDinamico(3).remove_na_esquerda)

    def test_remove_na_direita_quando_deque_estiver_vazio(self):
        self.assertRaises(Exception, DequeDinamico(3).remove_na_direita)

    def test_pesquisa_quando_elemento_estiver_na_direita(self):
        elemento = 'd'

        deque = DequeDinamico(5)
        deque.insere_na_direita('d')
        deque.insere_na_direita('c')
        deque.insere_na_direita('b')
        deque.insere_na_direita('a')
        deque.insere_na_direita('e')

        expected = 'd'
        result = deque.pesquisa(elemento)

        self.assertEqual(expected, result)

    def test_pesquisa_quando_elemento_estiver_na_esquerda(self):
        elemento = 'b'

        deque = DequeDinamico(6)
        deque.insere_na_direita('d')
        deque.insere_na_direita('c')
        deque.insere_na_direita('b')
        deque.insere_na_direita('a')
        deque.insere_na_direita('e')

        expected = 'b'
        result = deque.pesquisa(elemento)

        self.assertEqual(expected, result)

    def test_pesquisa_quando_elemento_nao_existir(self):
        elemento = 'f'

        deque = DequeDinamico(5)
        deque.insere_na_direita('d')
        deque.insere_na_direita('c')
        deque.insere_na_direita('b')
        deque.insere_na_direita('a')
        deque.insere_na_direita('e')

        self.assertRaises(Exception, deque.pesquisa, elemento)

    def test_is_vazia(self):
        self.assertTrue(DequeDinamico(1).is_vazia())

    def test_listagem_quando_deque_estiver_vazio(self):
        self.assertRaises(Exception, DequeDinamico(1).all)

    def test_str_de_node(self):
        expected = 'Cristian'
        node = Node('Cristian')
        result = node.__str__()
        self.assertEqual(expected, result)

    def test_get_tamanho_apos_remocao(self):

        deque = DequeDinamico(5)
        deque.insere_na_direita('d')
        deque.insere_na_direita('c')
        deque.insere_na_direita('b')
        deque.insere_na_direita('a')
        deque.insere_na_direita('e')

        expected = 5
        result = deque.get_tamanho()

        self.assertEqual(expected, result)

        deque.remove_na_direita()
        deque.remove_na_direita()

        expected = 3
        result = deque.get_tamanho()

        self.assertEqual(expected, result)
