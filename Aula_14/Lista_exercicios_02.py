#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string com uma frase informada pelo usuário e 
#conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.

def frase_sem_vogal(frase):
    print()
    cont =0
    for i in frase:
        if i in 'aeiouAEIOUÁÀÃÂáàâãÉÈÊêéèÓÒÔÕóòõôÚÙÛúùûüÍÌÎíìî':
            cont += 1
            frase = frase.replace(i,'')
    print('Número de vogais:', cont,'\n')
    return frase

print(frase_sem_vogal(input('Digite uma frase: ')))
print()