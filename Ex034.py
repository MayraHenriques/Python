salario = float(input('Digite o salario R$ '))

if salario <=1250:
    aumento = salario + (salario * 0.15)
    print('Salario atual R$: {:.2f}'.format(aumento))
else:
    aumento = salario + (salario * 0.10)
    print('Salario atual R$: {:.2f}'.format(aumento))
