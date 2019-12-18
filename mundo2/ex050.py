## EX050 ##

soma = 0
count = 0
for i in range(0, 6):
    num = int(input('Digite o numero {}: '.format(i+1)))
    if (num % 2) == 0:
        soma = soma + num
        count = count + 1
if count == 0:
    print('Não foi digitado números pares.')
else:
    print('A soma dos numeros pares digitados é: {}'.format(soma))
