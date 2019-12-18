## EX064 ##

n = contador = soma = 0
while n != 999:
    n = int(input('Digite valores (999 termina o programa): '))
    if n != 999:
        soma = soma + n
        contador = contador + 1
print('Foram digitados {} numeros e a soma vale {}'.format(contador, soma))
