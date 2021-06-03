class Elevador:
    def __init__(self, andar_atual=0, total_andares=0, capacidade=0,pessoas_dentro=0):
        self.__andar_atual = andar_atual
        self.__total_andares = total_andares
        self.__capacidade = capacidade
        self.__pessoas_dentro = pessoas_dentro

    @property
    def andar_atual(self):
        return self.__andar_atual
    
    @andar_atual.setter
    def andar_atual(self, andar_atulal):
        self.__andar_atual = andar_atulal
    
    @property
    def total_andares(self):
        return self.__total_andares
    
    @total_andares.setter
    def total_andares(self, total_andares):
        self.__total_andares = total_andares

    @property
    def capacidade(self):
        return self.__capacidade
    
    @capacidade.setter
    def capacidade(self, capacidade):
        self.__capacidade = capacidade

    @property
    def pessoas_dentro(self):
        return self.__pessoas_dentro
    
    @capacidade.setter
    def pessoas_dentro(self, pessoas_dentro):
        self.__pessoas_dentro = pessoas_dentro
    
    def inicializar(self, total_andares, capacidade):
        self.__init__(0, total_andares, capacidade, 0)

    def entrar(self):
        if self.__pessoas_dentro < self.__capacidade:
            self.__pessoas_dentro += 1
        else:
            print('Capacidade Máxima do elevador foi atingida')
    
    def sair(self):
        if self.__pessoas_dentro > 0:
            self.__pessoas_dentro -= 1
        else:
            print('Elevador vazio')

    def subir(self):
        if self.__andar_atual < self.__total_andares:
            self.__andar_atual += 1
        else:
            print('Elevador está no último andar')

    def descer(self):
        if self.__andar_atual > 0:
            self.__andar_atual -= 1
        else:
            print('Elevador está no térreo')

if (__name__ == '__main__'):
    elevador = Elevador()
    #print(vars(elevador))
    print('*** JOGO DO ELEVADOR ***')
    capac = int(input('Digite a capacidade do elevador: '))
    andares = int(input('Didite o total de andares: '))

    elevador.inicializar(andares, capac)
    #print(vars(elevador))

    while True:
        print('Digite uma opção para ser executada: ')
        print('1 - Entrar (1 pessoa)')
        print('2 - Sair (1 pessoa)')
        print('3 - Subir (1 pessoa)')
        print('4 - Descer (1 pessoa)')
        print('0 - Encerrar')
        print()
        while True:
            try:
                op = int(input('Digite uma opção: '))
                print()
            except ValueError:
                print('Opção Inválida!!!')
                print()
            else:
                break

        if op == 0:
            print('\tObrigado por jogar o jogo do elevador!!!')
            print()
            print('\t- Andar atual:', elevador.andar_atual)
            print('\t- Total de andares:', elevador.total_andares)
            print('\t- Capacidade:', elevador.capacidade)
            print('\t- Quantidade de Pessoas:', elevador.pessoas_dentro)
            print()         
            break
        
        elif op == 1:
            print('Entrando 1 pessoa!')
            print()
            elevador.entrar()

        elif op == 2:
            print('Saindo 1 pessoa!')
            print()
            elevador.sair()

        elif op == 3:
            print('Subindo!')
            print()
            elevador.subir()
        
        elif op == 4:
            print('Descendo!')
            print()
            elevador.descer()
        
        else:
            print('Opção Inválida!!!')
            print()

    