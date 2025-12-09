# 3. Agenda Telefônica

# Crie um programa que:

# Armazene contatos em um dicionário no formato:
# { "nome": "telefone" }

# Tenha uma função para adicionar contatos.

# Outra função para buscar um contato pelo nome.

# Use um loop para permitir várias buscas.

# Use condições para informar se o contato existe ou não.
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

agenda = {
    'pedro' : 123456789,
    'lais' :  987654321,
    'fabio': 123456788,
    'natalia' : 456789123,
    'goncalo': 666666666
}

def buscar_contato(buscar_nome, agenda):
    if buscar_nome not in agenda:
        print(f'{buscar_nome} não constas na agenda')
    else:
        print(agenda[buscar_nome])
    

def adicionar_contatos(agenda, nome, telefone):
    agenda[nome] = telefone #Adiciona ou atualiza contato

def editar_contato():
    while True:
        print("-" * 30)
        print("Contatos".center(30))
        contatos = sorted(agenda.keys())
        print("-" * 30)
        print(f"{'cod':<5} {'Nome':<15} {'Telefone':<15}")
        print("-" * 30)
        for i, nome in enumerate(sorted(contatos)):
            print(f" {i+1}    {nome:<15} {agenda[nome]:<15}")
        
        escolha = input("Digite o número do contato que desejar alterar ou '0' para sair: ")
        
        try:
            if escolha.isdigit():
                escolha_int = int(escolha)
                
            else:
                print("Digite um indice válido")
        except ValueError:
            print("Digite um indice válido")
        
        if escolha_int == 0:
            break
        elif escolha_int < 0 or escolha_int > len(contatos):
            print("Opção inválida. Tente novamente.")
        
        #Seleciona o contato
        nome_antigo = contatos[escolha_int -1]

        #Seleciona novos dados

        novo_nome = input(f"Novo nome (Enter para manter '{nome_antigo}'): ")
        if novo_nome == '':
            novo_nome = nome_antigo

        novo_telefone = input(f"Novo telefone (enter para manter '{agenda[nome_antigo]}'): ")
        if novo_telefone == "":
            novo_telefone = agenda[nome_antigo]
        else:
            novo_telefone = int(novo_telefone)

        #atualiza agenda

        if novo_nome != nome_antigo:
            del agenda[nome_antigo]
        
        agenda[novo_nome] = novo_telefone

while True:
    
    print("[1] para adicionar contato\n"
            "[2] editar contatos\n"
            "[3] para buscar contatos\n"
            "[4] para sair\n")

    opcao = int(input("Qual opção desejas: "))


    if opcao == 1:
        while True:
            nome = input("Nome: ")
            telefone = int(input('Telefone:'))

            adicionar_contatos(agenda, nome, telefone)
            resp = input("Quer continuar [S] para sim e [N] para não? ").upper()

            if resp == "N":
                break
    elif opcao == 2:
                
        editar_contato()

    
    elif opcao == 3:
        buscar_nome = input("Digite o nome da busca: ")

        buscar_contato(buscar_nome, agenda)
        while True:
            resp = input("Quer continuar [S] para sim e [N] para não? ").upper()

            break
    else:
        break

print("-" * 30)
print("      AGENDA FINAL")
print("-" * 30)
print(f"{'Nome':<15} {'Telefone':<15}")
print("-" * 30)

for nome in sorted(agenda.keys()):
    print(f"{nome:<15} {agenda[nome]:<15}")