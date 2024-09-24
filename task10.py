''' 10 - O que é permitido no nome da função? '''
# letras, números e underline 
# O nome da função deve começar com letra ou underline, mas não pode começar com um número

''' Escreva uma função que recebe um inteiro e uma string. Essa função deve escrever no terminal a contagem de vezes que ela foi chamada e ao lado o texto que você desejar.
Exemplo:
> 1 primeira execução
> 2 a soma de 2 + 2 é 4 '''

contador = 0

def conta_execucao(numero,texto):
    global contador
    contador += 1
    print(f'{contador}° execução - {texto}')
    
conta_execucao(8,'Python')
conta_execucao(9,'Java')

''' - Há um limite para a quantidade de argumentos que uma função pode ter? '''
# Não há limites para a quantidade de argumentos 

''' - Explique a diferença entre parâmetros e argumentos. '''
# Parâmetros são as varáveis listadas na definição de uma função
# Exemplo:
# def soma(a, b) a e b são parâmetros

# Argumentos são o valores passados para a função quando ela é chamada
# Exemplo:
# soma(2, 3) 2 e 3 são argumentos
    
''' - Crie uma função que receba uma lista de notas de um aluno e calcule a média. Se a média for inferior a 4, exiba 'Reprovado' na tela; caso contrário, exiba 'Aprovado'. '''

def calcula_media(notas):
    media = sum(notas) / len(notas)

    if media < 4:
        return(f'Reprovado média {media:.1f}')
    else:
        return(f'Aprovado média {media:.1f}')

notas = [4,6,7,7,9]
resultado = calcula_media(notas)
print(resultado)

''' - Escreva uma função chamada verificar_par que receba um número e retorne True se for par e False caso contrário. '''

def verifica_par(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
print(verifica_par(42))

''' - Crie uma função chamada contar_letras que receba uma string e retorne a quantidade de letras (desconsiderando espaços). '''

def contar_letras(string):
    string_sem_espaco = string.replace(" ","") 
    print(f'Quantidade de letras da string: ', len(string_sem_espaco))

contar_letras('Simone    Amaral')

''' - O que é uma função recursiva? '''
# É quando uma função chama a si mesma durante sua execução