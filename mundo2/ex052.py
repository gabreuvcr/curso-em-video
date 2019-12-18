## EX052 ##

num = int(input('Digite um numero para saber se ele é primo: '))
count = 0
divisores = []
for i in range(1, num+1):
    if (num % i) == 0:
        count = count + 1
        divisores.append(i)
print('Os divisores são: {}'.format(divisores))
if count == 2:
    print('O numero é primo.')
else:
    print('O numero não é primo.')
