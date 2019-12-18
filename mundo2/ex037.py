## EX037 ##

num = int(input('Digite um numero: '))
print('\n(1) Binário')
print('(2) Octal')
print('(3) Hexadecimal')
while True:
    aux = int(input('Digite a opção: '))
    if aux == 1:
        print('\nBinário: {}'.format(bin(num)[2:]))
        break
    elif aux == 2:
        print('\nOctal: {}'.format(oct(num)[2:]))
        break
    elif aux == 3:
        print('\nHexadecimal: {}'.format(hex(num)[2:]))
        break
    else:
        print('ERROR: Valor invalido')
