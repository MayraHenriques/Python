from time import sleep
valor = int(input('Digite um valor: '))
valor2 = int(input('Digite um valor: '))
opcao = 0
soma = 0
while opcao != 5:
    print('-+-'* 10)
    print('''    MENU : 
    [ 1 ] SOMAR 
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NUMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    print('-+-' * 10)
    opcao = int(input('\033[1;31mQual a sua opcao? \033[m'))
    if opcao == 1:
        soma = valor + valor2
        print('\033[1;33mA soma dos valores e : {}\033[m'.format(soma))
        sleep(1)
    elif opcao == 2:
        print(valor * valor2)
    elif opcao == 3:
        if valor > valor2:
            maior = valor
        else:
            maior = valor2
        print(maior)
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        valor = int(input('Digite um valor: '))
        valor2 = int(input('Digite um valor: '))
    elif opcao == 5:
        print('Finalizando....')
        sleep(2)
    else:
        print('Opcao invalida !!!')
