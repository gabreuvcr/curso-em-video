## EX076 ##

produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
            'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.80, 'Canetas', 22.30, 'Livro', 34.90)
print('')
print('~' * 40)
print(f'{"Lista de Compras":^40}')
print('~' * 40)
i = 0
j = 1
while True:
    print(f'{produtos[i]:.<25}R$ {produtos[j]:>11.2f}')
    i += 2
    j += 2
    if j == 19:
        break
print('~' * 40)
