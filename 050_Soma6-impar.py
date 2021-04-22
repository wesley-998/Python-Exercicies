''' O programa recebe 6 valores e soma apenas o números pares'''
print('Digite 6 valores: ')
soma = 0
for c in range (0,7):
    n1 = int(input())
    if n1 % 2 == 0:
        soma = soma + n1

print(soma)
    