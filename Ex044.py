print('\33[1;34m{:=^30}\33[m'.format(' LOJAS LISBOA '))
preco = float(input('Digite o valor da compra: R$ '))
print(''' FORMAS DE PAGAMENTO
[ 1 ] A VISTA dinheiro/cheque
[ 2 ] A VISTA cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao''')
opcao = int(input('Qual a opcao de pagamento? '))
if opcao == 1:
     total = preco - (preco * 10 / 100)
elif opcao == 2:
     total = preco - (preco * 0.05)
elif opcao == 3:
     total = preco
     parcela = total / 2
     print('Sua compra sera parcelado em 2x de R$ {:.2f}'.format(parcela))
elif opcao == 4:
     total = preco + (preco * 0.20)
     totalParc = int(input('Quantas parcelas? '))
     parcela = total / totalParc
     print('Sua compra sera parcelada em {}x de R$ {:.2f}'.format(totalParc, parcela))

else:
    total = preco
    print('Opcao Invalida!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, total))