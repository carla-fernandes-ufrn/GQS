import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestNavegacao(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/index.html")

    def tearDown(self):
        self.driver.quit()

    def test_pagina_inicial_tem_titulo_correto(self):
        self.assertEqual(self.driver.title, "Página Inicial")

        titulo = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(titulo.text, "Página Inicial")

    def test_navega_para_pagina_sobre(self):
        link_sobre = self.driver.find_element(By.ID, "link-sobre")
        link_sobre.click()

        titulo = self.driver.find_element(By.TAG_NAME, "h1")

        self.assertEqual(self.driver.title, "Sobre")
        self.assertEqual(titulo.text, "Sobre o Sistema")

    def test_navega_para_pagina_contato_e_envia_mensagem(self):
        link_contato = self.driver.find_element(By.ID, "link-contato")
        link_contato.click()

        nome = self.driver.find_element(By.ID, "nome")
        email = self.driver.find_element(By.ID, "email")
        mensagem = self.driver.find_element(By.ID, "mensagem")
        botao = self.driver.find_element(By.ID, "enviar")

        nome.send_keys("Maria")
        email.send_keys("maria@email.com")
        mensagem.send_keys("Gostaria de mais informações.")

        botao.click()

        resultado = self.driver.find_element(By.ID, "resultado")

        self.assertEqual(
            resultado.text,
            "Mensagem enviada com sucesso"
        )

    def test_volta_para_pagina_inicial(self):
        link_sobre = self.driver.find_element(By.ID, "link-sobre")
        link_sobre.click()

        link_inicio = self.driver.find_element(By.ID, "link-inicio")
        link_inicio.click()

        titulo = self.driver.find_element(By.TAG_NAME, "h1")

        self.assertEqual(self.driver.title, "Página Inicial")
        self.assertEqual(titulo.text, "Página Inicial")

    def test_contato_com_campos_vazios(self):
        link_contato = self.driver.find_element(By.ID, "link-contato")
        link_contato.click()

        botao = self.driver.find_element(By.ID, "enviar")
        botao.click()

        resultado = self.driver.find_element(By.ID, "resultado")

        self.assertEqual(
            resultado.text,
            "Preencha todos os campos"
        )


if __name__ == "__main__":
    unittest.main()