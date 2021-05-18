# 6.	Faça um script que peça ao usuário o número de matérias da escola, ou seja, um inteiro positivo. 
# Em seguida, ele vai digitando o valor de cada nota, de cada matéria e isso será armazenado numa lista.
# Ao final, seu script deverá fornecer a média geral do aluno.

num_mat = int(input('Digite a quantidade de matérias: '))
notas = []
for i in range(1,num_mat+1):
    notas.append(float(input(f'Digite a nota da matéria {i}: ').replace(',','.')))

print('Média:', format(sum(notas)/len(notas),'.1f').replace('.',','))