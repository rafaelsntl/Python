'''
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'Sigla':'RJ'}
estado2 = {'uf': 'São Paulo', 'Sigla':'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])

'''
#declarando a lista e o dicionário
estado = dict()
brasil = list()

#usando um for para pedir o UF e a sigla dos estádos
for c in range(0,3):
    estado['uf']= str(input('UF: '))
    estado['sigla']= str(input('Sigla: '))
    #adicionando o dicionário na lista
    brasil.append(estado.copy()) #copy é um método do próprio dicionário para copiar o elemento
    
#mostrando a lista 
for e in brasil:
    for v in e.items():
        print (v, end = ' ')
    print()