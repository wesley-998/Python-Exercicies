'''' Programa que lê N números e só para quando o usuário digitar 999,
 no final mostra quantos números foram digitados e a soma entre eles'''


input('Digite N números: ')

n = int(input())

c = 0
tot = 0
while n != 999:
     c += 1
     tot = tot + n
     n = int(input())


print(f'Foram digitados {c} e a soma entre eles é de {tot}')

