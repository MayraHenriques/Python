soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('\33[35mDigite o {}º numero: \33[m'.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print(soma)
