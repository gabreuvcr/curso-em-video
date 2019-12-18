## EX084 ##

dados = []
pessoas = []
maior = menor = total = 0
nomemaior = []
nomemenor = []
while True:
    dados.append(str(input('Nome: ')).strip().upper())
    dados.append(float(input('Peso: ')))
    if dados[1] > maior:
        maior = dados[1]
    if dados[1] < menor or total == 0:
        menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    total = total + 1
    res = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if res == 'N':
        break
for p in pessoas:
    if p[1] == maior:
        nomemaior.append(p[0])
    if p[1] == menor:
        nomemenor.append(p[0])
print(f'\nAo todo, você cadastrou {total} pessoas.')
print(f'O maior peso foi de {maior} kg. Peso de {nomemaior}')
print(f'O menor peso foi de {menor} kg. Peso de {nomemenor}')
