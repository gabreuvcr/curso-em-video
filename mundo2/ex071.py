## EX071 ##

print('\nBanco\n')
saque = int(input('Bom dia! Qual o valor do saque? R$'))
notas = [50, 20, 10, 1]
c = 0
while saque > 0:
    qntnotas = saque // notas[c]
    saque = saque % notas[c]
    if qntnotas > 0:
        print(f'Cédulas de R${notas[c]}: {qntnotas}')
    c += 1
