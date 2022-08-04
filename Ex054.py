from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}º pessoa: '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior +=1
        print('\033[1;35mAtingiu a maioridade!!!\033[m')
    else:
        totmenor +=1
        print('Essa pessoa e menor de idade!!!')
    print('{} anos.'.format(idade))
print(totmaior, totmenor)
