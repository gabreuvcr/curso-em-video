## EX061 ##

ptermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
i = 0 
termo = ptermo
while i < 10:
    print("{}".format(termo), end = ' → ')
    termo = termo + razao
    i = i + 1
print('Fim ')
