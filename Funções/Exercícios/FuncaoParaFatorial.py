def fatorial(n=1, show = False):
    '''
    -> Calcula o fatorial de um numero
        :param n : valor a ser calculado
        :param show : se quer mostrar ou nao a conta
        :return : O valor fatorial de um numero n
    '''
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c, end = '')
            if c > 1:
                print(' x ', end = '')
            else:
                print (' = ', end = '')
        f*=c
    return f
#help(fatorial)
print(fatorial(5, show = True))