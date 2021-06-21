aluno = dict()

aluno['nome'] = str(input('Digite o nome: '))
aluno['nota'] = float (input('Digite a nota: '))


if aluno['nota'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5<= aluno['nota'] < 7:
    aluno['situação']= 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

# print (f'O nome é: {aluno["nome"]}') #aspas duplas pq n pode usar aspas simples dentro de aspas simples
# print (f'a nota é: {aluno["nota"]}')
# print (f'a situação de {aluno["nome"]} é: {aluno["situação"]}')

print ('-=' *30)
for k,v in aluno.items():
    print(f'{k} é igual a {v}')