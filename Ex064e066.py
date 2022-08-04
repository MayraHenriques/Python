
numero = cont = soma = 0
# numero = int(input('Digite um numero [999 para parar]: '))
while True:
    numero = int(input('\033[1;36mDigite um numero [999 para parar]: \033[m'))
    if numero == 999:
        break
    soma += numero
    cont += 1
print('Acabou! Voce digitou {} numeros e a soma e: {}'.format(cont, soma))
print(f'\033[34mAcabou! Voce digitou {cont} numeros e a soma e: {soma}\033[m')
