# 3.	Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# •	"Telefonou para a vítima?"
# •	"Esteve no local do crime?"
# •	"Mora perto da vítima?"
# •	"Devia para a vítima?"
# •	"Já trabalhou com a vítima?"  

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

lista_perguntas = ['Telefonou para a vítima?: ', 'Esteve no local do crime?: ', 'Mora perto da vítima?: ', 'Devia para a vítima?: ', 'Já trabalhou com a vítima?: ']
lista_respostas = []

for pergunta in lista_perguntas:
    lista_respostas.append(input(pergunta).upper())

if lista_respostas.count('S') == 5:
    print('Assassino')
elif 3 <= lista_respostas.count('S') <= 4:
    print('Cúmplice')
elif lista_respostas.count('S') == 2:
    print('Suspeito')
else:
    print('Inocente')