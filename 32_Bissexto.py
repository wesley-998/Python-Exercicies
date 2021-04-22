ano = int(input('Digite o ano: '))


t1 = ano % 4
t2 = ano % 100
t3 = ano % 400

if t1 == 0 and t2 != 0:
    print('O ano {} é bissexto!'.format(ano))

else:
    print('O ano {} não é bissexto'.format(ano))


print(t1)
print(t2)
print(t3)
