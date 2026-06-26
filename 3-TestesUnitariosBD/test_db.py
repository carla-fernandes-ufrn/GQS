from MockDB import MockBD

import sys
sys.path.insert(0, '..')
from conexaoDB import *
from queries_usuarios import *

class TestDB(MockBD):
    def test_select_all(self):
        retorno_esperado = [(1, 'Carla F.', 'c@c.com'),
                            (2, 'Danilo', 'd@d.com'),
                            (3, 'Daniel', 'd2@d2.com'),
                            (4, 'Alice', 'a@a.com'),
                            (5, 'Ana carla', 'c@c.com'),
                            (6, 'maria carla fernandes', 'c@c.com')]
        self.assertEqual(ler_todos_usuarios(self.mock_db_config.get('bd')), retorno_esperado)


    def test_filtro_nome(self):
        retorno_esperado = [('Carla F.',), ('Ana carla',), ('maria carla fernandes',)]
        self.assertEqual(ler_usuario_nome(self.mock_db_config.get('bd'), 'Carla'), retorno_esperado)
