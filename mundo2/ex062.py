## EX063 ##

ptermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
i = 0 
termo = ptermo
maistermos = 1
while i < 10:
    print("{}".format(termo), end = ' → ')
    termo = termo + razao
    if i == 9:
        while maistermos != 0:
            print('PAUSA')
            maistermos = int(input('Deseja mais alguma quantidade de termos? '))
            j = 0
            while j < maistermos:
                print("{}".format(termo), end = ' → ')
                termo = termo + razao
                j = j + 1
                i = i + 1
    i = i + 1
print('Finalizado, foram mostrados {} termos.'.format(i))
