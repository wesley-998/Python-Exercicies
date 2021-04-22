'''
Programa que sorteia um valor de 0 a 6 (dado) para 4 jogadores,
guarda o resultado em um dicionário e depois cria um ranking. 
'''

jogadores = {'Jogador1': 0 ,'Jogador2' : 0 , 'Jogador3' : 0 , 'Jogador4' : 0}

from random import randint
from time import sleep
from operator import itemgetter
l = 1
print('_' * 100)

jogadores['Jogador1'] = randint(1,6)
jogadores['Jogador2'] = randint(1,6)
jogadores['Jogador3'] = randint(1,6)
jogadores['Jogador4'] = randint(1,6)

for c,v in jogadores.items():
    print(f'{c} tirou o número {v} ')
    sleep(1)
print('_' * 100)

ranking = {}
ranking = sorted(jogadores.items(), key = itemgetter(1), reverse = True)
print(ranking)

for c in enumerate(ranking):
    print(f'{l} lugar: {ranking[c][0]} com {ranking[c][1]}.')
    sleep(1)
    l += 1