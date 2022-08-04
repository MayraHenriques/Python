nota = float(input('Digite a nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = float((nota + nota2) / 2)
print("\33[1;35mMedia do aluno {:.2f}\33[m".format(media))
if media < 5:
    print('Aluno reprovado!')
elif media >= 5 and media < 6.9:
    print('Aluno em recuperacao!')
else:
    print('Aluno Aprovado!')


