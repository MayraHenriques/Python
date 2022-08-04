from math import hypot


cateto = float(input('cateto: '))
cateto2 = float(input('cateto oposto: '))
#hi = (cateto**2 + cateto2**2) ** (1/2)
hi = hypot(cateto,cateto2)
print('{:.2f}'.format(hi))



