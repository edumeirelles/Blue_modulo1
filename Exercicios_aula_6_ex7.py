# 7. Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.

def maior(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return 'Os números são iguais'

print('Maior número =', maior(float(input('Digite o primeiro número: ').replace(',','.')), float(input('Digite o segundo número: ').replace(',','.'))))