from .produto import Produto
import json

CAMINHO_PRODUTOS = 'data/produtos.json'

class Carrinho:
    def __init__(self):
        self.itens = []

    def __str__(self):
        return f"Carrinho com {len(self.itens)} itens"
    
    def __repr__(self):
        return f"Carrinho(itens={self.itens!r})"
    
    def atualizar_json(self, produto, quantidade, operacao):
        with open(CAMINHO_PRODUTOS, 'r') as arquivo: # reescreve o arquivo JSON com o estoque atualizado
            produtos = json.load(arquivo)
            for dicionario in produtos:
                if dicionario["quantidade"] < quantidade:
                    print(f"Não há estoque suficiente para {produto['nome']}. Quantidade disponível: {dicionario['quantidade']}")
                    return False
                if dicionario["nome"].lower() == produto["nome"].lower():
                    if operacao == "adicionar":
                        produtos[produtos.index(dicionario)]["quantidade"] -= quantidade
                    elif operacao == "remover":
                        produtos[produtos.index(dicionario)]["quantidade"] += quantidade
                    break
        with open(CAMINHO_PRODUTOS, 'w') as arquivo:
            json.dump(produtos, arquivo, indent=4)
            return True

    def adicionar_produto(self, produto, quantidade_produto):
        nome_produto = produto.nome_produto if isinstance(produto, Produto) else produto
        
        if quantidade_produto <= 0:
            print("A quantidade deve ser maior que zero.")
            return
        
        with open(CAMINHO_PRODUTOS, 'r') as arquivo:
            produtos = json.load(arquivo) # carrega todos os produtos do arquivo JSON
            
            for item in self.itens: # verifica se o produto já está no carrinho
                if nome_produto.lower() == item["nome"].lower():
                    item["quantidade"] += quantidade_produto
                    print(f"{quantidade_produto} unidades(s) de {nome_produto} adicionado(s) ao carrinho.")
                    self.atualizar_json(item, quantidade_produto, "adicionar") # atualiza o arquivo JSON com a nova quantidade
                    return
                    
            for p in produtos: # lê cada dicionário com os dados de cada produto
                if p["nome"].lower() == nome_produto.lower():
                    if self.atualizar_json(p, quantidade_produto, "adicionar"): # atualiza o arquivo JSON com a nova quantidade
                        self.itens.append({"nome": p["nome"], "quantidade": quantidade_produto})
                        print(f"{quantidade_produto} unidades(s) de {nome_produto} adicionado(s) ao carrinho.")
                        return

            print(f"Produto \'{nome_produto}\' não encontrado.")    
    
    def remover_produto(self, nome_produto, quantidade):   
        for i in self.itens: # tem dicionários com nome e quantidade
            if nome_produto.lower() == i["nome"].lower():
                if i["quantidade"] <= quantidade:
                    self.itens.remove(i)
                else:
                    i["quantidade"] -= quantidade
                print(f"{quantidade} unidades(s) de {nome_produto} removida(s) do carrinho.")
                self.atualizar_json(i, quantidade, "remover") # atualiza o arquivo JSON com a nova quantidade
                return                
        print("Produto não encontrado")
    
    def listar_produtos(self):
        if len(self.itens) == 0:
            print("O carrinho está vazio.")
            return
        
        print("Produtos no carrinho:")
        for item in self.itens:
            print(f'{item["quantidade"]}x {item["nome"]}')
