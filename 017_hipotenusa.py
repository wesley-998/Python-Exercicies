import math

n1 = int(input('Digite o cateto oposto: '))
n2 = int(input('Digite o cateto adjacente: '))

hypo = math.hypot(n1,n2)

print('A hipotenusa talvez seja: {} ' .format(hypo))
