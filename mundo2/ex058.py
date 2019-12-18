## EX058 ##
from random import randint
from time import sleep

print('Eu pensarei em um número entre 0 e 10 e você deverá acertar.')
rand = randint(0, 10)
jogador = False
tentativas = 0
todos = []
while jogador == False:
    if tentativas == 0:
        numero = int(input('Tente a sorte: '))
    else:
        print('\nVocê errou.')
        if numero > rand:
            print('Um pouco menos...', end = '')
        elif numero < rand:
            print('Um pouco mais...', end = '')
        numero = int(input('Tente novamente: '))
        while numero in todos:
            print('')
            numero = int(input('Você ja tentou esse numero.\nTente novamente: ')) 
    todos.append(numero)
    print('\nPROCESSANDO...\n')
    sleep(0.5)
    if numero == rand:
        print('Parabéns, você me venceu! Realmente o número era {}'.format(rand))
        jogador = True
        tentativas = tentativas + 1
    else:
        tentativas = tentativas + 1
if tentativas == 1:
    print('Você é um vidente, acertou de primeira!')
else:
    print('Você acertou com {} palpites.'.format(tentativas))
