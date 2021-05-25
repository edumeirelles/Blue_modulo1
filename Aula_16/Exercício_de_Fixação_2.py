class conta():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def sacar(self):
        saque = float(input('Digite o valor do saque: '))
        self.saldo -= saque
        print(vars(self))
    
    def depositar(self):
        deposito = float(input('Digite a quantia a ser depositada: '))
        self.saldo += deposito
        print(vars(self))

a = conta(input('Digite o nome do cliente: '), float(input('Digite o Saldo: ')))

print(vars(a))

a.sacar()
a.depositar()
