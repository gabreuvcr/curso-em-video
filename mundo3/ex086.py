## EX086 ##

matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
         matriz[l].append(int(input(f'Digite o valor [{l}][{c}]: ')))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print('')
