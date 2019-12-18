## EX102 ##

def fatorial(n, show = False):
    """
    - Calcula o fatorial de um numero
    n : O numero a ser calculado
    show (opcional): Opção de mostrar ou não a sequencia da conta
    return: O valor do fatorial de n.
    """
    f = 1
    for i in range(n, 0, -1):
        f = f * i
        if show == True:
            if i != 1:
                print(f'{i} x ', end = '')
            else:
                print(f'{i} = ', end ='')
    return f


print(fatorial(5))
print(fatorial(8, False))
print(fatorial(7, True))
help(fatorial)
