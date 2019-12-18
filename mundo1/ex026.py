## EX026 ##

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('Posição do primeiro "A": {}'.format(frase.find('A')+1))
print('Posição do ultimo "A": {}'.format(frase.rfind('A')+1))
