while True:
    n = int(input('Tabuada de qual numero? '))
    if n < 0:
        break
    print('*-' * 12)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('*-' * 12)
