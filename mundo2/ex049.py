## EX049 ##

num = int(input('Digite o numero para saber sua tabuada: '))
for i in range(0, 21):
    print('{} x {:2} = {}'.format(num, i, num * i))
