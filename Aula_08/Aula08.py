# def testa_idade(idade=18):
#     #idade = int(input('Digite a idade: '))

#     if idade >= 18:
#         print('Maior de idade')
#     else:
#         print('Menor de idade')

# testa_idade(30)

# lista1 = [1, 2, 3]
# print(lista1[0])

# for a in range(5):
#     print(a)

# lista = ['Ana', 'Bernardo', 'Carlos', 'Daniel', 'Eurico', 'Filipe', 'Gabriel']
#     # print(lista[0])
#     # print(lista[1])

# for nome in lista:
#     for letra in nome:
#         print(letra)
#     input()
    

# for nome in lista:
#     print(nome)

# for item in lista:
#     print(item)
# 

# for item in range(11):
#     if item % 2 == 0 and item != 0:
#         print(item)

# lista = [1, 2, 'bla', 'bla']
# for item in lista:
#     print(item)

# nome = 'Eduardo Meirelles'
# for letra in nome:
#     if letra != " ":
#         print(letra) 

lista = [10, 20, 10, 30, 10, 40, 10, 50, 10]
# contador = 0
# for item in lista:
#     if item == 10:
#         contador += 1
#         print(item)
#     if contador >= 3:
#         print('Existe mais que 3 10')
#         break

lista2 = []
for item in lista:
    if item not in lista2:
        lista2.append(item)
lista2.sort()
print(lista2[1])