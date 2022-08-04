num = int(input('Digite um numero: '))
num1 = int(input('Digite o segundo numero: '))
num2 = int(input('Digite o terceiro numero: '))
menor = num
if num1 < num and num1 < num2:
    menor = num1
if num2 < num and num2 < num1:
    menor = num2
maior = num
if num1 > num and num1 > num2:
    maior = num1
if num2 > num and num2 > num1:
    maior = num2
print('O {} e o menor'.format(menor))
print('O {} e o maior'.format(maior))
