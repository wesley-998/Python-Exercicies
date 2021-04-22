'''
Programa que executa 3 contagens
a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada
'''


from time import sleep

def linha():
    print("__" * 50)


def conta1():
    linha()
    print('Primeira contagem de 1 até 10')
    for n in range(1, 10+1):
        print(n, end=' ', flush=True)
        sleep(0.5)

def conta2():
    print('Segunda contagem de 10 até 1')
    for n in range(10, 1, -1):
        print(n, end=' ', flush=True)
        sleep(0.5)

def conta3():
    print('Terceira contagem - Customizada')
    i = int(input('INICIO: '))
    f = int(input('FINAL: '))
    p = int(input('PASSO: '))

    if f < 0 and p != 0:
        p *= -1
    
    if f < i and p >= -1:
        p *= -1

    if p == 0 and f < i:
        p = -1
    
    for n in range(i,f+1,p):
        print(n, end=' ', flush=True)
        sleep(0.5)



linha()


conta1()

print()
linha()

conta2()

print()
linha()

conta3()


print()
linha()