''' 8 - Altere o programa anterior para que o programa solicite uma nova entrada para o usuário 
até que seja digitado um número. '''

entrada = input('Digite um número ou uma letra: ')

while not entrada.isdigit():
    entrada = input('Digite um número ou uma letra: ')

print('Você digitou um número, programa encerrado.')