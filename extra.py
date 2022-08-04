for x in range(1,6):
    for y in range(5,x-1,-1):
        print(y, end='')
    print()


my_string = "paralelepipedo"
x = 0
for i in my_string:
    x = x + 1
    print(my_string[0:x])
for i in my_string:
    x = x - 1
    print(my_string[0:x])

for c in range(0, 10, 3):
    print (c)
