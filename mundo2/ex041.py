## EX041 ##
from datetime import date

ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano
print('Idade: {} anos'.format(idade))
if idade <= 9:
    print('O atleta é MIRIM.')
elif idade <= 14:
    print('O atleta é INFATIL.')
elif idade <= 19:
    print('O atleta é JUNIOR.')
elif idade <= 25:
    print('O atleta é SÊNIOR.')
else:
    print('O atleta é MASTER.')
