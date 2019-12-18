# EX088 ##
from random import randint
from time import sleep

jogos = []
dados = []
n = int(input('Quantos jogos você deseja? '))
print()
for i in range(0, n):
    for j in range(0, 6):
        while True:
            aleatorio = randint(1, 60)
            if aleatorio not in dados:
                break
        dados.append(aleatorio)
    dados.sort()
    jogos.append(dados[:])
    dados.clear()
for i in range(0, n):
    sleep(0.75) 
    print(f'Jogo {i + 1}: {jogos[i]}')   
print('\nBoa sorte!')
