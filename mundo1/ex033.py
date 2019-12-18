## EX033 ##

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
print('Entre os valores {}, {} e {}. O maior é {} e o menor é {}'.format(n1, n2, n3, maior, menor))

