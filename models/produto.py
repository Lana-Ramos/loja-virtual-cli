class Produto:
    def __init__(self, id_produto, nome_produto, preco_produto):
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto

    def __str__(self):
        return f"Produto: {self.nome_produto} (ID: {self.id_produto}) - Preço: R${self.preco_produto:.2f}"
    
    def __repr__(self):
        return f"Produto(id_produto={self.id_produto!r}, nome_produto={self.nome_produto!r}, preco_produto={self.preco_produto!r})"
