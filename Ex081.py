num = []
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Voce digitou {len(num)} elementos.')
num.sort(reverse=True)
print(f'Os valores em ordem decrescente: {num}')
if 5 in num:
    print('O valor 5 esta dentro da lista!')
else:
    print('O valor 5 nao esta na lista.')
