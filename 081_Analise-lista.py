'''Programa que lê inumeros números digitados pelo usuário, depois disso mostra:
A) Quantos números foram digitados. 
B) A lista de valores ordenados de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista'''

lista = []
cont = 0
cont5 = 0
print('__' * 30)

while True:
    n = int(input('Digite o valor: '))
    lista.append(n)
    if n == 5:
        cont5 +=1

    cont +=1
    r = str(input('Deseja digitar outro valor? [N/S] '))
    if r in 'Nn':
        break

lista.sort(reverse=True)
print('__' * 30)

if cont5 != 0:
    print(f'O número 5 foi digitado {cont5} vezes.')
else:
    print('O número 5 não foi digitado.')

print(f'Foram digitados os seguintes valores {lista}')
print(f'Foram digitados {cont} números')
print('__' * 30)
