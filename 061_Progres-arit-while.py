'''Programa lê o primeiro termoe a razão de uma PA,
 mostrando os 10 primeiros termos'''

primeiro = int(input('\nDigite o Primeiro termo: '))
razao = int(input('\nDigite a Razão: '))

n = 0
pa = primeiro
while n != 10:
    pa = pa + razao
    n = n + 1
    print(pa)

