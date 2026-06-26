from conexaoDB import *

def ler_todos_usuarios(bd):
    return ler_bd(bd, "SELECT * FROM Usuario")

def ler_usuario_nome(bd, nome):
    query = "SELECT nome FROM Usuario WHERE upper(nome) LIKE ?"
    return ler_bd(bd, query, ('%'+nome.upper()+'%',))
