## EX038 ##

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print('O primeiro número é maior. ({} > {})'.format(num1, num2))
elif num2 > num1:
    print('O segundo número é maior. ({} < {})'.format(num1, num2))
else:
    print('Não existe valor maior, os dois são iguais. ({} == {})'.format(num1, num2))
