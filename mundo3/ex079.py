## EX079 ##

numeros = []
while True:
    num = int(input('Digite um valor: '))
    if num in numeros:
        print('Valor duplicado! Não irei adicionar.')
    else:
        numeros.append(num)
        print('Valor adicionado com sucesso.')
    while True:
        r = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if r == 'S' or 'N':
            break
    print('')
    if r == 'N':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')
