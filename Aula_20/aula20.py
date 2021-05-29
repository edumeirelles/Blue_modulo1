class Pessoa:
    
    def __init__(self, nome, idade, cpf, telefone):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__telefone = telefone
    
    # Get = Receber -> Definir o método que vai passar o valor do atributo de fora da classe

    def nome(self):
        return self.__nome

    # Set = Alterar
    
pessoa = Pessoa('Eduardo', 36, '352.756.448-92', '16 99260 - 1155')