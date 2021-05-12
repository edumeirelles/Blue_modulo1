# Exercício Treino 2 - Escreva uma função que recebe dois números (a e b) como parâmetro e retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.

def soma_maior(x, y, z):
    return x + y > z

print(soma_maior(int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')), int(input('Digite o terceiro número: '))))
    