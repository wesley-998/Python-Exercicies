nome = input('Digite o seu nome: ')


result = nome.upper().find('SILVA')


if result == -1:
    print('Você não tem "Silva" no nome ')

else:
    print('Vocé tem "Silva" no nome')