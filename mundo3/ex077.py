## EX077 ##

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'grátis',
            'estudar', 'ufmg', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro',
            'ciência', 'computação')
vogais = ('a', 'e', 'i', 'o', 'u',
          'á', 'é', 'í', 'ó', 'ú',
          'à', 'è', 'ì', 'ò', 'ù',
          'â', 'ê', 'î', 'ô', 'û',
          'ã', 'õ')
for c in palavras:
    print('Na palavra {} temos'.format(c.upper()), end = ' ')
    i = 0
    while i < len(c):
        if c[i] in vogais:
            print(c[i], end = ' ')
        i += 1
    print('')
