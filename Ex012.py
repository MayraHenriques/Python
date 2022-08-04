# Calculo de porcentagem:
preco = float(input('Digite o valor: '))
desconto = preco * 5 / 100
precoFinal = preco - desconto
print('Valor do desconto e: ' + str(desconto))
print('Valor final com desconto e: {}'.format(precoFinal))