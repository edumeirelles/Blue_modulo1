class Pessoa:
    
    def __init__(self, nome, idade, cpf, telefone):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__telefone = telefone
    
    # Get = Receber -> Definir o método que vai passar o valor do atributo de fora da classe

    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
    def getCPF(self):
        return self.__cpf
    
    def getTelefone(self):
        return self.__telefone

    # Set = Alterar

    def setNome(self, nome):
        self.__nome = nome
    
    def setIdade(self, idade):
        self.__idade = idade

    def setCPF(self, cpf):
        senha = input('Digite a senha para alterar: ')
        if senha == '12345':
            self.__cpf = cpf
            print('CPF Alterado com sucesso!')
        else:
            print('Senha Incorreta!')
    
    def setTelefone(self, telefone):
        self.__telefone = telefone


pessoa = Pessoa('Eduardo', 36, '352.756.448-92', '16 99260 - 1155')
pessoa2 = Pessoa('Zé', 55, '021.021.021-02','66 6666 - 6666')

# print(pessoa.getNome())
# pessoa.setNome('Zé')
# print(pessoa.getNome())

pessoa2.setCPF('000.000.000-00')

class Advogado(Pessoa):

    def __init__(self, nome, idade, cpf, telefone, oab):
        self.__oab = oab
        super().__init__(nome, idade, cpf, telefone)

adevogado = Advogado('Zé', 64, '000.555.666-85', '45 5464 - 5824', '123456')
adevogado.setCPF('555.666.777-88')
print(vars(adevogado))

class Medico(Pessoa):

    def __init__(self, nome, idade, cpf, telefone, crm):
        self.__crm = crm
        super().__init__(nome, idade, cpf, telefone)
        