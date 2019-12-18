## EX105 ##

def notas(* notas, sit=False):
    geral = {}
    geral['total'] = len(notas)
    geral['maior'] = max(notas)
    geral['menor'] = min(notas)
    geral['media'] = sum(notas) / len(notas)
    if sit == True:
        if geral['media'] >= 7:
            geral['situacao'] = 'BOA'
        elif geral['media'] >= 5:
            geral['situacao'] = 'RAZOAVEL'
        else:
            geral['situacao'] = 'RUIM'
    return geral


resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)