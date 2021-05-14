# 1. Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
#       a.	tamanho da lista.
#       b.	maior valor da lista.
#       c.	menor valor da lista.
#       d.	soma de todos os elementos da lista.
#       e.	lista em ordem crescente.
#       f.	lista em ordem decrescente.

lista = [5, 7, 2, 9, 4, 1, 3]
print('O tamanho da lista é', len(lista))
print('O maior item da lista é', max(lista))
print('O menor item da lista é', min(lista))
print('A soma dos itens da lista é', sum(lista))
lista.sort()
print(lista)
lista.reverse()
print(lista)