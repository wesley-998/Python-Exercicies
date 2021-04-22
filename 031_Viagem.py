km = int(input('Quantos kilômetros tem a sua viagem?? '))

if km <= 200:
    valor = km*0.50
    print('Sua viagem irá custar R$ {}'.format(valor))

else:
    valor2 = km*0.45
    print('Sua viagem irá custar R$ {}'.format(valor2))

