## EX073 ##

times = ('Palmeiras', 'Flamengo', 'Internacional', 'Gremio', 'São Paulo', 'Atletico-MG', 'Atletico-PR',
         'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthias', 'Chapecoense', 'Ceará',
         'Vasco', 'Sport', 'America-MG', 'Vitoria', 'Paraná')
print(f'Os 5 primeiros colocados:\n{times[:5]}')
print(f'\nOs ultimos 4 colocados:\n{times[-4:]}')
print(f'\nOrdem alfabetica:\n{sorted(times)}')
print(f'\nPosição Chapecoense:\n{times.index("Chapecoense") + 1}º')
