peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em m: '))
imc = peso / (altura **2)
print('Seu IMC e de : {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta ABAIXO DO PESO! ')
elif 18.5 <= imc < 25:
    print('Voce esta no PESO IDEAL! ')
elif 25 <= imc < 30:
    print('Voce esta SOBREPESO! ')
elif 30 <= imc < 40:
    print('Voce esta OBESO! ')
else:
    print('Voce esta com OBESIDADE MORBIDA! ')