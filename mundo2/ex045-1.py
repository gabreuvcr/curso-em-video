## EX045 ##
from time import sleep
from random import choice   

print('-=-' * 10)
print('          JOKENPÔ ')
print('-=-' * 10)
print('\nO computador está escolhendo...')
sleep(2)
pc = choice(['PEDRA', 'PAPEL', 'TESOURA'])
while True:
    jogada = str(input('\nEscolha pedra, papel ou tesoura: ')).strip().upper()
    if (jogada == 'PEDRA') or (jogada == 'PAPEL') or (jogada == 'TESOURA'):
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
print('VOCÊ JOGOU: {} \nCOMPUTADOR JOGOU: {}'.format(jogada, pc))
print('-=-' * 10)
if jogada == pc:
    print('\nEmpate! Ambos escolheram {}.'.format(jogada))
elif jogada == 'PEDRA' and pc == 'TESOURA':
    print('\nVocê ganhou! A sua {} esmaga a {}.'.format(jogada, pc))
elif jogada == 'PEDRA' and pc == 'PAPEL':
    print('\nVocê perdeu! O {} embrulha a sua {}.'.format(pc, jogada))
elif jogada == 'PAPEL' and pc == 'TESOURA':
    print('\nVocê perdeu! O {} corta o seu {}.'.format(pc, jogada))
elif jogada == 'PAPEL' and pc == 'PEDRA':
    print('\nVocê ganhou! O seu {} embrulha a {}'.format(jogada, pc))
elif jogada == 'TESOURA' and pc == 'PAPEL':
    print('\nVocê ganhou! A sua {} corta o {}'.format(jogada, pc))
elif jogada == 'TESOURA' and pc == 'PEDRA':
    print('\nVocê perdeu! A {} esmaga a sua {}'.format(pc, jogada))
