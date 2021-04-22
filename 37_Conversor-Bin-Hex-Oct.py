"""Programa que lê um número qualquer inteiro e converte para Binário, Hexadecimal ou Octadecimal"""

n1 = int(input('Digite o número que você deseja converter: '))

opcao = int(input('''Digite a opção desejada.
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal
 '''))

if opcao == 1:
    print('{} em binário é {}'.format(n1, bin(n1)))

elif opcao == 2:
    print('{} em octal é {}'.format(n1, oct(n1)))
elif opcao == 3:
    print('{} em Hexadecimal é {}'.format(n1, hex(n1)))
else:
    print('Opção inválida.')
