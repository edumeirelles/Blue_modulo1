# 5.	O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
# Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
# Um valor zero deve ser informado pelo operador para indicar o final da compra. 
# O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. 
# Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

# Lojas Tabajara
# Produto 1: R$ 2,20
# Produto 2: R$ 5,80
# Produto 3: R$ 0
# Total: R$ 8,00
# Dinheiro: R$ 20,00
# Troco: R$ 12,00




produtos = []
print('Lojas Tabajara')
for i in range(1,1000):
      
    a = float(input(f'Produto {i}: R$ ').replace(',','.'))
    if a == 0:
        print('Total: R$', format(sum(produtos),'.2f').replace('.',','))
        din = float(input('Dinheiro: R$').replace(',','.'))
        troco = din - sum(produtos)
        print('Troco: R$', format(troco,'.2f').replace('.',','))
        produtos = []
        print('Lojas Tabajara')
        continue
                    
    else:
        produtos.append(a)
