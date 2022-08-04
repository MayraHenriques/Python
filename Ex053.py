frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
# inverso = junto [::-1] # Substitui o for
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(frase, junto, inverso)
    print('\033[1;33mTemos um PALINDROMO!!!\033[m')
else:
    print('Nao e palindromo.')
