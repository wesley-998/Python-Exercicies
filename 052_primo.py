''' Programa que identifica se o número é primo ou não'''

num = int(input('Digite um número: '))
tot = 0

for c in range(1,num + 1):
    if num % c == 0:
        tot += 1

print('O número {} foi divisível {} vezes. '.format(num, tot))
if tot == 2:
    print('É primo!')
else:
    print('Não é primo')
