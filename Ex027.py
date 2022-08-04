nome = str(input('Digite seu nome completo: ')).strip()
primeiro = nome.split()
print('Seu primeiro nome e: {}'.format(primeiro[0]))
print('Seu ultimo nome e: {}'.format(primeiro[len(primeiro)-1]))
print('Seu nome maisuculo e: {}'.format(nome.upper()))
print('Tem de no seu nome?: {}'.format('de' in nome))




