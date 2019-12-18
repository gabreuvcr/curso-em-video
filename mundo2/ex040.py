## EX040 ##

m1 = float(input('Digite sua primeira nota: '))
m2 = float(input('Digite sua segunda nota: '))
media = (m1 + m2) / 2
print('Sua média é {}.\n'.format(media))
if media >= 7:
    print('APROVADO!')
elif media >= 5:
    print('RECUPERAÇÃO!')
else:
    print('REPROVADO!')
