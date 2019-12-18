## EX099 ##
from time import sleep

def maior(* numeros):
    print('\nAnalisando os valores passados...')
    tam = len(numeros)
    maior = 0
    for k, v in enumerate(numeros):
        print(v, end = ' ', flush = True)
        sleep(0.1)
        if (k == 0) or (v > maior):
            maior = v
    print(f'\nForam informados {tam} valores ao todo.')
    print(f'O maior valor informado foi {maior}\n')
        


maior(2, 9, 4, 5, 7, 1)
maior(4, 7)
maior(1, 2)
maior(6)
maior()
maior(2, 3, 9, 3, 4, 5, 7, 10, 23, 76, 34, 23, 12, 35, 78, 92, 76, 73)
