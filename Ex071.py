print('Banco CEV')
valor = int(input('Valor do saque: '))
total = valor
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'\033[35mTotal de {totced} cedulas de R$ {ced},00\033[m')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
print('\033[4;31mSaque realizado com sucesso!! Have a good day!!\033[m')