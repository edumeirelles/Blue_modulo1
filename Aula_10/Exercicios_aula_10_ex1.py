#Exercício 0 - Escreva um programa que pede a senha ao usuário, e só sai do looping quando digitarem corretamente a senha.

senha = 'blue123'
entrada = input('Digite a senha: ')

while entrada != senha:
    print('Senha Incorreta. Tente novamente.')
    entrada = input('Digite a senha: ')

print('Acesso Liberado.')
