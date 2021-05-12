#DESAFIO -  Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. 
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida. 
# Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro terá 29 dias.

def data(dd, mm, aaaa):

    if mm == 2:
        if aaaa % 4 != 0 and dd > 28:
            print('Data inválida')
        elif aaaa % 4 == 0 and dd > 29:
            print('Data inválida')
        else:
            mm = 'Fevereiro'
            print(dd, 'de', mm, 'de', aaaa)

    elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
        if dd > 30:
            print('Data inválida')
        else:
            if mm == 4:
                mm = 'Abril'            
            if mm == 6:
                mm = 'Junho'            
            if mm == 9:
                mm = 'Setembro'           
            if mm == 11:
                mm = 'Novembro'
            print(dd, 'de', mm, 'de', aaaa)

    else:
        if dd > 31 or mm > 12:
            print('Data inválida')
        else:
            if mm == 1:
                mm = 'Janeiro'
            if mm == 3:
                mm = 'Março'
            if mm == 5:
                mm = 'Maio'
            if mm == 7:
                mm = 'Julho'
            if mm == 8:
                mm = 'Agosto'
            if mm == 10:
                mm = 'Outubro'
            if mm == 12:
                mm = 'Dezembro'
            print(dd, 'de', mm, 'de', aaaa)
    

data(int(input('Digite o dia: ')),int(input('Digite o mês: ')),int(input('Digite o ano: ')))