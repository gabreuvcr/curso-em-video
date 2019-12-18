## EX008 ##

metros = float(input('Digite um valor em metros: '))
cm = metros * 100
mm = metros * 1000
dm = metros * 10
dam = metros / 10
hm = metros / 100
km = metros / 1000
#{:.2f}  == duas casas decimais
print('{} metros equivale a: '.format(metros))
print('{:.2f} mm \n{:.2f} cm \n{:.2f} dm'.format(mm, cm, dm))
print('{:.2f} dam \n{:.2f} hm \n{:.2f} km'.format(dam, hm, km))
