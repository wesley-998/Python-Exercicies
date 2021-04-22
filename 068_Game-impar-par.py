''' Programa que joga par ou ímpar com o computador. O jogo só será interronpido 
quando o jogador perder, mostrando o total de vitórias consecutivas.'''
import random

print('\n--- VAMOS JOGAR ÍMPAR/PAR ---')
j = str(input('\nÍMPAR  ou PAR [I/P]:\n')) 
m = ' ' '''String vazia'''
contm = contj = 0
if j == 'i':
    m = 'p'
elif j == 'p':
    m = 'i'
elif j != 'i' and j != 'p':
    print('Escolha inválida!')

lista = [0,1,3,4,5,6,7,8,9,10]

while True:
    jn1 = int(input('\nEsolha um número: '))
    mn1 = random.choice(lista)
    r = (mn1 + jn1)%2
    print(f'\nO computador escolheu {mn1} e você {jn1}\n')

    if r == 0:
        if j == 'p':
            print('Você venceu!')
            contj += 1
        else:
            print('Você perdeu!')
            contm += 1
            break
    elif r != 0:
        if j == 'p':
            print('Voce perdeu!')
            contm += 1
            break
        else:
            print('Você venceu')
            contj += 1


print(f'O computador venceu {contm} vezes')
print(f'O Jogador venceu {contj} vezes')





