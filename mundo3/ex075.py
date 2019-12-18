## EX075 ##

numeros = (int(input('Digite um número: ')), 
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')), 
           int(input('Digite o último número: ')))
print(f'\nVocê digitou os valores {numeros}')
if numeros.count(9) == 0:
    print(f'\nO valor 9 apareceu nenhuma vez.')
elif numeros.count(9) == 1:
    print(f'\nO valor 9 apareceu {numeros.count(9)} vez.')
else:
    print(f'\nO valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'\nO valor 3 apareceu na {numeros.index(3) + 1}º posição.')
else:
    print('\nO valor 3 não foi digitado em nenhuma posição.')
par = 0
for c in numeros:
    if c % 2 == 0:
        if par == 0:
            print('\nOs valores pares digitados foram: ', end = '')
        par += 1
        print(c, end = '; ')
if par == 0:
    print('\nNão foi digitado nenhum valor par.')
else:
    print('')
