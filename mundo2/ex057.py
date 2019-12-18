## EX057 ##

sexo = ''
while (sexo != 'F')  and (sexo != 'M'):
    sexo = str(input('Digite o seu sexo (M/F): ')).strip().upper()
    if (sexo != 'F') and (sexo != 'M'):
        print('ERROR: Valor invalido.\n')
if sexo == 'F':
    print('\nSeu sexo é feminino!')
else:
    print('\nSeu sexo é masculino!')
