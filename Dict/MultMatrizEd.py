print ('O programa recebe duas matrizes e retorna, se possível'
       ' o resultado da multiplicação entre elas.')
L1 = int (input('\nQual a quantidade de linhas da matriz A? '))
C1 = int (input('Qual a quantidade de colunas da matriz A? '))
L2 = int (input('\nQual a quantidade de linhas da matriz B? '))
C2 = int (input('Qual a quantidade de colunas da matriz B? '))

matrizA = []
matrizB = []
matrizResultante = []

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

print('\nMatriz A:')
for i in range(L1):
    for j in range (C1):
        print(f'[{matrizA[i][j]}]', end = '')
    print()

print('\nMatriz B:')
for i in range(L2):
    for j in range (C2):
        print(f'[{matrizB[i][j]}]', end = '')
    print()
    
    
print('\nQual a multiplicação que você deseja realizar?'
      '\nAxB - Digite 1 \nBxA - Digite 2')
op = int(input('Digite a opção: '))
print()

while op != 1 and op !=2:
    print('Opção inválida! Digite novamente:')
    op = int(input())

if op == 1:
    if C1 != L2:
        print ('Não é possível realizar a operação!')
    else:
        for linha in range(0, L1):
            for coluna in range(0, C2):
                produtoSoma = 0
                for i in range(0,L1):
                    produtoSoma+=matrizA[linha][i]*matrizB[i][coluna]
                matrizResultante.append(produtoSoma)
                        
        print('\nMatriz resultante:')
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
                produtoSoma = 0
                for i in range(0,L2):
                    produtoSoma+=matrizA[linha][i]*matrizB[i][coluna]
                matrizResultante.append(produtoSoma)
                
        print('\nMatriz C:')
        for i in range(L2):
            for j in range (C1):
                print(f'[{matrizResultante[i]}]', end = '')
            print()