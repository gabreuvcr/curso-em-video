## EX096 ##

def area(l, c):
    print(f'\nA área de um terreno {l} x {c} é de {l * c} m².')


print('\nControle de terrenos\n')
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
