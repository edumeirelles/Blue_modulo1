# Exercício 5 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros: o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome, gols):
    
    print('O jogador', nome, 'marcou', gols, 'gols!')

ficha(input('Digite o nome do Jogador: '), input('Quantos gols ele fez?: '))

