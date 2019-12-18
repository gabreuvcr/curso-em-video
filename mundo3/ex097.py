## EX097 ##

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)


m = str(input('Digite uma mensagem: ')).strip().capitalize()
escreva(m)
