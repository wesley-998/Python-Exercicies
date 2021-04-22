import random

print('Estou pensando em um número de 0 a 5, tente adivinhar qual é!')
aposta = int(input('Digite um número de 0 a 5! '))

lista = [0,1,2,3,4,5]

pc = random.choice(lista)
print(pc)
if aposta == pc:
    print('VOCÊ ACERTOU!!')
else:
    print('VOCÊ ERROU!!')
