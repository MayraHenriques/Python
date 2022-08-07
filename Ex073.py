times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atletico', 'Botafogo', 'At-PR', 'Bahia',
         'Sao Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitoria', 'Coritiba', 'Avai', 'Ponte Preta',
         'Atletico-GO')
for t in times:
    print(t)
print(f'Os 5 primeiros : {times[0:5]}')
print('-=' * 20)
print(f'Os 4 ultimos: {times[-4:]} ')
print('-=' * 20)
print(f'Em ordem alfabetica: {sorted(times)}')
print('-=' * 20)
print(f'O Chapecoense esta : {times.index("Chapecoense")+1}º posicao.')
print('-=' * 20)