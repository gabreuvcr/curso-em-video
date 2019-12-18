## EX087 ##

matriz = [[], [], []]
pares = tercol = maiorseg = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite o valor [{i}][{j}]: ')))
print()
for i in range(0, 3):
    for j in range(0, 3):
        print(f' [ {matriz[i][j]:2}  ] ', end = '')
        if matriz[i][j] % 2 == 0:
            pares = matriz[i][j] + pares
        if j == 2:
            tercol = matriz[i][j] + tercol
        if i == 1:
            if matriz[i][j] > maiorseg:
                maiorseg = matriz[i][j]
    print()
print(f'\nA soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {tercol}')
print(f'O maior valor da segunda coluna é {maiorseg}')
