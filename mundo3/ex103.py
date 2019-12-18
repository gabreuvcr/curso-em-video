## EX103 ##

def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '' or (gols.isnumeric() == False):
        gols = 0
    print(f'\nO jogador {nome} fez {gols} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: ')).capitalize()
gols = str(input('Digite a quantidade de gols: '))
ficha(nome, gols)
