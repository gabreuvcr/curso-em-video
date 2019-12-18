## EX100 ##
from time import sleep
from random import randint

def sorteia(lst):
    print('\nSortenado 5 valoresda lista: ')
    for i in range(0, 5):
        num = randint(1, 10)
        print(num, end = ' ', flush = True)
        sleep(0.2)
        lst.append(num)  


def somaPar(lst):
    print(f'\nSomando os valores pares de {lst}, temos: ', end = '')
    soma = 0 
    for i in lst:
        if (i % 2) == 0:
            soma = soma + i
    print(soma)
        

numeros = []
sorteia(numeros)
somaPar(numeros)
