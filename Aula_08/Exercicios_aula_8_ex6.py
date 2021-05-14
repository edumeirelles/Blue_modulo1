#6.	Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal.

def frase_sem_vogal(frase):
    for vogal in frase:
        if vogal in 'aeiouAEIOUÁÀÃÂáàâãÉÈÊêéèÓÒÔÕóòõôÚÙÛúùûüÍÌÎíìî':
            frase = frase.replace(vogal,'')
    return frase

print('Frase sem vogais:', frase_sem_vogal(input('Digite uma frase: ')))