numero = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversao:
\33[32m[1] converter para BINARIO\33[m
\33[33m[2] converter para OCTAL\33[m
\33[34m[3] converter para HEXADECIMAL\33[m''')
opcao = int(input('Sua opcao: '))
if opcao == 1 :
    print('{} convertido para BINARIO: {}'.format(numero,bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL: {}'.format(numero,oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL: {}'.format(numero,hex(numero)[2:]))
else:
    print('Opcao invalida, tente novamente.! ')