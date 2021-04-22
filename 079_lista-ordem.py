''' Programa onde o usuário digita infinitos números, 
só adiciona números novos e no final mostra todos em ordem crescente'''

lista = []

while True:
    i = int(input('Digite um valor: '))
    if i not in lista:
        lista.append(i)
    else: 
        print('Número já cadastrado!')
    r = str(input('Deseja adicionar outro valor? [S/N]'))
    if r in 'Nn':
        break

lista.sort()

print(lista)

