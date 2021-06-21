from random import randint #pra gerar valores aleatórios
from time import sleep #pra usar a função parecida com o delay
from operator import itemgetter #pra ordenar

#mandando sortear valores de 1 a 6
jogo = {'jogador1' : randint(1,6),
        'jogador2' : randint(1,6),
        'jogador3' : randint(1,6),
        'jogador4' : randint(1,6)}

print('-----Valores sorteados:-----')
for k,v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(1) #delay de 1

#vamos ordenas através do metódo sort   
#se fosse pra mostrar em ordem de chave, usariamos o itemgetter(0)    
#reverse = True pra mostrar de cima p baixo
ranking = sorted(jogo.items(), key = itemgetter(1), reverse= True)

#o resultado saíra em forma de lista, entao, para organizar direitinho, vamos fazer o for:
print('\n-----O ranking dos jogadores:-----')
for i, v in enumerate(ranking):
    print (f'o {i+1}º lugar: {v[0]} com {v[1]}.')