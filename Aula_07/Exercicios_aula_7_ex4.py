#Exercício 4 - Crie um programa que tenha uma função chamada voto () que vai receber como parâmetro o ano de nascimento de uma pessoa, 
#retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições. 
#Para resolver esse exercício, pesquise sobre a função date da biblioteca Datetime.

from datetime import date

def voto(ano_nas):
    if (date.today().year - ano_nas) < 16:
        return 'NEGADO'
    elif 16 <= (date.today().year - ano_nas) < 18 or (date.today().year - ano_nas) > 70:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'

print(voto(int(input('Digite o ano de nascimento: '))))
