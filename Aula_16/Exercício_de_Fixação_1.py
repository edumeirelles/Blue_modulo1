class pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    
    def mostrar_dados(self):
        print(vars(self))

a = pessoa(input('Digite o nome: '),input('Digite o sobrenome: '),int(input('Digite a idade: ')))

a.mostrar_dados()