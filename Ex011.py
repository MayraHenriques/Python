largura = float(input('Medida da largura da parede: '))
altura = float(input('Medida da altura da parede: '))
area = largura * altura
tinta = area / 2
print('A area total e: {:.2f} metros'.format(area))
print('Precisa de {}l de tinta'.format(tinta))