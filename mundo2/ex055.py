## EX055 ##

maior = 0
menor = 0
for i in range(0, 5):
    while True:
        peso = float(input('Digite o {}º peso: '.format(i+1)))
        if peso >= 0:
                break
        else:
                print('Digite um valor positivo.')
    if peso > maior:
        maior = peso
        if i == 0:
            menor = peso
    if peso < menor:
        menor = peso
print('O maior peso registrado foi {:.2f} kg \nO menor peso é {:.2f} kg'.format(maior, menor))
