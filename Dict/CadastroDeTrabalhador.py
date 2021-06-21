from datetime import datetime # pra pegar a data do computador
#declarando logo q eé um dicionário
dados = dict()
dados['Nome'] = str (input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year- nascimento #calculando automaticamente a idade 
dados['ctps'] = int (input('Carteira de tarbalho (0 se nao tiver): '))

if dados['ctps'] != 0:
    dados['contratação'] = float(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
    #Calculando com que idade a pessoa irá se aposentar

print ('-='*30)
for k,v in dados.items():
    print(f'- {k} tem o valor {v}')