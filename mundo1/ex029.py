## EX029 ##

vel = int(input('Digite a velocidade do carro em km/h: '))
if vel > 80:
    print('Você foi multado por excesso de velocidade!')
    print('A velocidade máxima é de 80 km/h, você estava a {} km/h'.format(vel))
    print('É {} km/h acima do limite.'.format(vel-80))
    print('A sua multa é de R$ {}'.format((vel-80)*7))
else:
    print('Você está na velocidade permitida!')
