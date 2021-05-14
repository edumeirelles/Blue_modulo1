#4.	Dada uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte quantas vezes aparece uma vogal.

frase = input('Digite uma frase: ').upper()
cont = 0

for vogal in frase:
    if vogal in 'AEIOU':
        cont += 1

print ('Número de vogais: ', cont)