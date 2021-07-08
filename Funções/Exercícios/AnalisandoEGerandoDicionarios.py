def notas(*n, sit = False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max (n)
    r['menor'] = min (n)
    r['media'] = sum(n)/len(n)
    
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(0,6,6, sit = True)
print (resp)