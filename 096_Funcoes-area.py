'''
Programa com a função área(), que recebe as dimenções de um terreno retangular e 
mostre a área do terreno.
'''

def area(largura,comprimento):
    m3 = a * l
    print(f'A área do terreno com {a}m de largura e {l}m de largura é {m3}m².  ')


def linha():
    print('__' * 50)

linha()
print('Controle de Terrenos')
linha()

a = float(input('LARGURA (m): '))
l = float(input('COMPRIMENTO (m): '))

linha()
area(a,l)
linha()
