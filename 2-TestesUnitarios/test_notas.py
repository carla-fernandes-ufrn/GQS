from notas import *
from exceptions import *

import unittest

class TestNotaParaAprovacao (unittest.TestCase):
    def test_valor_valido(self):
        self.assertEqual(terceira_nota(10, 5), 6)
        self.assertEqual(terceira_nota(2, 5), 14)
    
    def test_valor_invalido(self):
        self.assertRaises(ValorInvalido, terceira_nota, -4, 6)
        self.assertRaises(ValorInvalido, terceira_nota, 4, -6)
    
    def test_tipo_valor_invalido(self):
        self.assertRaises(TypeError, terceira_nota, True, 10)
        self.assertRaises(TypeError, terceira_nota, 10, True)
        self.assertRaises(TypeError, terceira_nota, 5, "danilo")
        self.assertRaises(TypeError, terceira_nota, "danilo", 5)

class TestDadosAprovacao (unittest.TestCase):

    def test_arredondamento(self):
        self.assertEqual(arredondamento(6.765), 6.77)
        self.assertEqual(arredondamento(6.762), 6.76)
        self.assertEqual(arredondamento(6.768), 6.77)

    def test_valor_valido(self):
        # 12 no total
        # aprovados = Carla, Carla2, Danilo2 = 25%
        # aprovados_4a_prova = Daniel, Daniel2 = 16,67%
        # reprovados_nota = Alice, Silvia, Alice2, Silvia2 = 33,33%
        # reprovaod_falta = Danilo, Flávio, Flávio2 = 25%
        situacao = [
            ('Carla', 7.8, False, False),
            ('Danilo', 7.8, True, False),
            ('Daniel', 7.8, False, True),
            ('Alice', 5.4, False, True),
            ('Flávio', 5.4, True, True),
            ('Silvia', 5.4, False, False),
            ('Carla2', 8.4, False, False),
            ('Danilo2', 9.9, False, False),
            ('Daniel2', 10, False, True),
            ('Alice2', 2, False, True),
            ('Flávio2', 4, True, True),
            ('Silvia2', 3, False, False)
        ]

        self.assertEqual(dados_aprovacao(situacao), (25, 16.67, 33.33, 25))
        self.assertEqual(dados_aprovacao([]), (0,0,0,0))