'''
Programa que sorteia uma lista com 5 números e soma o valores pares
'''
from random import randint

#def sorteio():
#    lista = [randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)]



def somapar():
    lista = [randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)]
    soma = 0
    for n in lista:
        print(n, end=', ')
        if n % 2 == 0:
            soma += n
    print('Foram sorteados.')
    print(f'\nA soma dos pares é {soma}')

def linha():
    print('__' * 50)


linha()
somapar()
linha()
