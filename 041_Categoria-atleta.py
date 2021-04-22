'''Programa que lê o ano de nascimento de um atleta e de acordo com a idade o classifica'''

ano = int(input('Digite o ano de nascimento do atleta. '))

idade = 2020 - ano

if idade < 9:
    print('Sua idade é de {} anos, portando você é um atleta Mirim'.format(idade))
elif idade > 9 and idade < 14:
    print('Sua idade é de {} anos, portando você é um atleta Infantil'.format(idade))
elif idade > 14 and idade < 19:
    print('Sua idade é de {} anos, portando você é um atleta Junior'.format(idade))
elif idade == 20:
    print('Sua idade é de {} anos, portando você é um atleta Sênhor'.format(idade))
elif idade > 20:
    print('Sua idade é de {} anos, portando você é um atleta Master'.format(idade))

    