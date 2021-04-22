''' Programa que simula o saque de um caixa eletronico, 
solicitando o valor a ser sacado, e mostrando quais cédulas 
de 50, 20, 10, 1 serão necessárias. '''

print('---- CAIXA ELETRÔNICO BRADESCÃO ----')

valor = int(input('Qual valor você quer sacar? '))
total = valor // 50
if total > 0:
    print(f'{total} de 50')

total = (valor % 50) // 20
if total > 0:
    print(f'{total} de 20')

total = ((valor % 50) % 20) // 10
if total > 0:
    print(f'{total} de 10')
    
total = (((valor % 50)  % 20) % 10) // 1
if total > 0:
    print(f'{total} de 1')