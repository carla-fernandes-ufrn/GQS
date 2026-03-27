from exceptions import *

from decimal import Decimal, ROUND_HALF_UP

def terceira_nota (nota1, nota2):
    if (isinstance(nota1, bool) or isinstance(nota2, bool) or
        not isinstance(nota1, (int, float)) or not isinstance(nota2, (int, float))):
        raise TypeError('O valor indicado como nota deve ser inteiro ou real.')
    
    if (nota1 < 0 or nota2 < 0):
        raise ValorInvalido("O valor da nota não pode ser negativo")

    return 21-nota1-nota2

def arredondamento(numero):
    d = Decimal(str(numero))
    formato = '0.00'
    return float(d.quantize(Decimal(formato), rounding=ROUND_HALF_UP))

# [('Nome', nota, reprovou_falta, fez_quarta_prova), (), ()]
# (aprovados, aprovados_quarta_prova, reprovados_nota, reprovados_falta)
def dados_aprovacao(dados):
    qnt_alunos = len(dados)

    if (qnt_alunos == 0):
        return (0,0,0,0)

    aprovados = 0
    aprovados_quarta_prova = 0
    reprovados_nota = 0
    reprovados_falta = 0

    for aluno in dados:
        if aluno[2]:
            reprovados_falta+=1
        elif aluno[1] >= 7 and aluno[3] == False:
            aprovados += 1
        elif aluno[1] >= 7 and aluno[3] == True:
            aprovados_quarta_prova += 1
        else:
            reprovados_nota += 1
    
    aprovados = 100*aprovados/qnt_alunos
    aprovados_quarta_prova = 100*aprovados_quarta_prova/qnt_alunos
    reprovados_nota = 100*reprovados_nota/qnt_alunos
    reprovados_falta = 100*reprovados_falta/qnt_alunos

    return (arredondamento(aprovados), arredondamento(aprovados_quarta_prova),
            arredondamento(reprovados_nota), arredondamento(reprovados_falta))