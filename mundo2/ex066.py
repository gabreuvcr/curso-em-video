## EX066 ##

qnt = soma = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    qnt += 1
    soma += n
print(f'A soma dos {qnt} valores foi {soma}! ')
