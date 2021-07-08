def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f +=c
    return f
n = fatorial(5)
n2 = fatorial(9)
n3 = fatorial(4)
print (f'Os resultados foram: {n}, {n2}, {n3}')