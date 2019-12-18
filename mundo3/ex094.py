## EX094 ##

todos = []
pessoa = {}
media = 0 
while True:
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] == 'M' or pessoa['sexo'] == 'F':
            break
        print('Erro! Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    media = media + pessoa['idade']
    todos.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
        if resp == 'S' or resp == 'N':
            break
        print('Erro! Digite apenas S ou N.')
    print()
    if resp == 'N':
        break
total = len(todos)
media = media / total
print(f' → O grupo tem {total} pessoas.')
print(f'\n → A média de idade é de {media:.2f} anos.')
print(f'\n → As mulheres cadastradas foram: ')
for p in todos:
    if p['sexo'] == 'F':
        print(p['nome'], end = '; ')
print(f'\n\n → Lista das pessoas que estão acima da idade media: ')
for p in todos:
    if p['idade'] > media:
        print(f'Nome: {p["nome"]}; Sexo: {p["sexo"]};  Idade: {p["idade"]};')
