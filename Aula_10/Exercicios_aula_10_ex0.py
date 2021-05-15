#Exercício 0 – Crie um laço while que vai pedir para o usuário dois números e faça a soma dos dois. Enquanto a soma não for 50, ele deve continuar repetindo.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

while num1 + num2 != 50:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))

print('A soma é igual que 50')