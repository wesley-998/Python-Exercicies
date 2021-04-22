#Crie um programa que leia dois números e mostre a soma entre eles

n1 =  int(input('Digite o primiero valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = n1 + n2
print('A soma entre {}{}{} e {} é {}' .format('\033[4;m', n1, '\033[m', n2,n3))
