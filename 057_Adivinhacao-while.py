''' O programa escolhe um número entre 0 e 10 e o usuário tenta até 
adivinhar e monstra quantas tentativas foram necessárias'''

import random

print( '\n\nEscolhi um número entre 0 e 10, qual é o número?')

n1 = int(input())
tot = 0

lista = [0,1,2,3,4,5,6,7,8,9,10]
n2 = random.choice(lista)

while n1 != n2:
    print('Errado, mais uma tentativa!\n')
    tot = tot + 1
    n1 = int(input())

if n1 == n2:
    print(f'\nParabéns, você acertou com {tot} tentativas.')

