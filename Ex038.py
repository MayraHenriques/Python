num = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
if num >num2 :
    print('\33[32m{}\33[m e maior que \33[34m{}\33[m'.format(num, num2))
elif num < num2:
    print('{} e maior que {}'.format(num2, num))
else:
    print('{} e {} sao iguais.'.format(num,num2))
