''' 9 - Escreva um programa que leia um arquivo .txt usando o open() '''

arquivo = open("mensagem.txt","r", encoding="utf-8")
print(arquivo.read()) 

arquivo.close()

''' - Escreva um programa que leia um arquivo .txt usando o with() '''

with open("frase.txt","r", encoding="utf-8") as arquivo2:
    print(arquivo2.read())

''' - Escreva um programa que crie um arquivo .txt e adicione um texto ao conteúdo do arquivo. '''

with open("novoarquivo.txt","w", encoding="utf-8") as novoarquivo:
    novoarquivo.write('Escrevendo o conteúdo do novoarquivo.txt')