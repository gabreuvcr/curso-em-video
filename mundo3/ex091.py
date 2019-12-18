## EX091 ##
from random import randint
from time import sleep

dados = {}
dados['jogador1'] = randint(1, 6)
dados['jogador2'] = randint(1, 6)
dados['jogador3'] = randint(1, 6)
dados['jogador4'] = randint(1, 6)
print('Valores sorteados: ')
ranking = sorted(dados.items(), key = lambda kv: kv[1])
ranking.reverse()
for k, v in dados.items():
    sleep(0.75)
    print(f'  O {k} tirou {v}')
print('\nRanking dos jogadores: ')
for i, v in enumerate(ranking):
    sleep(0.75)
    print(f'  {i + 1}º lugar: {v[0]} com {v[1]}')
