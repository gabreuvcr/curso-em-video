## EX032 ##
from datetime import date

ano = int(input('Digite um ano para saber se foi bissexto ou digite 0 para saber o ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0)):
    print('O ano {} É BISSEXTO.'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))
