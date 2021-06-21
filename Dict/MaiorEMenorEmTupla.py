#importando a biblioteca para ter os valores aleatórios
from random import randint
#criando a tupla com os valores aleatórios entre 1 e 10
numeros = (randint(1,10),randint(1,10),randint(1,10),
           randint(1,10),randint(1,10),)

for n in numeros:
    print (f'{n}', end = ' ')
    
#em python, eu posso mostrar o maior valor com o 'max'
print (f'\no maior valor sorteado foi: {max(numeros)}')
print (f'e o menor valor foi: {min(numeros)}')