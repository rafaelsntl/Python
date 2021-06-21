"""
  Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
  Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

"""
exemplo = ('bumbum', 'biluteteia', 'caveleiros')
for palavra in exemplo:
    print(f'na palavra {palavra.upper()}, temos: ', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print()