''' Programa que lê 7 datas de nacimento e identifica quem é menor e quem é maior de idade.'''


maiores = 0
menores = 0
cont = 1
for c in range(1,7):
    n1 = int(input('Qual o ano de nascimento da {} pessoa? '.format(cont)))
    cont = cont + 1
    idade = 2020 - n1 
    if idade >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1 

print('Há {} maiores e {} menores de idade.' .format(maiores,menores))

