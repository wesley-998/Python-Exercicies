''' Programa que lê N números e só para quando o usuário digitar 999,
 será mostrado quantos números foram digitados e qual a soma entre eles '''


print('Digite os números: \n')

cont = tot = n = 0

while true: '''Loop infinito'''
    n = int(input(''))
    if n == 999:
        break
    cont += 1
    tot += n
    
print(f'Foram digitados {cont} números e a soma deles é {tot}')

