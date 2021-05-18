# 7.	(DESAFIO) Desenvolva um código em Python que gere um número aleatório de 1 a 100 e dê ao usuário 10 chances para acertá-lo. 
# A cada tentativa, deve ser impressa a quantidade de tentativas restantes e se o número aleatório é maior ou menor do que o número inserido na tentativa atual. 
# Se o usuário não acertar em 10 tentativas, informe qual o número aleatório. [Dica: use a função randint para gerar o número aleatório]

from random import randint

num = randint(1,100)
chances = 10

for i in range(1,11):
    x = int(input('Digite um número inteiro de 1 a 100: '))
    if x != num:
        chances -= 1
        print('Você errou o número. Tente novamente!')
        if x > num:
            print('O número aleatório é MENOR que o informado!')
        else:
            print('O número aleatório é MAIOR que o informado!')
        if chances == 0:
            print('O número aleatório é:', num)
            break

    else:
        print('Você acertou o número aleatório!!!')
        break
    





