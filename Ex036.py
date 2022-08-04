casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario: R$ '))
anos = int(input('Quantos anos de financiamento: '))
prestacao = casa / (anos *12)
minimo = salario * 0.30
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa,anos),end='')
print(' a prestacao sera de R$ {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser \33[4;34mconcedido!\33[m')
else:
    print('\33[31mEmprestimo Negado!\33[m')
