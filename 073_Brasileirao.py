''' Programa que mostra os 5 primeiros colocados do Brasileirão, 
os ultímos 4 colocados da tabela e em qual posição na tabela o time da Chapecoense está '''


tupla = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico', 'São Paulo', 'Internacional','Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético -MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')

print('\n ---BRASILEIRÃO--- ')
print('\nOs cinco primeiros times são',tupla[:5])
print('Os cinco ultimos times são ',tupla[-5:])
print('Os time em ordem alfabética ', sorted(tupla))
print(f'O Chapecoense está na {tupla.index("Chapecoense")+1} posição')

