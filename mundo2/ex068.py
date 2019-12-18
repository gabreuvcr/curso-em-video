## EX068 ##
from random import randint

print('Vamos jogar par ou impar!\n')
vitorias = 0
while True:
    while True:
        parouimpar = str(input('Par ou impar? ')).strip().upper()[0]
        if (parouimpar == 'P') or (parouimpar == 'I'):
            break
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    soma = jogador + computador
    print(f'\nVoce jogou {jogador} e o computador {computador}. A soma {soma}', end = ' ')
    if parouimpar == 'P':
        if (soma % 2) == 0:
            print('é PAR.')
            print('Você venceu!\n')
            vitorias += 1
        else:
            print('é IMPAR.')
            print('Você perdeu!\n')
            break
    if parouimpar == 'I':
        if (soma % 2) == 0:
            print('é PAR.')
            print('Você perdeu!\n')
            break
        else:
            print('é IMPAR.')
            print('Você venceu!\n')
            vitorias += 1
print(f'GAME OVER. Você venceu {vitorias} vezes.')
