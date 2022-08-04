num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[1;31m', end='')
    print('{}'.format(c), end=' ')
if tot == 2:
    print('PRIMO !!!')
else:
    print('Nao PRIMO')
