pessoas = {'nome': 'Rafael',
           'sexo': 'M',
           'idade': 19}

del pessoas['sexo']
pessoas['nome'] = 'leando'

for k, v in pessoas.items():
    print(f'{k} = {v}')