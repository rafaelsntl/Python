def ficha(jog='<desconhecido>', gol=0):
    print ('-='*20)
    print(f'O jogador {jog} fez {gol} gol(s)!')
    
n = str(input('Digite o nome: '))    
g = str(input('Digite o número de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)