''' Programa que lê dois números e mostra um menu para o usuário
, somar, multiplicar, maior, novos números ou sair do programa'''

print('Digite dois valores: ')

n1 = int(input())
n2 = int(input())

print('''\nO que deseja fazer? 
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior valor
[ 4 ] Novos valores
[ 5 ] Sair
\n''')

op = int(input())

if op == 1:
    n3 = n1 + n2
    print(f'A soma de {n1} + {n2} é {n3}')

elif op == 2:
    n3 = n1 * n2
    print(f'A multiplicação de {n1} X {n2} é {n3}')

elif op == 3:
    if n1 > n2:
        print(f'\n{n1} é  maior que {n2}\n')
    elif n2 > n1:
        print(f'\n{n2} é maior que {n1}\n')
    elif n1 == n2:
        print('\nOs valores são iguais, poha.\n')

elif op == 4:

    print('Digite dois valores: ')
    n1 = int(input())
    n2 = int(input())

    print('''\nO que deseja fazer? 
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior valor
    [ 5 ] Sair
    \n''')
    op = int(input())
    if op == 1:
        n3 = n1 + n2
        print(f'A soma de {n1} + {n2} é {n3}')

    elif op == 2:
        n3 = n1 * n2
        print(f'A multiplicação de {n1} X {n2} é {n3}')

    elif op == 3:
        if n1 > n2:
            print(f'\n{n1} é  maior que {n2}\n')
        elif n2 > n1:
            print(f'\n{n2} é maior que {n1}\n')
        elif n1 == n2:
            print('\nOs valores são iguais, poha.\n')

    elif op == 5:
        print('Você saiu do programa.')


elif op == 5:
    print('Você saiu do programa.')
    