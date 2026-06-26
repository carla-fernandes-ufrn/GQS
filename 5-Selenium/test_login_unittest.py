import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_login_com_sucesso(self):

        self.driver.get(
            "http://localhost:8000/login.html"
        )

        usuario = self.driver.find_element(
            By.ID,
            "usuario"
        )

        senha = self.driver.find_element(
            By.ID,
            "senha"
        )

        botao = self.driver.find_element(
            By.ID,
            "login"
        )

        usuario.send_keys("admin")
        senha.send_keys("123")

        botao.click()

        mensagem = self.driver.find_element(
            By.ID,
            "msg"
        )

        self.assertEqual(
            mensagem.text,
            "Bem-vindo!"
        )
    
    def test_login_sem_sucesso(self):

        self.driver.get(
            "http://localhost:8000/login.html"
        )

        usuario = self.driver.find_element(
            By.ID,
            "usuario"
        )

        senha = self.driver.find_element(
            By.ID,
            "senha"
        )

        botao = self.driver.find_element(
            By.ID,
            "login"
        )

        usuario.send_keys("carla")
        senha.send_keys("123")

        botao.click()

        mensagem = self.driver.find_element(
            By.ID,
            "msg"
        )

        self.assertEqual(
            mensagem.text,
            "Login invalido"
        )


if __name__ == "__main__":
    unittest.main()