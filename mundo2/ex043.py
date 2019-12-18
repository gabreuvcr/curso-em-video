## EX043 ##

altura = float(input('Qual a sua altura em M? '))
peso = float(input('Qual o seu peso em KG? '))
imc = peso / (altura ** 2)
print('Seu IMC é: {:.2f}'.format(imc))
if imc > 40:
    print('Obesidade III.')
elif imc >= 35:
    print('Obesidade II.')
elif imc >= 30:
    print('Obesidade I.')
elif imc > 25:
    print('Sobrepeso.')
elif imc >= 18.5:
    print('Peso ideal.')
else:
    print('Abaixo do peso.')
