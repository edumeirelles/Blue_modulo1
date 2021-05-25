# 6. DESAFIO: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma
# lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando
# perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.


lista = []

dic = {}

p = ''
while p != 'N':
    
    dic['Nome'] = input('Digite o nome: ').capitalize()
    while dic['Nome'] == '':
        print('Nome inválido. Tente novamente.')
        dic['Nome'] = input('Digite o nome: ').capitalize()

    dic['Sexo'] = input('Digite o Sexo: ').upper()
    while dic['Sexo'] != 'F' and dic['Sexo'] != 'M':
        print('Sexo inválido. Digite F para Feminino ou M para Masculino.')
        dic['Sexo'] = input('Digite o Sexo: ').upper()
    
    while True:
        try:
            dic['Idade'] = int(input('Digite a idade: '))
        except ValueError:
            print('Idade inválida. Digite um número inteiro.')
        else:
            break

    lista.append(dic)
    dic = {}

    p = input('Deseja cadastrar outra pessoa? Digite S para SIM ou N para NÃO: ').upper()
    while p != 'S' and p != 'N':
        print('Resposta inválida. Digite S para SIM ou N para NÃO: ')
        p = input('Deseja cadastrar outra pessoa?: ').upper()

print(lista)




