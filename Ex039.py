from datetime import date
atual = date.today().year
ano = int(input('Digite seu \33[1;33mano de nascimento:\33[m '))
sexo = str(input('Digite \33[1;33m[F] se voce for mulher\33[m ou \33[1;34m[M] se for homem\33[m: ')).upper()
idade = atual - ano
print('Sua idade e: {} anos'.format(idade))
if sexo == 'F':
    print("Voce nao precisa se alistar.")
else:

    if idade == 18:
        print('Voce tem que se alistar IMEDIATAMENTE!')
    elif idade <18:
        saldo = 18 - idade
        print('Com {} anos, voce ainda nao precisa se alistar'.format(idade))
        ano2 = atual + saldo
        print('Seu alistamento sera em {}'.format(ano2))
    elif idade >18:
        saldo = idade - 18
        print('Ja deveria ter se alistado ha {} anos.'.format(saldo))
        ano2 = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano2))
