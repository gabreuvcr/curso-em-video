## EX106 ##
from time import sleep

while True:
    print('\nSistema de Ajuda PyHelp\n')
    resp = str(input('Função ou Biblioteca: ')).strip().lower()
    if resp == 'fim':
        break
    print(f'\nAcessando o manual do comando "{resp}"...\n')
    sleep(1)
    help(resp)
