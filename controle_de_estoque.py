# 2. Controle de Estoque

# Faça um programa que:

# Tenha um dicionário com produtos e quantidades.

# Use uma função para remover uma quantidade do estoque.

# Utilize um loop para permitir várias operações.

# Antes de remover, use condições para verificar se há estoque suficiente.

# Imprima o estoque atualizado ao final.

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

estoque = {
    "arroz": 10,
    "feijão": 5,
    "macarrão": 8
    }

def remover_estoque(produto, quantidade, estoque):
    limpar_tela()
    if produto not in estoque:
        print(f"❌ Produto '{produto}' não existe no estoque.")
        return
    if quantidade > estoque[produto]:
        print(f'estoque insuficiente de {estoque}. Disponível: {estoque[produto]} ')
        return
    estoque[produto] -= quantidade
    

while True:
    limpar_tela()
    print("=-" *20)
    for p, q in estoque.items():
        print(f'{p}: {q}')
    print("=-" *20)
    produto = input("Digite o produto que deseja remover: ").lower()

    try:
        quantidade = int(input("Digite a quantidade: "))
    except ValueError:
        print('ERRO! Digite um número válido.')
        continue

    remover_estoque(produto, quantidade, estoque)

    resp = input("Quer continuar [S] para sim e [N] para não? ").strip().upper()
    limpar_tela()
    
    if resp == 'N':
        break


print("\n=== Estoque atualizado ===")
for p, q in estoque.items():
    print(f'{p}: {q}')