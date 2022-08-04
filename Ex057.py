'''c = 1
while c < 10:
    print(c, end=' ')
    c +=1
print('FIM WHILE')
for c in range(1, 10):
    print(c, end=' ')
print('FIM FOR')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print(par, impar)'''
sexo = str(input('Informe seu sexo: [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Informe seu sexo: [M/F]: ')).strip().upper()[0]

