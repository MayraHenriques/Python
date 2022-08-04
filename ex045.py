from random import randint
from time import sleep
itens = ('\33[1;34mPedra\33[m' , '\33[1;33mPapel\33[m', '\33[1;31mTesoura\33[m')
computador = randint(0,2)
print(''' Suas opcoes:
[ 0 ] \33[34mPEDRA\33[m
[ 1 ] \33[33mPAPEL\33[m
[ 2 ] \33[31mTESOURA\33[m ''')
jogador = int(input('Qual a sua jogada? '))
print('\33[1;34mJO\33[m')
sleep(1)
print('\33[1;33mKEN\33[m')
sleep(1)
print('\33[1;31mPO!!!\33[m')
sleep(1)
print('-='* 12)
print('COMPUTADOR jogou {}'.format(itens[computador]))
print('JOGADOR jogou {}'.format(itens[jogador]))
print('-='* 12)
if computador ==0:
    if jogador == 0:
        print("** EMPATE !!! **")
    elif jogador ==1:
        print("** JOGADOR VENCEU !!! **")
    elif jogador ==2:
        print("** COMPUTADOR VENCEU !!! **")
    else:
        print('Jogada Invalida!')
elif computador ==1:
    if jogador ==0:
        print("** COMPUTADOR VENCEU !!! **")
    elif jogador ==1:
        print("** EMPATE !!! **")
    elif jogador ==2:
        print("** JOGADOR VENCEU !!! **")
    else:
        print('Jogada Invalida')
elif computador ==2:
    if jogador ==0:
        print("** JOGADOR VENCEU !!! **")
    elif jogador ==1:
        print("** COMPUTADOR VENCEU !!! **")
    elif jogador ==2:
        print("** EMPATE !!! **")
    else:
        print('Jogada Invalida')

