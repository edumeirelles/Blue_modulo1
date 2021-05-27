# Proposta de projeto de ficção interativa para avaliação de OO
# Sugestão: completar com classes filhas colocando pessoas saudáveis, trabalhos menos remunerados, casas melhor equipadas et cetera
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
  
def lista_musica():

    print ('Qual música você deseja tocar?: \n')
    print ('Pressione (1) para:  Metallica - Master of Puppets')
    print ('Pressione (2) para: Iron Maiden - Fear of the Dark')
    print ('Pressione (3) para: A se eu te pego!\n')
    musica = input ('Opção: ')
    print() 
        
    if musica == '1':
        if personagem.habilidade < 50:
            print('Você ainda não tem habilidade para tocar essa música! Escolha outra!!!\n')           
            lista_musica()
        else:
            personagem.fama += 30
            publico.publico += 200
            personagem.cansaco += 15
            personagem.habilidade += 40
            personagem.dinheiro += 200

            print ("Parace que a sua fama aumentou após esse som!!!")
            print (f'A sua fama agora é: {personagem.fama}. Público atual: {publico.publico} e cansaço: {personagem.cansaco} ')
            
    if musica == '2':
        personagem.fama += 25
        publico.publico += 150
        personagem.cansaco += 10
        personagem.habilidade += 30
        personagem.dinheiro += 100
        
        print ('Ao som do Maiden, o público foi a loucura!')
        print (f'A sua fama agora é: {personagem.fama}. Público atual: {publico.publico} e cansaço: {personagem.cansaco} ')
            
    if musica == '3':
        personagem.fama -= 20
        publico.publico -= 300
        personagem.cansaco += 5
        personagem.habilidade -= 10
        personagem.dinheiro += 50

        print ('O seu público não esperava tanta ousadia...contenha-se!')
        print (f'A sua fama agora é: {personagem.fama}. Público atual: {publico.publico} e cansaço: {personagem.cansaco} ')

if(__name__ == "__main__"):
    
    personagem = Personagem()
    publico = Publico()   
    
    subiu_no_palco = False
    
    # while True:
    #         print("---")
    #         print('Bem vindo à banda Turma 2B!!!')
    #         print('O seu show começa em')
    #         for cont in range (5, -1, -1):
    #             print (cont)
    #             sleep(1)
    #         if cont ==0:
    #             break

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
        opcao = input("Escolha sua ação: ")
        
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
                lista_musica()     
                
        elif opcao == '4':
            if personagem.cansaco <= 40:
                print('Tá cansado do quê??? Comece a tocar!!!')
            else:
                personagem.cansaco -= 40
                publico.publico *= 0.85

        elif opcao == '5':
            print('Você Abandonou o palco!')

            if personagem.dinheiro >= 1000:
                personagem.dinheiro -= 1000
                print('Você será multado em R$ 1000,00!!!')
            else:
                personagem.dinheiro = 0
                print('Você será multado em R$', format(personagem.dinheiro,'.2f').replace('.',','), '!!!')
            personagem.fama *= 0.5
            publico.publico *= 0.25
            print (f'A sua fama agora é: {personagem.fama}. Público atual: {publico.publico} e cansaço: {personagem.cansaco} ')
            sleep(1)
            print ("Abandonei o palco porque quero e posso!") 
            sleep(1)

        elif opcao == "0":
            break  