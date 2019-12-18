## EX095 ##

geral = []
aproveitamento = {}
gols = []
while True:
    aproveitamento['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou? '))
    for i in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols na {i}º partida? ')))
    aproveitamento['gols'] = gols[:]
    aproveitamento['total'] = sum(gols)
    geral.append(aproveitamento.copy())
    resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    gols.clear()
    print()
    if resp == 'N':
        break
print('-' * 50)
print(f'{"Cod":>4} {"Nome":>4}{"Gols":>15}{"Total":>16} ')
print('-' * 50)
for k, v in enumerate(geral):
    print(f'{k + 1:>4} ', end = '')
    for d in v.values():
        print(f'{str(d):<15}', end = '')
    print()
print('-' * 50)
while True:
    num = int(input('Mostrar dados de qual jogador? '))
    if num == 999:
        print('Finalizando...')
        break
    elif num > len(geral) or num <= 0:
        print('Valor invalido.')
    else:
        print(f'\nLevantamento do jogador {geral[num - 1]["nome"]}: ')
        for i, v in enumerate(geral[num - 1]['gols']):
            print(f'  → No jogo {i + 1}º fez {v} gols.')
    print()
