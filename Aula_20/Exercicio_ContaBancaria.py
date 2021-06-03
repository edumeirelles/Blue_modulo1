import datetime

class contaBancaria:
    def __init__(self, numero, agencia, saldo, codigo_tipo):
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo
        self.codigo_tipo = codigo_tipo

    def sacar(self):
        saque = float(input('Digite o valor do saque: '))
        if saque > self.saldo:
            print('Saldo Insuficiente.')
        else:
            self.saldo -= saque
            print(f'Seu novo saldo é {self.saldo}')
    
    def depositar(self):
        deposito = float(input('Digite a quantia a ser depositada: '))
        self.saldo += deposito
        print(f'Seu novo saldo é {self.saldo}')

class contaImposto(contaBancaria):
    def __init__(self, numero, agencia, saldo, codigo_tipo, aliquota):
        self.aliquota = aliquota
        super().__init__(numero, agencia, saldo, codigo_tipo)
    
    def calcularImposto(self):
        imposto = self.saldo * self.aliquota/100
        self.saldo -= imposto
        print(f'Seu novo saldo é {self.saldo}')

if __name__ == '__main__':

    conta = contaImposto('1234-5','0001',10000,1,27.5)

    while True:
        print('Banco Blue')
        print()
        print('\tDigite a opção desejada:')
        print('\t1 - Extrato')
        print('\t2 - Saque')
        print('\t3 - Depósito')
        print('\t4 - Calcular Imposto')
        print('\t0 - Sair')
        while True:
            try:
                op = int(input())
            except ValueError:
                print('Opção inválida.')
            else:
                break
        
        if op == 0:
            print('Obrigado por ser cliente do Banco Blue')
        elif op == 1:
            print('=== EXTRATO ===')
            print()
            print(str(datetime.datetime.now()))
            print(f'Agência: {conta.agencia}')
            if conta.codigo_tipo == '1':
                print(f'Conta Corrente: {conta.numero}')
            else:
                print(f'Conta Poupança: {conta.numero}')
            print(f'Saldo: R$ {conta.saldo:.2f}')
            print(f'Imposto: {conta.aliquota:.1f}%')
        elif op == 2:
            conta.sacar()
        elif op == 3:
            conta.depositar()
        elif op == 4:
            conta.calcularImposto()
            



    