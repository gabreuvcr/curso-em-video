## EX027 ##

nome = input('Digite o seu nome completo: ')
nome = nome.split()
#elementos = len(nome) - 1 antigo
# -1 == ultimo elemento   
# -2 == penultimo
print('Primeiro nome: {}'.format(nome[0]))
print('Ultimo nome: {}'.format(nome[-1]))
