## EX083 ##

exp = list(input('Digite uma expressão matemática: '))
di = exp.count('(')
es = exp.count(')')
if di == es:
    print('A expressão está correta!')
elif di > es:
    print('A expressão está errada! É preciso fechar os parenteses!')
elif di < es:
    print('A expressão está errada! É preciso abrir parenteses antes de fechar!')
