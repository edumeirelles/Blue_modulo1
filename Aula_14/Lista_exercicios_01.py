#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:

   # A soma deles;

   # A multiplicação entre eles;

   # A divisão inteira deles;

   # Mostre na tela qual é o maior;

   # Verifique se o resultado da soma é par ou impar e mostre na tela;

   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.

num1 = int(input('Digite o primeiro número inteiro: '))
print()
num2 = int(input('Digite o segundo número: '))
print()
print('Soma:', num1 + num2, '\n')
print('Divisão inteira:', num1 // num2, '\n')

if num1 > num2:
    print('Maior número:', num1,'\n')
elif num1 == num2:
    print('Os números são iguais!\n')
else:
    print('Maior número:', num2,'\n')

if (num1 + num2) % 2 == 0:
    print('A soma é PAR!\n')
else:
    print('A soma é ÍMPAR!\n')

if num1 * num2 > 40:
    x = format((num1 * num2) / (num1 // num2),'.2f').replace('.',',')
    print(x,'\n')
else:
    print('A multiplicação é menor que 40!\n')