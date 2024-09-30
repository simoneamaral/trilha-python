''' - O que é uma classe? '''
# É um modelo para a criação de objetos. 
# Uma classe define o estado e o comportamento de um objeto através de seus
# atributos e métodos.
# Os atributos armazenam as informações de um objeto e os métodos definem
# o comportamento de um objeto.

''' - O que é um método? '''
# É uma função definida dentro de uma classe que descreve o comportamento que os 
# objetos daquela classe podem realizar.

''' - O que é uma instância de uma classe? '''
# É um objeto criado a partir de uma classe. Quando você define uma classe, está 
# criando um modelo, e a instância é um objeto/exemplo concreto desse modelo. 

''' - Para que serve o self dentro da classe? '''
# Para referenciar o objeto que esta sendo criado

''' - Implemente uma classe animal e duas classes que herdam dela para cachorro 
e gato. A classe animal deve possuir os atributos cor, porte, raça. Já para as 
classes cachorro e gato deve possuir o atributo de brinquedo favorito e o 
método brincar. Ao executar esse método o código deve printar na tela 
brincando com o nome_do_brinquedo_da_classe. '''

class Animal():
    def __init__(self, cor, porte, raca):
        self.cor = cor
        self.porte = porte
        self.raca = raca

class Cachorro(Animal):
    def __init__(self, cor, porte, raca, brinquedo_favorito):
        super().__init__(cor, porte, raca)
        self.brinquedo_favorito = brinquedo_favorito

    def brincar(self):
        print(f'Brincando com {self.brinquedo_favorito}')

class Gato(Animal):
    def __init__(self, cor, porte, raca, brinquedo_favorito):
        super().__init__(cor, porte, raca)
        self.brinquedo_favorito = brinquedo_favorito
    
    def brincar(self):
        print(f'Brincando com {self.brinquedo_favorito}')

cachorro = Cachorro('preto','médio','SRD','bola')
cachorro.brincar()

gato = Gato('branco','médio','persa','varinha')
gato.brincar()

