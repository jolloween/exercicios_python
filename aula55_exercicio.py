#del lista[1] # é possível alterar um índice da lista com a função del
#lista.pop() # foi atribuido a variável o ultimo item removido com a funcão pop
lista = []
print('Selecione uma opção:')

while True:
    opc = input('[i]nserir [a]apagar [l]istar: ')
    if opc == 'i':
        valor = input('valor: ')
        lista.append(valor)
    
    elif opc == 'l':
        if lista:
            for indice, nome in enumerate(lista):
                print(indice, nome)
        else:
            print('A lista está vazia.')
    
    elif opc == 'a':
        if lista:
            print('Itens da lista: ')
            for indice, nome in enumerate(lista):
                print(indice, nome)
            try:
                indice = int(input('Qual indice do item que deseja apagar: '))
                if 0 <= indice < len(lista):
                    removido = lista.pop(indice)
                    print(f'Intem {removido} removido com sucesso!')
                else:
                    print('Item inválido')
            except ValueError as e:
                print(f'Por favor, digite um valor válido.\n{e}')
        else:
            print('A lista está vazia. Nada para apagar.')
    else:
        print('Opção inválida.')
    
    resp = input('Quer continuar [s]im ou [n]ão: ').lower()
    while resp not in ('s', 'n'):
        resp = input('Resposta inválida. Quer continuar [s]im ou [n]ão: ').lower()
        
    if resp == 'n':
        break
print(f'Lista final {lista} ')
print('Lista final', *lista, sep=", ")