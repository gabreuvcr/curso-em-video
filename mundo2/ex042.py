## EX042 ##

r1 = float(input('Digite o primeiro lado: '))
r2 = float(input('Digite o segundo lado: '))
r3 = float(input('Digite o terceiro lado: '))
if (r1+r2 > r3) and (r1+r3 > r2) and (r2+r3 > r1):
    print('É possivel formar um triangulo ', end = '')
    if (r1 == r2) and (r2 == r3):
        print('EQUILÁTERO!')
    elif (r1 != r2) and (r2 != r3) and (r1 != r3):
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Não é possivel formar um triangulo!')
