''' Programa que exibe a tabuada de qualquer número 
e para quando o valor informado for negativo'''

tab = 0 

while True:
    tab = int(input('Qual tabuda deseja? '))
    if tab < 0:
        break
    for n in range (0,11):
        print(f'{tab} X {n} = {tab*n}')

print('Programa encerrado, pague mais $10 ao traveco')

