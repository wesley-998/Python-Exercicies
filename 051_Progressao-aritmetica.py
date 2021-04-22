''' progressão aritmética, usuário entra com o primeiro termo e a razão'''

termo = int(input('\nQual o primeiro termo?? '))
razao = int(input('Qual a razão??  '))
decimo = termo + (10 - 1)* razao

for l in range(termo,decimo,razao):
    print('{}'.format(l))
