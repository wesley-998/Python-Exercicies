'''
Programa que cria palpitesda Mega Sena. 
O programa pergunta quantos jogos o usuário irá fazer e então sorteia as 6 dezenas, 
tudo em uma lista composta
'''
from random import randint
from time import sleep
print('_'*40)

p = int(input('Quantos jogo deseja fazer? '))
paupi = []
papi = 1

print('_'*40)

for c in range(0,p):
    while len(paupi)!=6:
        n = randint(0,60)
        if n not in paupi:
            paupi.append(n) 
    paupi.sort()
    print(f'O {papi}o paupite é {paupi}')
    sleep(1)
    papi += 1
    paupi.clear()
print('_'*40)
