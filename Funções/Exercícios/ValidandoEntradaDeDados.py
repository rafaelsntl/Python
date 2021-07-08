def leiaInt(msg):
    ok = False
    valor = 0 
    while True:
        n = str(input(msg))
        if n.strip().isnumeric():
            valor = int(n)
            ok = True
        else: 
            print('\033[0;31mERRO! Digite um valor válido!\033[m')
        if ok:
            break
    return valor

n = leiaInt('Digite um valor: ')
print (f'Você acabou de digitar o número {n}!')