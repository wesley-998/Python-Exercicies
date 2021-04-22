''' Programa lê o nome, idade e sexo de 4 pessoas,
e mostra a média das idades, qual o nome do homem mais velho e quantas mulheres com menos 20 anos'''

old = 0
oldname = 'pula'
novinhas = 0

nome1 = str(input('\nNome da primeira pessoa? ' ))
ano1 = 2020 - int(input('Qual o ano de nascimento? ' )) 
sexo1 = str(input('Qual o sexo? [M/F] '))
if sexo1 == 'm':
    old = ano1
    oldname = nome1
elif sexo1 == 'f' and ano1 <= 20:
    novinhas = novinhas + 1

nome2 = str(input('\nNome da segunda pessoa? ' ))
ano2 = 2020 - int(input('Qual o ano de nascimento? ' )) 
sexo2 = str(input('Qual o sexo? [M/F] '))
if sexo2 == 'm' and ano2 > old:
    oldname = nome2
elif sexo2 == 'f' and ano2 <= 20:
    novinhas = novinhas + 1

nome3 = str(input('\nNome da terceira pessoa? ' ))
ano3 = 2020 - int(input('Qual o ano de nascimento? ' )) 
sexo3 = str(input('Qual o sexo? [M/F] '))
if sexo3 == 'm' and ano3 > old:
    oldname = nome3
elif sexo3 == 'f' and ano3 <= 20:
    novinhas = novinhas + 1


nome4 = str(input('\nNome da quarta pessoa? ' ))
ano4 = 2020 - int(input('Qual o ano de nascimento? ' )) 
sexo4 = str(input('Qual o sexo? [M/F] '))
if sexo4 == 'm' and ano4 > old:
    oldname = nome4
elif sexo4 == 'f' and ano4 <= 20:
    novinhas = novinhas + 1

media = (ano1+ano2+ano3+ano4)/4
print('\nA média das idades é de {} anos '.format(media))
print('O homem mais velho é o {}'.format(oldname))
print('Há {} mulheres com menos de 20 anos\n'.format(novinhas))




