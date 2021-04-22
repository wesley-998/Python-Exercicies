'''Programa que lê a idade e o sexo de N pessoas e pergunta se o usuário deseja cadastrar mais uma pessoa, 
caso contrário mostrar quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados, 
quantas mulheres tem menos de 20 anos'''


print('--- CADASTRO DE PESSOAS ---')

r = ' ' 
maior = home = nov = 0

print('Deseja cadastrar uma pessoa? ')
r = str(input()).upper()

if r == 'S':
    while r == 'S':
        s = str(input('Qual o sexo? [M/F] ')).upper()
        if s == 'M':
            home += 1
        
        i = int(input('Qual a idade? '))
        if i > 18:
            maior += 1

        elif s == 'F' and i < 20:
            nov += 1

        print('Deseja cadastrar uma pessoa? ')
        r = str(input()).upper()
        if r == 'N':
            break

print(f'\nForam cadastradas: ')
print(f'{maior} pessoas maiores de idade')
print(f'{home} Homens')
print(f'e {nov} mulheres com menos de 20 anos\n')





