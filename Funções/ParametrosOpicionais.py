#caso o usuário não digite valor, 0 será atribuido como default  
def somar (a=0,b=0,c=0): 
    s = a + b + c
    print (f'A soma vale {s}')
somar(1,2)
#como eu só to adicionando dois valores, o 0 será atribuído para c