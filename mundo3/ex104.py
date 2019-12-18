## EX104 ##

def leiaInt(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            n = int(n)
            break
        print('ERRO! Digite um valor inteiro válido.')
    return n


n = leiaInt('Digite um numero: ')
print(f'O numero que você digitou foi {n}')
