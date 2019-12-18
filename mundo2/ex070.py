## EX070 ##

print('\nLojinha do Xingling: \n')
total = mais_caro = mais_mil = menor_preco = i = 0
while True:
    produto = str(input('Produto: ')).strip().upper()
    while True:
        preco = float(input('Preço: R$'))
        if preco >= 0:
            break
    while True:
        cont = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
        if (cont == 'S') or (cont == 'N'):
            break
    i += 1
    total += preco
    if preco > 1000:
        mais_mil += 1
    if (preco < menor_preco) or (i == 1):
        menor_preco = preco
        nome_mais_barato = produto
    print('')
    if cont == 'N':
        break
print(f'O total gasto foi: R${total:.2f}')
print(f'Produtos que custam mais de R$1000: {mais_mil}')
print(f'Nome do produto mais barato: {nome_mais_barato} (R${menor_preco:.2f})')
