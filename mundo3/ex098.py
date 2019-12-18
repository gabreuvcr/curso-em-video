## EX098 ##
import time

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:  
        passo = abs(passo)
    print(f'\nContagem de {inicio} até {fim} de {passo} em {passo}: ')
    if inicio > fim:
        fim = fim - 1
        passo = passo * -1
    else:
        fim = fim + 1
    for i in range(inicio, fim, passo):
        print(i, end = ' ', flush = True)
        time.sleep(0.2)
    print('FIM!\n')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
