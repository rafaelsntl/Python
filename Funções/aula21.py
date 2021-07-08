#help(print) #- mostra as funcionalidades de print
def contador(i,f,p):
#caso eu queira criar uma docstring de determinada função, eu faço assim:
    '''
    -> faz uma contagem e mostra na tela.
        -param i: inicio da contagem
        -param f: final da contagem
        -param p: passo da contagem
    '''
    c = i
    while c <= f:
        print(f'{c}', end = ' ') 
        c+=p
    print ('FIM!')
help (contador)