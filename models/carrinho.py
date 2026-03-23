class Carrinho:
    def __init__(self):
        self.itens = []

    def __str__(self):
        return f"Carrinho com {len(self.itens)} itens"
    
    def __repr__(self):
        return f"Carrinho(itens={self.itens!r})"
    
    