## EX035 ##

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a teceira reta: '))
if (r1+r2 > r3) and (r2+r3 > r1) and (r1+r3 > r2):
    print('É possivel formar um triangulo!')
else:
    print('Não é possivel formar um triangulo!')
