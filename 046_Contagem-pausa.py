'''Contagem regressiva com pausa de 1 segundo'''
import time
n1 = int(input('Quantos segundos?? '))

for l in range (n1,-1,-1):
    time.sleep(1)
    print(l)

