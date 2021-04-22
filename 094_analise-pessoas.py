'''
Programa que lê o nome, sexo e idade de N pessoas e armazena tudo em um dicionário 
e depois coloca tudo em uma lista e logo em seguida mostra:
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média
'''


pessoas = {}
listaM = []
listaida = []
contador = 0
listap = []
idade = []
obezu = {}
while True:
    pessoas['Nome'] = str(input('Nome da pessoa: '))
    contador += 1
    while True:
        pessoas['Sexo'] = str(input('Sexo [M/F]: '))
        if pessoas['Sexo'] not in 'MmFf':
            print('Sexo incorreto, escolha apenas F ou M')
        if pessoas['Sexo'] in 'MmFf':
            break

    pessoas['Idade'] = int(input('Idade: '))
    idade.append(pessoas['Idade'])

    if pessoas['Sexo'] in 'Ff':
        listaM.append(pessoas['Nome'])

    if pessoas['Idade'] >= 30:
        listap.append(pessoas['Nome'])
        obezu['Nome'] = pessoas['Nome']
        obezu['Sexo'] = pessoas['Sexo']
        obezu['Idade'] = pessoas['Idade']
    pessoas.clear()
    r = str(input('Deseja cadastrar outra pessoa? [N/S] '))

    if r in 'nN':
        break

média = sum(idade) / len(idade)

print(f'Foram cadastradas {contador} pessoas')
print(f'A média de idade é do grupo é {média}')
print(f'As mulheres que foram cadastradas são: {listaM}')
print(f'Pessoas com a idade acima da média:')

for n,s, in obezu.items():
    print(f'{n}; {s} ', end= ' ')
    print()
