import random

lista = input('digite uma lista de palavras separadas por espaço: ')
lista = lista.split(' ')


if len(lista) == 1:
    palavra = lista[0].upper()
else:
    palavra = random.choice(lista).upper()

palavra_forca = ['_' for i in palavra]

chance = 0

print('A palavra é: ', end = '')
print(' '.join(palavra_forca))


while palavra_forca.count('_') != 0 and chance != 6: 
    letra = input('Digite uma letra: ').upper()
    if letra in palavra_forca:
        print('Você já digitou essa letra antes.\nA palavra é: ', end = '')
        print(' '.join(palavra_forca))
        continue
    if letra in palavra:
        print('A palavra é: ', end = '')
        for n in range(len(palavra)):
            if letra == palavra[n]:
                del palavra_forca[n]
                palavra_forca.insert(n, letra)
                #palavra_forca[n] = letra
        print(' '.join(palavra_forca))        

    else:
        chance += 1
        if chance != 6:
            print('Você errou pela', str(chance), 'ª vez. Tente novamente!')

if palavra_forca.count('_') == 0:
    print('Parabéns! Você acertou a palavra!')
else:
    print('Você errou pela 6ª vez.\nFORCA!!! VOCÊ PERDEU!!!')