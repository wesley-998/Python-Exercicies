''' Programa executa uma PA de acordo com os
 termos dados pelo usuário, e pergunta mais alguns termos. '''

#INACABADO


p_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 10
while c > 0:
    print(p_termo, end=' ')
    p_termo += razao
    c -= 1
    if c == 0:
        c = int(input('\nAcrescentar mais números na sequência: '))

