list = []
mai = men = 0
for c in range(0, 5):
       list.append(int(input(f'Digite um valor para a posicao {c}:')))
       if c == 0:
               mai = men = list[c]
       else:
               if list[c] > mai:
                       mai = list[c]
               if list[c] < men:
                       men = list[c]
print(list)
print(f'O maior valor digitado foi {mai} nas posicoes ', end='')
for i, v in enumerate(list):
        if v == mai:
                print(f'{i}...', end='')
print()
print(f'O maior valor digitado foi {men} nas posicoes ', end='')
for i, v in enumerate(list):
        if v == men:
                print(f'{i}...', end='')


