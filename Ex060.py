from math import factorial
n = (int(input('Digite um numero: ')))
f = factorial(n)
print('O factorial de {} e : {}'.format(n, f))
c = n
print('WHILE: ')
while c > 0:
    print('\033[1;32m{}\033[m'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end ='')
    #f *= c
    c -= 1
print('{}'.format(f))
acumulador = 1
count = n
fator = 1
print('FOR: ')
for n in range(fator, count):
    print(f'{count}', end= '')
    print('x' if count > 1 else '=', end='')
    fator *= count
    count -= 1
print(f'\033[34m{fator}\033[m')


