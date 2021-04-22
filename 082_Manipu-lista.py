'''Programa que lê inúmeros valores digitados pelo usuário e armazena todos em uma lista,
no final exibe duas listas, uma todos os valores, outra com apenas números ímpares e por ultimo
uma lista com apenas números pares'''

lista = []
listaim = []
listapar = []
print('__' * 30)
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Desenha digitar outro valor? [S/N] '))
    if r in 'nN':
        break

for c in lista:
    if c % 2 == 0:
        listapar.append(c)
    elif c % 2 != 0:
        listaim.append(c)
print('__' * 30)
print(f'{lista} todos os valores digitados')
print(f'{listaim} todos o valores ímpares')
print(f'{listapar} todos os valores pares')
print('__' * 30)