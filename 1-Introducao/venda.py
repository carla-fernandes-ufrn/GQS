class Venda:

    def __init__(self, usuario):
        self.usuario = usuario
        self.produtos = []

    def inserir_produto(self, produto, quantidade):

        produto.remover_estoque(quantidade)

        self.produtos.append((produto, quantidade))