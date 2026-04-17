from models.produto import Produto
from models.usuario import Usuario
import json
import os

CAMINHO_PRODUTOS = "data/produtos.json"

def menu(resposta):
    try:
        resposta = int(resposta)
    except ValueError:
        print("Opção inválida. Por favor, digite um número.")
        return
    print("======================================================")
    print("Bem vindo à lojinha da Lana, o que deseja fazer hoje?")
    print("======================================================")
    print("1 - Ver produtos disponíveis")
    print("2 - Adicionar produto ao carrinho")
    print("3 - Remover produto do carrinho")
    print("4 - Listar produtos no carrinho")
    print("5 - Finalizar compra")
    print("0 - Sair")
    print("6 - Entrar como administrador")
    print("======================================================") 

def validar_resposta(resposta):
    try:
        resposta = int(resposta)
    except ValueError:
        print("Opção inválida. Por favor, digite um número.")
        return False
    if resposta > 6 or resposta < 0:
        print("Opção inválida. Por favor, escolha uma opção entre 0 e 6.")
        return False
    return True

while True:
    menu(0)
    resposta = input("Digite o número da opção desejada: ")
    if resposta == "0":
        print("Obrigado por visitar a lojinha da Lana! Volte sempre!")
        break
    if not validar_resposta(resposta):
        continue

    os.system(os.name == "nt" and "cls" or "clear")
    
    match resposta:
        case '1':
            print("Produtos Disponíveis:")
            with open(CAMINHO_PRODUTOS, "r") as a:
                produtos = json.load(a)
                for p in produtos:
                    print(f'ip: {p["id"]} - {p["nome"]} - R${p["preco"]:.2f} - Estoque: {p["quantidade"]}')
        case '2':
            ...