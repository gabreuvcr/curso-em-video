## EX051 ##

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
a10 = a1 + ((10 - 1) * r)
print('')
for i in range(a1, a10+1, r):
    print("{}".format(i), end = ' → ')
print('Fim ')