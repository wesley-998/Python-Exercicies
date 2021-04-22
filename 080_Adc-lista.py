'''Programa que lê 5 valores digitados pelo usuário, 
adiciona numa lista e coloca os valores em ordem crescente sem o Sort'''

lista = []
maior = 0
menor = 9999999

for c in range(0,5):
    n = int(input('Digite um valor: '))
    #if c == 0:
        #maior = menor = n
    if n > maior:
        maior = n
        lista.append(n)
    elif n < menor:
        menor = n
        if n not in lista: 
            lista.insert(0, n)
    elif n > menor and n < maior:
        lista.insert(1, n)

print(lista)
