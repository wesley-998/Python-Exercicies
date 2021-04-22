print('Digite 3 números: ')
n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1>n2>n3 or n1>n3>n2:
    print('{} é maior que {} e {}'.format(n1,n2,n3))

elif n2>n1>n3 or n2>n3>n2:
    print('{} é maior que {} e {}'.format(n2,n1,n3))

elif n3>n1>n2 or n3>n2>n1:
    print('{} é maior que {} e {}'.format(n3,n2,n1))
else: 
    print('else')


if n1<n2<n3 or n1<n3<n2:
    print('{} é menor que {} e {}'.format(n1,n2,n3))

elif n2<n1<n3 or n2<n3<n1:
    print('{} é menor que {} e {}'.format(n2,n1,n3))

elif n3<n1<n2 or n3<n2<n3:
    print('{} é menor que {} e {}'.format(n3,n2,n1))

else:
    print('else')



