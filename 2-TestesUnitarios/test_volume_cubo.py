 
from volume_cubo import *
from exceptions import *

import unittest

class TestVolumeCubo (unittest.TestCase):
    def test_valor_valido(self):
        self.assertEqual(volume_cubo(3), 27)
        self.assertEqual(volume_cubo(2.5), 15.63)
        self.assertEqual(volume_cubo(2.8), 21.95)
    
    def test_valor_invalido(self):
        self.assertRaises(ValorInvalido, volume_cubo, 0)
        self.assertRaises(ValorInvalido, volume_cubo, -1)
    
    def test_tipo_valor_invalido(self):
        self.assertRaises(TypeError, volume_cubo, True)
        self.assertRaises(TypeError, volume_cubo, False)
        self.assertRaises(TypeError, volume_cubo, "carla")