#criando o dicionario:
filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}

# print(filme.values()) #vai mostrar os valores (star wars...)
# print(filme.keys())#vai mostrar os valoresas chaves (titulo...)
# print(filme.items)#vai mostrar tudo

#mostrando no for
for k,v in filme.items():
    print(f'o {k} eh {v}')