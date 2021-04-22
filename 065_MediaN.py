'''Programa lê N números e no final 
mostra a média entre eles o maior e o menor número'''

print('Digite N números: ')

n = int(input())
tot = 0
c = 0
maior = 0
menor = 9999999


while n != 0:
    if n > maior:
        maior = n
    tot = tot + n
    c = c + 1
    if n < menor:
        menor = n
    print('Deseja digitar mais um valor?')
    n = int(input())
    


media = tot/c
print(f'A média de todos os números lidos foi {media}.')
print(f'{maior} foi o maior número digitado e {menor} o menor.')

