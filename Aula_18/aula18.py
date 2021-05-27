class aluno:
    def __init__(self,nome,classe, media):
        self.nome = nome
        self.classe = classe
        self.media = media

    def __str__(self):
        return 


a = input('Digite nome: ')
b = input('Digite classe: ')
c = input('Digite média: ')

x = aluno(a,b,c)
print(vars(x))
print(x.nome)


