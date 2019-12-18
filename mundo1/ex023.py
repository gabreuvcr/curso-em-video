## EX023 ##

print('Com matematica: ')
num = int(input('Digite um numero entre 0 e 9999: '))
unidade = (num // 1) % 10
dezena = (num // 10) % 10
centena = (num // 100) % 10
milhar = (num // 1000) % 10
if num > 9999 or num < 0:
    print('Valor invalido.')
else:
    print('unidade: {}'.format(unidade))
    print('dezena: {}'.format(dezena))
    print('centena: {}'.format(centena))
    print('milhar: {}'.format(milhar))

print('\nCom string: ')
num = input('Digite um numero entre 0 a 9999: ')
qnt = len(num)
n = int(num)
if n > 9999 or n < 0:
    print('Valor invalido.')
elif qnt == 1:
    print('unidade: {}'.format(num[0]))
    print('dezena: 0')
    print('centena: 0')
    print('milhar: 0')
elif qnt == 2:
    print('unidade: {}'.format(num[1]))
    print('dezena: {}'.format(num[0]))
    print('centena: 0')
    print('milhar: 0')
elif qnt == 3:
    print('unidade: {}'.format(num[2]))
    print('dezena: {}'.format(num[1]))
    print('centena: {}'.format(num[0]))
    print('milhar: 0')
elif qnt == 4:
    print('unidade: {}'.format(num[3]))
    print('dezena: {}'.format(num[2]))
    print('centena: {}'.format(num[1]))
    print('milhar: {}'.format(num[0]))
