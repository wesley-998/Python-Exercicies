velo = int(input('Qual foi a velocidade?? '))

if velo>80:
    multa = (velo-80)*7
    print('O valor da sua multa é R$ {}'.format(multa))
else:
    print('Você é muito lerdo e não foi multado!')
