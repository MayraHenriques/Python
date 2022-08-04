kmPercorrido = float(input('Quantidade de km percorrido: '))
diasAlugados = float(input('Dias alugados: '))
pagar = ((diasAlugados * 60) + (kmPercorrido * 0.15))
print('Valor a pagar R$ {:.2f}'.format(pagar))