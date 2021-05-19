# 4. Crie um programa em que 4 jogadores, joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário. No final coloque esse dicionário
# em ordem, sabendo que o vencedor tirou o maior número no dado. Dicas: procure
# sobre a função randint(), sleep() e itemgetter da bliblioteca operator

from time import sleep
from random import randint
from operator import itemgetter

lista = []

for i in range(1,5):
    dado = randint(1,20)
    lista.append([f'Jogador {i}',dado])
    if dado > 1:
        print(f'Jogador {i}:', dado, 'pontos!')
    else:
        print(f'Jogador {i}:', dado, 'ponto!')
    sleep(1)

dic = dict(lista)
dic2 = sorted(dic.items(), key = itemgetter(1), reverse = True)

print(f'O jogador {dic2[0][0]} tirou {dic2[0][1]} pontos' )