from conexaoDB import ler_bd

def buscar_medicos_ativos_por_nome(bd, nome):
    query = """
        SELECT nome
        FROM medico
        WHERE status = 'ativo'
          AND LOWER(nome) LIKE LOWER(?)
    """

    # Adiciona os % para busca parcial
    param = f"%{nome}%"

    resultado = ler_bd(bd, query, (param,))

    return resultado

def buscar_medicos_por_estado(bd, estado):
    query = """
        SELECT nome
        FROM medico
        WHERE LOWER(estado) = LOWER(?)
    """

    resultado = ler_bd(bd, query, (estado,))

    return resultado