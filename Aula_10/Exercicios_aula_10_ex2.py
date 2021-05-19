# Exercício 2 - Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros.  
# Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

import random

alunos = []

for i in range(1,11):
    alunos.append([i,random.randrange(150,180)])

x = [j for i,j in alunos]
y = x.index(max(x)) + 1

a = [j for i,j in alunos]
b = a.index(min(a)) + 1

print('O maior aluno tem', max([i[1] for i in alunos]), f'centímetros e seu número é {y}.')
print('O menor aluno tem', min([i[1] for i in alunos]), f'centímetros e seu número é {b}.')

print(alunos)
