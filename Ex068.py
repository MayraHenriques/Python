import random
v = 0
print('-*' * 12)
print('VAMOS JOGAR PAR OU IMPAR')
print('-*' * 12)
while True:
    num = int(input('Digite um numero: '))
    comp = random.randint(0, 11)
    total = num + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? ')).strip().upper()[0]
    print(f'Voce jogou {num} e o computador {comp}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[34mVOCE VENCEU!\033[m')
            v += 1
        else:
            print('\033[31mVOCE PERDEU!!\033[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('\033[34mVOCE VENCEU!\033[m')
            v += 1
        else:
            print('\033[31mVOCE PERDEU!\033[m')
            break
        print('Vamos jogar novamente...')
    print(f"GAME OVER! VOCE VENCEU {v} vezes." )
    print("\U0001f600")