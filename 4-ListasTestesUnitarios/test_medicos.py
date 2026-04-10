import unittest
from medicos import *

class TestMedicoComMaisHoras(unittest.TestCase):

    def test_caso_normal_varios_medicos(self):
        dados = [
            {"nome": "Dr. João", "horas": 120},
            {"nome": "Dra. Maria", "horas": 150},
            {"nome": "Dr. Pedro", "horas": 100},
        ]

        resultado = medico_com_mais_horas(dados)

        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]["nome"], "Dra. Maria")
        self.assertEqual(resultado[0]["horas"], 150)

    def test_lista_vazia(self):
        dados = []

        resultado = medico_com_mais_horas(dados)

        self.assertEqual(resultado, [])

    def test_empate_entre_medicos(self):
        dados = [
            {"nome": "Dr. João", "horas": 150},
            {"nome": "Dra. Maria", "horas": 150},
            {"nome": "Dr. Pedro", "horas": 100},
        ]

        resultado = medico_com_mais_horas(dados)

        self.assertEqual(len(resultado), 2)

        nomes = [medico["nome"] for medico in resultado]
        self.assertIn("Dr. João", nomes)
        self.assertIn("Dra. Maria", nomes)

        for medico in resultado:
            self.assertEqual(medico["horas"], 150)

class TestPercentualRendaPorHospital(unittest.TestCase):

    def test_caso_normal_varios_hospitais(self):
        dados = [
            {"hospital": "Hospital A", "valor": 4000},
            {"hospital": "Hospital B", "valor": 6000},
        ]

        resultado = percentual_renda_por_hospital(dados)

        self.assertEqual(len(resultado), 2)

        esperado = {
            "Hospital A": 40.00,
            "Hospital B": 60.00
        }

        for item in resultado:
            self.assertAlmostEqual(
                item["percentual"],
                esperado[item["hospital"]],
                places=2
            )

    def test_sem_renda_no_mes(self):
        dados = []

        resultado = percentual_renda_por_hospital(dados)

        self.assertEqual(resultado, [])

    def test_arredondamento_duas_casas_decimais(self):
        dados = [
            {"hospital": "Hospital A", "valor": 1000},
            {"hospital": "Hospital B", "valor": 1045},
            {"hospital": "Hospital C", "valor": 1046},
            {"hospital": "Hospital D", "valor": 1043},
        ]

        resultado = percentual_renda_por_hospital(dados)

        # Soma total = 4134
        # Percentuais esperados (aproximados):
        esperado = {
            "Hospital A": 24.19,
            "Hospital B": 25.28,
            "Hospital C": 25.30,  # arredondou pra baixo
            "Hospital D": 25.23,
        }

        for item in resultado:
            self.assertAlmostEqual(
                item["percentual"],
                esperado[item["hospital"]],
                places=2
            )

class TestPercentualMedioPorHospital(unittest.TestCase):

    def test_caso_normal_varios_meses(self):
        dados = [
            {"mes": "Maio", "hospital": "Hospital A", "valor": 1000},
            {"mes": "Maio", "hospital": "Hospital B", "valor": 2000},
            {"mes": "Maio", "hospital": "Hospital C", "valor": 500},
            {"mes": "Junho", "hospital": "Hospital A", "valor": 400},
            {"mes": "Julho", "hospital": "Hospital A", "valor": 2000},
            {"mes": "Julho", "hospital": "Hospital D", "valor": 300},
        ]

        resultado = percentual_medio_por_hospital(dados)

        esperado = {
            "Hospital A": 54.84,
            "Hospital B": 32.26,
            "Hospital C": 8.06,
            "Hospital D": 4.84,
        }

        self.assertEqual(len(resultado), 4)

        for item in resultado:
            self.assertAlmostEqual(
                item["percentual"],
                esperado[item["hospital"]],
                places=2
            )

    def test_lista_vazia(self):
        dados = []

        resultado = percentual_medio_por_hospital(dados)

        self.assertEqual(resultado, [])

    def test_todos_valores_zero(self):
        dados = [
            {"mes": "Maio", "hospital": "Hospital A", "valor": 0},
            {"mes": "Junho", "hospital": "Hospital B", "valor": 0},
        ]

        resultado = percentual_medio_por_hospital(dados)

        for item in resultado:
            self.assertEqual(item["percentual"], 0.00)

    def test_arredondamento_duas_casas(self):
        dados = [
            {"mes": "Maio", "hospital": "Hospital A", "valor": 1000},
            {"mes": "Maio", "hospital": "Hospital B", "valor": 1045},
            {"mes": "Junho", "hospital": "Hospital C", "valor": 1046},
            {"mes": "Julho", "hospital": "Hospital D", "valor": 1043},
        ]

        resultado = percentual_medio_por_hospital(dados)

        esperado = {
            "Hospital A": 24.19,
            "Hospital B": 25.28,
            "Hospital C": 25.30,
            "Hospital D": 25.23,
        }

        for item in resultado:
            self.assertAlmostEqual(
                item["percentual"],
                esperado[item["hospital"]],
                places=2
            )


if __name__ == "__main__":
    unittest.main()