# lista_contatos =[('Eduardo','16 99260-1155'),('Fulano','11 99999-0000'),('Beltrano','21 88888-5555'),('Sicrano','31 66666-7777'),('Zé','41 56565-7979')]
# # print(lista_contatos)

# dic_contatos = dict(lista_contatos)
# # print(dic_contatos)
# # print(len(dic_contatos))
# # dic1 = {'valor1':'valor2',}
# # print(len(dic1))

# print(dic_contatos['Eduardo'])
# nome = input('Digite o nome: ')
# #print(dic_contatos[nome])
# print(dic_contatos.get(nome,'Contato não encontrado'))

vingadores = {'Chris Evans':'Capitão América', 'Mark Ruffalo':'Hulk', 'Tom Hiddleston':'Loki', 'Chris Hemsworth':'Thor', 'Robert Downey Jr':'Homem de Ferro', 'Scarlet Johansson':'Viúva Negra'}
while True:
    print(vingadores.get(input('Digite o nome do(a) ator/atriz: '), 'Ator/atriz não encontrado.'))