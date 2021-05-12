#4.	Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário é pago conforme a quantidade de horas trabalhadas.
# Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

def salario(qtde_horas, valor_hora):
    if qtde_horas <= 40:
        return qtde_horas * valor_hora
    else:
        return (40 * valor_hora) + (qtde_horas - 40) * valor_hora * 1.5 

print('Salário =', format(salario(float(input('Qual a quantidade de horas trabalhadas?: ')), float(input('Qual o valor da hora trabalhada?: '))),'.2f'))