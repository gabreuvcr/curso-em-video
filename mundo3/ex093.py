## EX093 ##

aproveitamento = {}
gols = []
aproveitamento['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
partidas = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou? '))
for i in range(1, partidas + 1):
    gols.append(int(input(f'  Quantos gols na {i}º partida? ')))
aproveitamento['gols'] = gols[:]
aproveitamento['total'] = sum(gols)

print(f'\n{aproveitamento}\n')
    
for k, v in aproveitamento.items():
    print(f'O campo {k} tem o valor {v}')

print(f'\nO jogador {aproveitamento["nome"]} jogou {partidas} partidas.')
for i in range(1, partidas + 1):
    print(f'  → Na partida {i}, fez {aproveitamento["gols"][i - 1]} gols.')
print(f'Foi um total de {aproveitamento["total"]} gols.')
