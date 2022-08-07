cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze','doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        num = int(input('Digite um numero de 0 a 20: '))
        if 0 <= num <= 20:
            break
        print('Entre 0 e 20: ', end='')
    print(f'Voce digitou {cont[num]}')
    print()
    #resp = ' '
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
         break


'''while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <=20:
            break
        print('Número inválido. ', end='')
    print(f'O número digitado foi {cont[num]}.')
    print(' ')
    resp = str(input('Deseja continuar?[S/N]: ')).upper().strip()
    if resp == 'N':
        break'''
#print(input(f'Quer continuar? [S/N] '))
