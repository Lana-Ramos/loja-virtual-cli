from models.carrinho import Carrinho

class Usuario:
    def __init__(self, id_usuario, nome_usuario):
        self.id_usuario = id_usuario
        self.nome_usuario = nome_usuario
        self.carrinho = Carrinho()

    def __str__(self):
        return f"Usuário {self.id_usuario}: {self.nome_usuario}"
    
    def __repr__(self):
        return f"Usuario(id_usuario={self.id_usuario!r}, nome_usuario={self.nome_usuario!r})"
    