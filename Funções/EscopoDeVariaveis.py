def funcao():
    global n1
    n1 = 4
    print (f'N1 dentro vale: {n1}')
    #aqui, ele vai mostrar o n1 local que defini dentro da função
n1= 2
funcao()
print(f'N1 fora vale: {n1}')
#já aqui, ele vai mostrar o n1 global que defini FORA da função
