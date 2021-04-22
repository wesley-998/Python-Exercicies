'''Programa que joga Jokênpo com o usuário'''
import random
n1 = int(input('''ESCOLHA A SUA ARMA!

[ 1 ]   PAPEL
[ 2 ]   TESOURA
[ 3 ]   PEDRA
'''))

lista = [1,2,3]

pc = random.choice(lista)

if pc == 1  and n1 == 1:
    print('PAPEL E PAPEL = EMPATE!')

elif pc == 1 and n1 == 2:
    print('PAPEL E TESOURA = VOCÊ GANHOU!')

elif pc == 1 and n1 == 3:
    print('PAPEL E PEDRA = VOCÊ PERDEU!')


elif pc == 2  and n1 == 1:
    print('TESOURA E PAPEL = VOCÊ PERDEU!')

elif pc == 2 and n1 == 2:
    print('TESOURA E TESOURA = EMPATE!')

elif pc == 2 and n1 == 3:
    print('TESOURA E PEDRA = VOCÊ GANHOU!')



elif pc == 3  and n1 == 1:
    print('PEDRA E PAPEL = VOCÊ GANHOU!')

elif pc == 3 and n1 == 2:
    print('PEDRA E TESOURA = VOCÊ PERDEU!')

elif pc == 3 and n1 == 3:
    print('PEDRA E PEDRA = EMPATE')


else:
    print('Fez merda em...')