from models.produto import Produto
from models.usuario import Usuario
import json
import os

p1 = Produto(1, "Notebook", 3500.00)
p2 = Produto(2, "Smartphone", 1500.00)
u1 = Usuario(1, "Alice")

print(p1)
print(p2)

print(u1.carrinho)

with open('produtos.json', 'a') as f:
    ...