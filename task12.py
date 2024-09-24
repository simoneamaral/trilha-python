''' 12 - Crie uma lista com os valores 1, 3, a, c, abacate, dez e NTT. '''
lista = [1, 3, 'a', 'c', 'abacate', 'dez', 'NTT']

''' - Acesse somente os valores da lista acima que são números e escreva no terminal. '''
for item in lista:
    if isinstance(item, int): # verifica o item tipo int
        print(item)

''' - Acesse somente as strings que possuem 1 caractere e escreva no terminal. '''
for item in lista:
    if isinstance(item, str) and len(item) == 1: # verifica o item tipo string e tamanho 1
        print(item)

''' - Use o .pop para remover um elemento da lista. '''
lista.pop(4) # removendo índice 4 -> 'abacate'

''' - 
a = [1,2,3] 
print(a[-1:]) 
Qual o resultado será exibido na tela? '''
# [3] 
