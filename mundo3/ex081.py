## EX081 ##

numeros = []
while True:
    numeros.append(int(input('Valor: ')))
    r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    print('')
    if r == 'N':
        break
if len(numeros) == 1:
    print(f'Você digitou {len(numeros)} número.')
else:
    print(f'Você digitou {len(numeros)} números.')
numeros.sort(reverse = True)
print(f'Os valores em ordem decrescente são: {numeros}')
if 5 in numeros:
    print('O 5 faz parte da lista!')
else:
    print('O 5 não faz parte da lista!')
