from produto import Produto
from usuario import Usuario
from venda import Venda

produto1 = Produto("bolacha", 5.5, 10)
produto2 = Produto("chocolate", 7.5, 8)

usuario = Usuario("Carla")

venda = Venda(usuario)

venda.inserir_produto(produto1, 5)
venda.inserir_produto(produto2, 3)

for produto, qtd in venda.produtos:
    print(produto.nome, qtd)