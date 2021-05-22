#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. 
# Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.

def frase_sem_vogal(frase):
    print()
    cont = 0
    for i in frase:
        if i in 'aeiouAEIOUÁÀÃÂáàâãÉÈÊêéèÓÒÔÕóòõôÚÙÛúùûüÍÌÎíìî':
            cont += 1
            frase = frase.replace(i,'')
    print('Número de vogais:', cont,'\n')
    print(frase, '\n')
    x = 'Quantidade de letras retiradas: ' + str(cont)
    return x
    
print(frase_sem_vogal(input('Digite uma frase: ')))
print()