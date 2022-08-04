soma = 0
media = 0
maisVelho = 0
nomeVelho = ''
mulher = 0
for p in range(1, 5):
    print('--- {}º PESSOA ---'.format(p))
    nome = str(input('Digite o Nome: ')).strip()
    idade = int(input('Digite a Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    if p == 1 and sexo in 'Mm':
        maisVelho = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maisVelho:
        maisVelho = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1

media = soma / 4
print('\033[35mA media de idade do grupo e de {} anos.\033[m'.format(media))
print('\033[34mO Homem mais velho e o {} com {} anos\033[m'.format(nomeVelho,maisVelho))
print('\033[36mTemos {} mulheres com menos de 20 anos\033[m'.format(mulher))