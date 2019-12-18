## EX039 ##
from datetime import date

ano = int(input('Informe o seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade < 18:
    print('Ainda falta(m) {} ano(s) para o alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}'.format((18 - idade) + atual))
elif idade > 18:
    print('Você já deveria ter se alistado há {} ano(s).'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(atual - (idade - 18)))
else:
    print('É a hora de você se alistar!')
