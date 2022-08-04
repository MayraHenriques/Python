real = float(input("Insira o valor em R$: "))
moeda = real * 0.19
euro = real * 0.19
iene = real * 25.86
print('Voce pode comprar US$ {:.2f}'.format(moeda))
print('Voce pode comprar euros {:.2f}'.format(euro))
print('Voce pode comprar iene {:.2f}'.format(iene))