#1.	Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

#método 1
def soma():
    x = int(input('Digite o primeiro número: '))
    y = int(input('Digite o segundo número: '))
    z = int(input('Digite o terceiro número: '))
    print('Soma =', x + y + z)

soma()

#método 2
def soma2(x, y, z):
    return x + y + z

print('Soma =', soma2(int(input('Digite o primeiro número: ')),int(input('Digite o segundo número: ')),int(input('Digite o terceiro número: '))))

#2. Faça um programa, com uma função que necessite de um argumento.
#A função retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.

def num(x):
    if x > 0:
        return 'P'
    elif x < 0:
        return 'N'
    else:
        return '0'

print(num(int(input('Digite um número: '))))