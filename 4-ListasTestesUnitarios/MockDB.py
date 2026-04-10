from unittest import TestCase
import sqlite3
import sys

sys.path.insert(0, '..')
from conexaoDB import *

DB = "TestDB.db"


class MockBD(TestCase):

    @classmethod
    def setUpClass(cls):
        con = conectar(DB)
        cursor = con.cursor()

        # 🔹 Criação das tabelas
        queries_criacao = [
            """
            CREATE TABLE IF NOT EXISTS medico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                crm TEXT,
                estado TEXT,
                status TEXT
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS hospital (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS horas_plantao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                medico_id INTEGER,
                hospital_id INTEGER,
                horas INTEGER,
                dia TEXT,
                turno TEXT,
                FOREIGN KEY (medico_id) REFERENCES medico(id),
                FOREIGN KEY (hospital_id) REFERENCES hospital(id)
            );
            """
        ]

        try:
            for query in queries_criacao:
                cursor.execute(query)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na criação das tabelas:", error)
        else:
            print("Criação das tabelas: OK")

        # 🔹 Inserção de dados
        queries_insercao = [
            # Médicos
            ("INSERT INTO medico (nome, crm, estado, status) VALUES (?, ?, ?, ?)",
             ("Dr. João", "12345", "RN", "ativo")),
            ("INSERT INTO medico (nome, crm, estado, status) VALUES (?, ?, ?, ?)",
             ("Dra. Maria", "67890", "RN", "ativo")),
            ("INSERT INTO medico (nome, crm, estado, status) VALUES (?, ?, ?, ?)",
             ("Dr. Pedro", "11111", "PB", "inativo")),
             ("INSERT INTO medico (nome, crm, estado, status) VALUES (?, ?, ?, ?)",
            ("Carla Souza", "22222", "RN", "ativo")),

            ("INSERT INTO medico (nome, crm, estado, status) VALUES (?, ?, ?, ?)",
            ("Ana Carla Fernandes", "33333", "RN", "ativo")),

            ("INSERT INTO medico (nome, crm, estado, status) VALUES (?, ?, ?, ?)",
            ("João da Carla Silva", "44444", "RN", "ativo")),

            # Mesmo padrão mas INATIVO (não deve aparecer)
            ("INSERT INTO medico (nome, crm, estado, status) VALUES (?, ?, ?, ?)",
            ("Carla Inativa", "55555", "RN", "inativo")),

            # Hospitais
            ("INSERT INTO hospital (nome) VALUES (?)", ("Hospital A",)),
            ("INSERT INTO hospital (nome) VALUES (?)", ("Hospital B",)),
            ("INSERT INTO hospital (nome) VALUES (?)", ("Hospital C",)),

            # Plantões
            ("INSERT INTO horas_plantao (medico_id, hospital_id, horas, dia, turno) VALUES (?, ?, ?, ?, ?)",
             (1, 1, 12, "2026-04-01", "manha")),
            ("INSERT INTO horas_plantao (medico_id, hospital_id, horas, dia, turno) VALUES (?, ?, ?, ?, ?)",
             (1, 2, 8, "2026-04-02", "tarde")),
            ("INSERT INTO horas_plantao (medico_id, hospital_id, horas, dia, turno) VALUES (?, ?, ?, ?, ?)",
             (2, 1, 10, "2026-04-01", "noite")),
            ("INSERT INTO horas_plantao (medico_id, hospital_id, horas, dia, turno) VALUES (?, ?, ?, ?, ?)",
             (2, 3, 6, "2026-04-03", "manha")),
        ]

        try:
            for query, params in queries_insercao:
                cursor.execute(query, params)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na inserção de dados:", error)
        else:
            print("Inserção dos dados: OK")

        cursor.close()
        desconectar(con)

        cls.mock_db_config = {
            'bd': DB
        }

    @classmethod
    def tearDownClass(cls):
        print("TearDown")

        con = conectar(DB)
        cursor = con.cursor()

        queries_drop = [
            "DROP TABLE IF EXISTS horas_plantao;",
            "DROP TABLE IF EXISTS medico;",
            "DROP TABLE IF EXISTS hospital;"
        ]

        try:
            for query in queries_drop:
                cursor.execute(query)
            con.commit()
            print("Removeu as tabelas do banco.")
        except sqlite3.Error as error:
            print("Erro na remoção das tabelas:", error)
        finally:
            cursor.close()
            desconectar(con)