class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__salario = 0
        self.__horas_trabalhadas = 0

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, novo_salario):
        raise ValueError('Impossível alterar salário diretamente. Use o método calcular salário.')


    def registra_hora_trabalhada(self, horas):
        self.__horas_trabalhadas += horas

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada

piao = Funcionario('Pião', 'Pião', 5)
# print(piao.salario)
horas = float(input("Digite as horas trabalhadas: "))
piao.registra_hora_trabalhada(horas) 
piao.calcula_salario()
# print(piao.horas__trabalhadas)
# piao.__salario = 200
print(vars(piao))

