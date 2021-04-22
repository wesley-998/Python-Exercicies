''' Tabuada usando o for '''

n = int(input('Qual a tabuada desejada? '))

for c in range (0,11,1):
    p = c * n
    print('{} X {} = {}'.format(n,c,p))
