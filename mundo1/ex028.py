## EX028 ##
from random import randint
from time import sleep

print('-=-' * 19)
print(' Eu pensarei em um número entre 0 e 5, tente adivinhar: ')
print('-=-' * 19)
rand = randint(0, 5)
while True:
    numero = int(input('Tente a sorte: '))
    if numero > 5 or numero < 0:
        print('ERROR: Digite um numero entre 0 e 5.')
    else:
        break
print('PROCESSANDO...')
sleep(2)
if numero == rand:
    print('Parabéns, você me venceu! Realmente o número era {}!'.format(rand))
else:
    print('Você errou! O número correto era {} e não {}'.format(rand, numero))
