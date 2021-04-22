''' Programa que lê o sexo de uma pessoa [M/F],
 e caso esteja errado peça a digitação novamente até ter um valor correto.'''

n = str(input('Qual o sexo? [M/F] \n')).upper()


while n != 'M' and n != 'F':
    print(f'{n} é inválido!\n')
    n = str(input('Qual o sexo? [M/F] \n')).upper()

if n == 'M':
    print('Você é do sexo Masculino.')

else:
    print('Você é do sexo Feminino.')

