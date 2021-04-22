dias = int(input('Quantos dias você ficou com carro? '))
km = float(input('Quanto Km você percorreu? '))

valor = (dias * 60) + (km * 0.15)

print('O valor a ser pago é de R${}'.format(valor))


