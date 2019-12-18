## EX085 ##

numeros =[[], []]
for i in range(0, 7):
    n = int(input(f'Digite o {i + 1}º valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print(f'Numeros pares: {numeros[0]}')
print(f'Numeros impares: {numeros[1]}')
