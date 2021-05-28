# Proposta de projeto de ficção interativa para avaliação de OO
# Sugestão: completar com classes filhas colocando pessoas saudáveis, trabalhos menos remunerados, casas melhor equipadas et cetera

from time import sleep
from random import randint
import pygame

class Personagem:
    def __init__(self):
        self.habilidade = 0
        self.cansaco = 0
        self.fama = 0
        self.dinheiro = 0
        self.cache = 1000
    
    def __str__(self):
        return f'\nSua habilidade é {self.habilidade}, seu cansaço é {self.cansaco}, sua fama é {self.fama} e sua conta bancária é {self.dinheiro}.\n'

class Publico:

    def __init__(self):
        self.publico = 500
    
    def __str__(self):
        return f'Seu Público é {self.publico}!!!\n'

def Musica1(): 

    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('Projeto Jogo\Banda_T2B\corte_metallica.mp3')
    pygame.mixer_music.play()
    
def Musica2():

    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('Projeto Jogo\Banda_T2B\corte_iron.mp3')
    pygame.mixer_music.play()
    
def Musica3():

    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('Projeto Jogo\Banda_T2B\corte_telo.mp3')
    pygame.mixer_music.play()
    
def sound_rain():

    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('Projeto Jogo\Banda_T2B\corte_rain.mp3')
    pygame.mixer_music.play()
    
def sound_entrada():

    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('Projeto Jogo\Banda_T2B\corte_entrada.mp3')
    pygame.mixer_music.play()
    
def chuva():
    print('CHUVA!!!')
    print()
    print('O Show foi cancelado!!!')
    sound_rain()
    subiu_no_palco == False
    cumprimentou_publico == False
    personagem.cansaco = 0
    publico.publico *= 0.85 
    sleep(3)

def lista_musica():

    print ('Qual música você deseja tocar?: \n')
    print ('Pressione (1) para: Metallica - Master of Puppets')
    print ('Pressione (2) para: Iron Maiden - Fear of the Dark')
    print ('Pressione (3) para: Ah se eu te pego!\n')
    musica = input('Opção: ')
    print() 
        
    if musica == '1':

        if personagem.habilidade < 50:

            print('Você ainda não tem habilidade para tocar essa música! Escolha outra!!!\n')           
            lista_musica()
        else:

            Musica1()
            personagem.fama += 30
            publico.publico += 200
            personagem.cansaco += 15
            personagem.habilidade += 40
            personagem.dinheiro += 200

            print("Parace que a sua fama aumentou após esse som!!!")
            print(f'A sua fama agora é: {personagem.fama}. Público atual: {publico.publico} e cansaço: {personagem.cansaco} ')
            
    if musica == '2':

        Musica2()
        personagem.fama += 25
        publico.publico += 150
        personagem.cansaco += 10
        personagem.habilidade += 30
        personagem.dinheiro += 100
        
        print('Ao som do Maiden, o público foi a loucura!')
        print(f'A sua fama agora é: {personagem.fama}. Público atual: {publico.publico} e cansaço: {personagem.cansaco} ')
            
    if musica == '3':

        Musica3()
        personagem.fama -= 20
        publico.publico -= 300
        personagem.cansaco += 5
        personagem.habilidade -= 10
        personagem.dinheiro += 50

        print('O seu público não esperava tanta ousadia...contenha-se!')
        print(f'Sua habilidade foi reduzida em 10 pontos. Michel Teló faz você desaprender a tocar! Agora sua habilidade é de {personagem.habilidade}. ')
        print(f'A sua fama reduziu para: {personagem.fama}. Público ainda fiel: {publico.publico} e cansaço: {personagem.cansaco} ')

if(__name__ == "__main__"):
    
    personagem = Personagem()
    publico = Publico()   
    subiu_no_palco = False
    cumprimentou_publico = False
    cont = 0
    x = 0
    carreira = 0
    
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
        print(publico)
        sleep(1)
        print()
        print("Ações:")
        print()
        print('1 - Subir no palco')
        print('2 - Cumprimentar o público')
        print('3 - Tocar uma música')
        print('4 - Fazer uma pausa')
        print('5 - Abandonar Palco')
        print('0 - Sair')
        print()
        opcao = input("Escolha sua ação: ")
        print()
        
        if carreira <= 2:

            if opcao == '1':
                if cont >= 2: 
                    x = randint(1,5)
                    if x == 1:
                        chuva()
                    else:
                        if subiu_no_palco == False:
                            personagem.fama += 5
                            publico.publico += 100
                            subiu_no_palco = True
                            sound_entrada()
                            print('Você subiu no palco e o mosh já começou a se formar, hoje tem roda punk!!!!')
                            sleep(3)
                        else:
                            print('Você já está no palco!\n')
                            print()
                else:
                    if subiu_no_palco == False:
                            personagem.fama += 5
                            publico.publico += 100
                            subiu_no_palco = True
                            sound_entrada()
                            print('Você subiu no palco e o mosh já começou a se formar, hoje tem roda punk!!!!')
                    else:
                        print('Você já está no palco!\n')

            if opcao == '2':
                if cont >= 2:
                    x = randint(1,5) 
                    if x == 1:
                        chuva()
                    else:
                        if subiu_no_palco == False:
                            print('Vai cumprimentar quem? O Roadie??!! Suba no palco já!!!\n')
                        else:
                            if cumprimentou_publico == True:
                                print('Chega de cumprimentar!!! Comece a tocar!!!')
                            else:
                                personagem.fama += 10
                                publico.publico += 100
                                cumprimentou_publico = True
                                print('Que artista!!! o público delira com a sua simpatia! quase uma miss!!!\n')
                                sleep(1.5)
                else:
                    if subiu_no_palco == False:
                        print('Vai cumprimentar quem? O Roadie??!! Suba no palco já!!!\n')
                    else:
                        if cumprimentou_publico == True:
                            print('Chega de cumprimentar!!! Comece a tocar!!!')
                        else:
                            personagem.fama += 10
                            publico.publico += 100
                            cumprimentou_publico = True
                            print('Que artista!!! o público delira com a sua simpatia! quase uma miss!!!\n')
                            sleep(1.5)
                        
            if opcao == '3':
                if cont >= 2: 
                    x = randint(1,5)
                    if x == 1:
                        chuva()
                    else:
                        if subiu_no_palco == False:
                            print('O público pede a sua presença no palco! Suba já!\n')
                        else:
                            if cumprimentou_publico == False:
                                print('Seja educado!!! Cumprimente sua plateia!!!\n')
                            else:
                                if personagem.cansaco >= 60:
                                    print('Você está muito cansado!!! Melhor fazer uma pausa!!!\n')
                                else:
                                    lista_musica() 
                else:
                    if subiu_no_palco == False:
                        print('O público pede a sua presença no palco! Suba já!\n')
                    else:
                        if cumprimentou_publico == False:
                            print('Seja educado!!! Cumprimente sua plateia!!!\n')
                        else:
                            if personagem.cansaco >= 60:
                                print('Você está muito cansado!!! Melhor fazer uma pausa!!!\n')
                            else:
                                lista_musica()         
                cont += 1
                
            if opcao == '4':
                if personagem.cansaco <= 40:
                    print('Tá cansado do quê??? Comece a tocar!!!')
                else:
                    personagem.cansaco -= 40
                    publico.publico *= 0.85

            if opcao == '5':
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
                sleep(2)

            if opcao == "0":
                break

            carreira += 1
            print(carreira)
            if carreira == 5:                       #personagem.fama
                print('\nCOMEÇO DE CARREIRA!!!\n')  #personagem.dinheiro
            if carreira == 10:                      #publico.publico
                print('\nMEIO DA CARREIRA\n')
            if carreira == 15:
                print('\nDECLÍNIO DA CARREIRA\n')
        else:
            print('\nAPOSENTADORIA\n')
            print('\nStatus da Carreira\n')
            sleep(10)
            