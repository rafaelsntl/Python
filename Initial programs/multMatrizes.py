print ('O programa recebe duas matrizes e retorna, se possível,'
       ' o resultado da multiplicação entre elas.')
L1 = int (input('\nQual a quantidade de linhas da primeira matriz? '))
C1 = int (input('Qual a quantidade de colunas da primeira matriz? '))
L2 = int (input('\nQual a quantidade de linhas da segunda matriz? '))
C2 = int (input('Qual a quantidade de colunas da segunda matriz? '))

#Criando as matrizes vazias
matrizA = []
matrizB = []
matrizResultante = []

#Armazenando as matrizes
print()
for i in range (L1):
    linhaA = []
    for j in range (C1):
        linhaA.append(int(input(f'Digite o elemento [{i+1}][{j+1}] da primeira matriz: ')))
    matrizA.append(linhaA)
print()
for i in range (L2):
    linhaB = []
    for j in range (C2):
        linhaB.append(int(input(f'Digite o elemento [{i+1}][{j+1}] da segunda matriz: ')))
    matrizB.append(linhaB)

#Pedindo a opção de multiplicação ao usuário
print('\nQual a multiplicação que você deseja realizar?'
      '\nPrimeira x Segunda - Digite 1 \nSegunda x Primeira - Digite 2')
op = int(input('Digite a opção: '))
print()

#Verificando se ele digidtou
while op != 1 and op !=2:
    print('Opção inválida! Digite novamente:')
    op = int(input())

#Testando a opção digitada e vendo se é possível multiplicar as matrizes desejadas
if op == 1:
    #Verificando se o numero de colunas não é diferente do número de linhas
    if C1 != L2:
        print ('Não é possível realizar a operação!')
    #Se o número de linhas e colunas for igual, haverá a multiplicação
    else:
        for linha in range(0, L1):
            for coluna in range(0, C2):
                aux = 0
                for i in range(0,L1):
                    aux+=matrizA[linha][i]*matrizB[i][coluna]
                matrizResultante.append(aux)
                        
        print('\nResultado da multiplicação das matrizes:')
        for i in range(L1):
            for j in range (C2):
                print(f'[{matrizResultante[i]}]', end = '')
            print()
            
elif op == 2:
    if C2 != L1:
        print ('Não é possível realizar a operação!')
    else:
        for linha in range(0, L2):
            for coluna in range(0, C1):
                aux = 0
                for i in range(0,L2):
                    aux+=matrizA[linha][i]*matrizB[i][coluna]
                matrizResultante.append(aux)
                
        print('\nResultado da multiplicação das matrizes:')
        for i in range(L2):
            for j in range (C1):
                print(f'[{matrizResultante[i]}]', end = '')
            print()