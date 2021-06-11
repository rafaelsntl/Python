def Reverse(lin):
    reverseMatrix = []
    
    for i in range(len(lin)-1, -1, -1):
        reverseMatrix.append(lin[i])
    return reverseMatrix

def NewMatrix(oldMatrix, lin, col):
    newMatrix = []
    
    for i in range(0, lin, 1):
        oldMatrix.append([])
        
        for j in range(0, col, 1):
            oldMatrix[i].append(int(input()))
    
    for k in range(lin-1, -1, -1):
        newMatrix.append(Reverse(oldMatrix[k]))
    return newMatrix
    
lin = int(input())
col = int(input())
currentMatrix = []
output = []

output = NewMatrix(currentMatrix, lin, col)
print(output)