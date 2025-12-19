# 6. Sistema de Reservas de Hotel

# Crie um programa que:

# Tenha quartos armazenados com:
# {numero: {"tipo": "solteiro/casal", "ocupado": True/False}}

# Função para reservar quarto (mudar status).

# Verificar se está livre.

# Loop para operações.

# Mostrar relatório final com quartos ocupados e livres.


quartos = {
        101 : {'tipo': 'solteiro', 'situacao': False},
        102 : {'tipo': 'solteiro', 'situacao': True},
        201 : {'tipo': 'casal', 'situacao': False},
        202 : {'tipo': 'casal', 'situacao': True},
        301 : {'tipo': 'solteiro', 'situacao': False},
        302 : {'tipo': 'solteiro', 'situacao': False},
        401 : {'tipo': 'casal', 'situacao': False},
        402 : {'tipo': 'casal', 'situacao': False},
        501 : {'tipo': 'casal', 'situacao': False},
        502 : {'tipo': 'solteiro', 'situacao': False}
}

def reservar_quartos(quartos, número_quarto):
    disponiveis = []
    if número_quarto not in quartos:
        for q in quartos:
            if quartos[q]['situacao'] == False:
                disponiveis.append(q)
        return f'não temos o quarto {número_quarto}, quartos disponíveis: {disponiveis}'
    if quartos[número_quarto]['situacao'] == True:
        for q in quartos:
            if quartos[q]['situacao'] == False:
                disponiveis.append(q)
        return f'quarto {número_quarto} está ocupado. Quartos disponíveis: {disponiveis} '
    else:
        quartos[número_quarto]['situacao'] = True
        
        return f'Reserva do quarto {número_quarto} feita com sucesso. '
    
        quartos[número_quarto]['situacao'] = True
for k, v in quartos.items():
    print(k, v)

while True:

    número_quarto = int(input('digite o número do quarto digite [0] para sair: '))
    if número_quarto == 0:
        break

    print(reservar_quartos(quartos, número_quarto))

print('listagem de quartos atualiza')
for k, v in quartos.items():
    print(f'{k}: {v}')


for k, info in quartos.items():
    print('=-' *30)
    tipo = info['tipo']
    situacao = 'ocupado' if info['situacao'] else 'disponível'
    print(f'Quarto: {k} | Tipo: {tipo} | Situação: {situacao}')
