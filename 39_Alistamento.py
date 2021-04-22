'''Programa que diz se o usuário está na época de alistamento e quanto tempo falta'''

idade = int(input('Digite o ano de nascimento:  '))

alist = 2020 - idade

if alist == 17 or alist == 18:
    print('Está na hora de Capinar! ')

elif alist > 18:
    past =  alist - 18 
    print('Já se passaram {} anos do seu alistamento! '.format(past))

elif alist < 17:
    future = 17 - alist
    print('Ainda faltam {} anos para o seu alistamento!'.format(future))
