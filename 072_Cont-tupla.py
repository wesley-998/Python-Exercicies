''' Programa que recebe um número de 0 a 20 e mostra-lo por extenso '''

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze','desseseis', 'dessesete', 'dezoito', 'dezenove', 'vinte')

while True:
    valor = int(input('\nDigite um valor entre 0 e 20: '))
    if 0 <= valor <= 20:
        break

for cont in range (0,valor + 1 ,1):
    if valor == cont:
        print('Você digitou o número',tupla[valor])

