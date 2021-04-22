import math

n1 = int(input('Digite o valor: '))

seno = math.sin(n1)
cosseno = math.cos(n1)
tangente = math.tan(n1)

print('O seno de {} é {:.3}' .format(n1,seno))
print('O Cosseno de {} é {:.3}'.format(n1,cosseno))
print('A Tangente de {} é {:.3} '.format(n1,tangente))
