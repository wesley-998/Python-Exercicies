''' Programa que soma todos os números impares 
que são multiplos de 3 e se encontram entre 1 a 500 '''
soma = 0
num = 0
for c in range(1,500,2):
    if c % 3 == 0:
        soma = soma + c
        num = num + 1


print('A soma dos {} valores é {}'.format(num,soma))

    


