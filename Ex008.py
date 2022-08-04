valor = float (input('Digite um valor em metros: '))
centimetros = valor * 100
milimetros = valor * 1000
print('A medida de {}m corresponde a {}cm e {:10}mm'. format(valor,centimetros,milimetros))
km = valor / 1000
hm = valor / 100
print('A medida de {}m corresponde a {}km e {}hm'.format(valor,km,hm))

