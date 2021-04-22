'''Programa que lê a nota do aluno e diz a situação dele'''

print('Para sabera sua média, digite as notas da prova 1 e prova 2 ')

p1 = int(input('Nota da Prova 1: '))
p2 = int(input('Nota da Prova 2: '))

media = (p1 + p2)/2

if media < 5:
    print('Sua média foi {}, você está reprovado! '.format(media))

elif media > 5.0 and media < 5.9:
    print('Sua média foi {}, você está de recuperação!'.format(media))

elif media>5.9:
    print('Sua média foi {}, você está aprovado'.format(media))

