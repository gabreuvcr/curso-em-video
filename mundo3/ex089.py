## EX089 ##

geral = []
while True:
    nome = str(input('Nome: ')).strip().upper()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    media = (nota1 + nota2) / 2
    geral.append([nome, [nota1, nota2], media])
    print()
    if resp == 'N':
        break
print(f'{"No.":>3}{"NOME":>6}{"MEDIA":>15}')
print('-' * 25)
tamanho = len(geral)
for i in range(0, tamanho):
    print(f'{i + 1:>3}  {geral[i][0]:<12}  {geral[i][2]:<5.1f}')
print('-' * 25)
while True:
    print()
    n = int(input('Mostrar notas de algum aluno? (999 interrompe): '))
    if n == 999:
        break
    elif n > tamanho or n < 0:
        print('Valor invalido.')
    else:
        print(f'As notas de {geral[n - 1][0]} são {geral[n - 1][1]}')
print('Finalizando...')
