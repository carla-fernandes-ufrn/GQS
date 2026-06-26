from listas import *
from exceptions import *

import unittest

class TestOrdenacao (unittest.TestCase):
    def test_valor_valido(self):
        self.assertEqual(ordenacao([10, -10, 5, 0, 2, -2, 2, 1.9]), [-10, -2, 0, 1.9, 2, 2, 5, 10])
    
    def test_tipo_valor_invalido(self):
        self.assertRaises(TypeError, ordenacao, [10, -10, True, 0, 2, -2, 2, 1.9])
        self.assertRaises(TypeError, ordenacao, [10, -10, 0, 2, False, 2, 1.9])
        self.assertRaises(TypeError, ordenacao, [10, -10, "carla", 0, 2, -2, 2, 1.9])

class TestLocalizacao (unittest.TestCase):
    def test_valor_valido(self):
        self.assertEqual(menor_elemento([10, -10, 5, 0, 2, -2, 2, 1.9]), -10)
        self.assertEqual(menor_elemento([10, 10, -5, 0, -5, -2, 2, 1.9]), -5)
        self.assertEqual(posicao_menor_elemento([10, -10, 5, 0, 2, -2, 2, 1.9]), 1)
        self.assertEqual(posicao_menor_elemento([10, 10, -5, 0, -5, -2, 2, 1.9]), 2)
    
    def test_tipo_valor_invalido(self):
        self.assertRaises(TypeError, menor_elemento, [10, -10, True, 0, 2, -2, 2, 1.9])
        self.assertRaises(TypeError, menor_elemento, [10, -10, 0, 2, False, 2, 1.9])
        self.assertRaises(TypeError, menor_elemento, [10, -10, "carla", 0, 2, -2, 2, 1.9])
        self.assertRaises(TypeError, posicao_menor_elemento, [10, -10, True, 0, 2, -2, 2, 1.9])
        self.assertRaises(TypeError, posicao_menor_elemento, [10, -10, 0, 2, False, 2, 1.9])
        self.assertRaises(TypeError, posicao_menor_elemento, [10, -10, "carla", 0, 2, -2, 2, 1.9])