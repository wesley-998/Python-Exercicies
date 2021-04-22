'''Programa que gera o fatorial digitado pelo usuário'''

n = int(input('\nDigite o número que deseja o Fatorial:'))


n1 = n - 1
fat = n * n1

while n1 != 1:
    n1 = n1 - 1
    fat = fat * n1

print(f'O fatorial de {n} é {fat}\n')
    



