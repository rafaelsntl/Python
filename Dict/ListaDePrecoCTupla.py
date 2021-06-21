#criando a tupla
listagem = ('lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9,
            'estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99,
            'mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.9)

print('-' * 5, end = '')
print(f'{"LISTAGEM DE PREÇOS"}', end='')
print('-' * 5)

#for começando de 0 até o tamanho da tupla
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end = '') # :.<30 serve para deixar a linha com 30 casas
    else:
        print(f'R${listagem[pos]:>7.2F}') # .2f para deixar com 2 casas décimais
        
print('-' * 30)