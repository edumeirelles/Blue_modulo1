# 3. Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para
# aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é
# reprovado.

lista = []

for i in range(1,6):
    aluno = input('Digite o nome do Aluno: ')
    media = float(input('Digite a média do Aluno: ').replace(',','.'))
    if media >= 7:
        lista.append([aluno, 'Aprovado'])
    elif 7 > media >= 5:
        lista.append([aluno, 'Recuperação'])
    else:
        lista.append([aluno, 'Reprovado'])

dic = dict(lista)

for i,j in dic.items():
    print(f'O aluno {i} está {j}')