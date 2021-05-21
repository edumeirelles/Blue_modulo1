# 5. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastreos (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário
# receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve
# contribuir por 35 anos para se aposentar.
from datetime import date

dic = {}

dic['Nome'] = input('Digite o nome: ').capitalize()
while dic['Nome'] == '':
    print('Nome inválido!')
    dic['Nome'] = input('Digite o nome: ')
    
while True:
    try:
        dic['Ano de Nascimento'] = int(input('Digite o ano de nescimento: '))
    except ValueError:
        print('Ano de nascimento inválido')
        continue
    else:
        break
    
dic['CTPS'] = int(input('Digite o número da carteira de trabalho: '))

if dic['CTPS'] != 0:
    while True:
        try:
            dic['Ano da Contratação'] = int(input('Digite o ano da contratação: '))
        except ValueError:
            print('Ano da contratação inválido')
            continue
        else:
            break
    dic['Salário'] = float(input('Digite o Salário: ').replace(',','.'))
    dic['Idade'] = date.today().year - dic['Ano de Nascimento']
    dic['Idade para aposentadoria'] = dic['Ano da Contratação'] + 35 - dic['Ano de Nascimento']
    print(dic)
else:
    del dic['CTPS']
    print(dic)
