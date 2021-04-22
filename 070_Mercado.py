'''Programa que recebe o nome e o preço de N produtos digitados pelo usuário, 
e mostra o total gasto na compra, quantos produtos custam mais de $1000 e 
qual é o nome do produto mais barato'''

print('\n---- MERCADO PREDREIRA ----\n')

tot = 0
barao = 0
barato = ' '
fix = 999999

while True:
    produto = str(input('Nome do Produto: '))

    preco = int(input('Preço do Produto: '))
    tot += preco
    if preco > 1000:
        barao += 1
    if preco < fix:
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('\nDeseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print(f'''\nO total da compra é R$ {tot}
{barao} Produtos custaram mais de R$ 1000
{barato} é produto mais barato\n''')
