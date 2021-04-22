n = int(input('Digite um valor: '))

n1 = n%2
print(n1)

if n1 == 0:
    print('{} é Par!'.format(n))
else:
    print('{} é Impar!'.format(n)) 
