## EX025 ##

nome = input('Digite seu nome completo: ')

print('Com find: ')
existe = nome.upper().find('SILVA')
if existe == -1:
    print('O nome não possui SILVA!')
else:
    print('O nome tem SILVA!')

print('\nCom in: ')
existe = 'SILVA' in nome.upper()
if existe: #if true
    print('Existe SILVA!')
else:
    print('Nao existe SILVA!')
