''' Programa que identifica se a frase é um palídromo ou não '''

frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) -1, -1, -1):
    inverso += junto [letra]
if inverso == junto:
    print('Temos um palíndromo!')

else:
    print('A frse digitada não é um palímedro!')



