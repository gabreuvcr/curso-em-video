## EX054 ##
from datetime import date

atual = date.today().year
menor = 0
maior = 0
for i in range(0, 7):
    ano = int(input('Digite o seu ano de nascimento: '))
    if (atual - ano) >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('{} pessoas atingiram a maioridade e {} são menores.'.format(maior, menor))
