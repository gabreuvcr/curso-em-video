## EX082 ##

num = []
par = []
impar = []
while True:
    num.append(int(input('Valor: ')))
    r = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if r == 'N':
        break
for i in num:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(f'Lista completa: {num}')
print(f'Lista de pares: {par}')
print(f'Lista de impares: {impar}')
