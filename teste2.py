class Personagem:
    def __init__(self):
        self.habilidade = 50
        self.cansaco = 0
        self.fama = 0
        self.dinheiro = 0
        self.cache = 1000
    
    def __str__(self):
        return f'Sua habilidade é, {self.habilidade}, Seu cansaço é, {self.cansaco}, Sua fama é {self.fama}, e sua conta bancária é {self.dinheiro}.'

class Publico:
    def __init__(self):
        self.publico = 500
 
if(__name__ == "__main__"):
    
    personagem = Personagem()
    publico = Publico()   
    while True:
        print("---")
        print('Bem vindo à banda Turma 2B!!!')
        print(personagem)
        print("")
        print("Ações:")
        print('1 - Cumprimentar o público')
        print('2 - Tocar uma música')
        print('3 - Abandonar Palco')
        print('0 - Sair')
        opcao = input("Escolha sua ação:")
        if opcao == '1':
            personagem.fama += 5
            publico.publico += 100
        
        
        
        if opcao == '3':
            print('Você Abandonou o palco!')
            if personagem.fama >= 10:
                personagem.fama -= 10
            else:
                personagem.fama = 0

        print(f'Sua habilidade é, {personagem.habilidade}, Seu cansaço é, {personagem.cansaco}, Sua fama é {personagem.fama}, e sua conta bancária é {personagem.dinheiro}.')










