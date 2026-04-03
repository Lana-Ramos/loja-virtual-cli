from .produto import Produto
import json

caminho_produtos = 'data/produtos.json'

class Carrinho:
    def __init__(self):
        self.itens = []

    def __str__(self):
        return f"Carrinho com {len(self.itens)} itens"
    
    def __repr__(self):
        return f"Carrinho(itens={self.itens!r})"
    
    def adicionar_produto(self, produto, quantidade_produto):
        nome_produto = produto.nome_produto if isinstance(produto, Produto) else produto
        with open(caminho_produtos, 'r') as arquivo:
            produtos = json.load(arquivo) # carrega todos os produtos do arquivo JSON
            for p in produtos: # lê cada dicionário com os dados de cada produto
                if p["nome"].lower() == nome_produto.lower():
                    self.itens.append({"nome": p["nome"], "quantidade": quantidade_produto})
                    print(f"{quantidade_produto} unidades(s) de {nome_produto} adicionado(s) ao carrinho.")
                    produtos[produtos.index(p)]["quantidade"] -= quantidade_produto # diminui o estoque do produto
                    with open(caminho_produtos, 'w') as arquivo: # reescreve o arquivo JSON com o estoque atualizado
                        json.dump(produtos, arquivo, indent=4)
                    return
                print(f"Produto \'{nome_produto}\' não encontrado.")
                break    
    
    def remover_produto(self, produto):
        ...
