## EX056 ##

media = 0
idademaisvelho = -1
countmulher = 0
for i in range(0, 4):
    print('{}º Pessoa: '.format(i+1))
    nome = input('Digite seu nome: ').strip().upper()
    while True:
        idade = int(input('Digite a sua idade: '))
        if idade < 0:
            print('Digite um valor valido.')
        else:
            break
    while True:
        sexo = str(input('Digite seu sexo (M/F): ')).strip().upper()
        if (sexo == 'M') or (sexo == 'F'):
            break
        else:
            print('Digite corretamente.')
    print('')
    media = media + idade
    if (sexo == 'M') and (idade > idademaisvelho):
        idademaisvelho = idade
        nomemaisvelho = nome
    if (sexo == 'F') and (idade < 20):
        countmulher = countmulher + 1
print('\nA media das idade é {:.2f}'.format(media / 4))
if idademaisvelho == -1:
    print('Não existe homens.')
else:
    print('O homem mais velho é o {} com {} anos'.format(nomemaisvelho, idademaisvelho))
if countmulher == 0:
    print('Não existe mulheres com menos de 20 anos.')
elif countmulher == 1:
    print('Há somente uma mulher com menos de 20 anos.')
else:
    print('Há {} mulheres com menos de 20 anos.'.format(countmulher))
