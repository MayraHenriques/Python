# Ex 35 e ex42.
segmento = float(input('Digite um segmento: '))
segmento2 = float(input('\33[1;31;40mDigite o segundo segmento: \33[m'))
segmento3 = float(input('\33[7;34mDigite o terceiro segmento: \33[m'))
if segmento < segmento2 + segmento3 and segmento2 < segmento + segmento3 and segmento3 < segmento + segmento2:
    print('Formou um triangulo!')
    if segmento == segmento2 == segmento3:
        print('Formou um EQUILATERO')
    elif segmento != segmento2 != segmento3 != segmento:
        print('Formou um ESCALENO')
    else:
        print('Formou um ISOSCELES')
else:
    print('Nao forma triangulo!')