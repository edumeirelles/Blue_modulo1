class Herói():
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def engordar(self, peso):
        self.peso += peso

a = Herói('Capitão América',30, 85)
b = Herói('Homem de Ferro', 30, 300)
print(vars(a))
print(vars(b))


a.engordar(10)
b.peso = a.peso
print(vars(a))
print(vars(b))

class Pessoa():
    def __init__(self, nome, altura, peso):
        self.nome = nome
        self.altura = altura
        self.peso = peso

    def emagrecer(self, peso):
        self.peso -= peso

print('====== CLASSE PESSOA ======')

a = Pessoa('Steve Rogers',1.80, 90)
print(vars(a))
a.emagrecer(10)
print(vars(a))

class aluno():
    def __init__(self, nome, idade, serie, nota1, nota2, matricula, sala):
        self.nome = nome
        self.idade = idade
        self.serie = serie
        self.nota1 = nota1
        self.nota2 = nota2
        self.matricula = matricula
        self.sala = sala
        self.media = 0
    def calcula_media(self):
        self.media = (self.nota1 + self.nota2) / 2
        print(f'A média do {self.nome} é {self.media}')

    def altera_sala(self):
        nova_sala = input('Digite a nova sala: ')
        confirmacao = input(f'Você deseja alterar o aluno {self.nome} da sala {self.sala} para a sala {nova_sala}?: ')
        if confirmacao == "S":
            self.sala = nova_sala
        else:
            print('Ok, nada alterado.')
        print(f'A sala do aluno {self.nome} é a sala {self.sala}')

aluno_eduardo = aluno("Eduardo", 36, '3am', 10, 8, '0123456', 15)
aluno_zé = aluno('Zé', 20, '3e',8 ,6 ,'554125', 18)
