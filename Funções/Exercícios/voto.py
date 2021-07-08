from datetime import datetime
def voto(nasc):
    idade = datetime.now().year - nasc
    print (f'Sua idade é de: {idade}')
    print ('Seu voto é: ', end = '')
    
    if idade < 16:
        print ('Negado!')
    elif idade >= 16 and idade <= 18:
        print ('Opicional!')    
    elif (idade > 18 and idade < 65):
        print ('Obrigatório!') 
    else:
        print ('Opicional')
        
nascimento = int (input('Digite seu ano de nascimento: '))
voto (nascimento)