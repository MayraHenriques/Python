import random
comp = random.randint(0, 10)
print('Ja pensei num numero! Sua vez!!')
acertou = False
palpites = 0
# num = int(input('Digite um numero: '))
while not acertou:
    jogador = int(input('Digite um numero: '))
    palpites += 1
    if jogador == comp:
        acertou = True
        print('\033[1;32mParabens, acertou!\033[m')
    else:
        if jogador < comp:
            print('\033[35mMais...\033[m')
        elif jogador > comp:
            print('\033[37mMenos...\033[m')
    #print('Ganhei ! Eu pensei no numero {} e voce no {}'.format(comp,num))

print(palpites)