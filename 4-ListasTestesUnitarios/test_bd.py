import unittest
import sys

sys.path.insert(0, '..')

from MockDB import MockBD
from queries_medicos import *

class TestBuscaMedicosAtivos(MockBD):

    def test_busca_por_nome_parcial(self):
        resultado = buscar_medicos_ativos_por_nome(
            self.mock_db_config['bd'],
            "carla"
        )

        nomes = [linha[0] for linha in resultado]

        self.assertIn("Carla Souza", nomes)
        self.assertIn("Ana Carla Fernandes", nomes)
        self.assertIn("João da Carla Silva", nomes)

    def test_ignora_maiusculo_minusculo(self):
        resultado = buscar_medicos_ativos_por_nome(
            self.mock_db_config['bd'],
            "CARLA"
        )

        nomes = [linha[0] for linha in resultado]

        self.assertIn("Carla Souza", nomes)
        self.assertIn("Ana Carla Fernandes", nomes)
        self.assertIn("João da Carla Silva", nomes)

    def test_nao_retorna_inativos(self):
        resultado = buscar_medicos_ativos_por_nome(
            self.mock_db_config['bd'],
            "carla"
        )

        nomes = [linha[0] for linha in resultado]

        self.assertNotIn("Carla Inativa", nomes)

    def test_retorna_todos_os_medicos_corretos(self):
        resultado = buscar_medicos_ativos_por_nome(
            self.mock_db_config['bd'],
            "carla"
        )

        nomes = [linha[0] for linha in resultado]

        esperado = {
            "Carla Souza",
            "Ana Carla Fernandes",
            "João da Carla Silva"
        }

        self.assertEqual(set(nomes), esperado)

class TestBuscaMedicosPorEstado(MockBD):

    def test_retorna_medicos_do_estado(self):
        resultado = buscar_medicos_por_estado(
            self.mock_db_config['bd'],
            "RN"
        )

        nomes = [linha[0] for linha in resultado]

        # Médicos que estão no RN (baseado no mock)
        self.assertIn("Dr. João", nomes)
        self.assertIn("Dra. Maria", nomes)

    def test_nao_retorna_medicos_de_outros_estados(self):
        resultado = buscar_medicos_por_estado(
            self.mock_db_config['bd'],
            "RN"
        )

        nomes = [linha[0] for linha in resultado]

        # Esse é da PB (mock inicial)
        self.assertNotIn("Dr. Pedro", nomes)

    def test_estado_inexistente(self):
        resultado = buscar_medicos_por_estado(
            self.mock_db_config['bd'],
            "SP"
        )

        self.assertEqual(resultado, [])

    def test_case_insensitive_estado(self):
        resultado = buscar_medicos_por_estado(
            self.mock_db_config['bd'],
            "rn"
        )

        nomes = [linha[0] for linha in resultado]

        self.assertIn("Dr. João", nomes)
        self.assertIn("Dra. Maria", nomes)

    def test_retorna_todos_do_estado(self):
        resultado = buscar_medicos_por_estado(
            self.mock_db_config['bd'],
            "RN"
        )

        nomes = [linha[0] for linha in resultado]

        esperado = {
            "Dr. João",
            "Dra. Maria",
            "Carla Souza",
            "Ana Carla Fernandes",
            "João da Carla Silva",
            "Carla Inativa",  # importante: aqui NÃO filtramos status
        }

        self.assertEqual(set(nomes), esperado)

if __name__ == "__main__":
    unittest.main()