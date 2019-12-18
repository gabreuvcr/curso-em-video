## EX063 ##

n = int(input('Digite o numero de elementos da Sequência de Fibonacci: '))
i = 0
fibo1 = 1
fibo2 = 1
while i < n:
    if i == 0:
        print('0', end = '; ')
    elif i == 1:
        print('1', end = '; ')
    elif i == 2:
        print('1', end = '; ')
    else:
        fn = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = fn
        print('{}'.format(fn), end = '; ')
    i = i + 1   
