''' - Exercício para revisão de classes.
Vamos criar um programa para representar um sistema bancário. 

classe Conta

Atributos:
- número da conta
- nome
- saldo
- limite

Ela deve conter os métodos: 
- sacar (recebe um valor e uma conta, esse valor deve ser checado no saldo, caso o saldo seja maior que o valor a ser sacado, subtrair o valor do saldo e atualizar. Caso contrário retornar uma mensagem de saldo insuficiente.
- depositar (recebe um valor e uma conta, somar o valor no saldo da conta)
- transferir (recebe um valor, o número da conta de origem e o número da conta de destino. Subtrair o saldo da conta de origem e somar na de destino. Também deve verificar por saldo negativo)
- exibir saldo (retornar o valor do saldo da conta) '''

class Conta():
    def __init__(self, num_conta, nome, saldo, limite):
        self.__num_conta = num_conta
        self.__nome = nome
        self.__saldo = saldo
        self.__limite = limite

    def get_num_conta(self):
        return self.__num_conta
        
    def get_nome(self):
        return self.__nome
        
    def get_saldo(self):
        return self.__saldo
        
    def get_limite(self):
        return self.__limite
        
    def set_limite(self, limite):
        self.__limite = limite
            
    def sacar(self, valor):
        if self.get_saldo() >= valor and self.get_limite() >= valor:
            self.__saldo -= valor
            return f'Saque de R${valor:.2f} realizado com sucesso.'
        else:
            return f'Não foi possível realizar o saque. Saldo insuficiente ou valor acima do limite de saque.'


    def depositar(self, valor):
        self.__saldo += valor
        return f'Deposito de R${valor:.2f} realizado com sucesso.'

    def transferir(self, valor, conta_destino):
        if self.get_saldo() >= valor:
            self.__saldo -= valor
            conta_destino.depositar(valor)
            return f'Transferência de R${valor:.2f} realizada com sucesso para Conta n° {conta_destino.get_num_conta()} Titular: {conta_destino.get_nome()}.'
        else:
            return f'Saldo insuficiente para a transferência'   
        
    def exibir_saldo(self):
        return f'Saldo da conta {self.__num_conta}: R${self.__saldo:.2f}'

conta1 = Conta(1234,'Simone Amaral',2000,1000)
print(conta1.exibir_saldo())
print(conta1.sacar(600))
print(conta1.exibir_saldo())
print(conta1.depositar(200))
print(conta1.exibir_saldo())

print()

conta2 = Conta(5678,'Ana Maria',500,1000)
print(conta2.exibir_saldo())
print(conta1.transferir(400,conta2))
print(conta2.exibir_saldo())
print(conta1.exibir_saldo())
print(conta2.depositar(100))
print(conta2.exibir_saldo())

conta3 = Conta(91011,'Ana Carolina',1300,500)
print(conta3.exibir_saldo())
print(conta3.transferir(200,conta1))
print(conta1.exibir_saldo())
print(conta3.exibir_saldo())
print(conta3.sacar(600))

print()

conta1.set_limite(2000)
print(conta1.get_limite())


''' - Como deixar um atributo privado no python? '''
# Utilizando dois underline antes do nome do atributo 
# Exemplo: __atributo
