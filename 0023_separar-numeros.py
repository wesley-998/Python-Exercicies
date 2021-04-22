n = int(input('Digite um número: '))

u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n //1000 % 10
print('A unidade é {}'.format(u))
print('A dezena é {}'.format(d))
print('A centena é {}'.format(c))
print('A milher é {}'.format(m))