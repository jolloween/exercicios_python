# 2. Controle de Presença

# Dicionário {aluno: presença(True/False)}

# Função para marcar presença.

# Informar total de presentes e ausentes.

presenca = {
        "Lais": False,
        "Maria": False,
        "Priscila": False,
        "Natália": False,
        "Patricia": False,
        "Relly": False,
        "Felipe": False,
        "João": False
}

def marcar_presenca(presenca):
    global presentes, ausentes
    presentes = 0
    ausentes = 0
    for aluno in presenca:
        if aluno in presenca:
            while True:
                situacao = input(f"{aluno} está presente? [S/N] ").upper()
                if situacao not in ('S', 'N'):
                    print('⚠️ Por favor, digite "S" para sim e "N" para não.' )
                else:
                    break
        if situacao == 'S':
            presenca[aluno] = True
            presentes += 1
        else:
            presenca[aluno] = False
            ausentes +=1
        
    

    # global presentes, ausentes
    # presentes = 0
    # ausentes = 0
    # if aluno not in presenca:
    #     print(f"{aluno} não consta na lista de presença!")
    # if aluno in presenca:
    #     while True:
    #         situação = input(f" {aluno} está presente? [S/N]").upper()
    #         if situação not in ('S', 'N'):
    #             print('⚠️ Por favor, digite "S" para sim e "N" para não.')
    #             continue
    #         if situação == 'S':
    #             presenca[aluno] = True
    #             presentes += 1
    #             break
    #         else:
    #             presenca[aluno] = False
    #             ausentes += 1
    #             break



import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


limpar_tela()


marcar_presenca(presenca)
# while True:
#     resp = input('deseja continuar? [S/N]').upper()
#     if resp not in ('S', 'N'):
#         print('⚠️ Por favor, digite "S" para sim e "N" para não.')
#     else:
#         break
#     if resp == "N":
#         break


for nome, presente_ou_ausente in presenca.items():
    print('=-' *20)
    situacao = 'Presente' if presente_ou_ausente else "Ausente"
    print(f"Nome: {nome} | Situação: {situacao}")
print('=-' *20)
print("")
print('>>> total de presentes e ausentes <<<')
print(f"      Total de presentes foi: {presentes}")
print(f"      Total de ausentes foi: {ausentes}")