from datetime import date

dic_nome = {}
dic_dados = {}

nome = input('Digite o nome: ').capitalize()

while  nome == '':
    print('Nome inválido!')
    dic_nome[nome] = input('Digite o nome: ')

dic_nome[nome] = dic_dados

while True:
    try:
        dic_dados['Ano de Nascimento'] = int(input('Digite o ano de nascimento: '))
    except ValueError:
        print('Ano de nascimento inválido')
        continue
    else:
        break

dic_dados['CTPS'] = int(input('Digite o número da carteira de trabalho: '))

if dic_dados['CTPS'] != 0:
    while True:
        try:
            dic_dados['Ano da Contratação'] = int(input('Digite o ano da contratação: '))
        except ValueError:
            print('Ano da contratação inválido')
            continue
        else:
            break
    dic_dados['Salário'] = float(input('Digite o Salário: ').replace(',','.'))
    dic_dados['Idade'] = date.today().year - dic_dados['Ano de Nascimento']
    dic_dados['Idade para aposentadoria'] = dic_dados['Ano da Contratação'] + 35 - dic_dados['Ano de Nascimento']
    print(dic_nome)
else:
    del dic_dados['CTPS']
    print(dic_nome)
