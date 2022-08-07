numeros = list()
par = list()
impar = list()

while True:
    numeros.append(int(input('Digite um valor: ')))
    res = str(input('\033[31mQuer continuar? [S/N] \033[m'))
    if res in 'Nn':
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(numeros)
print(par)
print(impar)
