''' Programa que lê 5 valores e guarda numa lista,
no final mostra qual foi o maior e o menor valor e suas posições na lista'''

lista = []

for count in range(0,5):
    lista.append(int(input('Digite um valor: ')))


maior = (max(lista))
menor = (min(lista))

print(f'Você digitou os valores {lista}')

print (f'{maior} foi o maior valor digina na posição {lista.index(maior)}')
print (f'{menor} foi o menor valor digitado na posição {lista.index(menor)}')
