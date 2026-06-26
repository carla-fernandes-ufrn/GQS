from unittest import TestCase

import sys
sys.path.insert(0, '..')
from conexaoDB import *

DB = "TestDB.db"

class MockBD(TestCase):

    @classmethod
    def setUpClass(cls):
        con = conectar(DB)
        cursor = con.cursor()

        query_criar_tabela_usuario = """CREATE TABLE Usuario (
                          id int NOT NULL PRIMARY KEY ,
                          nome text NOT NULL,
                          email text NOT NULL
                        )"""
        query_criar_tabela_turma = """CREATE TABLE Turma (
                          id int NOT NULL PRIMARY KEY ,
                          numero int NOT NULL
                        )"""

        query_criar_tabela_disciplina = """CREATE TABLE Disciplina (
                          id int NOT NULL PRIMARY KEY ,
                          nome text NOT NULL
                        )"""
        try:
            cursor.execute(query_criar_tabela_usuario)
            cursor.execute(query_criar_tabela_turma)
            cursor.execute(query_criar_tabela_disciplina)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na criação das tabelas:", error)
        else:
            print("Criação das tabelas: OK")

        query_inserir_usuario = """INSERT INTO Usuario (id, nome, email) VALUES
                            (1, 'Carla F.', 'c@c.com'),
                            (2, 'Danilo', 'd@d.com'),
                            (3, 'Daniel', 'd2@d2.com'),
                            (4, 'Alice', 'a@a.com'),
                            (5, 'Ana carla', 'c@c.com'),
                            (6, 'maria carla fernandes', 'c@c.com')"""
        query_inserir_turma = """INSERT INTO Turma (id, numero) VALUES
                            (1, 23),
                            (2, 2),
                            (3, 8),
                            (4, 10)"""
        query_inserir_disciplina = """INSERT INTO Disciplina (id, nome) VALUES
                            (1, 'APOO'),
                            (2, 'GQS'),
                            (3, 'ALG'),
                            (4, 'PA I')"""
        try:
            cursor.execute(query_inserir_usuario)
            cursor.execute(query_inserir_turma)
            cursor.execute(query_inserir_disciplina)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na inserção de dados:", error)
        else:
            print("Inserção dos dados: OK")

        cursor.close()

        desconectar(con)

        testconfig ={
            'bd': DB
        }
        cls.mock_db_config = testconfig

    @classmethod
    def tearDownClass(cls):

        print("TearDown")
        con = conectar(DB)
        cursor = con.cursor()

        try:
            cursor.execute("DROP TABLE Usuario")
            cursor.execute("DROP TABLE Turma")
            cursor.execute("DROP TABLE Disciplina")
            con.commit()
            cursor.close()
            print("Removeu as tabelas do banco.")
        except sqlite3.Error as error:
            print("Banco de dados não existe. Erro na remoção do BD.", error)
        finally:
            desconectar(con)
