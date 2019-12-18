## EX078 ##

valores = []
for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posiçao {i}: ')))
print(f'Você digitou os valores {valores}')
#pegando os indices dos maiores e dos menores valores
maior = max(valores)
menor = min(valores)
print(f'\nO maior valor foi {max(valores)} nas posições: ', end = '')
for ind, val in enumerate(valores):
    if val == maior:
        print(f'{ind}; ', end = '')
print(f'\nO menor valor foi {min(valores)} nas posições ', end = '')
for ind, val in enumerate(valores):
    if val == menor:
        print(f'{ind}; ', end = '')
