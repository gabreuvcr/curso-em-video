## EX015 ##

km = float(input('Digite a quantidade de km rodados: '))
dias = int(input('Digite a quantidade de dias que foi alugado: '))
preco = (60 * dias) + (0.15 * km)
print('Total a pagar: R${:.2f}'.format(preco))
