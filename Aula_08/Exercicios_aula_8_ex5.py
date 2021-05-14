# 5.	Desenvolva um código que pergunte um número n para o usuário e exiba todos seus divisores. 
# Caso seja um número primo, o programa ainda deve informar que se trata de um número primo! 

num = int(input('Digite um número: '))

divisores = []


for i in range(num, 0, -1):
    if num % i == 0:
        divisores.append(i)

if len(divisores) == 2:
    print('O número é primo! Seus divisores são:', ' e '.join(str(x) for x in divisores)) #soulução para remover os colchetes encontrada no stackoverflow!
else:
    print('Os divisores do número são:', ', '.join(str(x) for x in divisores)[:-3], 'e', divisores[-1]) #soulução para remover os colchetes encontrada no stackoverflow!