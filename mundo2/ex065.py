## EX065 ##

resp = 'S'
maior = soma = i = 0
while resp == 'S':
    num = int(input('Digite o {}º número: '.format(i + 1)))
    if num > maior:
        maior = num
        if i == 0:
            menor = num
    if num < menor:
        menor = num
    soma = soma + num
    resp = str(input('Deseja continuar (S/N)? ')).strip().upper()
    print('')
    i = i + 1
print('A média entre os numeros é: {:.2f}'.format(soma / i))
print('O maior número é: {}'.format(maior))
print('O menor número é: {}'.format(menor))