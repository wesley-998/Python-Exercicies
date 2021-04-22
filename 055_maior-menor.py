''' Programa que lê 7 valores e identifica o maior e o menor valor da lista'''


maior = 0
menor = 9999999
pessoa = 1

for c in range(1,7):

    n1 = int(input('Qual o peso da {} pessoa? '.format(pessoa)))
    pessoa = pessoa + 1
    if n1 > maior:
        maior = n1
    elif n1 < menor:
        menor = n1

print('O maior peso foi de {} e o menor peso foi de {}' .format(maior, menor))

