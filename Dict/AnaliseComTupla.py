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
        








# criando uma função para multiplicar as matrizes
def multiplicacao(matrizA, linA, colA, matrizB, linB, colB):
    #escolhendo qual multiplicação o usuário deseja realizar
    print("\nInsira de acordo com a multiplicação que deseja"
            " realizar: \n1 - AxB\n2 - BxA")
    opcao = int(input("--> "))

    # recebendo a opção informada acima e fazendo uma verificação
    while opcao !=1 and opcao != 2:
        print("Opção inválida, insira novamente.\n")
    
    # verificando se podemos realizar a operação
    if opcao == 1:
        if colA != linB:
            # retorna uma mensagem de erro pois não é possível realizar a operação
            return "Não é possível realizar a operação com as matrizes inseridas."
        else:
            matrizC=[]
            # definindo a operação de multiplicação
            for linha in range(0, linA):
                for coluna in range(0, colB):
                    produtoSoma = 0
                    for i in range(0,linA):
                        produtoSoma+=matrizA[linha][i]*matrizB[i][coluna]
                    matrizC.append(produtoSoma)
          # retornando o resultado 
            return matrizC
    elif opcao == 2:
        if colB != linA:
            return "Não é possível realizar a operação com as matrizes inseridas."
        else: 
            matrizC=[]
            for linha in range(0, linB):
                for coluna in range(0, colA):
                    produtoSoma = 0
                    for i in range(0,linB):
                        produtoSoma+=matrizB[linha][i]*matrizA[i][coluna]
                    matrizC.append(produtoSoma)
        # retornando o resultado
            return matrizC

# recendo a quantidade de linhas e colunas das matrizes
linA = int(input("Insira a quantidade de linhas da matriz A: "))
colA = int(input("Insira a quantidade de colunas da matriz A: "))
linB = int(input("Insira a quantidade de linhas da matriz B: "))
colB = int(input("Insira a quantidade de colunas da matriz B: "))

print()

# inicializando as matrizes 
matrizA=[]
matrizB=[]

# implementando os elementos da matriz A
for i in range(linA):
    linhaA=[]
    for j in range(colA):
        linhaA.append(float(input(f'Insira o elemento [{i + 1}][{j + 1}] da matriz A: ')))
    matrizA.append(linhaA)

print()

# implementando os elementos da matriz B
for i in range(linB):
    linhaB=[]
    for j in range(colB):
        linhaA.append(float(input(f'Insira o elemento [{i + 1}][{j + 1}] da matriz B: ')))
    matrizB.append(linhaB)


# imprime a matriz A
print("\nMatriz A:")
print(matrizA)

# imprime a matriz B
print("\nMatriz B:")
print(matrizB)

print(f'\nMultiplicação: \n{(multiplicacao(matrizA, linA, colA, matrizB, linB, colB))}')