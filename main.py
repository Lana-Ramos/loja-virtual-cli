from models.produto import Produto
from models.usuario import Usuario

p1 = Produto(1, "Notebook", 3500.00, 5)
p2 = Produto(2, "Smartphone", 1500.00, 10)
u1 = Usuario(1, "Alice")

u1.carrinho.adicionar_produto(p1, 2)
u1.carrinho.adicionar_produto("Produto A", 1)
print(u1.carrinho)
