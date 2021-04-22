'''
Programa que lê o nome e a média de um aluno, 
quandando a situação em um dicionário, 
no final mostra o conteudo na tela
'''
alunos = {}
print('_' * 100)

alunos['Nome'] = str(input('Qual o nome do aluno? '))
alunos['Média'] = float(input(f'Qual a Média do(a) {alunos["Nome"]}? '))
print('_' * 100)

if alunos['Média'] >= 7:
    alunos['Situação'] = 'Aprovado'
else:
    alunos['Situação'] = 'Reprovado'

print(f'O nome do aluno é {alunos["Nome"]}.')
print(f'A Média é {alunos["Média"]}.')
print(f'A situação de {alunos["Situação"]}.')

print('_' * 100)