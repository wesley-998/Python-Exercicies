''' Programa que lê 2 números e diz qual é o maior ou se são iguais'''

n1 = int(input('Digite o primeiro número:  '))
n2 = int(input('Digite o segundo número:   '))

if n1>n2:
    print('O primeiro valor é maior que {}'.format(n2))

elif n2>n1:
    print('O primeiro valor é menor que {}'.format(n2))

elif n1 == n2:
    print('Os valores são iguais')