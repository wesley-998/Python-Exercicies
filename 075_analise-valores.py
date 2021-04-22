'''Programa que lê 4 valores digitados pelo usuário e diz:
 Quantas vezes o número 9 apareceu, Em qual posição o valor 3 foi digitado, Quais foram os números pares'''

nove = 0
par = 0

n1 = int(input('\nDigite o primeiro valor: '))
if n1 == 9:
    nove += 1
if n1 % 2 == 0:
    par += 1

n2 = int(input('Digite o segundo valor: '))
if n2 == 9:
    nove += 1
if n2 % 2 == 0:
    par += 1


n3 = int(input('Digite o terceiro valor: '))
if n3 == 9:
    nove += 1
if n3 % 2 == 0:
    par += 1

n4 = int(input('Digite o quarto valor: '))
if n4 == 9:
    nove += 1
if n4 % 2 == 0:
    par += 1


tupla = (n1,n2,n3,n4)

print(tupla)
print(f'O número nove foi digitado {nove} vezes')
print(f'Foram digitados {par} números pares')

if n1 == 3:
    print('O valor 3 foi digitado na Primeira posição')
if n2 == 3:
    print('O valor 3 foi digitado na Segunda posição')
if n3 == 3:
    print('O valor 3 foi digitado na Terceira posição')
if n4 == 3:
    print('O valor 3 foi digitado na Quarta posição')
print('Os valores pares digitados foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print (n, end = ' ')
