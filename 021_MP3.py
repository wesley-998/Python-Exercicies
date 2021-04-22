"""Programa que lê um número qualquer inteiro e converte para Binário, Hexadecimal ou Octadecimal"""

n1 = int(input('Digite o número que você deseja converter: '))

opcao = int(input('''Digite a opção desejada.
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal
 '''))

if opcao == 1:
    print('{} em binário é {}'.format(n1, bin(n1)))