## EX011 ##

altura = float(input('Digite a altura em metros da parede: '))
largura = float(input('Digite a largura em metros da parede: '))
#1 litro = 2m²
area = altura * largura
litros = area / 2
print('A area total é {:.2f} m²'.format(area))
print('A quantidade total de tinta necessaria é de {:.2f} litros.'.format(litros))
