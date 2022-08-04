primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
vigesimo = primeiro + (20 - 1) * razao
termo = primeiro
cont = 1
mais = 10
total = 0
print('FOR: ')
for c in range(primeiro, vigesimo + razao, razao):
    print(c, end='-> ')
print('FIM')
print('WHILE: ')
while mais != 0:
    total = total + mais
    while cont <= total:
        print('\033[34m{} -> \033[m'.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('{} Termos utilizados'.format(total))
print('FIM')
