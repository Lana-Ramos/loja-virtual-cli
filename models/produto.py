class Produto:
    def __init__(self, id_produto, nome_produto, preco_produto, quantidade_produto):
        self.id_produto = id_produto
        self._nome_produto = nome_produto
        self.preco_produto = preco_produto
        self.quantidade_produto = quantidade_produto

    @property
    def nome_produto(self):
        return self._nome_produto

    @nome_produto.setter
    def nome_produto(self, valor):
        self._nome_produto = valor

    def __str__(self):
        return f"Produto: {self.nome_produto} (ID: {self.id_produto}) - Preço: R${self.preco_produto:.2f} - Quantidade: {self.quantidade_produto}"
    
    def __repr__(self):
        return f"Produto(id_produto={self.id_produto!r}, nome_produto={self.nome_produto!r}, preco_produto={self.preco_produto!r}, quantidade_produto={self.quantidade_produto!r})"
