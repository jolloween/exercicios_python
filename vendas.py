total_vendas = 0
vendas = []

while True:
    try:
        valor = input("Digite o valor da venda: (0 para encerrar) ")
        valor.isdigit()
        
        novo_valor = float(valor) #converte para float
                
        if novo_valor < 0: # se for negativo ira repetir a operação
            print("❌ Por favor, digite um número válido.")
            continue #volta ao loop caso digite um número negativo
        
        if novo_valor == 0: #cancela a operação ao digitar "0"
            print("operação cancelada")
            break
        
        total_vendas += novo_valor
        vendas.append(novo_valor)
        
        
    except ValueError: # tratamento de erro ao digitar letras
        print('❌ Opcão inválida')
        
print(f"Total de vendas foi: R${total_vendas:.2f}")
print(f"Lista de vendas: {vendas}")

if vendas:  # só calcula se a lista não estiver vazia
    print(f"Maior venda foi: R${max(vendas):.2f}")
    print(f"Menor venda foi: R${min(vendas):.2f}")
else:
    print("Nenhuma venda registrada.")



