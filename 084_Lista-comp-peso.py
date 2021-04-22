'''Programa que cadastra nome e peso de infinitas pessoas e depois analisa:
A) Quantas pessoas foram cadastradas.
B) Uma lista com as pessoas mais pessadas cadastradas.
C) Uma lista com as pessoas mais leves.'''



dado = []
acima = []
abaixo = []
cont = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    cont += 1
    if dado[1] >= 90:
        acima.append(dado[:])
        dado.clear()
    elif dado[1] <= 70:
        abaixo.append(dado[:])
        dado.clear()
    r = str(input('Deseja cadastrar outra pessoa? [S/N] '))
    if r in 'Nn':
        break

print(f'Foram cadastradas ao todo {cont} pessoas')

for c in acima:
    print(f'{c[0]},',  end=' ')
print('são do grupo de maior peso.')

for d in abaixo:
    print(f'{d[0]},', end=' ')
print('são do grupo de menor peso.')

    
