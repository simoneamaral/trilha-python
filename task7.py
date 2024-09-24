''' 7 - Escreva um programa que peça uma entrada ao usuário. Esse valor deve ser
armazenado em uma variável. Em seguida, crie um if para checar se é um número 
ou uma letra e escreva na tela o resultado. '''

entrada = input('Digite um número ou uma letra: ')

if entrada.isdigit(): # retorna true se for apenas números
    print('Voce digitou um número')
else:
    print('Você digitou uma letra')

''' - Qual a diferença entre x = 1 e x == 1?'''
# x = 1 a váriavel x esta recebendo o valor 1
# x == 1 verifica se o conteúdo da váriavel x é igual o número 1

# = atribuição
# == comparação de igualdade