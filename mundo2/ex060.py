## EX060 ##

num = int(input('Digite um numero para saber seu fatorial: '))
num1 = num
fatorial = 1
while num > 0:
    fatorial = fatorial * num
    num = num - 1
print('Fatorial com while: {}'.format(fatorial))

fatorial = 1
for i in range(num1, 0, -1):
    fatorial = fatorial * i
print('Fatorial com for: {}'.format(fatorial))
