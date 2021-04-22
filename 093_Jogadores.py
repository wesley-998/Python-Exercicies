'''
Programa que cadastra um jogador de futebol, o programa lê o nome do jogador, quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feito em cada partida. No final, tudo será mostrado, 
incluindo o total de gols feitos durante o campeonato.'''

jogador = {}
partidas = []
c1 = 1
print('__' * 50)
jogador['Nome'] = str(input('Nome do jogador: '))
gols = 0
p = int(input(f'Quantas partidas {jogador["Nome"]} participou? ' ))

for c in range(1,p+1):
    partidas.append(int(input(f'Quantos gols {jogador["Nome"]} fez na partida {c}? ')))
       
gols = sum(partidas)

jogador['Total'] = gols

print('_' * 50)

print(f'O nome de jogador é {jogador["Nome"]}')
print(f'O número de gols nas partidas é {partidas}')
print(f'O total de gols é {jogador["Total"]}')

print('_' * 50)

print(f'O jogador {jogador["Nome"]} jogou {p} partidas.')

for c in partidas:
    print(f'        Na partida {c1}, {jogador["Nome"]} fez {c} gols')
    c1 += 1

print(f'Foi um total de {jogador["Total"]} gols')


print('_' * 50)

