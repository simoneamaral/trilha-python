''' 11 - Listas em Python é a mesma coisa que um array? '''
# Não, listas podem conter vários tipos de dados e em arrays todos elementos devem
# ser do mesmo tipo 

''' - Por que a função for i in range(1, 3):  faz um loop apenas duas vezes? '''
# Porque a função range(1, 3) inicia com o valor 1 (start) e vai até o valor 3 (stop), mas não
# inclui o valor de stop.

''' - elements = list() O que é e para que serve a função append? elements.append() '''
# elements = list() Cria uma lista vazia chamada elements
# A função append() adiciona um elemento ao final da lista

''' - Faça um programa que leia 5 números e informe o maior número. '''
numeros = []

for i in range(1,6):
    numero = float(input(f'Digite o {i}° número: '))
    numeros.append(numero)

maior_numero = max(numeros)

print(f'Maior número informado: {maior_numero} ')