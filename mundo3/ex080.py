## EX080 ##

numeros = []
for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if i == 0:
        numeros.append(num)
        print('Adicionado o primeiro elemento da lista.')
    if i > 0:
        for j in range(0, len(numeros)):
            if num > max(numeros):
                numeros.append(num)
                print('Adicionado no final da lista.')
                break
            if num < min(numeros):
                numeros.insert(0, num)
                print('Adicionado no inicio da lista.')
                break
            if num == numeros[j]:
                numeros.insert(j, num)
                if j == 0:
                    print('Adicionado no inicio da lista.')
                else:
                    print(f'Adicionado na posição {j} da lista.')
                break
            if numeros[j] < num < numeros[j + 1]:
                numeros.insert(j + 1, num)
                print(f'Adicionado na posição {j + 1} da lista.')
                break
print(f'Os numeros adicionados foram: {numeros}')
