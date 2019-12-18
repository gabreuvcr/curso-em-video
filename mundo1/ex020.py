## EX020 ##
from random import shuffle

aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação é: {}'.format(lista))
print('O primeiro elemento é {}'.format(lista[0]))
print('O ultimo elemento é {}'.format(lista[-1]))
