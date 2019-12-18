## EX036 ##

casa = float(input('Qual o valor da casa: '))
salario = float(input('Digite o seu salario: '))
anos = int(input('Em quantos anos você deseja comprar? '))
prestação = casa/(anos*12)
trinta = salario * 0.3
print('O valor da prestação será de R${:.2f}'.format(prestação))
if prestação <= trinta:
    print('Emprestimo concedido!')
    print('Bom aproveito!')
else:
    print('Emprestimo negado!')
