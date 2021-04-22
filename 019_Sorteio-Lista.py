import random

a1 = str(input('Digite o nome do Primeiro aluno: '))
a2 = str(input('Digite o nome do Segundo aluno: '))
a3 = str(input('Digite o nome do Terceiro aluno: '))
a4 = str(input('Digite o nome do Quarto aluno: '))

lista = [a1,a2,a3,a4]
sorteado = random.choice(lista)

print('O aluno escolhido foi o {}'.format(sorteado))
