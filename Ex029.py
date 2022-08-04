velocidade = float(input('A velocidade do carro e: '))
if velocidade > 80 :
    print('Voce foi multado!')
    multa = (velocidade - 80) * 7
    print('Voce deve pagar uma multa de R$ {:.2f}!'.format(multa))
else:
    print('Tenha um bom dia!')
