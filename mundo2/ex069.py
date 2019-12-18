## EX069 ##

print('\nCadastro de pessoas: \n')
maior_18 = homens = mulher_menor_20 = 0
while True:
    idade = int(input('Idade: '))
    while True:
         sexo = str(input('Sexo: ')).strip().upper()[0]
         if (sexo == 'M') or (sexo == 'F'):
             break
    if sexo == 'M':
        homens += 1
    if idade >= 18:
        maior_18 += 1
    if (sexo == 'F') and (idade < 20):
        mulher_menor_20 += 1
    while True:
        cont = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
        if (cont == 'S') or (cont == 'N'):
            break
    print('')
    if cont == 'N':
        break
print(f'Pessoa(s) com mais de 18 anos: {maior_18}')
print(f'Homens: {homens}')
print(f'Mulheres com menos de 20 anos: {mulher_menor_20}')
