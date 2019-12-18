## EX053 ##

texto = str(input('Digite um texto: ')).strip().upper().replace(' ', '')
print('Texto: {}'.format(texto))
textoinv = texto[::-1]
print('Inverso: {}'.format(textoinv))
if texto == textoinv:
    print('É um palíndromo.')
else:
    print('Não é palíndromo.')
print('\nCom join e função reversed:')
print(''.join(list(reversed(texto))))