'''Programa que sorteia cinco números aleatórios e coloca em uma tupla, 
depois disso mostra o maior e o menor número'''

from random import randint

tupla = (randint(0,100), randint(0,9) ,randint(0,9) ,randint(0,9) ,randint(0,9))

print(tupla)
print('O maior número é',max(tupla))
print('o menor número é',min(tupla))

