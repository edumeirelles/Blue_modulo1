# Exercício Treino 1 - Escreva uma função que recebe dois parâmetros (números) e imprime o menor dos dois. Se eles forem iguais, imprima que são valores idênticos.

def menor(x, y):
    if x < y:
        return x
    elif x > y:
        return y
    else:
        return 'Os números são iguais'

print('Menor número =', menor(float(input('Digite o primeiro número: ').replace(',','.')), float(input('Digite o segundo número: ').replace(',','.'))))