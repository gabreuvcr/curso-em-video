## EX101 ##

def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if (idade < 16):
        cond = f'Com {idade} anos: NÃO VOTA'
    elif (idade < 18) or (idade > 69):
        cond = f'Com {idade} anos: VOTO FACULTATIVO.'
    else:
        cond = f'Com {idade} anos: VOTO OBRIGATORIO.'
    return cond


nascimento = int(input('Digite a data de nascimento: '))
print(voto(nascimento))
