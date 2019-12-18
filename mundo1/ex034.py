## EX034 ##

salario = float(input('Digite seu salario: '))
if salario > 1250:
    print('Você terá um aumento de 10%!')
    print('Seu salario antigo era: R${:.2f}'.format(salario))
    print('Seu novo salario é: R${:.2f}'.format(salario*1.1))
else:
    print('Você terá um aumento de 15%!')
    print('Seu salario antigo era: R${:.2f}'.format(salario))
    print('Seu novo salario é: R${:.2f}'.format(salario*1.15))
