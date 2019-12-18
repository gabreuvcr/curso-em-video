## EX090 ##

aluno = {}
aluno['nome'] = str(input('Nome: ')).strip().capitalize()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] < 5:
    aluno['situação'] = 'Reprovado'
elif aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'
print(f'\nNome: {aluno["nome"]}')
print(f'Média: {aluno["média"]}')
print(f'Situação: {aluno["situação"]}')
print('\n\n')
for k, v in aluno.items():
    print(f'{k.capitalize()}: {v}')
