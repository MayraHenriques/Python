num = (int(input('Digite o primeiro numero: ')),
       int(input('Digite o segundo numero: ')),
       int(input('Digite o terceiro numero: ')),
       int(input('Digite o quarto numero: ')))
print(num)
print(f'O valor 9 apareceu {num.count(9)} vezes')
print(f'O valor 5 apareceu {num.count(5)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}º posicao')
else:
    print('O valor 3 nao foi digitado.')
print(f'Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n)
print(f'Os valores impares digitados foram ', end='')
for i in num:
    if i % 2 == 1:
        print(i)