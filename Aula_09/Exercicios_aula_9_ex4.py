# 4. Crie um código em Python que receba uma lista de nomes informados pelo usuário com tamanho indefinido (a lista deve ser encerrada quando o usuário digitar 0) e,
# na sequência, receba um nome para que seja verificado se este consta na lista ou não.
# Observação: ignorar diferenças entre maiúsculas e minúsculas.


# Usando FOR

lista = []

for i in range(1,1000):
    a = input('Digite um nome: ').lower()
    if a == '0':
        break
    else:
        lista.append(a)

nome = input('Digite um nome para verificar: ').lower()

if nome in lista:
    print(f'O nome {nome.capitalize()} está na lista')
else:
    print(f'O nome {nome.capitalize()} NÃO está na lista')

#Usando WHILE

lista2 = []

while True:
    b = input('Digite um nome: ').lower()
    if b != '0':
        lista2.append(b)
    else:
        break

nome2 = input('Digite um nome para verificar: ').lower()

if nome2 in lista2:
    print(f'O nome {nome2.capitalize()} está na lista ')
else:
    print(f'O nome {nome2.capitalize()} não está na lista')


