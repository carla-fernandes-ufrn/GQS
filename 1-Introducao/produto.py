from exceptions import EstoqueInsuficiente

class Produto:

    def __init__(self, nome, valor, estoque):
        self.nome = nome
        self.valor = valor
        self.estoque = estoque

    def remover_estoque(self, quantidade):
        if quantidade > self.estoque:
            raise EstoqueInsuficiente(
                f"Produto {self.nome} não possui estoque suficiente"
            )

        self.estoque -= quantidade
        return True