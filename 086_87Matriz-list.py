'''Programa que armazena valores em uma matriz 3x3
Mostrar no fina:
    A) A soma de todos os valores pares
    B) A soma dos valores da segunda coluna
    C) O maior valor da segunda linha'''

linha1 = [[], [], []]
linha2 = [[], [], []]
linha3 = [[], [], []]
soma = 0
colum2 = 0
lin2 = 0

n = int(input('Digite o valor para a posição [0][0]:'))
if n % 2 == 0:
    soma += n
linha1[0].append(n)
 
n = int(input('Digite o valor para a posição [0][1]:'))
colum2 += n
if n % 2 == 0:
    soma += n
linha1[1].append(n)

n = int(input('Digite o valor para a posição [0][2]:'))
if n % 2 == 0:
    soma += n
linha1[2].append(n)


n = int(input('Digite o valor para a posição [1][0]:'))
lin2 = n
if n % 2 == 0:
    soma += n
linha2[0].append(n)

n = int(input('Digite o valor para a posição [1][1]:'))
if n > lin2:
    lin2 = n
colum2 +=n
if n % 2 == 0:
    soma += n
linha2[1].append(int(n))

n = int(input('Digite o valor para a posição [1][2]:'))
if n > lin2:
    lin2 = n
if n % 2 == 0:
    soma += n
linha2[2].append(n)


n = int(input('Digite o valor para a posição [2][0]:'))
if n % 2 == 0:
    soma += n
linha3[0].append(n)

n = int(input('Digite o valor para a posição [2][1]:'))
colum2 += n
if n % 2 == 0:
    soma += n
linha3[1].append(n)

n = int(input('Digite o valor para a posição [2][2]:'))
if n % 2 == 0:
    soma += n
linha3[2].append(n)


print(linha1)
print(linha2)
print(linha3)

print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da segunda coluna é {colum2}')
print(f'O maior valor da segunda linha é {lin2}')

