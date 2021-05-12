#Exercício Treino 3 - Crie uma função que receba uma string como argumento e retorne a mesma string em letras maiúsculas. 
#Faça uma chamada à função, passando como parâmetro uma string.

def palavra(x):
    return x.upper()

print(palavra(input('Digite uma palavra: ')))