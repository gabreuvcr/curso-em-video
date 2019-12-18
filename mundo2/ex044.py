## EX044 ##

print('{:=^40}'.format(' LOJA DO JOSIVALDO ')) #centraliza em 40 espaços
produto = float(input('Qual o valor do produto? R$'))
print('(1) À vista dinheiro/cartão: 10% de desconto.')
print('(2) À vista no cartão: 5% de desconto. ')
print('(3) Em até 2x no cartão: preço normal.')
print('(4) 3x ou mais no cartão: 20% de juros.')
i = int(input('Selecione a opção de pagamento: '))
if i == 1:
    print('Preço final: R${}'.format(produto * 0.9))
elif i == 2:
    print('Preço final: R${}'.format(produto * 0.95))
elif i == 3:
    print('Preço final: R${}'.format(produto))
elif i == 4:
    parcela = int(input('Quantas parcelas? '))
    print('Cada parcela será R${:.2f} \nPreço final: R${}'.format((produto * 1.2) / parcela, produto * 1.2))
else:
    print('Digite um valor valido.')
