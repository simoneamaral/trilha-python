''' 5 - Escreva um programa que faça operações de soma, subtração, multiplicação
e divisão. '''

print('''
      1 - Soma
      2 - Subtração
      3 - Multiplicação
      4 - Divisão
      ''')

operacao = input('Informe a aperação que deseja fazer: ')

num1 = int(input('Informe um número inteiro: '))
num2 = int(input('Informe mais um número inteiro: '))

if operacao == '1':
    print(f'A soma de {num1} + {num2} = {num1 + num2}')
elif operacao == '2':
    print(f'A subtração de {num1} - {num2} = {num1 - num2}')
elif operacao == '3':
    print(f'A multiplicação de {num1} x {num2} = {num1 * num2}')
elif operacao == '4':
    while num2 == 0:
        num2 = int(input('Digite um número maior que 0: '))
    print(f'A divisão de {num1} / {num2} = {num1 / num2}')
else:
    print('Não foi possível fazer o cálculo, operação inválida.')

''' - O que faz o operador lógico % em uma operação? '''
# Retorna o resto de uma divisão entre dois números

''' - É possível somar duas strings? '''
# Não, o operador + entre duas ou mais strings faz a concatenação/junção das strings e não a adição.

''' - Como obtenho um número de entrada para fazer um cálculo? '''
# Utilizando a função input()