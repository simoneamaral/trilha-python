''' - Crie um programa que leia um número inteiro e mostre na 
tela seu sucessor e seu antecessor. '''

num = int(input('Digite um número inteiro: '))

print(f'Antecessor de {num} é {(num - 1)}')
print(f'Sucessor de {num} é {(num + 1)}') 

''' - Crie um algoritmo que leia um número e mostre sua metade, dobro e triplo. '''

num = float(input('Digite um número: '))
print(f'Metade = {num/2} | dobro = {num*2} | triplo = {num * 3}')

''' - Desenvolva um script em Python que receba o salário de um funcionário e mostre o seu novo salário, com 12% de reajuste. '''
salario = float(input('Digite seu salário: R$ '))
aumento = salario * (12/100)
novo_salario =  salario + aumento
print(f'Novo salário com 12% de aumento R$ {novo_salario:.2f}')

''' - Crie um programa que receba três valores diferentes e mostre na tela o maior e o menor valor digitado. '''

num1 = int(input('Digite o primeiro valor: ')) 
num2 = int(input('Digite o segundo valor: ')) 
num3 = int(input('Digite o terceiro valor: ')) 

maior = num1
menor = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print(f'Maior número informado: {maior}')
print(f'Menor número informado: {menor}')