from random import randint
num = (randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10))
for n in num:
    print(n, end=' ')
print(f'\nO maior foi: {max(num)}')
print(f'O menor foi: {min(num)}')
