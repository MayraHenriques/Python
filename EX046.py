'''i = int(input('Inicio: '))
f = int(input('Final: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)
print('FIM')'''
from time import sleep
s = 0
for c in range(10,0-1,-1):
    sleep(1)
    print(c)
    print('...'*12)
    print('\33[1;32m** Contagem Regressiva **\33[m')
    print('...' * 12)
print('FIM')
