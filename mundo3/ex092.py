## EX092 ##
from datetime import date

geral = {}
geral['nome'] = str(input('Nome: ')).strip().capitalize()
ano = date.today().year
nascimento = (int(input('Ano de nascimento: ')))
geral['idade'] = ano - nascimento
geral['ctps'] = int(input('Carteira de trabalho (Digite 0, se não tiver): '))
if geral['ctps'] > 0:
    geral['contratacao'] = int(input('Ano de contratação: '))
    geral['salario'] = float(input('Salario: '))
    geral['aposentadoria'] = (geral['contratacao'] + 35) - nascimento
print(f'\n{geral}\n')
for k, v in geral.items():
    print(f'{k.capitalize()}: {v}')
