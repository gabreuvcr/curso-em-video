## EX067 ##

while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    if n < 0:
        break
    print('')
    for i in range(1, 11):
        print(f'{n} x {i:2} = {n * i}')
    print('')
print('\nTabuada Encerrada. Volte sempre!')
