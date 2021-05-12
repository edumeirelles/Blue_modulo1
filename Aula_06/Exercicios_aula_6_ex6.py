#6.	Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).
#
#   Nota	 Conceito
#  >=9.0	    A
#  >=8.0     	B
#  >=7.0    	C
#  >=6.0    	D
#  <=4.0	    F

def conceito(nota):
    if nota >= 9:
        return 'A'
    elif 9 > nota >= 8:
        return 'B'
    elif 8 > nota >= 7:
        return 'C'
    elif 7 > nota >= 6:
        return 'D'
    elif 6 > nota >= 4:
        return 'E'
    else:
        return 'F'

print('Conceito =', conceito(float(input('Digite a nota do aluno: ').replace(',','.'))))