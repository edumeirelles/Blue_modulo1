#Exercício 6 
#Um professor, muito legal, fez 3 provas durante um semestre, mas só vai levar em conta as duas notas mais altas para calcular a média.
#Faça uma aplicação que peça o valor das 3 notas, mostre como seria a média com essas 3 provas, a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.

def notas(x, y, z):
    if x <= y and x <= z:
        media = (y + z) / 2
        menor = x
        if y > z:
            maior = y
        else:
            maior = z
    elif y <= x and y <= z:
        media = (x + z) / 2
        menor = y
        if x > z:
            maior = x
        else:
            maior = z
    else:
        media = (x + y) / 2
        menor = z
        if x > y:
            maior = x
        else:
            maior = y
    
    print('A média é', format(media,'.2f').replace('.',','),'\nA menor nota é', format(menor,'.2f').replace('.',','),'\nA maior nota é', format(maior,'.2f').replace('.',','))

notas(float(input('Digite a primeira nota: ').replace(',','.')),float(input('Digite a segunda nota: ').replace(',','.')),float(input('Digite a terceira nota: ').replace(',','.')))
    
    
