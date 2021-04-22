'''Programa que recebe 7 números que cadastra todos em uma única lista que mantenha separados os valores impares e pares. 
No final mostre os valores impares e pares em ordem crescente.'''

lista = [[],[]]
n = 0

for n in range(0,7):
    n = int(input('Digite o valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

lista[0].sort()
lista[1].sort()

print(lista)
