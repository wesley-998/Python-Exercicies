'''
Programa que lê o nome e duas notas de infinitos alunos e armazena numa lista composta. 
No final mostra o boletim contendo média de cada aluno 
e permita que o usuário mostrar as notas de casa aluno individualmente
'''
from time import sleep
print('_'*50)
lista = []
n1 = 0
while True: 
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    média = (nota1 + nota2)/2
    lista.append([nome,[nota1, nota2], média])
    r = str(input('Deseja cadastrar outro aluno? [S/N]'))
    if r in 'Nn':
        break

print('_'*50)
print(f'No.    ALUNO     MÉDIA')
print('_'*50)

for c in lista:
    print(f'{n1}      {c[0]}        {c[2]}')
    n1 += 1
    sleep(1)

busc = int(input('Qual aluno você deseja mostrar as notas? '))
sleep(1)
print(f'As notas do {lista[busc][0]} são {lista[busc][1]}')

print('_'*40)


print('_'*50)