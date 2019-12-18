## EX017 ##
from math import hypot

catop = float(input('Digite o comprimento do cateto oposto: '))
catad = float(input('Digite o comprimento do cateto adjacente: '))
#hipotenusa = math.sqrt(math.pow(catop, 2) + math.pow(catad, 2))
hipotenusa = hypot(catop, catad)
print('O valor da hipotenusa: {:.2f}'.format(hipotenusa))
