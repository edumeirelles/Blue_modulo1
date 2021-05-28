class bombaCombustivel:
    def __init__(self,tipoCombustivel,valorLitro):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = 1000

    def abastecerPorValor(self,valor):

        quantidade_abastecida = valor / self.valorLitro
        print(f'R$ {valor:.2f} abastece {quantidade_abastecida:.2f} litros de {self.tipoCombustivel}')
        self.quantidadeCombustivel -= quantidade_abastecida
        print(f'Sobraram {self.quantidadeCombustivel:.2f} litros na bomba.')

    def abastecerPorLitro(self,quantidade_abastecida):

        self.quantidadeCombustivel -= quantidade_abastecida
        print(f'{quantidade_abastecida:.2f} litros de {self.tipoCombustivel} ficam em R$ {quantidade_abastecida*self.valorLitro:.2f}')
        print(f'Sobraram {self.quantidadeCombustivel} litros na bomba.')

    def alterarValor(self):
        
        novo_valor = float(input(f'Digite o novo valor do {self.tipoCombustivel}'))
        self.valorLitro = novo_valor
    
    def alterarCombustivel(self):

        tipo = input('Digite o tipo de combustível a ser alterado: ')
        
    
    def alterarQuantidadeCombustivel(self):

        quantidade = self.quantidadeCombustivel

valor = 0
tipo = input('Digite o tipo: ')
if tipo == "Gasolina":
    valor = 5.5
    gasolina = bombaCombustivel(tipo,valor)
    x = input('Deseja abastecer por Valor ou por Litros?: ').lower()
    if x == 'valor':
        v = float(input('digite o valor: '))
        gasolina.abastecerPorValor(v)
    elif x == 'litros':
        q = float(input('Digite a quantidade: '))
        gasolina.abastecerPorLitro(q)
elif tipo == "Etanol":
    valor = 3.99
    etanol = bombaCombustivel(tipo,valor)
    x = input('Deseja abastecer por Valor ou por Litros?: ').lower()
    if x == 'valor':
        v = float(input('digite o valor: '))
        etanol.abastecerPorValor(v)
    elif x == 'litros':
        q = float(input('Digite a quantidade: '))
        etanol.abastecerPorLitro(q)
elif tipo == "Diesel":
    valor = 4.5
    diesel = bombaCombustivel(tipo,valor)
    x = input('Deseja abastecer por Valor ou por Litros?: ').lower()
    if x == 'valor':
        v = float(input('digite o valor: '))
        diesel.abastecerPorValor(v)
    elif x == 'litros':
        q = float(input('Digite a quantidade: '))
        diesel.abastecerPorLitro(q)
else:
    print('Combustível inválido')













    


