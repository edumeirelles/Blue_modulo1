from time import sleep

class Personagem:
    def __init__(self):
        self.habilidade = 0
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
    
    print("---")
    print('Bem vindo à banda Turma 2B!!!')
    print("---")
    sleep(1)

    personagem = Personagem()
    publico = Publico()   
    musicas_tocadas = 0
    subiu_no_palco = False
    
    while True:
                
        print(personagem)
        sleep(1)
        print("")
        print("Ações:")
        print('1 - Subir no palco')
        print('2 - Cumprimentar o público')
        print('3 - Tocar uma música')
        print('4 - Fazer uma pausa')
        print('5 - Abandonar Palco')
        print('0 - Sair')
        opcao = input("Escolha sua ação:")
        
        if opcao == '1':
            personagem.fama += 5
            publico.publico += 100
        
        elif opcao == '2':
            personagem.fama += 10
            publico.publico += 100
                       
        elif opcao == '3':
            if personagem.cansaco >= 60:
                print('Você está muito cansado!!! Melhor fazer uma pausa!!!')
            else:
                if personagem.habilidade >= 75:
                    personagem.habilidade += 5
                    personagem.cansaco += 5

                elif 75 > personagem.habilidade >= 50:
                    personagem.habilidade += 5
                    personagem.cansaco += 10

                elif 50 > personagem.habilidade >= 25:
                    personagem.habilidade += 10
                    personagem.cansaco += 15

                else:
                    personagem.habilidade += 10
                    personagem.cansaco += 20
            musicas_tocadas += 1
            personagem.dinheiro += musicas_tocadas*100
        
        elif opcao == '4':
            personagem.cansaco -= 40
            publico.publico *= 0.85


        elif opcao == '5':
            print('Você Abandonou o palco!')
            personagem.dinheiro -= 1000
            personagem.fama *= 0.5
            publico.publico *= 0.25
               
            

        elif opcao == "0":
            break

       # print(f'Sua habilidade é, {personagem.habilidade}, Seu cansaço é, {personagem.cansaco}, Sua fama é {personagem.fama}, e sua conta bancária é {personagem.dinheiro}.')










