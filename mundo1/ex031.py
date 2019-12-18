## EX031 ##

distancia = float(input('Digite em km a distancia da viagem: '))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print('A passagem irá custar R${:.2f}'.format(preco))
print('Boa viagem!')
