## EX022 ##

nome = str(input('Digite seu nome completo: ')).strip() #eliminando espaços
separado = nome.split() #separando palavras para lista
nospace = ''.join(separado) #juntando a lista sem espaço
#nospace = nome.replace(' ', '')  tambem tira espaço
print('Maiusculo: {}'.format(nome.upper()))
print('Minusculo: {}'.format(nome.lower()))
print('[sem count] Quantidade de letras (sem espaço): {}'.format(len(nospace))) #quantidade de letras no nospace
print('[com count] Quantidade de letras (sem espaço): {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(separado[0], len(separado[0])))
