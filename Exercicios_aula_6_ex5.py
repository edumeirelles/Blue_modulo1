#5.	Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.
def imc(alt, peso):
    return peso / alt ** 2

print('IMC =', format(imc(1.68, 75),'.2f'))