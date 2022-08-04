maiorpeso = 0
menorpeso = 0
media = 0
soma = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {}º pessoa:'.format(p)))
    if p == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
    soma += peso
    media = soma / 5
print('\033[1;32mMaior peso: {:.2f} Kg\033[m'.format(maiorpeso))
print('\033[1;33mMenor peso: {:.2f} Kg\033[m'.format(menorpeso))
print(media)
print(soma)
