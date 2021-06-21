#nas tuplas nós podemos fazer isso
núm = (int(input('Digite um número: ')),int(input('Digite um número: ')),
       int(input('Digite um número: ')),int(input('Digite um número: ')))

print ('-='*20)
#mostrando a tupla
print (f'você digitou os valores{núm}')

#mandando contar a quantidade de vezes que o 9 apareceu
print (f'o valor 9 apareceu {núm.count(9)} vezes.')

#temos que fazer um if pois o index daria um erro se o valor 3 não fosse digitado
if 3 in núm:
    print (f'o valor 3 apareceu na posição {núm.index(3)+1}')
else:
    print ('O valor 3 não foi digitado em nenhuma posição')
print('os valores pares digitados foram:', end = ' ')

for n in núm:
    if n % 2 == 0:
        print(n, end = ' ')