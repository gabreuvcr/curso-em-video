## EX018 ##
from math import sin, cos, tan, radians

angulo = float(input('Digite o angulo: '))
rad = radians(angulo)
sen = sin(rad)
cos = cos(rad)
tg = tan(rad)
print('O seno é: {:.2f} \nO cosseno é: {:.2f} \nA tangente é: {:.2f}'.format(sen, cos, tg))
