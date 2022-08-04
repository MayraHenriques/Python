total = totmil = menor = cont = 0
barato = ' '
print(' -+' * 8)
print('{:-^34}'.format('\033[1;32m LOJAS MEL\033[m'))
print(' -+' * 8)
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preco: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('\033[1;32m Fim do Programa \033[m '))
print(f'O total da compra foi R$ {total:6.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
