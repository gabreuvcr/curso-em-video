## EX072 ##

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    if n >= 0 and n <= 20:
        break
    else:
        print('Tente novamente.', end = ' ')
print(f'Você digitou o número {numeros[n]}.')
