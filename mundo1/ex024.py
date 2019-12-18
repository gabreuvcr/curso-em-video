## EX024 ##

cidade = str(input('Digite o nome da sua cidade: ')).strip().upper()

print('Com true and false: ')
print(cidade[0:5] == 'SANTO')

print('\nCom if and else: ')
existe = cidade.upper().find('SANTO')
if existe == 0:
    print('A cidade começa com SANTO!')
else:
    print('A cidade não começa com SANTO!')
