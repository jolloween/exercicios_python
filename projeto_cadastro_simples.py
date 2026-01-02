import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_usuario(usuarios):
    while True:
        email = input("digite o e-mail: ")
        if "@" not in email:
            print("email inválido.")
            
        
        else:
            usuarios[email] = {}
            
            while True:
                nome = input("nome: ")
                if nome.isdigit():
                    print(f"Não pode conter números")
                    continue
                senha = input("senha: ")
                dados = {'nome' : nome, 'senha': senha}
                usuarios[email] = dados
                return

def listar_usuarios(usuarios):
    for k, v in usuarios.items():
        print(f"email: {k}")
        print(f"Nome: {v['nome']}")
        print(f"senha: {v['senha']}")

def buscar_usuario(usuarios):
    busca = input("Digite o email: ")
    if busca not in usuarios:
        print(f"{busca} email não cadastrado.")
    else:
        for email, senha in usuarios.items():
            if busca in usuarios:
                print(f"email: {email}")
                print(f"senha: {senha['senha']} ")

def remover_usuario(usuarios):
    email = input("Digite o email: ")
    if email in usuarios:
        del usuarios[email]
        print(f"{email} removido com sucesso.")
    else:
        print("Email não cadastrado")

def menu():
    print('[1] Cadastrar usuário')
    print('[2] Listar usuários')
    print('[3] Buscar usuário')
    print('[4] Remover usuário')
    print('[5] Sair')
usuarios = {'jp@email.com':{
            'nome': 'João',
            'senha': "1234"}
}

limpar_tela()
menu()

while True:
    try:
        opção = int(input("Escolha sua opção: "))
        if opção < 1 or opção > 5:
            print("⚠️  Código inválido.")
            continue
        else:
            break
    except ValueError:
        print("⚠️  Código inválido.")
        continue
match opção:
    case 1:
        cadastrar_usuario(usuarios)
    case 2:
        listar_usuarios(usuarios)
    case 3:
        buscar_usuario(usuarios)
    case 4:
        remover_usuario(usuarios)
    case 5:
        print("Programa encerrado...")
        exit()