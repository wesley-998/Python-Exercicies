'''
Programa que lê o nome, ano de nascimento e carteira de trabalho e cadastra tudo em um dicionário, 
se caso a CPTS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente com quantos anos a pessoa vai se aposentar. 35
'''

trabaiador = {}

print('_' * 100)

trabaiador['Nome'] = str(input('Nome: '))
trabaiador['Nascimento'] = 2020 - int(input('Ano de nascimento: '))
trabaiador['CPTS'] = int(input('Carteira de Trabalho: (0 não tem)'))

if trabaiador['CPTS'] != 0:
    trabaiador['Ano de Contratação'] = int(input('Ano de contratação: '))
    trabaiador['Salário'] = float(input('Salário : R$ ')) 
    aposentadoria = ((35 - (2020 - trabaiador['Ano de Contratação'])) + trabaiador['Nascimento'])

print('_' * 100)

print(f'Nome tem valor {trabaiador["Nome"]}')
print(f'Idade tem valor {trabaiador["Nascimento"]}')
print(f'CPTS tem valor {trabaiador["CPTS"]}')

if trabaiador['CPTS'] != 0:
    print(f'Salário tem valor {trabaiador["Salário"]}')
    print(f'Aposentadoria tem valor {aposentadoria}')

print('_' * 100)

