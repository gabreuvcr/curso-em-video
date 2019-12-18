## EX045-2 ##
from time import sleep
from random import randint   

print('-=-' * 10)
print('          JOKENPÔ ')
print('-=-' * 10)
print('\nO computador está escolhendo...')
sleep(2)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
pc = randint(1, 3)
while True:
    print('\n[1] PEDRA.')
    print('[2] PAPEL.')
    print('[3] TESOURA.')
    jogada = int(input('Digite uma opção: '))
    if jogada == 1 or jogada == 2 or jogada == 3:
        break
    else:
        print('Digite uma opção valida.')
print('')
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ\n')
print('-=-' * 10)
print('VOCÊ JOGOU: {} \nCOMPUTADOR JOGOU: {}'.format(lista[jogada-1], lista[pc-1]))
print('-=-' * 10)
if jogada == pc:
    print('\nEmpate!')
elif (jogada == 1 and pc == 3) or (jogada == 2 and pc == 1) or (jogada == 3 and pc == 2):
    print('\nVocê ganhou!')
else:
    print('\nVocê perdeu!')
